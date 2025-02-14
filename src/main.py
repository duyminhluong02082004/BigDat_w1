from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from src.crawlers.websosanh_crawler import WebSoSanhCrawler
from src.crawlers.vnexpress_crawler import VnExpressCrawler
from src.database.mysql_handler import MySQLHandler
from src.database.postgres_handler import PostgresHandler
from src.database.mongo_handler import MongoHandler
from src.database.txt_handler import TXTHandler
import csv

def save_to_csv(data, filename):
    """Lưu dữ liệu vào CSV"""
    if not data:
        return
    keys = data[0].keys()
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

def run_crawlers():
    process = CrawlerProcess(get_project_settings())

    print("Đang crawl dữ liệu từ WebSoSanh...")
    process.crawl(WebSoSanhCrawler)

    print("Đang crawl dữ liệu từ VnExpress...")
    process.crawl(VnExpressCrawler)

    process.start()  # Chạy tất cả các crawlers

    # Dữ liệu sau khi crawl sẽ được lưu trong database thông qua pipeline của Scrapy

if __name__ == "__main__":
    run_crawlers()
