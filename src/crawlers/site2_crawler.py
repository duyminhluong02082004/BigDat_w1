#from .base_crawler import BaseCrawler
from bs4 import BeautifulSoup
from src.crawlers.base_crawler import BaseCrawler


class Site2Crawler(BaseCrawler):
    def __init__(self):
        super().__init__("https://example.com/jobs")

    def parse(self, html):
        """Parse dữ liệu từ HTML"""
        soup = BeautifulSoup(html, "html.parser")
        jobs = []

        for job in soup.select(".job-item"):  # Chỉnh selector theo trang thực tế
            title = job.select_one(".job-title").text.strip()
            company = job.select_one(".company-name").text.strip()
            location = job.select_one(".job-location").text.strip()
            salary = job.select_one(".job-salary").text.strip() if job.select_one(".job-salary") else "N/A"
            link = job.select_one("a")["href"]

            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "salary": salary,
                "link": link
            })

        return jobs
