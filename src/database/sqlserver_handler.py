import pyodbc

class SQLServerHandler:
    def __init__(self, server="sqlserver", database="bigdata_crawler", username="sa", password="sapassword"):
        self.conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server},1433;DATABASE={database};UID={username};PWD={password}"
    
    def save_news(self, data):
        if not data:
            return

        conn = pyodbc.connect(self.conn_str)
        cursor = conn.cursor()

        insert_query = """
        INSERT INTO news (title, link, description, category, published_at)
        VALUES (?, ?, ?, ?, ?)
        """

        for item in data:
            cursor.execute(insert_query, item['title'], item['link'], item['description'], item['category'], item['published_at'])

        conn.commit()
        cursor.close()
        conn.close()
    
    def save_products(self, data):
        if not data:
            return
        
        conn = pyodbc.connect(self.conn_str)
        cursor = conn.cursor()

        insert_query = """
        INSERT INTO products (name, price, original_price, discount, merchant, link)
        VALUES (?, ?, ?, ?, ?, ?)
        """

        for item in data:
            cursor.execute(insert_query, item['name'], item['price'], item['original_price'], item['discount'], item['merchant'], item['link'])

        conn.commit()
        cursor.close()
        conn.close()
