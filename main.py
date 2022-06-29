import math
import random

custumer = [1,2,3,4,5,6,7,8,9,10]
i = 0
infoCount = []
while i < 10:
    infoCount.append(random.randint(1,5))
    i += 1

index = 0
infoWeight = []
i = 0
while i < 10:

    infoWeight.append((random.randint(1,3)) * infoCount[index])
    i += 1
    index += 1

a1 = 0
for e in infoCount:
    if e >= 2:
        a1 += 1

for e in infoWeight:
    print (custumer.index(e))

print(infoCount)
print(infoWeight)

print("____________________________")
print(a1)
print(a1)
print('ghjglhlkhlh')