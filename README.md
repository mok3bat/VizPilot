# 📊 VizPilot — Your AI Copilot for Tableau Metadata

**VizPilot** is a Streamlit-based assistant designed for Tableau Cloud and Tableau Server users. It connects to the Tableau Metadata API and uses vector search with OpenAI to help you:

- 🔍 Search and explore published datasources
- 🧠 Ask natural language questions about dashboards and fields
- 📚 View detailed metadata about any Tableau datasource
- 🧬 Automatically build a vector index from Tableau fields

---

## 🚀 Features

- **Tableau Configuration Panel** – Easily connect to your Tableau environment using PATs.
- **Vector Indexing** – Build a vector store for fast semantic search using OpenAI.
- **Metadata Search** – Ask questions like “Which dashboards use customer name?” or “Find fields with missing descriptions.”
- **Datasource Details** – View fields, owners, descriptions, and more for each datasource.
- **Modular Design** – Clean structure for extending with new capabilities like lineage, usage stats, etc.

---

## 🛠️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/mok3bat/VizPilot.git
cd VizPilot
````

### 2. Set up Python environment

Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Once the app is running, it will open in your browser automatically at:

```
http://localhost:8501
```

---

## ⚙️ Configuration

In the app sidebar, configure your Tableau and OpenAI settings:

* **Tableau Server URL** (e.g., `https://your-tableau-server.com`)
* **Site ID** (usually blank for the default site)
* **PAT Name** and **PAT Secret**
* **OpenAI API Key** (for semantic search capabilities)

Click **💾 Save & Apply** to store the configuration for your session.

---

## 🧭 How to Use

### 📚 Tab 1: View Datasources

Click **🔍 Load Datasource List** to see all published datasources.

Each datasource can be expanded to view its name, description, and LUID.

---

### 🧬 Tab 2: Datasource Metadata

Enter a Tableau **Datasource ID (LUID)** and click **Fetch Metadata** to see detailed field-level metadata, including:

* Field names
* Types
* Descriptions
* Owner

---

### 🔍 Tab 3: Ask Questions

Enter a natural language question like:

> *"Which datasources contain customer revenue fields?"*

And get a semantic response powered by OpenAI.

---

## 🧪 Example Use Cases

* Quickly find and review Tableau datasources across your organization
* Document metadata and identify missing field descriptions
* Search fields by description, name, or type using semantic vector search
* Prototype future features for Tableau governance or content auditing

---

## 🛤️ Roadmap

Planned features for upcoming releases:

* 📈 Dashboard lineage and relationships
* 🧑‍🤝‍🧑 User/group permissions insight
* 🗂️ Project-based filtering
* 📦 Export metadata to CSV or Excel
* 🧭 Content recommendation system

---

## 🧱 Built With

* [Streamlit](https://streamlit.io/)
* [Tableau Metadata API](https://help.tableau.com/current/api/metadata_api/en-us/)
* [Chroma Vector DB](https://www.trychroma.com/)
* [OpenAI GPT Embeddings](https://platform.openai.com/docs/guides/embeddings)

---

## 🛡️ Security Notes

* All secrets (PATs, API Keys) are stored only in memory during runtime.
* You can extend `config_utils.py` to store credentials more securely (e.g., encrypted file or Vault integration).

---

## 💬 Feedback & Feature Requests

Please [open an issue](https://github.com/yourusername/vizpilot/issues) or contact me on LinkedIn if you have ideas, suggestions, or feedback. I’d love to hear from fellow Tableau users and data engineers!

---

## 👨‍💻 Developer Info

**Author:** [Mo. Setit](https://www.linkedin.com/in/mohamed-steit)

* 💼 [LinkedIn](https://www.linkedin.com/in/mohamed-steit)
* 🌐 [GitHub](https://github.com/mok3bat)
* 📊 [Tableau Public](https://public.tableau.com/app/profile/mohamed6599)

---

## 📝 License

MIT License — feel free to fork, contribute, and enhance VizPilot for your team or organization.
