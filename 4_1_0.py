# N ** 2
def strcounter(s):
    for sym in s:
        counter=0
        for sub_sym in s:
            if sym==sub_sym:
                counter+=1
        print(sym, counter)
    print('')



# N * M
def strcounter1(s):
        for sym in set(s):
         counter=0
         for sub_sym in s:
            if sym==sub_sym:
                counter+=1
         print(sym, counter)
        print('')




# N
def strcounter2(s):
    sym_counter={}
    for sym in s:
        sym_counter[sym]=sym_counter.get(sym, 0) + 1

    for sym, count in sym_counter.items():
        print(sym, count)
    print('')


num_s=[0,1,2]

s=int(input('Введи число 0-2: '))
if s not in num_s:
    print('qwerty')
else:
    if s==0:
      strcounter(str(input('Введите строку: ')))
    elif s==1:
        strcounter1(str(input('Введите строку: ')))
    elif s==2:
        strcounter2(str(input('Введите строку: ')))




        

