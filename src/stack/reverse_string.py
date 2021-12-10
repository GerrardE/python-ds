from stack import StackClass

def reverse_string(string):
    stack = StackClass()

    for i in string:
        stack.push(i)

    reversed = ""

    while not stack.is_empty():
        reversed = reversed + stack.pop()

    return reversed

print("String : Damian = naimaD")
print(reverse_string("Damian"))
print(reverse_string("Educative"))
