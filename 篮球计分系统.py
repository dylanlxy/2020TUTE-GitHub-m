# 篮球计分系统
# print('当前：%s：%s比分为：'% (t1,t2),sum(tuan1),'：',sum(tuan2))
# print('当前：%s：%s比分为：%d：%d' % (t1, t2, sum(tuan1), sum(tuan2)))
# t1 = str(input('请输入参数球队名称：'))

"""

题目：编写一个篮球记分系统，操作者输入球队名字和获得分数，由程序进行累加并显示
到屏幕上,然后等待下次输入球队得分，当输入game over时，屏幕显示比赛结束，并自动判
断胜利一方，显示Winer is ×××。

"""

# 定义两个空列表
tuan1 = []
tuan2 = []
# 打印计分系统分隔符
print('****************NBA比赛计分系统****************')
# 定义两个需要输入的常量
t1 = input('请输入参赛团队一名称：\n')
t2 = input('请输入参赛团队二名称：\n')


def get_score():    # 获取比分
    print('****************当前比分情况****************')     # 打印比分分隔符
    print('当前：%s：%s比分为：%d：%d' % (t1, t2, sum(tuan1), sum(tuan2)))      # 打印当前比分情况
    tuan = input('请选择得分球队：%s【1】 %s【2】比赛结果按：game over\n请输入：' % (t1, t2))     # 输入得分球队进行计分
    if tuan == '1':     # 如果选择1
        while True:     # 循环输入得分
            defen = input('您选择的是【%s】请输入得分：\n得分(输入q退出)：' % t1)
            if (defen == 'Q') or (defen == 'q'):
                get_score()
            elif defen.isdigit():       # 判断输入的变量是否是int
                defen = int(defen)      # 定义输入的变量为int
                tuan1.append(defen)     # 在tuan1列表结尾追加输入的数据
            else:
                print('输入有误，请输入数字！')
    elif tuan == '2':
        while True:
            defen = input('您选择的是【%s】请输入得分：\n得分(输入q退出)：' % t2)
            if (defen == 'Q') or (defen == 'q'):
                get_score()
            elif defen.isdigit():
                defen = int(defen)
                tuan2.append(defen)
            else:
                print('输入有误，请输入数字！')
    elif tuan == 'game over':        # 查看比分结果
        print('%s总得分：' % t1, sum(tuan1))       # 打印tuan1的总分
        print('%s总得分：' % t2, sum(tuan2))       # 打印tuan2的总分
        if sum(tuan1) > sum(tuan2):     # 判断比分大小
            print('Winer is：%s\n比赛结束！\n\n****************NBA比赛计分系统****************' % t1)
            exit()      # 结束程序
        elif sum(tuan1) == sum(tuan2):
            print('比赛为平局！\n比赛结束！\n\n****************NBA比赛计分系统****************')
            exit()
        else:
            print('Winer is：%s\n比赛结束！\n\n****************NBA比赛计分系统****************' % t2)
            exit()
    else:
        print('输入有误，请重新输入！')
        get_score()


get_score()
