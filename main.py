

# for i in range(1, 5):
#     num2 = i
#     for x in range (0,i+1):
#         print(x,end=' ')
#     print()
        
num = range(1, 6)
for i in num:
    num2 = num
    for x in num2:
        print(x, end=' ')
    print()


num = range(1, 6)

for i in num:
    for x in num:
        if x <= i:
            print(x, end=' ')
    print()



