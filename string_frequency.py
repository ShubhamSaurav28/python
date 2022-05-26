def frequency():
    str=input()
    dct={}
    for i in str:
        a=str.count(i)
        if i not in dct:
            dct.update({i:a})
    print(dct)
frequency()
