from flask import Flask, jsonify, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# Consider sourcing these from environment variables for security
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'roottoor'
app.config['MYSQL_DB'] = 'rohith_ece'

mysql = MySQL(app)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         # Process submitted form
#         name = request.form.get('Name')
#         # Validate all fields
#         if not name or name not in allowed_list:  # example check
#             return render_template('register.html', error="Required field missing.")
#         # Insert into database or other logic here
#         return redirect(url_for('home'))
#     # GET request: show the empty form
#     return render_template('register.html')

# @app.route('/register')
# def register():
#     return render_template('register.html')

@app.route('/myweb',methods=['GET'])
def myweb():
    return render_template("index.html")


@app.route('/myname')
def print_my_name():
    return "your name"

@app.route('/people_detail', methods=['GET'])
def user_detail():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM people")
    results = cur.fetchall()
    col_names = [desc[0] for desc in cur.description]
    data = [dict(zip(col_names, row)) for row in results]
    cur.close()
    return jsonify(data)

@app.route('/add', methods=['POST'])
def add():
    form = request.form
    fields = ('id', 'Name', 'Email', 'Password', 'City')
    if not all(field in form for field in fields):
        return "Missing form data", 400

    values = tuple(form[f] for f in fields)
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO people (id, Name, Email, Password, City) VALUES (%s, %s, %s, %s, %s)",
        values
    )
    mysql.connection.commit()
    cur.close()
    return "Register success", 201

if __name__ == '__main__':
    app.run(debug=True)
