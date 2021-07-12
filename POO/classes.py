class Student:
    def __init__(self, name):
        self.__name = name
        self__tool = None
        
    @property
    def name(self):
        return self.__name
    
    @property
    def tool(self):
        return self.__tool
    
    @tool.setter
    def tool(self, tool):
        self.__tool = tool
        
class Book:
    def __init__(self,matter):
        self.__matter = matter
    
    @property
    def matter(self):
        return self.__matter
    
    def name(self):
        print('O livro é de espanhol!')