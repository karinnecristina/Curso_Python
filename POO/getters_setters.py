import re

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
    def discount(self,percentage):
        self.price = self.price - round((self.price * (percentage) / 100),2) # Calculando o desconto e arredondando o valor para 2 casas decimais
        
    # Getter
    @property
    def price(self):
        return self._price
    
    # Setter
    @price.setter
    def price(self,value):
        if isinstance(value, str):
            value = float(re.findall(r'[\d]*[.][\d]+|[\d]+',value)[0]) # Extrai apenas o valor se o parâmetro informado for uma string
        self._price = value
        

product_1 = Product('Camiseta',50)
product_1.discount(10)
print(product_1.price)
    
product_2 = Product('Caneca','R$39.90')
product_2.discount(5)
print(product_2.price)