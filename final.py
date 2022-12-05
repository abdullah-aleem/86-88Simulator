# tkinter window
import App as application
from tkinter import *
import pygame
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
contents_reg0 = {"AL": "0000", "CL": "0000", "DL": "0000",
                 "BL": "0000", "AH": "0000", "BH": "0000", "CH": "0000", "DH": "0000"}


operand1 = ""
operand2 = ""
D = "1"
word = "1"
MOD = '11'
rule=0
def getapp():
    application.run(rule)
def getvals():
    global inps
    inps=instructionentry.get()

    start()
    # Label(window, text='10101010 00001111', font='ar 9').grid(row=4, column=3)


def tohex(val, nbits):
    return hex((val + (1 << nbits)) % (1 << nbits))


def Direction():
    global D
    if operand1[0] == "[":
        D = "0"


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
    global D, word, MOD, operand1, operand2, reg0, contents_reg0, contents_mem, opcode,inps,rule
    result=""
    mmm = "111"
    D = "1"
    word = "1"
    MOD = '11'
    bool = False
    inst =str(inps)
    x = inst.split(" ")
    opr = x[0]
    y = x[1]
    length = len(inst)
    if length > 7:
        bool = True
        z = y.split(",")
        operand1 = z[0]
        operand2 = z[1]
    
    if opr=="MOV" or opr== "SUB" or opr== "OR" or  opr=="XOR" or opr== "ADD" or opr== "AND" :
        Direction()
        MOD_1()
        if operand1 in reg0 and operand2 in reg0:
            rule=1
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
            Label(window, text=str(
                opcode[opr]+ D+word+ MOD+ reg0[operand1]+ reg0[operand2]), font='ar 9').grid(row=4, column=3)
        elif operand1[0] == "[" and operand2 in reg0:
            rule=2
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
                contents_mem[operand1] = str((hex(dec).lstrip('0x')))
            Label(window, text=str(
                opcode[opr]+D+word+MOD+reg0[operand2]+mmm)).grid(row=4, column=3)

            

        elif operand1 in reg0 and operand2[0] == "[":
            rule=3
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
            
            Label(window, text=str(opcode[opr]+ D+ word+ MOD+ reg0[operand1]+ mmm), font='ar 9').grid(row=4, column=3)
            print(result)
            
    if opr=="NEG":
        rule=1
        rrr = "011"
        contents_reg0[y] = str(
            (tohex(int(contents_reg0[y]*-1, 16), 8).lstrip('0x')))
    if opr=="DIV":
        rule=1
        rrr = '110'

    if opr=="INC":
        rule=1
        rrr = "000"
        dec = int(contents_reg0[y], 16)+1

        contents_reg0[y]=str(hex(dec).lstrip('0x'))
    if opr=="MUL":
        rule=1
        rrr = "100"

    if opr=="NOT":
        rule=1
        rrr = '010'
        contents_reg0[y] = str(
            hex((~int(contents_reg0[y], 16))).replace('0x', ""))
        print(contents_reg0[y])
    if opr=="IMUL":
        rule=1
        rrr = "101"
    if opr=="IDIV":
        rule=1
        rrr = "111"
    if opr=="DEC":
        rule=1
        rrr = '001'
        dec = int(contents_reg0[y], 16)-1
        print(tohex(dec, 64).lstrip('0x'))
    if bool == False:
        print(opcode[opr], D, word, MOD, rrr, reg0[y])
        Label(window,text=str(opcode[opr]+ D+ word+ MOD+ rrr+ reg0[y])).grid(row=4, column=3)
       
    sets()
    
# Field name
instruction = Label(window, text='Enter instruction:',
                    font='ar 9', padx=30, pady=20)
