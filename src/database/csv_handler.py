import csv

class CSVHandler:
    def __init__(self, filename="data/csv/websosanh_data.csv"):
        self.filename = filename

    def save(self, data):
        if not data:
            return
        keys = data[0].keys()
        with open(self.filename, mode="w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
