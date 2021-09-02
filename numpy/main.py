# -*- coding = utf-8 -*-
# @Time : 2021/8/18 9:42
# @Author : 何帅
# @File : main.py
# @software : PyCharm

import numpy as np
import random

#1.创建矩阵（数组），ndarray数据类型
'''
①创建数组：array([1,2,3]) array(range(10)) arange(2,10,2)
②改变数组值的数据类型：dtype astype
③指定形状
④修改形状：reshape()返回新形状数组；shape修改原数组形状
'''
# #传入list
# t1 = np.array([1,2,3])
# t2 = np.array(range(10))
# #arange方法（同t2）
# t3 = np.arange(2,10,2)
# #创建指定数据类型的数组（numpy的数据类型类似C语言）
# t4 = np.array(range(2,10),dtype="float")
# t5 = np.array([1,1,0,0],dtype="bool")
# #修改数据类型，不改变原数据
# t6 = t4.astype("int64")
# #numpy创建小数并指定位数
# #创建5个随机小数
# t7 = np.array([random.random() for i in range(5)])
# #指定小数位数
# t8 = np.round(t7,2)
# #创建指定形状（维数）的数组
# #二维
# t9 = np.array([[1,2,3],[4,5,6]])
# #三维
# t10 = np.array([[[1,2,3]], [[7,8,9]]])
# #改变数据形状（维数）
# #修改为一维
# t11 = t2.reshape((10,))
# t14 = t2.flatten()#形状未知转换为一维
# #修改为二维（不改变原数据）
# t12 = t2.reshape((2,5))#2x5=10#t2不变
# t2.shape = (2,5)#t2变化
# #修改为三维
# t13 = t2.reshape((2,1,5))

# print(t8)
# print(type(t8))
# print(t8.dtype)#数组内数据的类型
# print(t14)
# print(t11.shape)#查看数组形状，返回元组（有几个数就是几维）
#print(t9.shape[0])#行数
#print(t9.shape[1])#列数

# #2.数组的运算
'''
①两个不同形状数组：广播 
②两个相同形状数组：算术函数 add() subtract() multiply() divide() reciprocal() power()
#运算条件：广播：一维数组只要与二维数组的一个数字相同即可运算，二维数组需要与三维数组的后两位（内部二维）相同才能运算
         算术函数：相同维数形状相同即可运算
'''
#①广播
# t1 = np.arange(10)
# #数组与数的+、-、*、/运算
# t2 = t1 +2
# t3 = t1 *2
# #数组与数组的运算（行或者列数据个数相同即可，不一定同维数）
# t4 = np.array(range(0,15)).reshape((3,5))
# t5 = np.array(range(0,5))
# t6 = np.array(range(0,3)).reshape((3,1))
# t7 = t4 - t5#t4每列减t5每列
# t8 = t4 - t6#t4每行减t5每行
# t9= t4 * t5#t4每列与t5每列相乘
# t10 = np.array(range(0,30)).reshape((2,3,5))
# t11 = t10 * t4
#
#②算术函数
# t12 = np.array(range(10)).reshape((2,5))
# t13 = np.array(range(10,20)).reshape((2,5))
#加
# t14 = np.add(t12,t13)
# t14 = t12 + t13#同上
#减
# t15 = np.subtract(t12,t13)
# t15 = t12 - t13
#乘
# t16 = np.multiply(t12,t13)
# t16 = t12 * t13
#除
# t17 = np.divide(t12,t13)
# t17 = t12 / t13
#倒数
# t18 = np.reciprocal(t13.astype("float"))
#幂函数
# t19 = np.power(t12,t13)#t12^t13
#求余
# t20 = np.mod(t13,t12)
# print(t12,'\n',t13,'\n',t20)



# #3.数组转置
'''
transpose() swapaxes() T
'''
# t1 = np.array(range(10)).reshape((2,5))
# # t2 = t1.transpose()
# # t2 = t1.swapaxes(1,0)#交换0,1轴
# t2 = t1.T
#
# print(t1,'\n',t2)