output = Label(window, text='Output:', font='ar 9', pady=20)
# Creating registers
reg1 = Label(window, text='AL:', font='ar 9')
reg2 = Label(window, text='BL:', font='ar 9')
reg3 = Label(window, text='CL:', font='ar 9')
reg4 = Label(window, text='DL:', font='ar 9')
reg5 = Label(window, text='AH:', font='ar 9')
reg6 = Label(window, text='BH:', font='ar 9')
reg7 = Label(window, text='CH:', font='ar 9')
reg8 = Label(window, text='DH:', font='ar 9')
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
instructionvalue = StringVar()
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
mem1value = StringVar(window,contents_mem["M0000"])
mem2value = StringVar(window,contents_mem["M0001"])
mem3value = StringVar(window,contents_mem["M0010"])
mem4value = StringVar(window,contents_mem["M0011"])
mem5value = StringVar(window,contents_mem["M0100"])
mem6value = StringVar(window,contents_mem["M0101"])
mem7value = StringVar(window,contents_mem["M0110"])
mem8value = StringVar(window,contents_mem["M0111"])
mem9value = StringVar(window,contents_mem["M1000"])
mem10value = StringVar(window,contents_mem["M1001"])
mem11value = StringVar(window,contents_mem["M1010"])
mem12value = StringVar(window,contents_mem["M1011"])
mem13value = StringVar(window,contents_mem["M1100"])
mem14value = StringVar(window,contents_mem["M1101"])
mem15value = StringVar(window,contents_mem["M1110"])
mem16value = StringVar(window,contents_mem["M1111"])



def sets():
    global reg1value,reg2value,reg3value,reg4value,reg5value,reg6value,reg7value,reg8value,mem1value,mem2value,mem3value,mem4value,mem5value,mem6value,mem7value,mem8value,mem9value,mem10value,mem11value,mem12value,mem13value,mem14value,mem15value,mem16value

    print("in")
    print(contents_reg0["AL"])
    
    reg1entry.delete(0,100)
    reg1entry.insert(0,contents_reg0["AL"])
    reg2entry.delete(0,END)
    reg2entry.insert(0,contents_reg0["BL"])
    reg3entry.delete(0,END)
    reg3entry.insert(0,contents_reg0["CL"])
    reg4entry.delete(0,END)
    reg4entry.insert(0,contents_reg0["DL"])
    reg5entry.delete(0,END)
    reg5entry.insert(0,contents_reg0["AH"])
    reg6entry.delete(0,END)
    reg6entry.insert(0,contents_reg0["BH"])
    reg7entry.delete(0,END)
    reg7entry.insert(0,contents_reg0["CH"])
    reg8entry.delete(0,END)
    reg8entry.insert(0,contents_reg0["DH"])
    mem1entry.delete(0,END)
    mem1entry.insert(0,contents_mem["M0000"])
    mem2entry.delete(0,END)
    mem2entry.insert(0,contents_mem["M0001"])
    mem3entry.delete(0,END)
    mem3entry.insert(0,contents_mem["M0010"])
    mem4entry.delete(0,END)
    mem4entry.insert(0,contents_mem["M0011"])
    mem5entry.delete(0,END)
    mem5entry.insert(0,contents_mem["M0100"])
    mem6entry.delete(0,END)
    mem6entry.insert(0,contents_mem["M0101"])
    mem7entry.delete(0,END)
    mem7entry.insert(0,contents_mem["M0110"])
    mem8entry.delete(0,END)
    mem8entry.insert(0,contents_mem["M0111"])
    mem9entry.delete(0,END)
    mem9entry.insert(0,contents_mem["M1000"])
    mem10entry.delete(0,END)
    mem10entry.insert(0,contents_mem["M1001"])
    mem11entry.delete(0,END)
    mem11entry.insert(0,contents_mem["M1010"])
    mem12entry.delete(0,END)
    mem12entry.insert(0,contents_mem["M1011"])
    mem13entry.delete(0,END)
    mem13entry.insert(0,contents_mem["M1100"])
    mem14entry.delete(0,END)
    mem14entry.insert(0,contents_mem["M1101"])
    mem15entry.delete(0,END)
    mem15entry.insert(0,contents_mem["M1110"])
    mem16entry.delete(0,END)
    mem16entry.insert(0,contents_mem["M1111"])

# Creating entry field
# instructionentry = Entry(window, textvariable=instructionvalue)
instructionentry= Entry(window, width= 42)
instructionentry.place(relx= .5, rely= .5, anchor= CENTER)
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
Button(text='simulate', command=getapp).grid(row=3, column=4)
window.mainloop()
