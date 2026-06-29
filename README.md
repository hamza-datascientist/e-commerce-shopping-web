# 🛍️ Lafz Collection

> A full-stack e-commerce web application for a modern fashion brand — built with Python, Flask, and vanilla HTML/CSS/JS.

---

## 📌 About The Project

**Lafz Collection** is a fully functional e-commerce platform built from scratch — no frameworks, no templates. This project demonstrates end-to-end web development including a customer-facing storefront, a real SQLite database, REST API design, and a secure admin dashboard.

Built as a portfolio project to showcase practical skills in backend development, database management, and UI design — relevant to both software development and data analyst roles.

---

## ✨ Features

### 🛒 Customer Side
- Browse products with search and category filter
- Add to cart with quantity management
- Free delivery logic (orders above ₹999)
- Checkout form with validation
- Order confirmation with unique Order ID

### 🔐 Admin Panel
- Secure login (username + password protected)
- Real-time order dashboard
- View customer details — name, phone, email, address
- Filter orders by status (Pending, Confirmed, Shipped, Delivered, Cancelled)
- Update order status with one click
- Revenue tracking and order statistics
- Auto-refresh every 30 seconds

### 🗄️ Backend & Database
- REST API built with Python Flask
- SQLite database for persistent order storage
- Session-based admin authentication
- CORS enabled for frontend-backend communication

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Backend | Python, Flask |
| Database | SQLite |
| Auth | Flask Sessions |
| Hosting (local) | Flask Dev Server |

---

## 🚀 Getting Started

## Access

| Page | URL |
|------|-----|
| 🛍️ Shop | `http://127.0.0.1:5000` |
| 🔐 Admin | `http://127.0.0.1:5000/admin` |
---

## 📊 Database Schema

```sql
CREATE TABLE orders (
    id          TEXT PRIMARY KEY,   -- Unique Order ID (e.g. ORD20260628120000)
    date        TEXT,               -- Order date and time
    customer    TEXT,               -- Customer full name
    phone       TEXT,               -- Contact number
    email       TEXT,               -- Email (optional)
    address     TEXT,               -- Full delivery address
    items       TEXT,               -- JSON array of ordered items
    subtotal    REAL,               -- Order subtotal
    delivery    REAL,               -- Delivery charges
    total       REAL,               -- Final total
    status      TEXT                -- Pending / Confirmed / Shipped / Delivered / Cancelled
)
```
---

## 📈 What I Learned

- Designing and querying a **relational database** (SQLite)
- Building a **REST API** from scratch using Flask
- **Session-based authentication** for route protection
- **Frontend-backend integration** using Fetch API
- **JSON data handling** between Python and JavaScript
- Real-world **e-commerce flow** — cart, checkout, order management

---

## 👤 Author

**Hamza Siddiqui**
- GitHub: [Hamza siddiqui](https://github.com/hamza-datascientist/e-commerce-shopping-web)
- LinkedIn: [Hamza-datascientist](https://www.linkedin.com/in/hamza-siddiqui-990b48330/)

---