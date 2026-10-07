from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


# =================================================
# DATABASE FUNCTION
# Get one product using the first column as ID
# =================================================
def get_product(product_id):

    connection = sqlite3.connect("food.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    # Get all products
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    connection.close()

    # The first column contains FOOD001, FOOD002, etc.
    for row in rows:

        if str(row[0]).upper() == str(product_id).upper():
            return row

    return None


# =================================================
# HOME PAGE
# =================================================
@app.route("/")
def home():

    return render_template("index.html")


# =================================================
# SCAN PAGE
# =================================================
@app.route("/scan")
def scan():

    return render_template("scan.html")


# =================================================
# PRODUCT ID SEARCH
# =================================================
@app.route("/search", methods=["POST"])
def search():

    product_id = request.form["product_id"]

    product = get_product(product_id)

    if product:

        return render_template(
            "result.html",
            product=product
        )

    return """
    <h2>❌ Product not found</h2>
    <br>
    <a href="/scan">
        <button>Try Again</button>
    </a>
    """


# =================================================
# FOOD NAME SEARCH
# =================================================
@app.route("/search-food", methods=["POST"])
def search_food():

    food_name = request.form["food_name"]

    connection = sqlite3.connect("food.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM products WHERE name LIKE ?",
        ("%" + food_name + "%",)
    )

    products = cursor.fetchall()

    connection.close()

    return render_template(
        "search_results.html",
        products=products,
        search=food_name
    )


# =================================================
# QR CODE PRODUCT ROUTE
# =================================================
@app.route("/product/<product_id>")
def product_page(product_id):

    product = get_product(product_id)

    if product:

        return render_template(
            "result.html",
            product=product
        )

    return """
    <h2>❌ Product not found</h2>
    <br>
    <a href="/scan">
        <button>Try Again</button>
    </a>
    """


# =================================================
# DNA VERIFICATION HOME
# Shows ALL food products
# =================================================
@app.route("/dna")
def dna_home():

    connection = sqlite3.connect("food.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    # Get all products
    cursor.execute("SELECT * FROM products")

    rows = cursor.fetchall()

    products = []

    # First column = Product ID
    # name column = Food Name
    for row in rows:

        products.append({
            "product_id": row[0],
            "name": row["name"]
        })

    connection.close()

    return render_template(
        "dna.html",
        products=products
    )


# =================================================
# DNA VERIFICATION FOR ONE PRODUCT
# =================================================
@app.route("/dna/<product_id>", methods=["GET", "POST"])
def dna_verification(product_id):

    result = None

    # Sample DNA reference IDs
    # This is a software demonstration
    dna_database = {

        "FOOD001": "DNA001",
        "FOOD002": "DNA002",
        "FOOD003": "DNA003",
        "FOOD004": "DNA004",
        "FOOD005": "DNA005",
        "FOOD006": "DNA006",
        "FOOD007": "DNA007",
        "FOOD008": "DNA008",
        "FOOD009": "DNA009",
        "FOOD010": "DNA010",
        "FOOD011": "DNA011",
        "FOOD012": "DNA012",
        "FOOD013": "DNA013",
        "FOOD014": "DNA014",
        "FOOD015": "DNA015"

    }

    # Find expected DNA for selected food
    expected_dna = dna_database.get(
        product_id.upper()
    )

    # When Verify DNA button is clicked
    if request.method == "POST":

        dna_id = request.form["dna_id"].strip().upper()

        if expected_dna is not None and dna_id == expected_dna:

            result = "✅ DNA Match - Authentic Food"

        else:

            result = "❌ DNA Mismatch - Possible Adulteration"

    # IMPORTANT:
    # This return is outside the POST block
    return render_template(
        "dna.html",
        product_id=product_id,
        result=result
    )


# =================================================
# RUN FLASK
# =================================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)