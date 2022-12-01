a = int(input())
b = int(input())

result = list(range(a, b + 1))  # a와 b사이 자연수들을 list로 나타냄

for num in range(a, b + 1):
    if num == 1:
        result.remove(1)  # 1의 경우 소수가 아니므로 1이 있을경우 list에서 제외시킴
    else:
        for i in range(2, num):
            if num % i == 0:
                result.remove(num)  # 반복시 소수가 아닌 자연수가 나올 경우 list에서 제외 시킴
                break
            else:
                pass

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))
