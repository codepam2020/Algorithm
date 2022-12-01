n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

for i in range(m):
    result = m_list[i] in n_list
    if result == True:
        print(1)
    else:
        print(0)
