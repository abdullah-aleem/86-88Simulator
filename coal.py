#iqra's code

inst = "MOV AX,BX"

def split_instruction():
    x = inst.split(" ")
    print(x)
    y = x[1]
    z = y.split(",")
    print(z)

split_instruction()