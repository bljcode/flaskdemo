import json

class you:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class people:
    def __init__(self, name, age, you):
        self.name = name
        self.age = age
        self.you = you

if __name__ == '__main__':
    y = you(5,3)
    t = people('f',13,y)
    #自定义对象this must  default=lambda obj: obj.__dict__
    print(json.dumps(t, default=lambda obj: obj.__dict__))


