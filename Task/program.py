codes = []
names = []
while True:
    """Cycle for input values"""
    a = input('(input <stop> if you want to get result) code:')
    if a == 'stop':
        break
    b = input('name:')
    codes.append(a.split('.'))
    names.append(b)
    print(codes, names)


codes = sorted(codes)
result = []
k =0
for i in range(len(codes)):
    try:
        if codes[i][0] == codes[i+1][0]:
            s = codes.pop(i+1)
    except IndexError:
        continue
    di = {'code': '.'.join(codes[i]), 'name': 'name '+'.'.join(codes[i]), 'children':['.'.join(s)]}
    result.append(di)
print(result)





    # res = [
    #     {'code' : a, 'name': b, 'children': []}
    # ]
    # print (res)