#4.索引与切片
'''
①某一行、列
②连续多行、列
③任意多行、列
④任意一点
⑤任意多点
'''
# t1 = np.array(range(20)).reshape((4,5))
# #取某一行
# t2 = t1[0]
# #取连续多行
# # t3 = t1[2:]
# t3 = t1[1:3]
# #取任意多行
# t4 = t1[[0,2,3]]
# t5 = t1[[0,2,3],1]#逗号前取行，逗号后取列
# #取任意列
# t6 = t1[1:4,1:4]#取第2-4行和第2-4列交叉点
# t7 = t1[1:,[0,1]]
# #取任意值
# t8 = t1[0,1]#numpy.int32类型
# #取任意多个点
# t9 = t1[[0,1],[0,2]]#取[0,0]、[1,2]交叉点
#
# print(t1,'\n','\n',t9,type(t8))


#5.数值的修改
'''
①修改数值
②布尔索引：返回布尔数组
③三元运算符
④裁剪：clip()
'''
# t1 = np.array(range(30)).reshape(5,6)
# #修改数值
# t1[0:2,1:3] = 5
# #布尔索引
# print(t1< 10)
# t1[t1>25] = 25#使大于25的值修改为25
# #三元运算符
# t2 = np.where(t1<5,0,t1)#t1<5处的数值为0，否则不变
# #裁剪
# t3 = t1.clip(10,20)#使t1<10处数值为10，t1>20处数值为20
# print(t3,'\n')


#6.数组的拼接
'''
①垂直拼接：vstack() 
②水平拼接：hstack()
③行列交换： = 
'''
# t1 = np.array(range(10)).reshape((2,5))
# t2 = np.array(range(10,20)).reshape((2,5))
# #垂直拼接
# t3 = np.vstack((t1,t2))
# #水平拼接
# t4 = np.hstack((t1,t2))
# #行列交换
# t1[[0,1],:] = t1[[1,0],:]#行交换
# t2[:,[0,1]] = t2[:,[1,0]]#列交换
#
# print(t3,'\n','\n',t4)


# #7.其余功能函数
'''
①创建特殊数组：zeros() ones() eye() 
②获取最大最小值位置：argmax() argmin()
③生成随机数组：random()
④无复制：地址相同，修改同变化（改变形状、改值） 浅拷贝：地址独立，仅改值同变化； 深拷贝：地址独立，修改不同变
  无复制：=  浅拷贝：view()、切片复制（行列无元组）  深拷贝：copy()
'''
# #创建全为0的数组
# t1 = np.zeros((2,3))
# #创建全为1的数组
# t2 = np.ones((3,4))
# #创建单位阵
# t3 = np.eye(4)
# #获取最大、最小值的位置
# t3 = np.array(range(10)).reshape((2,5))
# t4 = np.argmax(t3,axis=1)#行方向上每列的最大值位置
# # t3[t3==1] = -1
# t5 = np.argmin(t3,axis=1)#列方向上每行的最小值位置
# #生成随机数
# # np.random.seed(10)#随即种子，使后面随机生成的数组一样
# t6 = np.random.randint(10,20,(3,4))#生成3行4列的[19,20)的随机数组
# #传值
#无复制：改变t7的值或形状，t6一起变（二者存储地址一致）
# t7 = t6
# t7.shape = (2,6)#t6变
# t7[t7>10] = 10#t6变
#浅拷贝：仅改变t7数值时，t6一起变
# t7 = t6.view()#t6变
# t7 = t6[:,0:2]#行列均为切片时才产生浅拷贝，含元组为深拷贝
# t7 = t6[:,[0,1]]#深拷贝，t6不变
# t7[0:2] = 10
# t7.shape = (2,6)#t6不变
#深拷贝：改变t6，t7不变（二者存储地址不一致）
# t8 = t6.copy()
# t8[0] = 10#不变
# t8.shape = (2,6)#不变
#
# print(t6,'\n','\n',t7)


#8.nan和inf、-inf
'''
①计数nan：count_nonzero(t1!=t1) 和 count_nonzero(np.isnan(t1))
②查找nan位置：t1[t1!=t1]!=0成立
'''
# #nan:not a number(0/0、无穷-无穷)
# #inf:infinity 正无穷 -inf:负无穷（分母为0）
# np.nan != np.nan#两次生成的nan不是一致的
# t1 = np.eye(4)
# #计数不为0的个数
# t2 = np.count_nonzero(t1)
# #查看数组中哪些值为nan，返回True、Flase的数组
# t2 = np.isnan(t1)
# #计数数组中nan的个数
# t1[3,3] = np.nan
# t2 = np.count_nonzero(t1!=t1)#①
# t2 = np.count_nonzero(np.isnan(t1))#②
# #求和（nan和数的计算结果为nan）
# t1 = np.array(range(10)).reshape((2,5)).astype("float")
# t1[1,4] = np.nan
# t3 = np.sum(t1,axis=0)#行方向上每列的和
# t4 = np.sum(t1,axis=1)#列方向上每行的和
#
# print(t3,'\n','\n',t4)


