opcode = {
 "MOV": '100010',"SUB": '000101',"XOR":'000110',"INC":'111111',
    "NEG": '111101',"DIV": '111101', "MUL":'111101',"OR":'000010', 
    "ADD": '000000',"NOT":'111101',"IMUL":'111101',"IDIV":'111101',
    "DEC":'111111',"":'',"":''}


reg0={
    "AL": "000","CL": "001","DL": "010","BL": "011", 
    "AH": "100","CH": "101","DH": "100","BH": "111" }

reg1={
    "AX": "000","CX": "001","DX": "010","BX": "011", 
    "SP": "100","BP": "101","SI": "100","DI": "111" }
# contents of memory locations

M0000=00
M0001=00
M0010=00
M0011=00
M0100=00
M0101=00
M0110=00
M0111=00
M1000=00
M1001=00
M1010=00
M1011=00
M1100=00
M1101=00
M1110=00
M1111=00

# contents of 16 bits registers
AX=0000
CX=0000
DX=0000
BX=0000
SP=0000
BP=0000
SI=0000
DI=0000

# contents of 8 bits registers
contents_reg0={"AL":10,"CL":11,"DL":00,"BL":00,"AH":00,"CH":00,"DH":00,"BH":00}


# mmm={
#     "[BX+SI]": "000","[BX+DI]": "001","[BP+SI]": "010","[BP+DI]": "011", 
#     "[SI]": "100","[DI]": "101","[BP]": "100","[BX]": "111" }


bool=False
inst = input('enter instruction')
x = inst.split(" ")
opr =x[0]
y = x[1]
length=len(inst)
if length>6:
    bool=True
    z = y.split(",")
    operand1 = z[0]
    operand2 = z[1]

#         if RM in reg0 or RM in reg1:
#             MOD= '11'
#     print(opcode["opr"],reg1["reg"],reg1["RM"])

def Word():
    global word,dic,flag
    flag=True
    if bool==True:
        if operand1 in reg0 and operand2 in reg0:
            word=0
            dic = reg0
        elif operand1 in reg1 and operand2 in reg1:
            word=1
            dic=reg1
        else:
            print("invalid operands")
            flag=False
    else:
        if y in reg0:
            word=0
            dic=reg0
        elif y in reg1:
            word=1
            dic=reg1
        else:
            print("invalid operands")

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
                if opr== "AND":
                    contents_reg0[operand1]=contents_reg0[operand1]&contents_reg0[operand2]
                    print(contents_reg0[operand1])

                    # print(opcode[opr],D,word,MOD,dic[operand1],dic[operand2])
                
            case "NEG":
                rrr="011"
                def to_hex(val, nbits):
                    return hex((val + (1 << nbits)) % (1 << nbits)).lstrip('0x')
            case "DIV":
                rrr='110'
            case "INC":
                rrr="000"
            case "MUL":
                rrr="100"
            case "NOT":
                rrr='010'
            case "IMUL":
                rrr="101"
            case "IDIV":
                rrr="111"
            case "DEC":
                rrr='001'
    if bool==False:
        print(opcode[opr],D,word,MOD,rrr,dic[y])
       
        





