sb = int(input())
li = list(map(int, input().split()))
sum = 0
for i in range(sb):
    sum += (li[i]/max(li))*100
print(sum/sb)
