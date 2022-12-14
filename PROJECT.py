opcode = {
 "MOV": '100010',"SUB": '000101',"XOR":'000110',"INC":'111111',
    "NEG": '111101',"DIV": '111101', "MUL":'111101',"OR":'000010', 
    "ADD": '000000',"NOT":'111101',"IMUL":'111101',"IDIV":'111101',
    "DEC":'111111',"AND":'001000',"":''}

#backend code
# reg0={
#     "AL": "000","CL": "001","DL": "010","BL": "011", 
#     "AH": "100","CH": "101","DH": "100","BH": "111" }

reg0={
    "AX": "000","CX": "001","DX": "010","BX": "011", 
    "SP": "100","BP": "101","SI": "100","DI": "111" }

# contents of memory locations
contents_mem={"M0000":"00","M0001":"00","M0010":"00","M0011":"00","M0100":"00",
"M0101":"00","M0110":"00","M0111":"00","M1000":"00","M1001":"00","M1010":"00","M1011":"00",
"M1100":"00","M1101":"00","M1110":"00","M1111":"00"}

# contents of 16 bits registers
contents_reg0={"AX":"0000","CX":"0000","DX":"0000","BX":"0000","SP":"0000","BP":"0000","SI":"0000","DI":"0000"}

# mem code for addressing mode DS:[BX]
mmm=111

bool=False
inst = input('enter instruction')
x = inst.split(" ")
opr =x[0]
y = x[1]
length=len(inst)
if length>7:
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
D=1
word=1
def Direction():
    global D
    if operand1[0]=="[":
        D=0
MOD='11'
def MOD_1():
    global MOD
    if operand1[0]=="[" and operand2 in reg0:
                MOD='00'
    elif operand1 in reg0 and operand2[0]=="[":
                MOD='00'
    
    
match opr:
        case "MOV"|"SUB"|"OR"|"XOR"|"ADD"|"AND":
            Direction()
            MOD_1()
            if operand1 in reg0 and operand2 in reg0:
                if opr== "AND":
                    contents_reg0[operand1]=str(hex(int(contents_reg0[operand1],16)&int(contents_reg0[operand2],16)).lstrip('0x'))
                    print(contents_reg0[operand1])
                elif opr== "OR":
                    contents_reg0[operand1]=str(hex(int(contents_reg0[operand1],16)|int(contents_reg0[operand2],16)).lstrip('0x'))
                    print(contents_reg0[operand1])
                elif opr== "XOR":
                    contents_reg0[operand1]=str(hex(int(contents_reg0[operand1],16)^int(contents_reg0[operand2],16)).lstrip('0x'))
                    print(contents_reg0[operand1])
                elif opr=="ADD":
                    dec=(int(contents_reg0[operand1],16))+(int(contents_reg0[operand2],16))
                    contents_reg0[operand1]=str((hex(dec).lstrip('0x')))
                elif opr=="MOV":
                    contents_reg0[operand1]=str(contents_reg0[operand2])
                elif opr=="SUB":
                    dec=(int(contents_reg0[operand1],16))-(int(contents_reg0[operand2],16))
                    contents_reg0=str((hex(dec).lstrip('0x')))
                print(opcode[opr],D,word,MOD,reg0[operand1],reg0[operand2])

            elif operand1[0]=="[" and operand2 in reg0:
                operand1=operand1.lstrip("[")
                operand1=operand1.rstrip("]")
                print(operand1)
                if opr== "AND":
                    contents_mem[operand1]=str(hex(int(contents_mem[operand1],16)&int(contents_reg0[operand2],16)).lstrip('0x'))
                    print(contents_mem[operand1])
                elif opr== "OR":
                    contents_mem[operand1]=str(hex(int(contents_mem[operand1],16)|int(contents_reg0[operand2],16)).lstrip('0x'))
                    print(contents_mem[operand1])
                elif opr== "XOR":
                    contents_mem[operand1]=str(hex(int(contents_mem[operand1],16)^int(contents_reg0[operand2],16)).lstrip('0x'))
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
                operand2=operand2.lstrip("[")
                operand2=operand2.rstrip("]")
                print(operand2)
                if opr== "AND":
                    contents_reg0[operand1]=str(hex(int(contents_reg0[operand1],16)&int(contents_mem[operand2],16)).lstrip('0x'))
                    print(contents_reg0[operand1])
                elif opr== "OR":
                    contents_reg0[operand1]=str(hex(int(contents_reg0[operand1],16)|int(contents_mem[operand2],16)).lstrip('0x'))
                    print(contents_reg0[operand1])
                elif opr== "XOR":
                    contents_reg0[operand1]=str(hex(int(contents_reg0[operand1],16)^int(contents_reg0[operand2],16)).lstrip('0x'))
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
            contents_reg0[y]=str((tohex(int(contents_reg0[y]*-1, 16),8).lstrip('0x')))
        case "DIV":
            rrr='110'

        case "INC":
                rrr="000"
                dec=int(contents_reg0[y],16)+1
                print(hex(dec).lstrip('0x'))
        case "MUL":
                rrr="100"
               
        case "NOT":
                rrr='010'
                contents_reg0[y]=str(hex((~int(contents_reg0[y],16))).replace('0x',""))
                print(contents_reg0[y])
        case "IMUL":
                rrr="101"
        case "IDIV":
                rrr="111"
        case "DEC":
                rrr='001'
                dec=int(contents_reg0[y],16)-1
                print(tohex(dec,64).lstrip('0x'))
if bool==False:
    print(opcode[opr],D,word,MOD,rrr,reg0[y])
       
        





