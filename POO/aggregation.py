class ShoppingCart:
    def __init__(self):
        self.products = []
        
    def insert_products(self, product):
        self.products.append(product)
        
    def list_products(self):
        for product in self.products:
            print(product.name,product.price)          
            
    def total_sum(self):
        total = 0
        for product in self.products:
            total += product.price
        print()
        return f'O valor total de suas compras é de R$ {total:.2f}'.replace('.',',')
        
class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price