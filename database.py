import sqlite3

connection = sqlite3.connect("food.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id TEXT PRIMARY KEY,
    name TEXT,
    category TEXT,
    ingredients TEXT,
    allergens TEXT,
    calories TEXT,
    protein TEXT,
    carbohydrates TEXT,
    fat TEXT,
    food_type TEXT
)
""")

products = [

    (
        "FOOD001",
        "Chocolate Biscuit",
        "Bakery",
        "Wheat flour, Sugar, Vegetable oil, Milk, Salt",
        "Gluten, Milk",
        "480 kcal / 100g",
        "6 g",
        "68 g",
        "20 g",
        "Vegetarian"
    ),

    (
        "FOOD002",
        "Milk Chocolate",
        "Chocolate",
        "Cocoa, Sugar, Milk, Cocoa butter",
        "Milk",
        "535 kcal / 100g",
        "7 g",
        "59 g",
        "30 g",
        "Vegetarian"
    ),

    (
        "FOOD003",
        "Potato Chips",
        "Snacks",
        "Potato, Vegetable oil, Salt",
        "None",
        "540 kcal / 100g",
        "6 g",
        "53 g",
        "34 g",
        "Vegetarian"
    ),

    (
        "FOOD004",
        "Instant Noodles",
        "Noodles",
        "Wheat flour, Palm oil, Salt, Spices",
        "Gluten",
        "450 kcal / 100g",
        "9 g",
        "60 g",
        "18 g",
        "Vegetarian"
    ),

    (
        "FOOD005",
        "Fruit Juice",
        "Beverage",
        "Water, Fruit concentrate, Sugar",
        "None",
        "45 kcal / 100ml",
        "0 g",
        "11 g",
        "0 g",
        "Vegetarian"
    ),

    (
        "FOOD006",
        "Bread",
        "Bakery",
        "Wheat flour, Water, Yeast, Sugar, Salt",
        "Gluten",
        "265 kcal / 100g",
        "9 g",
        "49 g",
        "3 g",
        "Vegetarian"
    ),

    (
        "FOOD007",
        "Cheese",
        "Dairy",
        "Milk, Salt, Starter culture",
        "Milk",
        "402 kcal / 100g",
        "25 g",
        "1 g",
        "33 g",
        "Vegetarian"
    ),

    (
        "FOOD008",
        "Strawberry Yogurt",
        "Dairy",
        "Milk, Strawberry, Sugar, Yogurt culture",
        "Milk",
        "95 kcal / 100g",
        "4 g",
        "14 g",
        "3 g",
        "Vegetarian"
    ),

    (
        "FOOD009",
        "Popcorn",
        "Snacks",
        "Corn, Vegetable oil, Salt",
        "None",
        "375 kcal / 100g",
        "12 g",
        "74 g",
        "4 g",
        "Vegetarian"
    ),

    (
        "FOOD010",
        "Apple Juice",
        "Beverage",
        "Apple juice, Water, Sugar",
        "None",
        "46 kcal / 100ml",
        "0 g",
        "11 g",
        "0 g",
        "Vegetarian"
    ),

    (
        "FOOD011",
        "Pasta",
        "Pasta",
        "Durum wheat, Water",
        "Gluten",
        "350 kcal / 100g",
        "13 g",
        "72 g",
        "2 g",
        "Vegetarian"
    ),

    (
        "FOOD012",
        "Chocolate Cake",
        "Bakery",
        "Wheat flour, Sugar, Cocoa, Milk, Eggs, Butter",
        "Gluten, Milk, Eggs",
        "371 kcal / 100g",
        "5 g",
        "53 g",
        "16 g",
        "Vegetarian"
    ),

    (
        "FOOD013",
        "Corn Flakes",
        "Breakfast",
        "Corn, Sugar, Salt, Malt flavor",
        "None",
        "357 kcal / 100g",
        "7 g",
        "84 g",
        "0.4 g",
        "Vegetarian"
    ),

    (
        "FOOD014",
        "Tomato Soup",
        "Soup",
        "Tomato, Water, Salt, Spices",
        "None",
        "40 kcal / 100g",
        "1 g",
        "8 g",
        "0.5 g",
        "Vegetarian"
    ),

    (
        "FOOD015",
        "Salted Peanuts",
        "Snacks",
        "Peanuts, Salt, Vegetable oil",
        "Peanuts",
        "567 kcal / 100g",
        "26 g",
        "16 g",
        "49 g",
        "Vegetarian"
    )
]

cursor.executemany("""
INSERT OR REPLACE INTO products
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", products)

connection.commit()
connection.close()

print("Database created successfully!")