from flask import Flask, request, jsonify, send_from_directory, session, redirect
from flask_cors import CORS
import sqlite3, os, json
from datetime import datetime

app = Flask(__name__)
CORS(app)
app.secret_key = "myshop_secret_123"

# ── Admin credentials ─────────────────────────────────────────
ADMIN_USER = "lafz_admin"
ADMIN_PASS = "Lafz@2026#Secure"

DB = "shop.db"

# ── Database banao ────────────────────────────────────────
def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id          TEXT PRIMARY KEY,
            date        TEXT,
            customer    TEXT,
            phone       TEXT,
            email       TEXT,
            address     TEXT,
            items       TEXT,
            subtotal    REAL,
            delivery    REAL,
            total       REAL,
            status      TEXT DEFAULT 'Pending'
        )
    ''')
    conn.commit()
    conn.close()

# ── HTML files serve karo ────────────────────────────────
@app.route('/')
def home():
    return send_from_directory('.', 'myshop.html')
@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        return redirect('/login')
    return send_from_directory('.', 'admin.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data = request.json
        if data['username'] == ADMIN_USER and data['password'] == ADMIN_PASS:
            session['logged_in'] = True
            return jsonify({'success': True})
        return jsonify({'success': False, 'message': 'Galat username ya password!'})
    return send_from_directory('.', 'login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
# ── Order save karo ──────────────────────────────────────
@app.route('/api/order', methods=['POST'])
def place_order():
    data = request.json
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''
        INSERT INTO orders VALUES (?,?,?,?,?,?,?,?,?,?,?)
    ''', (
        'ORD' + datetime.now().strftime('%Y%m%d%H%M%S'),
        datetime.now().strftime('%d %b %Y, %I:%M %p'),
        data['customer'],
        data['phone'],
        data.get('email', ''),
        data['address'],
        json.dumps(data['items']),
        data['subtotal'],
        data['delivery'],
        data['total'],
        'Pending'
    ))
    conn.commit()
    conn.close()
    return jsonify({'success': True, 'message': 'Order placed!'})

# ── Saare orders admin ke liye ───────────────────────────
@app.route('/api/orders', methods=['GET'])
def get_orders():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('SELECT * FROM orders ORDER BY date DESC')
    rows = c.fetchall()
    conn.close()
    keys = ['id','date','customer','phone','email','address','items','subtotal','delivery','total','status']
    orders = []
    for row in rows:
        o = dict(zip(keys, row))
        o['items'] = json.loads(o['items'])
        orders.append(o)
    return jsonify(orders)

# ── Order status update karo ─────────────────────────────
@app.route('/api/order/<order_id>', methods=['PUT'])
def update_status(order_id):
    data = request.json
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('UPDATE orders SET status=? WHERE id=?', (data['status'], order_id))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

if __name__ == '__main__':
    init_db()
    print("✅ Server is on — localhost:5000")
# Nayi line
app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))