from .base_crawler import BaseCrawler
import csv
from src.database.sqlserver_handler import SQLServerHandler  # Import SQL Server Handler
from src.database.txt_handler import TXTHandler  # Import TXTHandler
from src.database.mongo_handler import MongoHandler  # Import MongoDB Handler
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class WebSoSanhCrawler(BaseCrawler):
    name = "websosanh"
    start_urls = ["https://websosanh.vn/"]
    collected_data = []

    def parse(self, response):
        products = []
        for product in response.css('div.product-single'):
            item = {
                'name': product.css('h3.product-single-name a::text').get(),
                'price': product.css('span.product-single-price::text').get(),
                'original_price': product.css('span.product-single-original-price::text').get(),
                'discount': product.css('span.discount::text').get(),
                'merchant': product.css('div.product-single-merchant::text').get(),
                'link': product.css('h3.product-single-name a::attr(href)').get()
            }
            if item['name'] and item['price']:  # Chỉ lưu sản phẩm hợp lệ
                products.append(item)
                yield item

        self.collected_data.extend(products)

        # Lưu vào CSV
        self.save_to_csv(products, "data/csv/websosanh_data.csv")

        # Lưu vào SQL Server
        sql_handler = SQLServerHandler()
        sql_handler.save_products(products)

        # Lưu vào TXT
        txt_handler = TXTHandler("data/txt/websosanh_data.txt")
        txt_handler.save_data(products)

        # Lưu vào MongoDB
        mongo_handler = MongoHandler(db_name="BigDataDB", collection_name="websosanh_products")
        mongo_handler.save_data(products)

    def save_to_csv(self, data, filename):
        if not data:
            return
        keys = data[0].keys()
        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)

# Cho phép chạy độc lập
if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl(WebSoSanhCrawler)
    process.start()
