from aggregation import ShoppingCart,Product

cart = ShoppingCart()

# Products
product_1 = Product('Camiseta',25.90)
product_2 = Product('Agenda',36.50)
product_3 = Product('Calça',99.99)
product_4 = Product('Caneca',15.70)

# Insert products
cart.insert_products(product_3)
cart.insert_products(product_2)
cart.insert_products(product_4)
cart.insert_products(product_1)

# Product list
cart.list_products()

# Total
print(cart.total_sum())
