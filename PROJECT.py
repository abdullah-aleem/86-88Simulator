
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




#iqras code
tokeni