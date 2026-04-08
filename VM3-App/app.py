from flask import Flask
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="192.168.2.2",
    user="appuser",
    password="password123",
    database="ecommerce"
)

@app.route('/')
def home():
    cursor = db.cursor()
    cursor.execute("SELECT 'DB CONNECTED'")
    result = cursor.fetchone()
    return result[0]

@app.route('/api')
def api():
    return {"message": "API working"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
