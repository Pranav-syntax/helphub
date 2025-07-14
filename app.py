from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",  
    database="helphub"
)

cursor = db.cursor()

# ✅ Home route should render index.html
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/info')
def info():
    return render_template('info.html')



# ✅ Submit route handles form submission
@app.route('/submit', methods=['POST'])
def submit_request():
    name = request.form.get('name')
    phone = request.form.get('phone')
    address = request.form.get('address')
    category = request.form.get('category')
    description = request.form.get('description')

    sql = """
        INSERT INTO requests (name, phone, address, category, description)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (name, phone, address, category, description)
    cursor.execute(sql, values)
    db.commit()

    return render_template("success.html")

# ✅ Optional route to open the form directly
@app.route('/form')
def show_form():
    return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True)



