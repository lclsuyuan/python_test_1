# celsius = eval(input("请输入摄氏温度"))
# #fahrenheit = (9/5)*celsius+32
# print('华氏温度为：',((9/5)*celsius+32))

# import math
# #引用数学模块
# radius = eval(input("请输入圆柱体的半径："))
# length = eval(input("请输入圆柱体的半径："))
# area = radius**2*math.pi
# #math.pi：引用圆周率
# print('圆柱体的底面积（area）为：',round(area,2))
# print('圆柱体的体积（volumn）为：',round(area*length,2))

# feet = eval(input("Enter a valus for feet:"))
# print(str(feet)+"is",feet*0.305,"meters")
# #,连接数值和字符串，+连接字符串和字符串
#
# M = eval(input("Enther the amount of water in kilograms:"))
# initalTemperature = eval(input("Enther the inital Temperature:"))
# finalTemperature = eval(input("Enther the final Temperature:"))
# print("The energy needed is : ",M*(finalTemperature-initalTemperature)*4184)

# balance_interest_rate = eval(input("请输入差额与年利率：（balance,interest rate）"))
# print(round(balance_interest_rate[0]*(balance_interest_rate[1]/1200),5))

# v0,v1,t = eval(input("Enter v0,v1,and t:"))
# print("The average acceleration is ",round((v1-v0)/t,4))

# sum0,lilv = eval(input("请输入本金和年利率："))
# sum = 0
# counter = 1
# while counter<=6:
#     sum = (sum0+sum)*(1+lilv/12)
#     counter +=1
# print("After the sixth month,the account value is : ",round(sum,2))

number = eval(input("请输入一个0到1000之间的整数"))
sum =0
while number>0:
    sum=sum+number%10
    number=number//10
print("这个数字的各位数子之和为：",sum)

