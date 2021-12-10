from stack import StackClass

def check_brackets(brackets):
    items = StackClass()

    for i in brackets:
        if i in "{[<(":
            items.push(i)
        else:
            if not is_balanced(items.pop(), i):
                return False

    if items.is_empty():
        return True

    return False     

def is_balanced(b1, b2):
    if b1 == "{" and b2 == "}":
        return True
    if b1 == "(" and b2 == ")":
        return True
    if b1 == "[" and b2 == "]":
        return True
    if b1 == "<" and b2 == ">":
        return True
    return False

print("String : (((({})))) Balanced or not?")
print(check_brackets("{(((())))}"))

print("String : [][]]] Balanced or not?")
print(check_brackets("[][]]]"))

print("String : [][] Balanced or not?")
print(check_brackets("[][]"))
