class TXTHandler:
    def __init__(self, filename):
        self.filename = filename

    def save_data(self, data):
        if not data:
            return

        with open(self.filename, "w", encoding="utf-8") as f:
            for item in data:
                f.write(" | ".join(f"{key}: {value}" for key, value in item.items()) + "\n")
