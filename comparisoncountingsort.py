list = [2,6,3,9,5,8]
count = []
S = []
for i in range(len(list)):
    count.append(0)
for i in range(len(list)):
    S.append(0)

for i in range(len(list)):
    for j in range (i+1,len(list)):
        if list[i] > list[j]:
            count[i] += 1
        elif list[i] < list[j]:
            count[j] += 1
print(count)
for i in range(len(list)):
    S[count[i]] = list[i]
print(S)

