# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

#绘制折线图
def show1():
    #宽高、像素点/inch
    fig = plt.figure(figsize=(12,8), dpi=40)
    x = range(2, 26, 2)
    y = [15, 18, 20, 19, 50, 20, 31, 35, 36, 45, 51, 28]
    # 折线图
    plt.plot(x, y)
    xticks_labels = [i/2 for i in range(4,49)]
    # x轴刻度(输入列表)
    plt.xticks(xticks_labels[::3])
    #y轴刻度
    plt.yticks(range(min(y),max(y)+1,5))
    # 保存到本地
    plt.savefig('./test1.svg')
    plt.show()


#绘制多折线图
def show2():
    #字体路径
    my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/simsun.ttc")
    #画布大小
    fig = plt.figure(figsize=(16, 8), dpi=40)
    #坐标轴列表
    x = range(0,120)#python3创建为可迭代对象，非列表
    y1 = [random.randint(10,30) for i in range(120)]
    y2 = [random.randint(15,35) for i in range(120)]
    #绘制折线图
    plt.plot(x, y1,label="数1",color='r',linestyle='--')
    plt.plot(x, y2,label="数2",color='g')
    #刻度列表
    xticks_labels = ["10点{}分".format(i) for i in range(60)]
    xticks_labels += ["11点{}分".format(i) for i in range(60)]
    #绘制刻度 对应点需要对应，步长一致
    plt.xticks(list(x)[::2],xticks_labels[::2],rotation=45,fontproperties=my_font)#旋转、中文字体
    plt.yticks(y1)
    #设置坐标轴名称、标题
    plt.xlabel("时间",fontproperties=my_font)
    plt.ylabel("温度 单位（℃）",fontproperties=my_font)
    plt.title("10点到12点的温度变化",fontproperties=my_font)
    #添加图例
    plt.legend(prop=my_font,loc="upper right")#中文字体、图例位置
    #绘制栅格（与刻度对应）
    plt.grid(alpha=0.4)#透明度
    #保存到本地
    plt.savefig('./test2.svg')
    #显示
    plt.show()


#绘制散点图
def show3():
    #中文字体
    my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/simsun.ttc")
    #设置画布
    fig = plt.figure(figsize=(16,8),dpi=40)
    #坐标轴列表
    x1 = range(1,32)
    x2 = range(51,82)
    y1 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
    y2 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,16]
    #绘制散点图
    plt.scatter(x1,y1,label="3月")
    plt.scatter(x2,y2,label="10月")
    #刻度列表
    x_axis = list(x1) + list(x2)
    xticks_labels = ["3月{}日".format(i) for i in range(1,32)] + ["10月{}日".format(i) for i in range(1,32)]
    #绘制刻度
    plt.xticks(x_axis[::2],xticks_labels[::2],rotation=45,fontproperties=my_font)
    #设置坐标轴名称、标题
    plt.xlabel("时间",fontproperties=my_font)
    plt.ylabel("温度",fontproperties=my_font)
    plt.title("3月和10月的温度",fontproperties=my_font)
    #添加图例
    plt.legend(prop=my_font,loc="upper left")
    #保存
    plt.savefig("test3.svg")
    #显示
    plt.show()


#绘制纵向条形图
def show4():
    #中文字体
    my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/simsun.ttc")
    #画布大小
    plt.figure(figsize=(16,10),dpi=40)
    #坐标轴列表
    x = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5：最后的骑士","摔跤吧！爸爸","加勒比海盗5：死无对证","金刚：骷髅岛","极限特工：终极回归","生化危机6：终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3：殊死一战","蜘蛛侠：英雄归来","悟空传","银河护卫队2","情圣","新木乃伊",]
    y = [56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]
    #绘制条形图
    plt.bar(range(len(x)),y)
    #刻度列表
    x_axis = range(len(x))
    plt.xticks(x_axis,x,rotation=90,fontproperties=my_font)
    #保存
    plt.savefig("./test4.svg")
    #显示
    plt.show()


