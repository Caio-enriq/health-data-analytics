# Health Data Analytics Platform

![Health Analytics](https://via.placeholder.com/1200x600?text=Health+Data+Analytics+Dashboard)

## 📌 Overview
The **Health Data Analytics Platform** is a powerful Python-based analytics suite designed for extracting, processing, and patching data into interactive HTML dashboards. It simulates a high-performance environment for hospital/clinic data processing (using mock data in this repository) and integrates seamlessly with Google Sheets and Google Apps Script ecosystems for frontend rendering.

> **Disclaimer**: This repository contains **mock data only** and does not connect to any real-world APIs, databases, or client systems. It serves as a structural portfolio piece. However, the architecture is fully production-ready and can be hooked up to internal APIs, BigQuery, or live Google Sheets to aggregate and process real data securely.

## ✨ Features
* **Data Extraction Pipeline (`extract_dashboard.py`):** Pulls raw analytical data and standardizes it for consumption.
* **Dashboard Patching (`patch_*.py`):** Injects dynamic datasets into static HTML templates (like `dashboard.html`) to render interactive charts and metrics.
* **HTML Compilation (`compile_html.py`):** Aggregates assets (CSS, JS, Logos) into a single, highly-portable HTML artifact for deployment in restricted environments (e.g., Apps Script).
* **Mock Google API Testing (`test_*.py`):** Suites to validate the connection integrity of Sheets and other external mock APIs.

## 🛠 Tech Stack
* **Language:** Python 3.10+
* **Data Processing:** Pandas / Numpy (Standard Data Science Stack)
* **Frontend Output:** HTML5, CSS3, JavaScript (Vanilla / CDN-based UI Libraries)
* **Authentication Modules (Mocked):** Google Auth Library / Service Accounts

## 🚀 Getting Started

### Prerequisites
* Python 3.10 or higher
* `pip` or `uv` for dependency management

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/health-data-analytics.git
   cd health-data-analytics
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt # (Ensure to create one if adding more deps)
   ```

### Running the Data Pipeline

To test the HTML generation and patching:
```bash
# Extract mock data
python extract_dashboard.py

# Patch the HTML file with new data
python patch_dash.py

# Compile into a single distributable HTML
python compile_html.py
```

## 📂 Project Structure
```
health-data-analytics/
├── backend/                  # API and microservice logic (mocked)
├── logo/                     # Static assets for the dashboard
├── dashboard.html            # Main HTML template for the analytics view
├── compile_html.py           # Script to inline CSS/JS into the HTML
├── patch_*.py                # Scripts for injecting specific modules (Charts, Modals)
├── extract_dashboard.py      # Core data extraction script
├── test_*.py                 # Testing scripts for connection validation
└── web_guidance.md           # Internal UI/UX guidelines for the dashboard
```

## 🤝 Contributing
Feel free to fork this project and adapt the extraction scripts to connect to your own databases!

## 📜 License
MIT License.
