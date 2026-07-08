# 🎯 Customizable Blind SQL Injection Dumper

A lightweight, high-performance, and fully customizable Python tool designed to automate data extraction via **Boolean-based** and **Time-based Blind SQL Injection**.

Unlike standard automated tools, this script allows full control over request headers (JWT, Cookies, Custom Proxies), HTTP methods, and injection payloads through a single `config.json` file—without editing a single line of Python code.

---

## 📊 Technical Specifications & Benchmarks

| Metric / Parameter | Value / Specification |
| :--- | :--- |
| **01. Extraction Speed** | ~1 to 3 characters/second (Time-based dependent on delay) |
| **02. Max String Length** | Up to **50 characters** per query (Configurable) |
| **03. Max Table Limits** | Up to **15 tables** enumerated per loop |
| **04. Max Column Limits** | Up to **15 columns** enumerated per table |
| **05. Max Row Dumping** | **20 rows** extracted per session |
| **06. Default Time Threshold** | **3.0 seconds** delay detection |
| **07. Supported Protocols** | HTTP / HTTPS (with SSL bypass) |

---

## ✨ Key Features

1. **Zero Code Modification:** Change target URLs, HTTP headers, and payloads via `config.json`.
2. **Dual Injection Support:** Handles both **Time-based** (`sleep`/`benchmark`) and **Boolean-based** SQLi.
3. **Interactive CLI:** Step-by-step interactive menus to enumerate databases, tables, and columns.
4. **Cross-Database Compatible:** Easily adapt payloads for MySQL, PostgreSQL, MSSQL, or Oracle.
5. **WAF Bypass Friendly:** Fine-tune time thresholds (e.g., `1.5s` to `5.0s`) and headers to bypass Security Filters.

---

## 🛠️ Installation & Setup

### Step 1: Clone the repository
```bash
git clone [https://github.com/MhnXp/BlindSQLi-Dumper.git](https://github.com/MhnXp/BlindSQLi-Dumper.git)
```
## Step 2: Navigate to directory
```bash
cd BlindSQLi-Dumper
```
## Step 3: Install dependencies
```bash
pip install -r requirements.txt
```
## 🚀 How to Use (Step-by-Step Guide)
Step 1: Configure config.json
Open config.json and adjust the target parameters, custom headers, and your specific payload:
```JSON
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
```
## Step 2: Run the Script
Execute the main script using Python:
```bash
python dumper.py -c config.json
```
## 📋 Interactive Workflow (4 Stages)
When you run the tool, it guides you interactively through the extraction process across 4 distinct stages:

 Stage 1 - Database Discovery: Automatically extracts the active database name character-by-character (1-50 chars).

 Stage 2 - Table Enumeration: Lists up to 15 tables in the active database with interactive selection indexes ([0] to [14]).

 Stage 3 - Column Extraction: Displays up to 15 available columns inside the selected table.

 Stage 4 - Data Dumping: Dumps the selected columns row-by-row (up to 20 rows per execution run).
 

## ⚠️ Disclaimer
This tool is created strictly for educational purposes and authorized penetration testing. The author assumes no liability for misuse or damage caused by this program.

## 📜 License
Distributed under the MIT License.



