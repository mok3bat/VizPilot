# 📊 VizPilot

An interactive Streamlit-based web app that connects to **Tableau's Metadata API** to help users:

- View all published Tableau datasources
- Retrieve and explore detailed metadata (including fields and owners)
- Ask natural language questions about Tableau dashboards using vector search powered by OpenAI and embeddings

---

## 🚀 Features

- 🔐 Secure configuration with Tableau PATs
- ⚡ Vector-based metadata search
- 📚 Datasource browser and detailed field-level metadata
- 🧠 Chroma DB for efficient semantic search
- 🧾 Built-in support for OpenAI API

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

### 🔍 Tab 1: Ask Questions

Enter a natural language question like:

> *"Which datasources contain customer revenue fields?"*

And get a semantic response powered by OpenAI.

---

### 📚 Tab 2: View Datasources

Click **🔍 Load Datasource List** to see all published datasources.

Each datasource can be expanded to view its name, description, and LUID.

---

### 🧬 Tab 3: Datasource Metadata

Enter a Tableau **Datasource ID (LUID)** and click **Fetch Metadata** to see detailed field-level metadata, including:

* Field names
* Types
* Descriptions
* Owner

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