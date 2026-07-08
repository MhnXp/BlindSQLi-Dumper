# 🎯 Fully Customizable Blind SQL Injection Dumper

A powerful, highly configurable Python-based tool designed to automate data extraction via **Boolean-based** and **Time-based Blind SQL Injection**.

Unlike standard tools, this script allows full customization of request headers, HTTP methods, authorization tokens, and injection payloads through a single `config.json` file.

## ✨ Key Features
- **Zero-Code Modification:** Configure target URLs, custom headers (JWT, Cookies), and payloads via `config.json`.
- **Dual Mode Support:** Works with both **Time-based** (`sleep`/`benchmark`) and **Boolean-based** injections.
- **Cross-Database Compatible:** Supports MySQL, PostgreSQL, MSSQL, or custom DBMS payloads.
- **Interactive CLI:** Extract databases, inspect table schemas, and dump specific columns step-by-step.
- **WAF Bypass Friendly:** Fine-tune time thresholds and headers to bypass Security Filters.

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/MhnXp/BlindSQLi-Dumper.git](https://github.com/MhnXp/BlindSQLi-Dumper.git)
   cd BlindSQLi-Dumper