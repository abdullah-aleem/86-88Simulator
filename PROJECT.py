
opcode = {
    "MOV": "100010","SUB": '000101',"XOR":'000110',"INC":'111111',
    "NEG": '111101',"DIV": '111101', "MUL":'111101',"OR":'000010', 
    "ADD": '000000',"NOT":'111101',"IMUL":'111101',"IDIV":'111101',
    "DEC":'111111',"":'',"":''}

# MOD=['00','01','10','11']
reg0={
    "AL": "000","CL": "001","DL": "010","BL": "011", 
    "AH": "100","CH": "101","DH": "100","BH": "111" }

reg1={
    "AX": "000","CX": "001","DX": "010","BX": "011", 
    "SP": "100","BP": "101","SI": "100","DI": "111" }

# mmm={
#     "[BX+SI]": "000","[BX+DI]": "001","[BP+SI]": "010","[BP+DI]": "011", 
#     "[SI]": "100","[DI]": "101","[BP]": "100","[BX]": "111" }

 
inst = input('enter instruction')
x = inst.split(" ")
opr =x[0]
y = x[1]
z = y.split(",")
operand1 = z[0]
operand2 = z[1]

#         if RM in reg0 or RM in reg1:
#             MOD= '11'
#     print(opcode["opr"],reg1["reg"],reg1["RM"])

def Word():
    global word
    global dic
    global flag
    flag=True
    if operand1 in reg0 and operand2 in reg0:
        word=0
        dic = reg0
    elif operand1 in reg1 and operand2 in reg1:
        word=1
        dic=reg1
    else:
        print("invalid operands")
        flag=False
# def Direction():
#     global D
#     if operand1[0]=="[":
#         D=0
#     elif operand2[0]=="[":
#         D=1
MOD="11"
D="1"
flag=True
Word()
if flag:
    match opr:
            case "MOV"|"SUB"|"OR"|"XOR"|"ADD"|"AND":
                print(opcode[opr],D,word,MOD,dic[operand1],dic[operand2])
            case "NEG":
                print(opcode[opr],D,word,MOD,'011',dic[operand2])
            case "DIV":
                print(opcode[opr],D,word,MOD,'110',dic[operand2])
            case "INC":
                print(opcode[opr],D,word,MOD,"000",dic[operand2])
            case "MUL":
                print(opcode[opr],D,word,MOD,"100",dic[operand2])
            case "NOT":
                print(opcode[opr],D,word,MOD,'010',dic[operand2])
            case "IMUL":
                print(opcode[opr],D,word,MOD,"101",dic[operand2])
            case "IDIV":
                 print(opcode[opr],D,word,MOD,"111",dic[operand2])
            case "DEC":
                print(opcode[opr],D,word,MOD,"001",dic[operand2])

            