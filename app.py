from flask import Flask, jsonify,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'roottoor'
app.config['MYSQL_DB'] = 'rohith_ece'
mysql = MySQL(app)

# Routes
@app.route('/')
def hello():
    return 'Hello, Flask!'

@app.route('/category')
def category():
    return render_template('category.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/listing')
def listing():
    return render_template('listing.html')

# @app.route('/myweb', methods=['GET'])
# def myweb():
#     return render_template("index.html")

@app.route("/index", methods=["GET"])
def index():
    sql = "SELECT * FROM people"
    cur = mysql.connection.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    return render_template("index.html",result=result)

# Start the server
if __name__ == '__main__':
    app.run(debug=True)
