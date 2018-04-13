# -----创建数值列表--------------

# 使用函数range() 打印0  - 4
for value in range(1,5):
	print(value)

# 使用range()创建数字列表
numbers = list(range(1,5))
print(numbers)

# 使用range() 指定步长 2 4 6 8 10

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表解析

squares = [value**2 for value in range(1,11)]
print(squares)

# 使用列表的一部分

# 切片
players = ['charles','martina','michael','florence','eli']
print(players)
print(players[0:3])
print(players[2:])
print(players[-3:])

# 遍历切片
for value in players[:3]:
	print(value.title())

# 复制列表
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