#绘制横向条形图
def show5():
    #中文字体
    my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/simsun.ttc")
    #画布大小
    plt.figure(figsize=(16,8),dpi=40)
    # 坐标轴列表
    y = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5：最后的骑士", "摔跤吧！爸爸", "加勒比海盗5：死无对证", "金刚：骷髅岛", "极限特工：终极回归", "生化危机6：终章",
         "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3：殊死一战", "蜘蛛侠：英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊", ]
    x = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88,
         6.86, 6.58, 6.23]
    # 绘制条形图
    plt.barh(range(len(y)), x,color="orange",height=0.5)
    # 刻度列表
    y_axis = range(len(y))
    plt.yticks(y_axis, y, fontproperties=my_font)
    #栅格
    plt.grid(alpha=0.3)
    # 保存
    plt.savefig("./test5.svg")
    # 显示
    plt.show()


#绘制多条条形图
def show6():
    bar_width = 0.4
    my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/simsun.ttc")
    plt.figure(figsize=(16,8),dpi=40)
    a = ["猩球崛起3：终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]
    b_16 = [15746, 312, 4497, 319]
    b_15 = [12357, 156, 2045, 168]
    b_14 = [2358, 399, 2358, 362]
    x_14 = list(range(0,2*len(a),2))
    x_15 = [i+bar_width for i in x_14]
    x_16 = [i+bar_width*2 for i in x_14]
    plt.bar(x_14,b_14,width=bar_width,label="9月14日")
    plt.bar(x_15,b_15,width=bar_width,label="9月15日")
    plt.bar(x_16,b_16,width=bar_width,label="9月16日")
    plt.legend(prop=my_font)
    plt.xticks(x_15,a,fontproperties=my_font)
    plt.savefig("./test6.svg")
    plt.show()


#绘制直方图
def show7():
    #中文字体
    my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/simsun.ttc")
    # 画布大小
    plt.figure(figsize=(16, 8), dpi=40)
    #数据
    a = [131, 98, 125, 131, 124, 139, 131, 117, 128, 108, 135, 138, 131, 102, 107, 114, 119, 128, 121, 142, 127, 130,
         124, 101, 110, 116, 117, 110, 128, 128, 115, 99, 136, 126, 134, 95, 138, 117, 111, 78, 132, 124, 113, 150, 110,
         117, 86, 95, 144, 105, 126, 130, 126, 130, 126, 116, 123, 106, 112, 138, 123, 86, 101, 99, 136, 123, 117, 119,
         105, 137, 123, 128, 125, 104, 109, 134, 125, 127, 105, 120, 107, 129, 116, 108, 132, 103, 136, 118, 102, 120,
         114, 105, 115, 132, 145, 119, 121, 112, 139, 125, 138, 109, 132, 134, 156, 106, 117, 127, 144, 139, 139, 119,
         140, 83, 110, 102, 123, 107, 143, 115, 136, 118, 139, 123, 112, 118, 125, 109, 119, 133, 112, 114, 122, 109,
         106, 123, 116, 131, 127, 115, 118, 112, 135, 115, 146, 137, 116, 103, 144, 83, 123, 111, 110, 111, 100, 154,
         136, 100, 118, 119, 133, 134, 106, 129, 126, 110, 111, 109, 141, 120, 117, 106, 149, 122, 122, 110, 118, 127,
         121, 114, 125, 126, 114, 140, 103, 130, 141, 117, 106, 114, 121, 114, 133, 137, 92, 121, 112, 146, 97, 137,
         105, 98, 117, 112, 81, 97, 139, 113, 134, 106, 144, 110, 137, 137, 111, 104, 117, 100, 111, 101, 110, 105, 129,
         137, 112, 120, 113, 133, 112, 83, 94, 146, 133, 101, 131, 116, 111, 84, 137, 115, 122, 106, 144, 109, 123, 116,
         111, 111, 133, 150]
    #分组
    dis = 3
    num_bins = (max(a)-min(a))//dis
    #绘制直方图
    # plt.hist(a,num_bins)#数量
    plt.hist(a, num_bins, density=True,stacked=True,label="电影时长频率")#频率
    #设置刻度
    plt.xticks(range(min(a),max(a)+dis,dis))
    #图例
    plt.legend(prop=my_font)
    # 栅格
    plt.grid(alpha=0.3)
    #保存
    plt.savefig("./test7.svg")
    #显示
    plt.show()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # show1()
    # show2()
    # show3()
    # show4()
    # show5()
    # show6()
    show7()