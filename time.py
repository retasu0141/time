import pytz,datetime
def time():

    if 'おはようございます' == input():
        print('おはようございます！今日も一日頑張りましょう！')
        if '頑張ります' == input():
            tz = pytz.timezone("Asia/Tokyo")
            t1 = datetime.datetime.now(tz=tz)
            print('いってらっしゃい！' + str(t1))
        else:
            print('頑張りますは？挨拶からやりなおし!')

    if 'お疲れ様でした' == input():
        tz = pytz.timezone("Asia/Tokyo")
        t2 = datetime.datetime.now(tz=tz)
        data = t2- t1
        print('お疲れ様です! 経過時間→' + str(data))

while True:
    time()