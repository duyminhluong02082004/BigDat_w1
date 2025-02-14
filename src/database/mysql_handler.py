import mysql.connector

class MySQLHandler:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="your_user",
            password="your_password",
            database="your_database"
        )
        self.cursor = self.connection.cursor()

    def insert_product(self, product):
        query = """
        INSERT INTO products (name, price, original_price, discount, merchant, link)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (
            product['name'], product['price'], product['original_price'], 
            product['discount'], product['merchant'], product['link']
        ))
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
