import sys

numbers = sys.argv[1:]

result = 0
for i in numbers:
    result += i

print(result)