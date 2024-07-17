### 오답 ###
# 백준 1251번 : 단어 나누기

string = list(input())

s1 = string[:-2]
i1 = string.index(sorted(s1)[0])
s1 = string[:i1+1]
s1.reverse()

s2 = string[i1+1:-1]
i2 = string.index(sorted(s2)[0])
s2 = string[i1+1:i2+1]
s2.reverse()

s3 = string[i2+1:]
s3.reverse()

rstring = s1 + s2 + s3
result = ''.join(rstring)
print(result)