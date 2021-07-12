from classes import Student,Book

student = Student('Pedro')
book = Book('Espanhol')

print(student.name)
print(book.matter)
print()

# Association
student.tool = book
student.tool.name()
