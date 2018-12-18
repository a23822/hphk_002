import requests
import random
from bs4 import BeautifulSoup as bs

url = 'https://m.dhlottery.co.kr/gameResult.do?method=byWin'
res = requests.get(url).text

soup = bs(res, 'html.parser')
pick = soup.select('#container > div > div.bx_lotto_winnum')
#print(pick)

#로또번호 뽑아오기
picknum = []
for i in pick:
  picknum.append(i.text)
#print(picknum)
#print(picknum[0])
tmp = str(picknum[0]).split('\n')
lastnum = []
for i in range(1,7):
  lastnum.append(int(tmp[i]))
lastnum.append(int(tmp[8]))
print("지난 주 로또 당첨 번호 결과는 {} 입니다.".format(lastnum))


#로또 사기
lotto = sorted(random.sample(list(range(1,46)),6))
#lotto = [2, 25, 28, 30, 6, 45]
print("구입하신 번호는 {} 입니다.".format(lotto))

#뽑은 로또번호를 지난 주 로또 결과와 확인
cnt = 0
for num in lastnum :
  if num in lotto :
    cnt = cnt + 1
print("번호를 총 {} 개 맞추셨습니다!!".format(cnt))
print("-------------------------------------------")
#당첨금 들고오기
money = soup.select('.tbl_basic')[0]
step = money.select('strong')
step2 = []
for i in step:
  step2.append(str(i.text))
mNum = step2
#print(step2)

#당첨인원 들고오기
people = soup.select('.tbl_basic')[0]
step3 = people.select('td')
tmpstep = [0, 5, 9, 13, 17]
step4 = []
for i in tmpstep:
  step4.append(str(step3[i].text))
pNum = []
for i in step4:
  pNum.append(i[:-1])
#print(pNum)

#3개맞추면 5등
if cnt == 3 :
  print("5등입니다")
  print("당첨금은 {} 이며 당첨 인원은 총 {} 명입니다.".format(mNum[4], pNum[4]))
#4개맞추면 4등
elif cnt == 4 :
  print("4등입니다")
  print("당첨금은 {} 이며 당첨 인원은 총 {} 명입니다.".format(mNum[3], pNum[3]))
#5개맞추면 3등, 보너스 숫자가 맞추면 2등
elif cnt == 5 :
  if lastnum[6] in lotto:
        print("2등입니다")
        print("당첨금은 {} 이며 당첨 인원은 총 {} 명입니다.".format(mNum[1], pNum[1]))
  else:
        print("3등입니다")
        print("당첨금은 {} 이며 당첨 인원은 총 {} 명입니다.".format(mNum[2], pNum[2]))
#6개맞추면 1등
elif cnt == 6 :
  print("1등입니다")
  print("당첨금은 {} 이며 당첨 인원은 총 {} 명입니다.".format(mNum[0], pNum[0]))
else:
  print("꽝입니다...쥬륵")