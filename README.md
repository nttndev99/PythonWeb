# BLOG PROJECT
---
## 🚀 Mục Lục

1. [Mục Tiêu Dự Án](#mục-tiêu-dự-án)
2. [Kiến Trúc Hệ Thống ](#kiến-trúc-hệ-thống)
3. [Luồng Tương Tác Người Dùng](#luồng-tương-tác)
4. [Cài Đặt](#cài-đặt)
5. [Cấu Trúc Thư Mục](#cấu-trúc-thư-mục)
5. [Chức Năng Phát Triển](#chức-năng-đang-phát-triển)

---

## 📝 MỤC TIÊU DỰ ÁN

**BLOG PROJECT** Xây dựng ứng dụng web tích hợp: 
Hệ thống quản lý bài viết (Giao diện form + WTforms):

- Thêm, xóa, sửa bài viết đối với tài khoản được cấp quyền
- Tìm kiếm bài viết
- Pagination
- Để lại bình luận trên bài viết
- Liên hệ với chủ Website bằng cách để lại thông tin email smtplib

Đăng ký, đăng nhập tài khoản

- Đăng ký: Lưu hash password
- Đăng nhập tài khoản: Kiểm tra thông tin và lưu session
- Logout: Xóa session
- Flask-Login: Quản lý phiên đăng nhập

Tạo API có tài liệu Swagger: Flask-RESTful Api + Swagger

- /api: get, post, patch, delete JSON
- /api/predit: Dự đoán inpute qua query hoặc JSON
- /apidocs: Giao diện Swagger UI
- Flasgger: Ghi tài liệu trực tiếp trong docstring bằng YAML

Phân tích dữ liệu CSV do người dùng tải lên

- Upload file: Giao diện tải lên file .csv
- Hiển thị dữ liệu: Dùng pandas để show bảng
- Trực quan hóa dữ liệu: Dùng matplotlib/searborn/plotly
- Thống kê: Dùng numpy thống kê chỉ số cơ bản

Tích hợp (Machine Learning model) + Flask API

- Model: scikit-learn
- Lưu model: joblib.dump()
- Sử dụng: Nạp lại model từ .pkl và trả về dự đoán
- Giao diện: Người dùng nhập input từ form, hiển thị kết quả dự đoán

---

## 🧱 KIẾN TRÚC HỆ THỐNG
Framework: Flask (service-based structure, Flask Blueprint)
ORM: SQLAIchemy
Database: SQLite, PostgreSQL
Authentication: Flask-Login
API Docs: Flasgger (Swagger UI)
Machine Learning model: scikit-learn (lưu bằng joblib)
Phân tích CSV: pandas, numpy, matplotlib, seaborn
Tools: Git/Github, Notion
Deployment: Docker / Heroku / Render

---

## 🔄 LUỒNG TƯƠNG TÁC NGƯỜI DÙNG
- Đăng nhập / Đăng ký
- Quản lý bài viết 
- Tải lên file CSV -> phân tích và trực quan hóa
- Gửi dữ liệu đầu vào đến mô hình -> xem kết quả dự đoán
- Dev sử dụng Swagger API để gửi request

---

## ⚙️ Cài Đặt

### 1. Clone Dự Án
```
git clone https://github.com/nttndev99/PythonWeb.git
cd PythonWeb 
```


### 2. Cài đặt môi trường
```
powershell
python -m venv venv
```

#### Bypass to activate powershel (nếu cần)
```
powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
Hoặc
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser
```

#### Activate
```
powershell 
.\venv\Scripts\Activate.ps1
```


### 3. Cài đặt các phụ thuộc
```
powershell
pip install -r requirements.txt
```


### 4. Chạy ứng dụng
```
powershell 
flask run
```

```
Local 
http://127.0.0.1:5000
```

---

## 📂 Cấu Trúc Thư Mục
```
/BLOG-CAPSTONE_PROJECT
    /app
        /forms
        /models
        /routes
            /api
            /web
        /services
        /static
            /assets
            /css
            /js
            /sass
            /webfonts
        /templates
        __init__.py
        config.py
        extensions.py
        seeds.py
    .gitignore
    requirements.txt
    README.md
    run.py
```

## 🧩 CHỨC NĂNG ĐÃ VÀ ĐANG PHÁT TRIỂN
### ✅ Đã hoàn thành:
- Hệ thống quản lý bài viết (Giao diện form + WTforms)
- Đăng ký, đăng nhập tài khoản

### 🚧 Đang phát triển:
- Tạo API có tài liệu Swagger: Flask-RESTful Api + Swagger
- Phân tích dữ liệu CSV do người dùng tải lên
- Tích hợp (Machine Learning model) + Flask API



