class Person:
    citizenship='Indian'
    def __init__(self,name,gender,age,work):
        self.na=name
        self.gen=gender
        self.age=age
        self.work=work
    def intro(self):
        print(f'Hello, My name is {self.na}.')
        print(f'I am an {Person.citizenship}')
        print(f'I am {self.age} years old, and I am working as {self.work}')
p1=Person("Kunal","M",25,"Doctor")
p1.intro()