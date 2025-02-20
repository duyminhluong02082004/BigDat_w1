import scrapy

class WebsosanhSpiderSpider(scrapy.Spider):
    name = "websosanh_spider"
    allowed_domains = ["websosanh.vn"]
    start_urls = ["https://websosanh.vn"]

    def parse(self, response):
        pass  # Chưa có logic parse dữ liệu

