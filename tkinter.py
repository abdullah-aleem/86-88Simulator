# tkinter window
from tkinter import *
window = Tk()
window.title("Main Window")
window.geometry("750x600")
window.configure(background='light blue')
opcode = {
    "MOV": '100010', "SUB": '000101', "XOR": '000110', "INC": '111111',
    "NEG": '111101', "DIV": '111101', "MUL": '111101', "OR": '000010',
    "ADD": '000000', "NOT": '111101', "IMUL": '111101', "IDIV": '111101',
    "DEC": '111111', "AND": '001000', "": ''}

# backend code
reg0={
    "AL": "000","CL": "001","DL": "010","BL": "011",
    "AH": "100","CH": "101","DH": "100","BH": "111" }

# reg0 = {
#     "AX": "000", "CX": "001", "DX": "010", "BX": "011",
#     "SP": "100", "BP": "101", "SI": "100", "DI": "111"}

# contents of memory locations
contents_mem = {"M0000": "00", "M0001": "00", "M0010": "00", "M0011": "00", "M0100": "00",
                "M0101": "00", "M0110": "00", "M0111": "00", "M1000": "00", "M1001": "00", "M1010": "00", "M1011": "00",
                "M1100": "00", "M1101": "00", "M1110": "00", "M1111": "00"}

# contents of 16 bits registers
contents_reg0 = {"AX": "0000", "CX": "0000", "DX": "0000",
                 "BX": "0000", "SP": "0000", "BP": "0000", "SI": "0000", "DI": "0000"}


operand1 = ""
operand2 = ""
D = 1
word = 1
MOD = '11'


def getvals():
    start()
    Label(window, text='10101010 00001111', font='ar 9').grid(row=4, column=3)


def tohex(val, nbits):
    return hex((val + (1 << nbits)) % (1 << nbits))


def Direction():
    global D
    if operand1[0] == "[":
        D = 0


def MOD_1():
    global MOD
    if operand1[0] == "[" and operand2 in reg0:
        MOD = '00'
    elif operand1 in reg0 and operand2[0] == "[":
        MOD = '00'


# Heading
Label(window, text='Assembly Language to Machine Code Convertor',
      font='ar 11 bold', pady=30).grid(row=0, column=3)


