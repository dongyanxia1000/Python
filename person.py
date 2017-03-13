       #!/usr/bin/python
       class Person:
            def __init__(self,name):
                self.name = name
            def sayhello(self):
                print('My name is'),self.name
                print('My name is',self.name)
       p = Person('vally')
       print(p)
       print(p.__class__)
       p.sayhello()
       print('===============')
       Person.sayhello(p)
