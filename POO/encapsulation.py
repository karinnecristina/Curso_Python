'''
Public
_ Protected -> Os atributos ou métodos da classe não devem ser acessados
__ -> Private -> É fortemente recomendado que os atributos e os métodos da classe
                 não sejam acessados (reforçando o príncipio do protected)
'''

class DataBase:
    def __init__(self):
        self._data = {}    
        
    def insert_client(self,id,name):
        if 'customers' not in self._data:
            self._data['customers'] = {id:name}
        else:
            self._data['customers'].update({id:name})
            
    def list_customers(self):
        for id, name in self._data['customers'].items():
            print(id,name)
            
    def delete_customers(self,id):
        del self._data['customers'][id]
        
bd = DataBase()

# Insert data:
bd.insert_client(3,'Felipe')
bd.insert_client(15,'Mariana')
bd.insert_client(91,'Adriana')
bd.insert_client(22,'Luiz')

# Remove data:
bd.delete_customers(91)

# List data:
bd.list_customers()