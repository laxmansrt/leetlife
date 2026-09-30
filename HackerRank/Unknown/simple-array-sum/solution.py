def simpleArraySum(ar):
    total = 0

    for num in ar:
        total += num

    return total


n = int(input())
ar = list(map(int, input().split()))

result = simpleArraySum(ar)

print(result)
