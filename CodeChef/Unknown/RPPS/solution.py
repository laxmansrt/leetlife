# cook your dish here
s = input().strip()

count = {}

for i in range(len(s) - 1):
    pair = s[i:i+2]
    count[pair] = count.get(pair, 0) + 1

answer = 0

for pair in count:
    if count[pair] >= 2:
        answer += 1

print(answer)