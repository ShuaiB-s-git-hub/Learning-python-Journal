# 工程创建人：袁某
# 创作时间：2022/10/15 22:20

#str()函数

name=' 张三'
age=20
print(type (name), type (age)) #说明name与age的数据类型不相同
#print ('我叫'+name+'今年,'+age+'岁') #当将str类型与int类型进行连接时,报错,解决方案,类型转换print ('我叫'+name+'今年,'+str (age)+'岁')
print('我叫' + name + '今年,' +str(age) + '岁') #将int类型通过str ()函数转成了str类型,这里 + 作为连接符而出现
#这个函数是否好用，可以用下面代码测试
print('-str()将其它类型转成str类型-')
a=10
b=198.8
c=False
print (type (a), type (b), type (c))
print (str (a), str (b), str (c), type (str (a)), type (str (b)), type (str (c)))



#int（）函数
print ('____________int ()  将其它的类型转int类型')
s1='128'
f1=98.7
s2=' 76. 77'
ff=True
s3=' hello'
print (type (s1), type (f1), type (s2), type (ff), type (s3))
print (int(s1), type (int (s1))) #将str转成int类型,字符串为 数字串
print (int (f1), type (int (f1))) #float转成int类型,截取整数部分,舍掉小数部分
# #print (int (s2), type (int (s2))) #将str转成int类型,报错,因为字符串为小数串
print (int (ff), type (int (ff)))
#print (int (s3), type (int (s3))) #将str转成int类型时,字符串必须为数字串(整数)，非数字串是不允许转换
#
#总结，这东西必须是纯粹整形的表现形式才能转化，bool类型本质是整形
#若数字串中含空格，则不算纯数字串，纯数字串必须由纯粹数字构成


print('_____________float()  将其他类型转换成浮点型')
s1=' 128.98'
s2=' 76'
ff=True
s3=' hello'
i=98
print(type (s1), type (s2), type (ff), type (s3), type (i))
print (float (s1), type (float (s1)))
print (float (s2), type (float (s2)))
print (float (ff), type (float (ff)))
#print(float (s3), type (float (s3))) #字符串中的数据如果是非数字串,则不允许转换
print (float (i), type (float (i)))
#
#总结：这东西必须是数字才能转化，整形转完后小数点会加一个 .0