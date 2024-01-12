import pyodbc
from flask import Flask, render_template

app = Flask(__name__)
server = 'lab8.database.windows.net'
database = 'lab8'
username = 'mprocys'
password = '{Dupadupa123}'
driver = '{ODBC Driver 17 for SQL Server}'


def get_black_products():
    with pyodbc.connect(
            'DRIVER=' + driver + ';SERVER=tcp:' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM [SalesLT].[Product] WHERE Color = 'Black'")
            black_products = [{"Name": row[1], "Color": row[3]} for row in cursor.fetchall()]
    return black_products


def get_addresses():
    with pyodbc.connect(
            'DRIVER=' + driver + ';SERVER=tcp:' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM [SalesLT].[Address] WHERE City = 'Toronto'")
            addresses = [{"City": row[3], "AddressLine1": row[1], "StateProvince": row[4]} for row in cursor.fetchall()]
    return addresses


def get_customer():
    with pyodbc.connect(
            'DRIVER=' + driver + ';SERVER=tcp:' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT TOP (1000) * FROM [SalesLT].[Customer] WHERE Title = 'Mr.'")
            customer = [{"Name": row[3], "Surname": row[5], "EmailAddress": row[9]} for row in cursor.fetchall()]
    return customer


@app.route("/")
def hello_world():
    print('Request for index page received')
    return "<p>Hello, everyone!</p>"


@app.route("/page/<int:page>")
def show_page(page):
    print('Request for index page received')
    return f"<h1>It is a page number: {page}</h1>"


@app.route("/black_products")
def black_product():
    black_products = get_black_products()
    print("Black Products:", black_products)
    return render_template("black_products.html", black_products=black_products)


@app.route("/address")
def address():
    addresses = get_addresses()
    print("Addresses:", addresses)
    return render_template("address.html", address=addresses)


@app.route("/customer")
def customer():
    customer = get_customer()
    print("Customers:", customer)
    return render_template("customer.html", customer=customer)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
