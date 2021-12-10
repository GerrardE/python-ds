from stack import StackClass

def convert_int_to_bin(dec_num):
    stack = StackClass()
    
    while dec_num > 0:
        stack.push(dec_num % 2)
        dec_num = dec_num // 2

    bin = []
    while not stack.is_empty():
        bin.append(stack.pop())

    return bin

print("Num : 242 = 11110010")
print(convert_int_to_bin(242))
