# -*- coding = utf-8 -*-
# @Time : 2021/8/22 17:53
# @Author : 何帅
# @File : main.py
# @software : PyCharm

import pandas as pd
import numpy as np

#1.Series数据类型：一维，带标签数组 索引->值 index->values
'''
①创建Series：pd.Series()：传入列表或字典
②修改数值类型：astype()
③取某个值：t[]：索引或键
④取多行：t[ : ] t[ , ]
⑤布尔索引：t[t>2]
⑥查看索引或值：t.index t.values（可迭代）
'''
# #通过列表创建索引
# t1 = pd.Series(range(1,10))#索引为0-9
# # t2 = pd.Series(range(2,7),index = ['a','b','c','d','e'])#指定索引
# t2 = pd.Series(range(2,7),index = list(('abcde')))
# #通过字典创建索引
# t3 = {"name":"xiaoming","age":"18","sex":"man"}
# t4 = pd.Series(t3)
# #修改数值类型
# t5 = t2.astype("float")#返回新Series
# #Series的切片和索引
# #取一个值：索引位置或者键
# # t6 = t4["name"]
# t6 = t4[0]#同上
# #取多行
# t7 = t4[:2]#连续多行
# # t8 = t4[[0,1]]#取任意多行
# t8 = t4[["name","age"]]#同上
# #布尔索引
# t9 = t2[t2>1]#返回大于1的值
# #查看Series的索引和值，二者的返回结果可迭代
# t10 = t4.index
# t11 = t4.values
# # for i in t4.index:
# #     print(i)
# t12 = len(t10)#计算长度
# t13 = list(t10)[:2]#转换为list并切片
#
# print(t13)


#2.DataFrame:二维，Series容器
'''
创建DataFrame：pd.DataFrame()：传入列表或字典
'''
# #创建DataFrame
# t1 = pd.DataFrame(np.array(range(12)).reshape((3,4)))#包含行索引index（axis=0）和列索引columns（axis=1）
# t2 = pd.DataFrame(np.arange(12).reshape((3,4)),index=list("abc"),columns=list("1234"))#加入索引
# t3 = {"name":["xiaoming","xiaohong"],"age":[18,20],"sex":["man","woman"]}#传入字典，键为列索引columns
# t4 = pd.DataFrame(t3)
# t5 = [{"name":"xiaoming","age":18,"sex":"man"},{"name":"xiaohong","age":20}]#传入列表，缺失值返回NaN
# t6 = pd.DataFrame(t5)
#
# print(t6)


#3.导入文件到DataFrame
'''
导入各种文件：read_***()
'''
# t1 = pd.read_csv("./nba.csv")
# t2 = pd.DataFrame(t1)
#
# print(t2)


#4.DataFrame基础属性及查询
'''
①基础属性：shape：形状 dtypes：类型 ndim：维数 index：行索引 columns：列索引 values：值
②查询：head()：显示头*行 tail()：显示尾*行 info()：数据信息 describe()：统计数据
'''
# t1 = pd.DataFrame(np.arange(12).reshape((3,4)),index=list("abc"))
#基础属性
# t2 = t1.shape#形状
# t2 = t1.dtypes#数据类型
# t2 = t1.ndim#维度
# t2 = t1.index#行索引
# t2 = t1.columns#列索引
# t2 = t1.values#对象值，ndarry类型
#查询
# t3 = t1.head(1)#显示头几行
# t3 = t1.tail(1)#显示尾几行
# t3 = t1.info()#显示行数、列数、索引、非空个数、类型、内存
# t3 = t1.describe()#显示数值类型的计数、均值、标准差、最小值、几分位数、最大值
#
# print(t3)


#5.数据排序
'''
升降序排序：sort_values()
'''
# t1 = pd.read_csv("./nba.csv")
# t2 = t1.head()
# t3 = t1.sort_values(by="Salary",ascending=False)#以Salary为基准，降序排序
#
# print(t3.head(10))


#6.切片与索引
'''
①原始索引：t[][]
②loc索引：t[ , ]
③iloc索引：t[ , ]
④布尔索引：t[()&()] t[()|()]
'''
# t1 = pd.DataFrame(np.arange(12).reshape((3,4)),index=list("abc"))
# t2 = t1[:'a']#取某一行
# t3 = t1[0]#取某一列
# t4 = t1[:'b'][0]#取某些行列交叉
# #loc：标签索引，逗号前为行，后为列
# t5 = t1.loc['a',0]#某一个值
# t6 = t1.loc['a',:]#某一行
# t7 = t1.loc[:,0:2]#某两列****注意：0:2切片包含2
# t8 = t1.loc[['a','c'],:]#任意多行
# t9 = t1.loc[['a','c'],[0,2]]#取任意多个值
# #iloc：位置索引逗号前为行，后为列（全为数字）
# t10 = t1.iloc[[0,1],0:2]#同 t1.col[['a','b'],0:1]
# #通过iloc修改值
# t1.iloc[0:2,0] = 100
#布尔索引
# t11 = t1[(t1.iloc[:,0]>2) & (t1.iloc[:,0]<8)]#返回True那一行
#
# print((t1.iloc[:,0]>2) & (t1.iloc[:,0]<8))#返回第一列的布尔值


#7.确实数据的处理
'''
①判断是否存在nan：pd.isnull() pd.notnull()
②删除nan所在行：dropna()
③替换nan数据：fillna(100)：填充常数 fillna(t.mean())：均值 fillna(t.median()) ：中值
'''
# t1 = pd.DataFrame(np.arange(12).reshape((3,4)),index=list('abc'))
# t1[t1[:'a']>1] = np.nan
# #①判断是否存在NaN
# t2 = pd.isnull(t1)
# t3 = t1[pd.isnull(t1[3])]#返回nan所在行数据
# #处理数据：删除或填充
# t1.dropna(axis=0,how="any",inplace=True)#删除nan所在行
# t4 = t1.fillna(t1.mean())#存在nan的位置替换为所在列的平均值
# t1[3] = t1[3].fillna(t1[3].mean())#某一列nan的位置替换为所在列的平均值
# t1 = t1.fillna(100)#替换为常数
# t1[t1==0] = np.nan#使等于0的位置的数值变为nan，不参与运算
# t1[0] = t1[0].fillna(t1[0].median())#nan数值替换为中值
#
# print(t1)