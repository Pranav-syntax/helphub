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

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')

@app.route('/all_requests')
def show_all_requests():
    category = request.args.get('category')
    
    if category and category != "All":
        cursor.execute("SELECT name, phone, address, category, description FROM requests WHERE category = %s ORDER BY id DESC", (category,))
    else:
        cursor.execute("SELECT name, phone, address, category, description FROM requests ORDER BY id DESC")
    
    requests_data = cursor.fetchall()
    return render_template("all_requests.html", requests=requests_data, selected_category=category)



    if not query:
        return render_template("search_results.html", results=[], query="")

    sql = """
        SELECT name, phone, address, category, description 
        FROM requests
        WHERE address LIKE %s OR category LIKE %s OR description LIKE %s
    """
    wildcard_query = f"%{query}%"
    cursor.execute(sql, (wildcard_query, wildcard_query, wildcard_query))
    results = cursor.fetchall()

    return render_template("search_results.html", results=results, query=query)


if __name__ == '__main__':
    app.run(debug=True)



