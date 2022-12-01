hour, minute = map(int, input().split())
processMin = int(input())


finalHour = hour + int((processMin + minute) / 60)
finalMinute = (minute + processMin) % 60

if finalHour >= 24:
    finalHour = finalHour - 24
    print(f"{finalHour} {finalMinute}")
else:
    print(f"{finalHour} {finalMinute}")
