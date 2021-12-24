# sum of the multiple of 3 or 5 in 1000
a,b = map(int,input("enter the multiples 2 :").split())
sum = 0
for i in range(int(input("enter How many you numbers you want "))):
    if i % a  == 0 or i % b ==0 :
        sum += i



print(sum)

