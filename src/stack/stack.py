class StackClass():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        self.items.pop(item)

    def is_empty(self):
        return self.items == []
    
    def peek(self):
        return self.items[-1]

    def get_stack(self):
        return self.items


cars = StackClass()

print(cars.is_empty())

cars.push("Bentley")
cars.push("Volvo")
cars.push("Mercedes")

print(cars.is_empty())

print(cars.get_stack())

print(cars.peek())
