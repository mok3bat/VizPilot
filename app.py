import streamlit as st
from tableau_utils import get_all_datasources, get_datasource_details
from agents.tableau_agent import search_metadata_with_vectors
from services.embeddings import is_chroma_index_ready, build_vector_store
from config_utils import load_config, save_config

st.set_page_config(page_title="Intelligent Report Generator")
st.title("📊 Intelligent Report Generator")

# === Load configuration early ===
config = load_config()

# === Validate config ===
required_keys = [
    "TABLEAU_SERVER_URL",
    "TABLEAU_SITE_ID",
    "TABLEAU_PERSONAL_ACCESS_TOKEN_NAME",
    "TABLEAU_PERSONAL_ACCESS_TOKEN_SECRET",
    "OPENAI_API_KEY"
]

missing_keys = [
    key for key in required_keys
    if not config.get(key) or "your-tableau-server.com" in config.get(key)
]

# === Sidebar config settings ===
with st.sidebar.expander("⚙️ Tableau Configuration", expanded=False):
    config["TABLEAU_SERVER_URL"] = st.text_input("🔗 Tableau Server URL", value=config.get("TABLEAU_SERVER_URL", ""))
    config["TABLEAU_SITE_ID"] = st.text_input("🌐 Tableau Site ID", value=config.get("TABLEAU_SITE_ID", ""))
    config["TABLEAU_PERSONAL_ACCESS_TOKEN_NAME"] = st.text_input("🔑 PAT Name", value=config.get("TABLEAU_PERSONAL_ACCESS_TOKEN_NAME", ""))
    config["TABLEAU_PERSONAL_ACCESS_TOKEN_SECRET"] = st.text_input("🕵️ PAT Secret", type="password", value=config.get("TABLEAU_PERSONAL_ACCESS_TOKEN_SECRET", ""))
    config["OPENAI_API_KEY"] = st.text_input("🧠 OpenAI API Key", type="password", value=config.get("OPENAI_API_KEY", ""))

    if st.button("💾 Save & Apply"):
        save_config(config)
        st.success("✅ Configuration saved!")
        st.rerun()

# === Halt app if config is incomplete ===
if missing_keys:
    st.warning("⚠️ Please complete the configuration in the sidebar and click **💾 Save & Apply** before using the app.")
    st.stop()

# === Build vector index if missing ===
if not is_chroma_index_ready():
    with st.spinner("⚠️ Vector index not found. Building now..."):
        build_vector_store()
        st.success("✅ Vector index built!")

# === Tabs ===
tab1, tab2, tab3 = st.tabs(["📚 View Datasources", "🧬 Datasource Metadata", "🔍 Query Dashboards"])

# === Tab 1: List all datasources ===
with tab1:
    st.subheader("📚 All Published Datasources")
    if st.button("🔍 Load Datasource List"):
        with st.spinner("Querying Tableau Metadata API..."):
            try:
                ds_list = get_all_datasources()
                for ds in ds_list:
                    with st.expander(f"{ds['name']} ({ds['luid']})"):
                        st.write(f"📝 Description: {ds.get('description', 'N/A')}")
                        st.write(f"🆔 LUID: {ds['luid']}")
            except Exception as e:
                st.error(f"❌ Failed to load datasources: {e}")

# === Tab 2: Fetch metadata for a selected datasource ===
with tab2:
    st.subheader("🔬 View Metadata for a Specific Datasource")
    ds_id = st.text_input("Enter Datasource ID:")
    if st.button("Fetch Metadata"):
        with st.spinner("Getting detailed metadata..."):
            try:
                details = get_datasource_details(ds_id)
                st.markdown(f"### 🧾 {details['name']}")
                st.write(f"🧑 Owner: {details.get('owner', {}).get('name', 'Unknown')}")
                st.dataframe(details.get("fields", []))
            except Exception as e:
                st.error(f"❌ Error fetching metadata: {e}")

# === Tab 3: Ask questions ===
with tab3:
    query = st.text_input("Ask a question about your Tableau dashboards:")
    if st.button("Generate Answer"):
        with st.spinner("Searching dashboards and generating insights..."):
            try:
                response = search_metadata_with_vectors(query)
                st.markdown(response)
            except Exception as e:
                st.error(f"❌ Failed to generate answer: {e}")


# 📌 Fixed Footer with Developer Links
st.markdown("""
<style>
.footer {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #f0f2f6;
    color: #6c757d;
    text-align: center;
    padding: 10px;
    font-size: 0.85rem;
    border-top: 1px solid #ddd;
    z-index: 100;
}
</style>

<div class="footer">
    👨‍💻 Developed by <a href="https://www.linkedin.com/in/mohamed-steit" target="_blank">Mo. Setit</a> |
    <a href="https://github.com/mok3bat" target="_blank">GitHub</a> |
    <a href="https://public.tableau.com/app/profile/mohamed6599" target="_blank">Tableau Public</a>
</div>
""", unsafe_allow_html=True)
