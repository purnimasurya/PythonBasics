list = []
n = int(input("Enter the number of values : "))
for i in range(0,n):
    ele = int(input("Enter value " + str(i+1) + " : "))
    list.append(ele)
for i in range(0,n):
    if list[i] > 0:
        print(list[i], end = ' ')