def start():
    global D, word, MOD, operand1, operand2, reg0, contents_reg0, contents_mem, opcode
    result=""
    mmm = 111
    D = 1
    word = 1
    MOD = '11'
    bool = False
    inst =str(instructionvalue.get()) 
    x = inst.split(" ")
    opr = x[0]
    y = x[1]
    length = len(inst)
    if length > 7:
        bool = True
        z = y.split(",")
        operand1 = z[0]
        operand2 = z[1]
    match opr:
        case "MOV" | "SUB" | "OR" | "XOR" | "ADD" | "AND":
            Direction()
            MOD_1()
            if operand1 in reg0 and operand2 in reg0:
                if opr == "AND":
                    contents_reg0[operand1] = str(hex(int(contents_reg0[operand1], 16) & int(
                        contents_reg0[operand2], 16)).lstrip('0x'))
                    print(contents_reg0[operand1])
                elif opr == "OR":
                    contents_reg0[operand1] = str(hex(int(contents_reg0[operand1], 16) | int(
                        contents_reg0[operand2], 16)).lstrip('0x'))
                    print(contents_reg0[operand1])
                elif opr == "XOR":
                    contents_reg0[operand1] = str(hex(int(contents_reg0[operand1], 16) ^ int(
                        contents_reg0[operand2], 16)).lstrip('0x'))
                    print(contents_reg0[operand1])
                elif opr == "ADD":
                    dec = (int(contents_reg0[operand1], 16)) + \
                        (int(contents_reg0[operand2], 16))
                    contents_reg0[operand1] = str((hex(dec).lstrip('0x')))
                elif opr == "MOV":
                    contents_reg0[operand1] = str(contents_reg0[operand2])
                elif opr == "SUB":
                    dec = (int(contents_reg0[operand1], 16)) - \
                        (int(contents_reg0[operand2], 16))
                    contents_reg0 = str((hex(dec).lstrip('0x')))
                result=str(opcode[opr], D, word, MOD, reg0[operand1], reg0[operand2])
                Label(window, text=str(
                    opcode[opr], D, word, MOD, reg0[operand1], reg0[operand2]), font='ar 9').grid(row=4, column=3)
            elif operand1[0] == "[" and operand2 in reg0:
                operand1 = operand1.lstrip("[")
                operand1 = operand1.rstrip("]")
                print(operand1)
                if opr == "AND":
                    contents_mem[operand1] = str(hex(int(contents_mem[operand1], 16) & int(
                        contents_reg0[operand2], 16)).lstrip('0x'))
                    print(contents_mem[operand1])
                elif opr == "OR":
                    contents_mem[operand1] = str(hex(int(contents_mem[operand1], 16) | int(
                        contents_reg0[operand2], 16)).lstrip('0x'))
                    print(contents_mem[operand1])
                elif opr == "XOR":
                    contents_mem[operand1] = str(hex(int(contents_mem[operand1], 16) ^ int(
                        contents_reg0[operand2], 16)).lstrip('0x'))
                    print(contents_mem[operand1])
                elif opr == "ADD":
                    dec = (int(contents_mem[operand1], 16)) + \
                        (int(contents_reg0[operand2], 16))
                    contents_mem[operand1] = str((hex(dec).lstrip('0x')))
                elif opr == "MOV":
                    contents_mem[operand1] = str(contents_reg0[operand2])
                elif opr == "SUB":
                    dec = (int(contents_mem[operand1], 16)) - \
                        (int(contents_reg0[operand2], 16))
                    contents_mem = str((hex(dec).lstrip('0x')))
                result=str(opcode[opr], D, word, MOD, mmm, reg0[operand2])
                Label(window, text=str(opcode[opr], D, word, MOD, mmm, reg0[operand2]), font='ar 9').grid(row=4, column=3)

            elif operand1 in reg0 and operand2[0] == "[":
                operand2 = operand2.lstrip("[")
                operand2 = operand2.rstrip("]")
                print(operand2)
                if opr == "AND":
                    contents_reg0[operand1] = str(hex(int(contents_reg0[operand1], 16) & int(
                        contents_mem[operand2], 16)).lstrip('0x'))
                    print(contents_reg0[operand1])
                elif opr == "OR":
                    contents_reg0[operand1] = str(hex(int(contents_reg0[operand1], 16) | int(
                        contents_mem[operand2], 16)).lstrip('0x'))
                    print(contents_reg0[operand1])
                elif opr == "XOR":
                    contents_reg0[operand1] = str(hex(int(contents_reg0[operand1], 16) ^ int(
                        contents_reg0[operand2], 16)).lstrip('0x'))
                    print(contents_reg0[operand1])
                elif opr == "ADD":
                    dec = (int(contents_reg0[operand1], 16)) + \
                        (int(contents_mem[operand2], 16))
                    contents_reg0[operand1] = str((hex(dec).lstrip('0x')))
                elif opr == "MOV":
                    contents_reg0[operand1] = str(contents_mem[operand2])
                elif opr == "SUB":
                    dec = (int(contents_reg0[operand1], 16)) - \
                        (int(contents_mem[operand2], 16))
                    contents_reg0 = str((hex(dec).lstrip('0x')))
                Label(window, text=str(opcode[opr], D, word, MOD, reg0[operand1], mmm), font='ar 9').grid(row=4, column=3)
                

        case "NEG":
            rrr = "011"
            contents_reg0[y] = str(
                (tohex(int(contents_reg0[y]*-1, 16), 8).lstrip('0x')))
        case "DIV":
            rrr = '110'

        case "INC":
            rrr = "000"
            dec = int(contents_reg0[y], 16)+1
            print(hex(dec).lstrip('0x'))
        case "MUL":
            rrr = "100"

        case "NOT":
            rrr = '010'
            contents_reg0[y] = str(
                hex((~int(contents_reg0[y], 16))).replace('0x', ""))
            print(contents_reg0[y])
        case "IMUL":
            rrr = "101"
        case "IDIV":
            rrr = "111"
        case "DEC":
            rrr = '001'
            dec = int(contents_reg0[y], 16)-1
            print(tohex(dec, 64).lstrip('0x'))
    if bool == False:
        print(opcode[opr], D, word, MOD, rrr, reg0[y])
    sets()

