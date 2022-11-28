
opcode = {
    "MOV": "100010","SUB": '',
    "NEG": '111101',"DIV": '111101',
    "ADD": '000000',"NOT":'111101'}


reg0={
    "AL": "000","CL": "001","DL": "010","BL": "011", 
    "AH": "100","CH": "101","DH": "100","BH": "111" }

reg1={
    "AX": "000","CX": "001","DX": "010","BX": "011", 
    "SP": "100","BP": "101","SI": "100","DI": "111" }

mmm={
    "[BX+SI]": "000","[BX+DI]": "001","[BP+SI]": "010","[BP+DI]": "011", 
    "[SI]": "100","[DI]": "101","[BP]": "100","[BX]": "111" }

   

print(reg0.keys())

operator= input("enter the operator")
RM= input("enter R/M")
reg= input("enter register")
if operator == "MOV":
    if RM=='DX' and reg=='AX':
        if RM in reg0.keys() or RM== reg1.keys():
            MOD= '11'
    print(opcode["MOV"],reg1["DX"],reg1["AX"])




#iqra's code

inst = "MOV AX,BX"

def split_instruction():
    x = inst.split(" ")
    print(x)
    y = x[1]
    z = y.split(",")
    print(z[0])
    print(z[1])

split_instruction()

#tkinter window
from tkinter import *
window = Tk()
window.title("Main Window")
window.geometry("750x600")
window.state('zoomed')
window.configure(background='light blue')

def getvals():
    if instructionentry != 0 and Button:
        print('10101010 00001111')
        Label(window, text='10101010 00001111', font='ar 9').grid(row=3, column=3)

#Heading
Label(window, text='Assembly Language to Machine Code Convertor', font='ar 11 bold', pady=30).grid(row=0, column=3)

#Field name
instruction = Label(window, text='Enter instruction:', font='ar 9', padx=30, pady=20)
output = Label(window, text='Output:', font='ar 9', pady=20)
#Creating registers
reg1 = Label(window, text='Reg1:', font='ar 9')
reg2 = Label(window, text='Reg2:', font='ar 9')
reg3 = Label(window, text='Reg3:', font='ar 9')
reg4 = Label(window, text='Reg4:', font='ar 9')
reg5 = Label(window, text='Reg5:', font='ar 9')
reg6 = Label(window, text='Reg6:', font='ar 9')
reg7 = Label(window, text='Reg7:', font='ar 9')
reg8 = Label(window, text='Reg8:', font='ar 9')
#Creating memory locations
mem1 = Label(window, text='Mem1:', font='ar 9', padx=10)
mem2 = Label(window, text='Mem2:', font='ar 9', padx=10)
mem3 = Label(window, text='Mem3:', font='ar 9', padx=10)
mem4 = Label(window, text='Mem4:', font='ar 9', padx=10)
mem5 = Label(window, text='Mem5:', font='ar 9', padx=10)
mem6 = Label(window, text='Mem6:', font='ar 9', padx=10)

#Packing fields
instruction.grid(row=1, column=2)
output.grid(row=3, column=2)
#Packing registers
reg1.grid(row=4, column=4)
reg2.grid(row=5, column=4)
reg3.grid(row=6, column=4)
reg4.grid(row=7, column=4)
reg5.grid(row=8, column=4)
reg6.grid(row=9, column=4)
reg7.grid(row=10, column=4)
reg8.grid(row=11, column=4)
#Packing memory locations
mem1.grid(row=5, column=1)
mem2.grid(row=6, column=1)
mem3.grid(row=7, column=1)
mem4.grid(row=8, column=1)
mem5.grid(row=9, column=1)
mem6.grid(row=10, column=1)

#variable to store data
instructionvalue = StringVar
outputvalue = StringVar
#Storing values in registers
reg1value = StringVar
reg2value = StringVar
reg3value = StringVar
reg4value = StringVar
reg5value = StringVar
reg6value = StringVar
reg7value = StringVar
reg8value = StringVar
#Storing values in memory locations
mem1value = StringVar
mem2value = StringVar
mem3value = StringVar
mem4value = StringVar
mem5value = StringVar
mem6value = StringVar

#Creating entry field
instructionentry = Entry(window, textvariable=instructionvalue)
outputentry = Entry(window, textvariable=outputvalue)
#Creating entry fields for registers
reg1entry = Entry(window, textvariable=reg1value)
reg2entry = Entry(window, textvariable=reg2value)
reg3entry = Entry(window, textvariable=reg3value)
reg4entry = Entry(window, textvariable=reg4value)
reg5entry = Entry(window, textvariable=reg5value)
reg6entry = Entry(window, textvariable=reg6value)
reg7entry = Entry(window, textvariable=reg7value)
reg8entry = Entry(window, textvariable=reg8value)
#Creating entry fields for memory locations
mem1entry = Entry(window, textvariable=mem1value)
mem2entry = Entry(window, textvariable=mem2value)
mem3entry = Entry(window, textvariable=mem3value)
mem4entry = Entry(window, textvariable=mem4value)
mem5entry = Entry(window, textvariable=mem5value)
mem6entry = Entry(window, textvariable=mem6value)

#Packing entry field
instructionentry.grid(row=1, column=3)
outputentry.grid(row=3, column=3)
#Packing entry fields for registers
reg1entry.grid(row=4, column=5)
reg2entry.grid(row=5, column=5)
reg3entry.grid(row=6, column=5)
reg4entry.grid(row=7, column=5)
reg5entry.grid(row=8, column=5)
reg6entry.grid(row=9, column=5)
reg7entry.grid(row=10, column=5)
reg8entry.grid(row=11, column=5)
#Packing entry fields for memory locations
mem1entry.grid(row=5, column=2)
mem2entry.grid(row=6, column=2)
mem3entry.grid(row=7, column=2)
mem4entry.grid(row=8, column=2)
mem5entry.grid(row=9, column=2)
mem6entry.grid(row=10, column=2)

#Creating conversion button
Button(text='Convert', command=getvals).grid(row=2, column=3)
window.mainloop()


