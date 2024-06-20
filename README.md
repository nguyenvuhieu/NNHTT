# Introduction

- Đồ án: **Ngôn ngữ học tính toán** - *Xây dựng công cụ hỗ trợ phát hiện tương đồng văn bản*
- Giáo viên: Lương An Vinh
- Sinh viên: Đoàn Văn Thanh An - Nguyễn Vũ Hiếu
- Tech stack: ReactJS, Python3, Docker, NLP

# Hướng dẫn cài đặt

## Backend

### Cài đặt [Python](https://www.python.org/downloads/) (3.12+)

### Cấu hình

Hiện tại, đang dùng mongodb từ [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register), có thể DB này sẽ shutdown trong tương lai, vì vậy người dùng có thể config MONGODB_URI trong [backend/config.py](backend/config.py) 

### Cài đặt các thư viện cần thiết

```bash
pip3 install -r requirements.txt
```

### Start sever

```bash
python3 -m uvicorn main:app --reload --port 8000
```

## Frontend

### Tải về các thư viện cần thiết

```bash
npm install
```

### Start app

```bash
npm start
```

# Hướng dẫn chạy bằng docker

## Chạy bằng MongoDB local (lưu trong folder [mongodb](./mongodb))

```bash
docker compose up
```

## Chạy bằng MongoDB cloud

```bash
docker compose -f compose.cloud.yaml up
```
