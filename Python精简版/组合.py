class Eye:

    def __init__(self, color):
        self.color = color


class Person:

    def __init__(self, eye):
        self.eye = eye

    def show(self):
        print(self.eye.color)


eye = Eye("黑色")
p = Person(eye)
p.show()