# Field name
instruction = Label(window, text='Enter instruction:',
                    font='ar 9', padx=30, pady=20)
output = Label(window, text='Output:', font='ar 9', pady=20)
# Creating registers
reg1 = Label(window, text='Reg1:', font='ar 9')
reg2 = Label(window, text='Reg2:', font='ar 9')
reg3 = Label(window, text='Reg3:', font='ar 9')
reg4 = Label(window, text='Reg4:', font='ar 9')
reg5 = Label(window, text='Reg5:', font='ar 9')
reg6 = Label(window, text='Reg6:', font='ar 9')
reg7 = Label(window, text='Reg7:', font='ar 9')
reg8 = Label(window, text='Reg8:', font='ar 9')
# Creating memory locations
mem1 = Label(window, text='0000', font='ar 9', padx=10)
mem2 = Label(window, text='0001', font='ar 9', padx=10)
mem3 = Label(window, text='0010', font='ar 9', padx=10)
mem4 = Label(window, text='0011', font='ar 9', padx=10)
mem5 = Label(window, text='0100', font='ar 9', padx=10)
mem6 = Label(window, text='0101', font='ar 9', padx=10)
mem7 = Label(window, text='0110', font='ar 9', padx=10)
mem8 = Label(window, text='0111', font='ar 9', padx=10)

mem9 = Label(window, text='1000', font='ar 9', padx=10)
mem10 = Label(window, text='1001', font='ar 9', padx=10)
mem11 = Label(window, text='1010', font='ar 9', padx=10)
mem12 = Label(window, text='1011', font='ar 9', padx=10)
mem13 = Label(window, text='1100', font='ar 9', padx=10)
mem14 = Label(window, text='1101', font='ar 9', padx=10)
mem15 = Label(window, text='1110', font='ar 9', padx=10)
mem16 = Label(window, text='1111', font='ar 9', padx=10)

# Packing fields
instruction.grid(row=2, column=2)
output.grid(row=4, column=2)
# Packing registers
reg1.grid(row=10, column=5)
reg2.grid(row=11, column=5)
reg3.grid(row=12, column=5)
reg4.grid(row=13, column=5)
reg5.grid(row=14, column=5)
reg6.grid(row=15, column=5)
reg7.grid(row=16, column=5)
reg8.grid(row=17, column=5)
# Packing memory locations
mem1.grid(row=6, column=1, padx=10)
mem2.grid(row=7, column=1)
mem3.grid(row=8, column=1)
mem4.grid(row=9, column=1)
mem5.grid(row=10, column=1)
mem6.grid(row=11, column=1)
mem7.grid(row=12, column=1)
mem8.grid(row=13, column=1)

mem9.grid(row=14, column=1)
mem10.grid(row=15, column=1)
mem11.grid(row=16, column=1)
mem12.grid(row=17, column=1)
mem13.grid(row=18, column=1)
mem14.grid(row=19, column=1)
mem15.grid(row=20, column=1)
mem16.grid(row=21, column=1)

# variable to store data
instructionvalue = StringVar
outputvalue = StringVar
# Storing values in registers
reg1value = StringVar
reg2value = StringVar
reg3value = StringVar
reg4value = StringVar
reg5value = StringVar
reg6value = StringVar
reg7value = StringVar
reg8value = StringVar
# Storing values in memory locations
mem1value = StringVar
mem2value = StringVar
mem3value = StringVar
mem4value = StringVar
mem5value = StringVar
mem6value = StringVar
mem7value = StringVar
mem8value = StringVar

mem9value = StringVar
mem10value = StringVar
mem11value = StringVar
mem12value = StringVar
mem13value = StringVar
mem14value = StringVar
mem15value = StringVar
mem16value = StringVar

