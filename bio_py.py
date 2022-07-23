import numpy as np
from datetime import datetime, timedelta

#strptime()함수는 string parse time의 줄임말이고 문자열을 가공해 time으로 만든다.
BIRTHDAY = datetime.strptime('2002-05-20', "%Y-%m-%d")
TODAY = datetime.now()
delta = TODAY - BIRTHDAY
n_days_ago = delta.days

#생일문자열을 time숫자로 변환
datetime.strptime('2002-05-20', '%Y-%m-%d')

for i in range(-15,16): #현재를 기준으로 과거 15일 미래 15일 총 30일을 분석한다.
    tdelta = TODAY + timedelta(days=i)
    count_days = n_days_ago + i
    date = tdelta.strftime('%Y-%m-%d')
    bio_phy = round( np.sin(2*3.14*count_days / 23) * 100 )
    bio_emo = round( np.sin(2*3.14*count_days / 28) * 100 )
    bio_int = round( np.sin(2*3.14*count_days / 33) * 100 )
    print(date,bio_phy, bio_emo, bio_int)

    #결과값은 numpy로 확인