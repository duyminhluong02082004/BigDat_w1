import pyodbc

server = "DESKTOP-V6HMFRN"
database = "bigdata_crawler"
username = "sa"
password = "sapassword"

try:
    conn_str = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("SELECT 1")  # Kiểm tra truy vấn đơn giản
    print("✅ Kết nối SQL Server thành công!")
    conn.close()
except Exception as e:
    print("❌ Lỗi kết nối SQL Server:", e)
