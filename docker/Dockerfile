# Sử dụng Python 3.12 làm base image
FROM python:3.12

# Cài đặt các gói cần thiết
RUN apt-get update && apt-get install -y \
    unixodbc \
    unixodbc-dev \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Tạo thư mục làm việc
WORKDIR /app

# Sao chép toàn bộ mã nguồn vào container
COPY src /app/src
COPY requirements.txt /app/requirements.txt

# Cài đặt các thư viện Python
RUN pip install --no-cache-dir -r /app/requirements.txt

# Chạy Scrapy khi container khởi động
CMD ["python", "-m", "src.main"]
