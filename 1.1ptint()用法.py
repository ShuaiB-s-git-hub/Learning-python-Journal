# 工程创建人：袁某
# 创作时间： 2022/10/15 18:57

#print()函数可以输出哪些内容?
# (1) print()函数输出的内容可以是数字
print(456789789788429845558875555)
print(3.1415926535867)
print(-5487)
# (2) print()函数输出的内容可以是字符串
print('ybxzs')
print("ybxzs")
# (3) print()函数输出的内容可以是含有运算符的表达式
print(96+4)

# print()函数可以将内容输出的目的地,
# (1)显示器

# (2)文件
                                           #未标明路径就放在默认路径中，这里是和该文件放在同一个文件中
fp = open('ybxzs.txt', 'a+')               #也可以标明路径如print('d:\print\ybxzs.txt','a+')
print('yuan bo xin zui shuai',file=fp)     #至于为啥这么写以后再说
fp.close()               #实践证明，可能这个函数不能直接往txt文件中写中文，否则会出现一堆乱码
# print()函数的输出形式
# (1)换行
#默认换行
# (2)不换行
print('ybx','sydx','zsd')

