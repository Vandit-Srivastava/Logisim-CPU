def bin_num(n: int, b: int):
    a = bin(n)[2:]
    ans = a.zfill(b)
    return ans

def output(bit_in):
    #op_I_IsEq
    op=bit_in[0:5]
    I=bit_in[5]
    IsEq=bit_in[6]
    ADD, SUB, CMP, LD, ST, BEQ, CALL, RET, HALT=bin_num(0,1), bin_num(0,1), bin_num(0,1), bin_num(0,1), bin_num(0,1), bin_num(0,1), bin_num(0,1), bin_num(0,1), bin_num(0,1)
    if op==bin_num(0,5):
        ADD=bin_num(1,1)
    if op==bin_num(1,5):
        SUB=bin_num(1,1)
    if op==bin_num(5,5):
        CMP=bin_num(1,1)
    if op==bin_num(14,5):
        LD=bin_num(1,1)
    if op==bin_num(15,5):
        ST=bin_num(1,1)
    if op==bin_num(16,5):
        BEQ=bin_num(1,1)
    if op==bin_num(19,5):
        CALL=bin_num(1,1)
    if op==bin_num(20,5):
        RET=bin_num(1,1)
    if op==bin_num(31,5):
        HALT=bin_num(1,1)
    
    RegWEn=bin_num(int(ADD)|int(SUB)|int(LD),1)
    FlWEn=CMP
    BSel=I
    #print("bit_in= ", bit_in, ", RegWEn= ", RegWEn, "BSel= ", BSel)
    BeqEn=bin_num(int(BEQ)&int(IsEq),1)
    CallEn=CALL
    RetEn=RET
    HaltEn=bin_num(3,2)
    if HALT==bin_num(0,1):
        HaltEn=bin_num(0,2)
    LoadEn=LD
    StoreEn=ST
    ALUSel=bin_num(0,4)
    if ADD==bin_num(0,1) and SUB==bin_num(1,1):
        ALUSel=bin_num(1,4)
    ans=RegWEn+BSel+FlWEn+ALUSel+LoadEn+StoreEn+BeqEn+CallEn+RetEn+HaltEn
    #print(op)
    #print(ans)
    #ans=bin_num(0,14)
    '''ans[0]=RegWEn
    ans[1]=BSel
    ans[2]=FlWEn
    ans[3:7]=ALUSel
    ans[7]=LoadEn
    ans[8]=StoreEn
    ans[9]=BeqEn
    ans[10]=CallEn
    ans[11]=RetEn
    ans[12:]=HaltEn'''
    #ans=HaltEn+RegWEn+BSel+FlWEn+ALUSel+LoadEn+StoreEn+BeqEn+CallEn+RetEn
    #print(ans)
    return ans

def bin2hex(bitstring):
    dec=int(bitstring,2)
    hex_num=hex(dec)[2:]
    hexnum=hex_num.zfill(4)
    return hexnum

print("v3.0 hex words addressed")
for i in range(2**7):
    if i%16==0:
        print((hex(i)[2:]).zfill(2), end=": ")
    cwrd=output(bin_num(i,7))
    cwrd=cwrd
    cwrd=bin2hex(cwrd)
    print(cwrd, end=" ")
    if i%16==15:
        print()