a = int(input())
b = int(input())

# print("a:", a)
# print("b:", b)
# print('------')

i = b % 10
j = (b % 100) - (b % 10)
k = b - (b % 100)

# print(i)
# print(j)
# print(k)
print(a * i)
print(int(a * j / 10))
print(int(a * k / 100))

print(int((a*i) + (a*j) + (a*k)))