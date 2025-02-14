from .base_crawler import BaseCrawler
import csv
from src.database.sqlserver_handler import SQLServerHandler  # Import SQL Server Handler
from src.database.txt_handler import TXTHandler  # Import TXTHandler
from src.database.mongo_handler import MongoHandler  # Import MongoDB Handler
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class VnExpressCrawler(BaseCrawler):
    name = "vnexpress"
    start_urls = ["https://vnexpress.net/"]
    collected_data = []

    def parse(self, response):
        articles = []
        for article in response.css('article.item-news'):
            item = {
                'title': article.css('h3.title-news a::text').get(),
                'link': article.css('h3.title-news a::attr(href)').get(),
                'description': article.css('p.description a::text').get(),
                'category': response.url.split('/')[3] if len(response.url.split('/')) > 3 else 'Trang chủ',
                'published_at': article.css('span.time-ago::text').get()
            }
            if item['title'] and item['link']:  # Chỉ lưu bài viết hợp lệ
                articles.append(item)
                yield item

        self.collected_data.extend(articles)

        # Lưu vào CSV
        self.save_to_csv(articles, "data/csv/vnexpress_data.csv")

        # Lưu vào SQL Server
        sql_handler = SQLServerHandler()
        sql_handler.save_news(articles)

        # Lưu vào TXT
        txt_handler = TXTHandler("data/txt/vnexpress_data.txt")
        txt_handler.save_data(articles)

        # Lưu vào MongoDB
        mongo_handler = MongoHandler(db_name="BigDataDB", collection_name="vnexpress_news")
        mongo_handler.save_data(articles)

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
    process.crawl(VnExpressCrawler)
    process.start()
