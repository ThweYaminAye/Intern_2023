name = 'mgmg@gmail.com'
res =[]
s = ''
for i in name:
    res += i
for i in range(len(res) - 10):
    s += res[i]
print(s)