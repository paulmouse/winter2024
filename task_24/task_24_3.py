def skobki_pair(str):
    while '()' in str:
        str = str.replace('()','')
    # return
    #     if str =='':
    #         True
    #     else:
    #         False
    return str

# '(())((((()()()()))()())' => true
# ')(()))' => false

tst = skobki_pair('(())((((()()()()))()()))')
if tst == '':
    print(True)
else:
    print(False)
# print(tst)