#9.统计函数
'''
①求和：sum()
②均值：mean()
③加权平均值：average()
④中值：median()
⑤最大最小值：max() min()
⑥极值：ptp()
⑦标准差和方差：std() var()
'''
# t1 = np.array(range(12)).reshape(3,4).astype("float")
# t1[2,3] = np.nan
# #求和
# t2 = t1.sum()#总和
# t3 = t1.sum(axis=0)#行方向上每列的和
# t3 = np.sum(t1,axis=0)#同上
# t4 = t1.sum(axis=1)#列方向上每行的和
# t4 = np.sum(t1,axis=1)#同上
# #均值
# t5 = t1.mean(axis=0)#行方向上每列的均值
# t5 = np.mean(t1,axis=0)
#加权平均值
# t12 = [1,2,3]
# t13 = np.average(t1,axis=0,weights=t12)
# #中值
# t6 = np.median(t1,axis=0)
# #最大值
# t7 = t1.max(axis=0)
# #最小值
# t8 = t1.min(axis=1)
# #极值（最大值-最小值）
# t9 = np.ptp(t1,axis=0)
# #标准差
# t10 = t1.std(axis=0)
# t10 = np.std(t1,axis=0)
#方差
# t11 = np.var(t1,axis=0)
#
# print(t1,'\n',t13)


# 练习：将数组中的nan数替换为对应列的均值
"""
①先遍历每列通过nan计数判断是否存在nan
②将非nan数组提取出来求均值
③将nan位置数据替换为均值
"""
# t1 = np.array(range(12)).reshape((3,4)).astype("float")
# t1[1,2:] = np.nan
# print(t1)
#
# for i in range(t1.shape[1]):
#     temp = t1[:,i]
#     # temp = t1[:,i].copy()
#     if np.count_nonzero(np.isnan(temp))!=0:
#         temp1 = temp[temp==temp]
#         temp2 = temp1.mean()
#         temp[temp!=temp] = temp2
#     # t1[:,i] = temp#使用浅拷贝时使用
# print(t1)


#10.矩阵：二维数组
# #转置矩阵
# t1 = np.array(range(10)).reshape((2,5))
# t2 = t1.T
# #生成指定类型的随意数组
# t3 = np.empty((2,2),dtype="int32")
# #全为0或1的矩阵、单位阵
# t4 = np.zeros((2,3))
# t5 = np.ones((2,3))
# t6 = np.eye(2)
# #随机值的矩阵
# t7 = np.random.randint(10,20,(3,3))
#
# print(t1,'\n',t7)


#11.线性代数运算
'''
①数组的点积：dot()
②向量的点积：vdot()，二维数组返回一个数
③数组的点积：inner()，一维数组返回一个数，二维数组返回数组
④计算行列式：linalg.det()
⑤计算逆矩阵：linalg.inv()，矩阵的行列式！=0才可逆
'''
# t1 = np.array(range(12)).reshape((3,4))
# t2 = np.array((range(12,24))).reshape((4,3))
# #数组的点积（即数组内积：行列相乘再相加）
# t3 = np.dot(t1,t2)#mxn nxm形状的数组
#
# t4 = t2.reshape((3,4))
# #向量的点积（即向量内积：对应相乘再求和，返回一个数）
# t5 = np.vdot(t1,t2)#mxn mxn同形状的数组
# #数组的点积（对应相乘再相加，返回一个mxn形状的数组）
# t6 = np.inner(t1,t4)
#
# t7 = np.array(range(1,10)).reshape((3,3))
# #计算输入矩阵的行列式(对角线法则)
# t8 = np.linalg.det(t7)
# #计算逆矩阵(AB=BA=E，则AB互为逆矩阵，A的行列式！=0则A可逆）
# t7[0,1] = 9
# t9 = np.linalg.inv(t7)#n阶矩阵
#
# print(t9)
