# Knowledge Graph RAG with LlamaIndex for Data Analysis

A financial sentiment analysis pipeline that uses **LlamaIndex** and a **Neo4j** knowledge graph for retrieval-augmented generation (RAG). The system ingests documents, builds a property graph, and answers natural-language queries with summarized reports.

## Features

- **Knowledge graph construction** — Extracts entities and relationships into a Neo4j property graph
- **RAG over the graph** — Queries the graph for context and uses an LLM to generate summary reports
- **Optional web-sourced dataset** — Uses Google Custom Search and OpenAI to generate search queries and fetch content (or use your own documents in `dataset/`)
- **Financial sentiment focus** — Example queries target EV sector, renewable energy, tech outlook, and related themes

## Project structure

```
├── engine.py              # Query the graph and generate reports
├── requirements.txt
├── .env.example            # Template for API keys and Neo4j config
├── notebook/
│   └── updated_market_data_analysis.ipynb
├── references/
│   └── Solution Methodology.pdf
├── src/
│   ├── constants.py        # Config (env vars or placeholders)
│   ├── graph_store_creation.py   # Build graph from documents
│   └── utils.py            # Search, scraping, report generation
└── storage/               # Persisted index (gitignored)
```

## Prerequisites

- **Python 3.10**
- **Neo4j** running (local or remote)
- **OpenAI API key**
- (Optional) Google Custom Search API key and Search Engine ID, if you use the built-in dataset creation

## Setup

1. **Clone and enter the project**

   ```bash
   cd "Knowledge Graph RAG With LlamaIndex for Data Analysis"
   ```

2. **Create a virtual environment**

   **Windows:**

   ```bash
   python -m venv myenv
   myenv\Scripts\activate
   ```

   **Linux/macOS:**

   ```bash
   python3.10 -m venv myenv
   source myenv/bin/activate
   ```

   With multiple Python versions (e.g. Windows): `py -3.10 -m venv myenv`

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure credentials**

   - Copy `.env.example` to `.env` and set your keys, or
   - Edit `src/constants.py` and set `neo4j_username`, `neo4j_password`, `neo4j_url`, and `open_ai_key` (and optionally `google_api`, `search_engine_id`).

   Do not commit `.env` or real credentials.

## Usage

### 1. Build the knowledge graph (first time)

Place documents (e.g. `.txt` files) in a `dataset/` folder, or use the script to create a dataset from web search:

```bash
python -m src.graph_store_creation
```

This loads documents from `dataset/`, builds the property graph in Neo4j, and persists the index under `storage/`.

### 2. Run queries and generate reports

```bash
python engine.py
```

This connects to the existing Neo4j graph, runs the predefined financial sentiment queries, and writes results to `financial_sentiment_reports.txt`.

You can change the query list in `engine.py` (variable `queries`) to suit your own analysis.





