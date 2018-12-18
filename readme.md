# 2018-12-18 학습 내용

#### 로또 번호 추첨 코딩

``` python
import random

# 1~45까지 숫자를 가진 배열을 갖는다.
numList = []
for i in range(1,46) :
  numList.append(i)
print(numList)

#numbers 에서 숫자 6개를 랜덤으로 비복원 추출
numbers = random.sample(numList, 6)

#랜덤으로 뽑은 숫자들을 lotto 변수에 담고 출력한다.
lotto = numbers
print(lotto)

#추가: lotto 변수에 담겨있는 숫자들을 오름차순으로 정렬
res = sorted(numbers)
print("이번 주 로또 추천 번호는 {} 입니다.".format(res))

#lotto = sorted(random.sample(list(range(1,46)),6))
```



#### 지난 주 로또번호와 비교하기

``` python
import requests
import random
from bs4 import BeautifulSoup as bs

url = 'https://m.dhlottery.co.kr/common.do?method=main'
res = requests.get(url).text

soup = bs(res, 'html.parser')
pick = soup.select('.prizeresult')[0]
picknum = pick.select('span')
# 지난 주 로또 번호 긁어오기
lastnum = []
for i in picknum:
  lastnum.append(int(i.text))
print(lastnum)


numList = []
for i in range(1,46) :
  numList.append(i)
  
#numbers 에서 숫자 6개를 랜덤으로 비복원 추출
numbers = random.sample(numList, 6)

#랜덤으로 뽑은 숫자들을 lotto 변수에 담고 출력한다.
lotto = numbers

#추가: lotto 변수에 담겨있는 숫자들을 오름차순으로 정렬
res = sorted(numbers)
print("로또 번호는 {} 입니다.".format(res))
#lotto = sorted(random.sample(list(range(1,46)),6))

cnt = 0
#자기가 뽑은 것을 지난 주 로또번호와 매치해보며 카운트세기
#for i in range(len(res)) :
#  for j in range(len(lastnum)) :
#    if res[i] == lastnum[j] :
#      cnt = cnt + 1
# 아래 방식이 처리 시 효율이 좋음
for num in lastnum :
  if num in res :
    cnt = cnt + 1
print("번호를 총 {} 개 맞추셨습니다!!".format(cnt))

```





## 복습 및 응용

#### 지난 주 로또 번호 및 결과 확인하기

``` python
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
```



## 네이버웹툰

##### 네이버 썸네일과 리스트 페이지, 제목을 끌어온다.

``` python
import requests
import time
from bs4 import BeautifulSoup as bs

#오늘 날짜 구하기
today = time.strftime("%a").lower()
#1.네이버 웹툰을 가져올 수 있는 주소를 파악한다.
url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=' + today
#2.해당 주소로 요청을 보내 정보를 가져온다.
res = requests.get(url).text
#3.받은 정보를 bs4를 이용해서 검색하기 좋게 만든다.
soup = bs(res, 'html.parser')

pick = soup.select('.thumb')

#print(tmp)
#4.네이버 웹툰 페이지로 가서 내가원하는 정보가 어디에 있는지 파악한다.
#웹툰의 리스트 페이지, 웹툰의 제목 + 썸네일까지
toons = []
li = soup.select('.img_list li')
for item in li:
  toon = {
    "title": item.select('dt a')[0].text,
    "url": "comic.naver.com" + item.select('dt a')[0]["href"],
    "thumbnail" : item.select('.thumb img')[0]["src"]
  }
  toons.append(toon)

#print(li)
#5.받았던 정보를 이용해 4번에서 파악한 위치를 뽑아내는 코드를 작성한다.

#6.출력한다.
print(toons)

```



## 다음웹툰

##### JSON

``` python
import requests
import time
import json

#1.내가 원하는 정보를 얻을 수 있는 주소를 url 변수에 담는다.
url = "http://webtoon.daum.net/data/pc/webtoon/list_serialized/thu"
#2.해당 url 에 요청을 보내 응답을 받는다.
res = requests.get(url).text
print(res)
#3.구글에 json은 파이썬으로 어떻게 파싱(딕셔너리형으로 변환)하는지 검색
#4.파싱
document = json.loads(res)
#print(type(document))
#5. 원하는 정보를 꺼내서 조합한다.
data = document["data"]
for toon in data:
  print(toon["title"])
  print(toon["pcThumbnailImage"]["url"])
  print("http://webtoon.daum.net/webtoon/view/{}".format(toon["nickname"]))

```





##### >  html, python 을 와리가리 할때 안 헤멜려면 공부할 것

>  https://www.codecademy.com 

---

