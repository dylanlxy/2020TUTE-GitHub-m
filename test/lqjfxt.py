#篮球记分系统
huren = []
zhongguo = []
print('****************NBA比赛记分系统****************')
def fenshu():
    dui = input('请选择得分球队：湖人队【1】 中国队【2】比赛结果按：e\n请输入：')
    if dui == '1':
        while 1:
            defen = input("您选择的是【湖人队】请输入得分：\n得分(输入q退出)：")
            if defen == 'q':
                fenshu()
            elif defen.isdigit():
                defen = int(defen)
                huren.append(defen)
            else:
                print('输入有误，请输入数字！')
    elif dui == '2':
        while 1:
            defen = input("您选择的是【中国队】请输入得分：\n得分(输入q退出)：")
            if defen == 'q':
                fenshu()
            elif defen.isdigit():
                defen = int(defen)
                zhongguo.append(defen)
            else:
                print('输入有误，请输入数字！')
    elif dui == 'e':
        print('湖人队得分：',sum(huren))
        print('中国队得分：',sum(zhongguo))
        if sum(huren) > sum(zhongguo):
            print('冠军是：湖人队')

        elif sum(huren) == sum(zhongguo):
            print('比赛为平局！')

        else:
            print('冠军是：中国队\n比赛结束！')
    else:
        print('输入有误，请重新输入！')
        fenshu()
fenshu()
print('****************NBA比赛记分系统****************')

