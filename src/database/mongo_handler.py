from pymongo import MongoClient

class MongoHandler:
    def __init__(self, db_name="BigDataDB", collection_name="products"):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def save_data(self, data):
        if data:
            self.collection.insert_many(data)
            print(f"✅ Đã lưu {len(data)} bản ghi vào MongoDB!")

# Kiểm tra kết nối
if __name__ == "__main__":
    mongo = MongoHandler()
    test_data = [{"name": "Sản phẩm A", "price": "100,000"}]
    mongo.save_data(test_data)
