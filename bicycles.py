# 列表
bicycles = ['1','2','3','4','5']
print(bicycles)

# 访问列表元素

print(bicycles[0]) # 1
print(bicycles[0].title()) #首字母大写

# 索引自0 开始

#使用列表中的各个值


# 1 修改 添加和删除元素

# 修改

motorcycles = ['honda','ddhd','hdjhsjhks']

motorcycles[0] = 'hjkssk'
print(motorcycles)

# 添加
addcycles = []
addcycles.append('add1')
addcycles.append('add2')
addcycles.append('add3')
print(addcycles)

# 末尾添加
motorcycles.append('jhssj')
print(motorcycles)

#在列表中插入新元素

addcycles.insert(0,'jjhjk')
print(addcycles)

#从列表中删除数据
del addcycles[0]
print(addcycles)

poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)



