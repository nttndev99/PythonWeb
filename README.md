# BLOG PROJECT
---
## 🚀 Mục Lục

1. [Giới Thiệu](#giới-thiệu)
2. [Cài Đặt](#cài-đặt)
4. [Cấu Trúc Thư Mục](#cấu-trúc-thư-mục)
5. [Công Nghệ - Kiến Thức ](#công-nghệ-kiến-thức)

---

## 📝 Giới Thiệu

**BLOG PROJECT** là một website giúp tạo và đăng bài viết. 
Một số tính năng cơ bản:

- Đăng ký và đăng nhập tài khoản
- Thêm, xóa, sửa bài viết đối với tài khoản được cấp quyền.
- Tìm kiếm bài viết.
- Để lại bình luận trên bài viết.
- Liên hệ với chủ Website bằng cách để lại thông tin email.

Hiện vẫn đang phát triển thêm...

---

## 🧩 Công nghệ - Kiến Thức
```
- UI: Templates(HTML, SCSS, CSS, JavaScript)
- Công cụ hỗ trợ: Git/Github, Notion
- Ngôn ngữ lập trình: Python
- Framework: Flask, Flask API
- Nguyên tắc thiết kế: OOP, MVT Pattern (Model-View-Template) , Clean Code, Clean Architecture
- Mẫu kiến trúc: service-based structure, Client-Server
- Kỹ thuật tương tác dữ liệu: SQLAlchemy (ORM), Jinja
- Cơ sở dữ liệu: SQLite / PostgreSQL
- Data Science:-----------
- Containers:---------
- Sercurity:...........
```

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

---


