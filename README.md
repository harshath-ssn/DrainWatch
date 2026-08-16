# 🌊 DrainWatch — Smart City Predictive Drainage & GIS Digital Twin

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://github.com/harshath-ssn/DrainWatch)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Team](https://img.shields.io/badge/Team-CodeCapitalists-blue.svg)](#)

> **AI-Driven Predictive Urban Drainage Digital Twin for Flood Prevention & Vector Breeding Control.**

---

## 📌 Problem Overview
Traditional municipal storm-drain management is purely reactive—acting only after roads are submerged. **DrainWatch** bridges the subterranean visibility gap by ingesting live weather radar, civic data, and municipal telemetry to forecast urban flooding and stagnant water zones 4–7 days before vector-borne outbreaks occur.

---

## 🚀 Key Features
- 🌧️ **Multi-Source Ingestion:** Aggregates IMD/OpenWeather radar streams and crowdsourced reports.
- 🧠 **Predictive Risk Engine:** PyTorch GCN-LSTM model estimating flood trajectories and node overflow probability.
- 🗺️ **GIS Municipal Command Dashboard:** Interactive dark-mode spatial map built with Streamlit.
- 🦟 **Vector Risk Analytics:** Automated stagnation tracking to prevent mosquito breeding.

---

## 🛠️ Tech Stack
- **Frontend / Dashboard:** Python, Streamlit, Pandas, NumPy
- **Spatial AI / Machine Learning:** PyTorch (GCN-LSTM Architecture)
- **Data & Ingestion:** Supabase (PostgreSQL + PostGIS) & REST Webhooks

---

## 💻 Quickstart (Run Locally)

### 1. Clone the Repository
```bash
git clone [https://github.com/harshath-ssn/DrainWatch.git](https://github.com/harshath-ssn/DrainWatch.git)
cd DrainWatch