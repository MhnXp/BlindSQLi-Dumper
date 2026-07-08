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
git clone [https://github.com/MhnXp/BlindSQLi-Dumper.git](https://github.com/YOUR_USERNAME/BlindSQLi-Dumper.git)