#value defining
reg1value = StringVar(window,contents_reg0["AL"])
reg2value = StringVar(window,contents_reg0["BL"])
reg3value = StringVar(window,contents_reg0["CL"])
reg4value = StringVar(window,contents_reg0["DL"])
reg5value = StringVar(window,contents_reg0["AH"])
reg6value = StringVar(window,contents_reg0["BH"])
reg7value = StringVar(window,contents_reg0["CH"])
reg8value = StringVar(window,contents_reg0["DH"])



def sets():
    global reg1value,reg2value,reg3value,reg4value,reg5value,reg6value,reg7value,reg8value
    reg1value = StringVar(window,contents_reg0["AL"])
    reg2value = StringVar(window,contents_reg0["BL"])
    reg3value = StringVar(window,contents_reg0["CL"])
    reg4value = StringVar(window,contents_reg0["DL"])
    reg5value = StringVar(window,contents_reg0["AH"])
    reg6value = StringVar(window,contents_reg0["BH"])
    reg7value = StringVar(window,contents_reg0["CH"])
    reg8value = StringVar(window,contents_reg0["DH"])
# Creating entry field
instructionentry = Entry(window, textvariable=instructionvalue)
outputentry = Entry(window, textvariable=outputvalue)
# Creating entry fields for registers
reg1entry = Entry(window, textvariable=reg1value)
reg2entry = Entry(window, textvariable=reg2value)
reg3entry = Entry(window, textvariable=reg3value)
reg4entry = Entry(window, textvariable=reg4value)
reg5entry = Entry(window, textvariable=reg5value)
reg6entry = Entry(window, textvariable=reg6value)
reg7entry = Entry(window, textvariable=reg7value)
reg8entry = Entry(window, textvariable=reg8value)
# Creating entry fields for memory locations
mem1entry = Entry(window, textvariable=mem1value)
mem2entry = Entry(window, textvariable=mem2value)
mem3entry = Entry(window, textvariable=mem3value)
mem4entry = Entry(window, textvariable=mem4value)
mem5entry = Entry(window, textvariable=mem5value)
mem6entry = Entry(window, textvariable=mem6value)
mem7entry = Entry(window, textvariable=mem7value)
mem8entry = Entry(window, textvariable=mem8value)

mem9entry = Entry(window, textvariable=mem9value)
mem10entry = Entry(window, textvariable=mem10value)
mem11entry = Entry(window, textvariable=mem11value)
mem12entry = Entry(window, textvariable=mem12value)
mem13entry = Entry(window, textvariable=mem13value)
mem14entry = Entry(window, textvariable=mem14value)
mem15entry = Entry(window, textvariable=mem15value)
mem16entry = Entry(window, textvariable=mem16value)

# Packing entry field
instructionentry.grid(row=2, column=3)
outputentry.grid(row=4, column=3)
# Packing entry fields for registers
reg1entry.grid(row=10, column=6)
reg2entry.grid(row=11, column=6)
reg3entry.grid(row=12, column=6)
reg4entry.grid(row=13, column=6)
reg5entry.grid(row=14, column=6)
reg6entry.grid(row=15, column=6)
reg7entry.grid(row=16, column=6)
reg8entry.grid(row=17, column=6)
# Packing entry fields for memory locations
mem1entry.grid(row=6, column=2)
mem2entry.grid(row=7, column=2)
mem3entry.grid(row=8, column=2)
mem4entry.grid(row=9, column=2)
mem5entry.grid(row=10, column=2)
mem6entry.grid(row=11, column=2)
mem7entry.grid(row=12, column=2)
mem8entry.grid(row=13, column=2)

mem9entry.grid(row=14, column=2)
mem10entry.grid(row=15, column=2)
mem11entry.grid(row=16, column=2)
mem12entry.grid(row=17, column=2)
mem13entry.grid(row=18, column=2)
mem14entry.grid(row=19, column=2)
mem15entry.grid(row=20, column=2)
mem16entry.grid(row=21, column=2)

# Creating conversion button
Button(text='Convert', command=getvals).grid(row=3, column=3)
window.mainloop()
