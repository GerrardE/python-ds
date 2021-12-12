from stack import StackClass

def convert_int_to_bin(dec_num):
    if dec_num == 0:
        return 0

    stack = StackClass()
    
    while dec_num > 0:
        stack.push(dec_num % 2)
        dec_num = dec_num // 2

    bin = ""
    
    while not stack.is_empty():
        bin = bin + str(stack.pop())

    return bin

print("Num : 242 = 11110010")
print(convert_int_to_bin(242))

print("\nNum : 0 = 0")
print(convert_int_to_bin(0))
