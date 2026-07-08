Markdown
# 🎯 Customizable Blind SQL Injection Dumper

A lightweight, highly customizable Python tool designed to automate data extraction via **Boolean-based** and **Time-based Blind SQL Injection**.

Unlike standard tools, this script allows full customization of request headers (JWT, Cookies, Custom Proxies), HTTP methods, and injection payloads through a single `config.json` file—without editing a single line of Python code.

---

## ✨ Key Features
- **Zero Code Modification:** Change target URLs, HTTP headers, and payloads via `config.json`.
- **Dual Injection Support:** Handles both **Time-based** (`sleep`/`benchmark`) and **Boolean-based** SQLi.
- **Interactive CLI:** Step-by-step interactive menus to enumerate databases, tables, and columns.
- **Cross-Database Compatible:** Easily adapt payloads for MySQL, PostgreSQL, MSSQL, or Oracle.
- **WAF Bypass Friendly:** Fine-tune time thresholds and headers to bypass Security Filters.

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/BlindSQLi-Dumper.git](https://github.com/YOUR_USERNAME/BlindSQLi-Dumper.git)
   cd BlindSQLi-Dumper
Install dependencies:

Bash
pip install -r requirements.txt
🚀 How to Use (Step-by-Step)
Step 1: Configure config.json
Open config.json and adjust the target parameters, custom headers, and your specific payload:

JSON
{
  "target_url": "[http://example.com/api/v1/search](http://example.com/api/v1/search)",
  "method": "POST",
  "target_param": "query",
  "injection_type": "time",
  "time_threshold": 3.0,
  "success_keyword": "Welcome",
  "payload_template": "admin' AND IF(({query}), sleep(3), 0)-- -",
  "headers": {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_TOKEN"
  }
}
Step 2: Run the Script
Execute the main script using Python:

Bash
python main.py -c config.json
📋 Interactive Workflow
When you run the tool, it guides you interactively through the extraction process:

Database Discovery: Automatically extracts the active database name character-by-character.

Table Enumeration: Lists all tables in the database with interactive selection indexes.

Column Extraction: Displays available columns inside the chosen table.

Data Dumping: Dumps the selected columns row by row.

⚠️ Disclaimer
This tool is created strictly for educational purposes and authorized penetration testing. The author assumes no liability for misuse or damage caused by this program.

📜 License
Distributed under the MIT License.
