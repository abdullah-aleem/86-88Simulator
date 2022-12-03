opcode = {
 "MOV": '100010',"SUB": '000101',"XOR":'000110',"INC":'111111',
    "NEG": '111101',"DIV": '111101', "MUL":'111101',"OR":'000010', 
    "ADD": '000000',"NOT":'111101',"IMUL":'111101',"IDIV":'111101',
    "DEC":'111111',"":'',"":''}


reg0={
    "AL": "000","CL": "001","DL": "010","BL": "011", 
    "AH": "100","CH": "101","DH": "100","BH": "111" }

# reg1={
#     "AX": "000","CX": "001","DX": "010","BX": "011", 
#     "SP": "100","BP": "101","SI": "100","DI": "111" }
# contents of memory locations

contents_mem={"M0000":"00","M0001":"00","M0010":"00","M0011":"00","M0100":"00",
"M0101":"00","M0110":"00","M0111":"00","M1000":"00","M1001":"00","M1010":"00","M1011":"00",
"M1100":"00","M1101":"00","M1110":"00","M1111":"00"}

# # contents of 16 bits registers
# AX=0000
# CX=0000
# DX=0000
# BX=0000
# SP=0000
# BP=0000
# SI=0000
# DI=0000

# contents of 8 bits registers
contents_reg0={"AL":"00","CL":"00","DL":"00","BL":"00","AH":"00","CH":"00","DH":"00","BH":"00"}


# mem code for addressing mode DS:[BX]
mmm=111



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


# def Word():
#     global word,dic,flag
#     flag=True
#     if bool==True:
#         if operand1 in reg0 and operand2 in reg0:
#             word=0
#             dic = reg0
#         elif operand1 in reg1 and operand2 in reg1:
#             word=1
#             dic=reg1
#         else:
#             print("invalid operands")
#             flag=False
#     else:
#         if y in reg0:
#             word=0
#             dic=reg0
#         elif y in reg1:
#             word=1
#             dic=reg1
#         else:
#             print("invalid operands")


def tohex(val, nbits):
  return hex((val + (1 << nbits)) % (1 << nbits))
def Direction():
    global D
    D=1
    if operand1[0]=="[":
        D=0
flag=True
word=1
Direction()
if flag:
    match opr:
            case "MOV"|"SUB"|"OR"|"XOR"|"ADD"|"AND":
                if operand1 in reg0 and operand2 in reg0:
                    MOD=11
                    if opr== "AND":
                        contents_reg0[operand1]=str(contents_reg0[operand1]&contents_reg0[operand2])
                        print(contents_reg0[operand1])
                    elif opr== "OR":
                        contents_reg0[operand1]=str(contents_reg0[operand1]|contents_reg0[operand2])
                        print(contents_reg0[operand1])
                    elif opr== "XOR":
                        contents_reg0[operand1]=str(contents_reg0[operand1]^contents_reg0[operand2])
                        print(contents_reg0[operand1])
                    elif opr=="ADD":
                        dec=(int(contents_reg0[operand1],16))+(int(contents_reg0[operand2],16))
                        contents_reg0[operand1]=str((hex(dec).lstrip('0x')))
                    elif opr=="MOV":
                        contents_reg0[operand1]=str(contents_reg0[operand2])
                    elif opr=="SUB":
                        dec=(int(contents_reg0[operand1],16))-(int(contents_reg0[operand2],16))
                        contents_reg0=str((hex(dec).lstrip('0x')))
                print(opcode[opr],D,word,MOD,dic[operand1],dic[operand2])

                elif operand1[0]="[" and operand2 in reg0:
                    MOD=00
                    if opr== "AND":
                    contents_mem[operand1]=str(contents_mem[operand1]&contents_reg0[operand2])
                    print(contents_mem[operand1])
                    elif opr== "OR":
                        contents_mem[operand1]=str(contents_mem[operand1]|contents_reg0[operand2])
                        print(contents_mem[operand1])
                    elif opr== "XOR":
                        contents_mem[operand1]=str(contents_mem[operand1]^contents_reg0[operand2])
                        print(contents_mem[operand1])
                    elif opr=="ADD":
                        dec=(int(contents_mem[operand1],16))+(int(contents_reg0[operand2],16))
                        contents_mem[operand1]=str((hex(dec).lstrip('0x')))
                    elif opr=="MOV":
                        contents_mem[operand1]=str(contents_reg0[operand2])
                    elif opr=="SUB":
                        dec=(int(contents_mem[operand1],16))-(int(contents_reg0[operand2],16))
                        contents_mem=str((hex(dec).lstrip('0x')))
                print(opcode[opr],D,word,MOD,mmm,reg0[operand2])

                elif operand1 in reg0 and operand2[0]=="[":
                    MOD=00
                    if opr== "AND":
                        contents_reg0[operand1]=str(contents_reg0[operand1]&contents_mem[operand2])
                        print(contents_reg0[operand1])
                    elif opr== "OR":
                        contents_reg0[operand1]=str(contents_reg0[operand1]|contents_mem[operand2])
                        print(contents_reg0[operand1])
                    elif opr== "XOR":
                        contents_reg0[operand1]=str(contents_reg0[operand1]^contents_mem[operand2])
                        print(contents_reg0[operand1])
                    elif opr=="ADD":
                        dec=(int(contents_reg0[operand1],16))+(int(contents_mem[operand2],16))
                        contents_reg0[operand1]=str((hex(dec).lstrip('0x')))
                    elif opr=="MOV":
                        contents_reg0[operand1]=str(contents_mem[operand2])
                    elif opr=="SUB":
                        dec=(int(contents_reg0[operand1],16))-(int(contents_mem[operand2],16))
                        contents_reg0=str((hex(dec).lstrip('0x')))
                print(opcode[opr],D,word,MOD,reg0[operand1],mmm)

              


                   
                
            case "NEG":
                rrr="011"
                print(hex(int(contents_reg0[operand1], 16)*-1).lstrip('0x'))
                # def to_hex(val, nbits):
                #     return hex((val + (1 << nbits)) % (1 << nbits)).lstrip('0x')
            case "DIV":
                rrr='110'
                if y[0]=="[":
                    print("invalid operands")
            case "INC":
                rrr="000"
                dec=int(contents_reg0[y],16)+1
                print(hex(dec).lstrip('0x'))
            case "MUL":
                rrr="100"
                x.__mul__(y)
            case "NOT":
                rrr='010'
                # abc= ~hex(contents_reg0[y])
                # print(abc)
            case "IMUL":
                rrr="101"
            case "IDIV":
                rrr="111"
            case "DEC":
                rrr='001'
                dec=int(contents_reg0[y],16)-1
                print(tohex(dec,64).lstrip('0x'))
    # if bool==False:
    #     print(opcode[opr],D,word,MOD,rrr,reg0[y])
       
        





