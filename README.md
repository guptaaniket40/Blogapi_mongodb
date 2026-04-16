# 🛒 Blog API (Django + MongoDB)

A RESTful Blog API built using **Django Rest Framework** and **MongoDB (MongoEngine)**.
This project provides APIs for managing blog posts with full CRUD functionality.

---

## 🚀 Features

* 📝 Create Blog Posts
* 📖 Read All / Single Post
* ✏️ Update Post
* ❌ Delete Post
* ⚡ Fast API using Django REST Framework
* 🍃 MongoDB integration using MongoEngine

---

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** MongoDB
* **ODM:** MongoEngine
* **Environment Management:** python-dotenv

---

## 📁 Project Structure

```
blogapi/
│── myapp/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
│── myproject/
│   ├── settings.py
│   ├── urls.py
│
│── .env
│── manage.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/blogapi.git
cd blogapi
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv myvenv
myvenv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup `.env` file

Create a `.env` file in root directory:

```env
SECRET_KEY=your_secret_key
DEBUG=True
MONGO_URI=mongodb://127.0.0.1:27017/blog_db
```

---

### 5️⃣ Configure MongoDB

Make sure MongoDB is running:

```bash
mongod
```

---

### 6️⃣ Run Server

```bash
python manage.py runserver
```

---

## 🔗 API Endpoints

### 📌 Blog APIs

| Method | Endpoint           | Description     |
| ------ | ------------------ | --------------- |
| GET    | `/api/posts/`      | Get all posts   |
| POST   | `/api/posts/`      | Create post     |
| GET    | `/api/posts/<id>/` | Get single post |
| PUT    | `/api/posts/<id>/` | Update post     |
| DELETE | `/api/posts/<id>/` | Delete post     |

---

## 📦 Example Request

### ➤ Create Post

```json
POST /api/posts/

{
  "title": "My First Blog",
  "content": "This is my blog content",
  "author": "Aniket"
}
```

---

## 📊 Database

* Data is stored in **MongoDB Compass**
* Database Name: `blog_db`
* Collections:

  * posts

---

## ⚠️ Important Notes

* This project uses **MongoDB instead of default Django SQL database**
* Django auth, session, and admin modules are disabled
* Make sure MongoDB is running before starting server

---

## 🧪 Testing

Use tools like:

* Postman
* Thunder Client (VS Code)

---

## 🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

**Aniket Gupta**

---

⭐ If you like this project, don't forget to star the repo!
