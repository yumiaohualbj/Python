

'''
变量
'''
m = "Hello Python Crash Course world!"
print(m)

name = "ada lovelace"
print(name.title()) #title()以首字母大写的方式显示每个单词
print(name.upper()) #字符串全部大写
print(name.lower()) #字符串全部小写

# 合并凭借字符串

first_name = "ada"
last_name = "jdkjdjk"
full_name = first_name + " " + last_name
print(full_name)
# 使用制表符或换行符来添加空白

print("\nPython")


# 删除空白  rstrip()
favorite_language = "python "
favorite_language = favorite_language.rstrip()
print(favorite_language)

print(2+3)
# **乘方
print(2**3)

# 使用函数str() 避免类型错误

age = 23
message = "happy " + str(age) + "rd birthday"
print(message)

