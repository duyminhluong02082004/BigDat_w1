import os

class PostgresHandler:
    def __init__(self):
        self.enabled = os.getenv("POSTGRES_ENABLED", "false").lower() == "true"
        if self.enabled:
            try:
                import psycopg2
                self.conn = psycopg2.connect(
                    dbname=os.getenv("POSTGRES_DATABASE", "bigdata_db"),
                    user=os.getenv("POSTGRES_USER", "user"),
                    password=os.getenv("POSTGRES_PASSWORD", "password"),
                    host=os.getenv("POSTGRES_HOST", "localhost"),
                    port=os.getenv("POSTGRES_PORT", "5432")
                )
                self.cursor = self.conn.cursor()
                self.create_table()
            except Exception as e:
                print(f"[Postgres] Không thể kết nối: {e}")
                self.enabled = False

    def create_table(self):
        if not self.enabled:
            return
        query = """
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name TEXT,
            price TEXT,
            original_price TEXT,
            discount TEXT,
            merchant TEXT,
            link TEXT
        );
        """
        self.cursor.execute(query)
        self.conn.commit()

    def save_products(self, data):
        if not self.enabled:
            return
        query = """
        INSERT INTO products (name, price, original_price, discount, merchant, link)
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        for item in data:
            self.cursor.execute(query, (
                item.get("name"),
                item.get("price"),
                item.get("original_price"),
                item.get("discount"),
                item.get("merchant"),
                item.get("link"),
            ))
        self.conn.commit()

    def close(self):
        if self.enabled:
            self.cursor.close()
            self.conn.close()

# Test tượng trưng
if __name__ == "__main__":
    handler = PostgresHandler()
    handler.save_products([{
        "name": "Sản phẩm mẫu",
        "price": "1000000",
        "original_price": "1200000",
        "discount": "10%",
        "merchant": "Tiki",
        "link": "https://tiki.vn"
    }])
    handler.close()
