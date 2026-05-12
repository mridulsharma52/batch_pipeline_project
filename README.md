#Enterprise Batch Pipeline & Medallion Warehouse

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-green)
![Gemini API](https://img.shields.io/badge/Gemini%20API-AI%20Insights-orange)
![Pipeline](https://img.shields.io/badge/Architecture-Medallion%20Bronze%2FSilver%2FGold-gold)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

An end-to-end batch data pipeline implementing **Medallion Architecture (Bronze/Silver/Gold)** with **AI-generated insights powered by Google Gemini API**. Built to demonstrate production-grade data engineering patterns — ingestion, transformation, quality validation, and LLM-augmented analytics in a single pipeline.

---

## Architecture Overview

```
External Data Source
        ↓
[ BRONZE LAYER ] — Raw ingestion via ingest.py
        ↓
[ SILVER LAYER ] — Data quality checks, deduplication, metadata tagging
        ↓
[ GOLD LAYER ]  — Analysis-ready dataset + AI insights via Gemini API
        ↓
  insights_report.txt (LLM-generated analytics output)
```

---

## What This Pipeline Does

### 1. `ingest.py` — Bronze Layer (Raw Ingestion)
- Ingests raw data from external sources (CSV / REST API)
- Tags every record with ingestion timestamp, source file, and pipeline version
- Runs automated quality checks — null removal, deduplication
- Saves validated data to the raw zone (`raw_data.csv`)

### 2. `ai_insights.py` — Gold Layer (AI-Augmented Analytics)
- Reads analysis-ready dataset from the Silver/Gold layer
- Sends schema metadata and dataset summary to **Google Gemini API**
- Generates 3 key data insights using LLM-powered analysis
- Saves insights to `insights_report.txt` for downstream consumption

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.9+ |
| Data Processing | Pandas |
| AI / LLM | Google Gemini API (gemini-2.0-flash) |
| Architecture | Medallion (Bronze / Silver / Gold) |
| Storage | CSV (local) → extendable to AWS S3 / PostgreSQL |
| Orchestration | Extendable to Apache Airflow DAGs |

---

## Getting Started

### Prerequisites
```bash
pip install pandas google-generativeai
```

### Set your Gemini API key
```bash
export GEMINI_API_KEY=your_api_key_here
```

### Run the pipeline
```bash
# Step 1 — Ingest and validate raw data
python ingest.py

# Step 2 — Generate AI insights
python ai_insights.py
```

---

## Project Structure

```
batch_pipeline_project/
│
├── ingest.py              # Bronze layer — raw ingestion + quality checks
├── ai_insights.py         # Gold layer — Gemini API insight generation
├── raw_data.csv           # Output from ingestion layer
├── raw_taxi_data.csv      # Secondary raw dataset
└── insights_report.txt    # AI-generated insights output
```

---

## Roadmap

- [ ] Add PostgreSQL as persistent storage layer
- [ ] Integrate Apache Airflow for DAG-based orchestration
- [ ] Add AWS S3 as staging layer for Bronze ingestion
- [ ] Implement dbt transformation models for Silver layer
- [ ] Add schema validation with Great Expectations
- [ ] Build Power BI dashboard on Gold layer output

---

## 👤 Author

**Mridul Sharma** — Data Engineer  
[LinkedIn](https://linkedin.com/in/mridulsharma05) · [GitHub](https://github.com/mridulsharma52)

---

> *"Most data pipelines don't fail because of bad code. They fail because nobody thought hard enough about what happens when things go wrong."*
