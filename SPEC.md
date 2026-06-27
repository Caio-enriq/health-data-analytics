# Health Data Analytics - Architecture & Specifications

## 1. System Architecture
The Health Data Analytics platform operates as an ETL (Extract, Transform, Load) pipeline coupled with a Static Site Generator logic for dashboards. 

### 1.1 Core Components
* **Data Extractor:** Interfaces with mocked external sources to fetch raw JSON/CSV data.
* **Data Transformer (Patchers):** Python scripts (`patch_chart.py`, `patch_modal.py`) that parse HTML templates using regex or BeautifulSoup and replace placeholder variables (`{{CHART_DATA}}`) with serialized JSON.
* **Compiler:** `compile_html.py` takes the patched HTML and minifies/inlines all external assets to create a single `index.html` payload. This is specifically designed to bypass limitations in restrictive enterprise environments (like Google Apps Script) which don't allow separate CSS/JS files easily.

## 2. Data Flow
1. **Trigger:** A chron job or manual execution starts the pipeline.
2. **Extraction:** `extract_dashboard.py` collects mocked metrics (e.g., patient admission rates, system uptime).
3. **Patching:** The data is formatted as JSON strings and injected into `dashboard.html` via `patch_dash.py`.
4. **Output:** A finalized, interactive HTML file is generated and can be served statically.

## 3. Supported Integrations (via Mocking)
To demonstrate enterprise capabilities, the architecture supports (in a mocked state):
* Google Sheets API (Data input source)
* Gemini API / AI Tools (`test_gemini_tools.py`) for predictive analytics and anomaly detection on the data.
* AppSheet (`test_appsheet.py`) for mobile triggers.

## 4. Known Limitations & Possible Errors

| Error Scenario | Potential Cause | Suggested Solution |
| :--- | :--- | :--- |
| **Regex Match Failure in Patching** | Changes to the `dashboard.html` template altered the placeholder tags (e.g., `{{DATA}}` became `{{ DATA }}`). | Use robust HTML parsers like `BeautifulSoup` instead of Regex, or strictly enforce template formatting. |
| **Authentication Error (Service Account)** | When connected to real APIs, the `credenciais.json` might expire or lack permissions. | Implement automated credential rotation alerts and ensure IAM roles are correctly assigned to the service account. |
| **Large File Size after Compilation** | Inlining all CSS/JS and base64 images makes the final HTML file too large for browser rendering limits. | Implement gzip compression on the server side and lazy-load non-critical assets. |

## 5. Connecting to a Real Database
To transition this project from mock data to a live database:
1. Provide a valid `credentials.json` for your Google Cloud Project or AWS IAM.
2. In `extract_dashboard.py`, replace the mocked dictionary returns with real API calls using libraries like `google-api-python-client` or `sqlalchemy` for SQL databases.
3. Ensure the structure of the data returned exactly matches the schema expected by the patch scripts (typically a List of Dictionaries).
4. Run the test suite (`python -m unittest discover`) to validate the new connections.

## 6. Future Scalability
* **Real-time Updates:** Move from a static compilation model to a WebSockets approach using FastAPI if real-time dashboard updates are required.
* **Data Lake Integration:** Hook the extraction layer directly into Snowflake or BigQuery to handle millions of rows efficiently before aggregation.
