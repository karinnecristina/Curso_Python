''' Criando a classe pessoa'''

class Pessoa:
    ano_atual = 2019
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self): # Método de instância
        print(self.ano_atual - self.idade)
        
    @classmethod # Método da classe    
    def ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
        
        
p1 = Pessoa('Luiz', 32)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
    