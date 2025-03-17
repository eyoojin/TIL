import random
import requests
from faker import Faker
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def hello(request):
    my_name = 'ruka kawai'

    context = {
        'my_name': my_name,
    }
    return render(request, 'hello.html', context)

def lunch(request):
    menu = '계란말이 숯불닭갈비 소고기무국 곰탕 갈비탕 호박전 치즈감자고로케 쫄병스낵 케밥 골뱅이무침 깍두기 비빔국수 꽃빵 참치비빔밥 불고기버거 겉절이 수제비 파전 명이나물 피자찐빵 오돌뼈 양념게장 팟타이 떡볶이 뼈해장국 가리비구이 비지찌개 무지개떡 간장새우 김밥 녹차모찌 생새우초밥 남산왕돈까스 모닥치기 조랭이떡 녹치케 골뱅이소면무침 김치만두 군만두 물만두 찐빵 멸치볶음 쫄면 순대 곱창 대창 막창 LA갈비 콩나물무침 모찌롤 냉치킨 선지해장국 깐쇼새우 유산슬 고구마빵 돼지국밥 횡성한우 파김치 새우죽 고추장찌개 통감자 엽떡 회냉면 낙지젓 육포 고구마밥 생선까스 오이지 된장국 찹쌀도넛 백김치 파래 안동찜닭 까르보나라떡볶이 설렁탕 석박지 육회비빔밥 어묵꼬치 열무비빔밥 광어회 고추잡채 닭도리탕 참치볶음 슈크림빵 오징어무침 도라지 양념갈비 닭똥집 식혜 한우스테이크 돌솥비빔밥 성게알 야쿠르트 조기구이 돼지갈비찜 명란스파게티 후쿠오카함바그 파무침 미숫가루 총각김치 쌈장 떡갈비 양꼬치 홍초 굴 짬뽕밥 말린과일 볶음우동 닭강정 된장국 동치미 떡꼬치 김말이튀김 두부 냉이된장국 치즈돈까스정식 쟁반짜장 연어알 삼계탕 카레우동 찹쌀도넛 관자 호로요이 순두부찌개 이삭토스트 국물닭발 해물순두부 오설록 군밤 붕어빵 규동 편육 쌀국수 볶음밥 김치전 소갈비찜 동그랑땡 유자차 송편 우삼겹 쟁반짜장 전병 뼈해장국 스테키동 텐텐 바나나맛우유 새우젓 감자떡 맥심골드 주먹김밥 갈치조림 안성국밥 호박나물 짜장밥 고구마 마파두부 감자탕 육사시미 곱창전골 불고기 숙주나물 호떡 참치김밥 타코야끼 참치뱃살 초코크림빵 떡국 김치전 춘장에양파 약과 호박찌개 알탕 잡채 카레라이스 마크정식 명란삼각김밥 녹차라떼 꽃등심 함박스테이크 소금구이 잡채밥 묵은지 토마토리조또 초고추장 복숭아 맥반석오징어 라면 파닭 찹쌀떡 로이스초콜릿 어포 홍합 양구이 백설기 단호박죽 오감자칠리 장조림 청국장 우동 김칫국 횡성한우 야채곱창 몽쉘 오예스 꼬막 돼지껍데기 빈대떡 샤브샤브 오리훈제구이 아침햇살 아구찜 전복 항정살 닭발 산낙지 생간 뻥튀기 찰보리밥 고구마스틱 삼각커피우유 메리딸기 메리초코 카스타드 육회 라볶이 제육볶음 취나물 꼬꼬면 오이냉국 삼각커피우유 짜글이 소고기야채죽 닭갈비 쭈꾸미 꼬마김밥 짬뽕밥 찹쌀탕수육 카레 양대창 짜장밥 파리바게트순수우유케이크 가츠동 밥버거 갓김치 틈새라면 닭발 계란찜 매운탕 홍어무침 꿔바로우 허니버터칩 곶감 표고버섯 오이김치 셀렉션 두유 주먹밥 날치알 립 고르곤졸라 꽃게랑 고기만두 감자수제비 왕만두 참치마요 고기육수 규카츠 라멘 낙지호롱구이 떡만두국 초코퍼지아이스크림 소갈비찜 기름떡볶이 염통 메로나 엽떡 가리비구이 불초밥 당면 스파클링와인 부대찌개 부추김치 천엽 간짜장 꽃게탕 홍합탕 두유 팥빙수 고구마피자 아구탕 내장볶음 두부김치 비름나물 조개구이 목살스테이크 버섯전골 간장치킨 스프링롤 북어탕 치즈곱창 팽이버섯 쭈꾸미 인절미 쌈무 민물장어 간 뚝배기불고기 인절미빙수 돈까스김밥 시래기국 찐옥수수 민트초코우유 검은콩우유 뽀글이 황태해장국 동태전 설빙 탕평채 무지개케익 소고기덮밥 등갈비 포카리스웨트 보쌈 짜장라면 쌀통닭 해파리냉채 돼지김치찌개 김치부침개 콩국수 동지팥죽 철판볶음밥 춘천닭갈비 가츠나베 깍두기밥 홍시 냉짬뽕 냉우동 더덕회무침 바지락칼국수 오꼬노미야끼 단호박식혜 녹차아이스크림 꽃게찜 감자전 아바이순대 매실주스 목살 호떡 구운김 오뜨 조개관자구이 매운새우깡 간짬뽕 피카츄돈까스 닭꼬치 명량핫도그 수육 내장탕 흑돼지 순댓국 해물삼합 녹차빙수 불닭볶음면 이슬톡톡 오므라이스 오징어튀김 왕교자 죠리퐁 김치찜 어묵탕 짜샤이 고구마피자 피자빵 매운새우깡 멘보샤 갈릭디핑소스 곤약 소머리국밥 전복죽 오레오오즈 꼬치구이 기름떡볶이 누룽지탕 후라이드치킨 닭꼬치 커스터드생크림빵 깻잎 해물전골 곤약 너구리에있는다시마 마늘장아찌 김구이 양송이버섯 마끼 흰쌀밥 버섯칼국수 들깨수제비 하이라이스 델리만쥬 전주비빔밥 크림레몬새우 단무지 기름장 낙지볶음밥 불족발 초코모찌 주먹밥 가지나물 꿀고구마 양대창 가래떡 성게알 막국수 유부초밥 계란국 굴국밥 해물탕 맛밤 컵밥 야끼우동 새우깡 소고기국밥 깡통도시락 사골우거지국 코다리냉면 치즈등갈비 갈치구이 오이소박이 시금치나물 우엉 다슬기국 도미회 대게살 새우구이 메로구이 고기국수 냉모밀 야끼소바 찹쌀닭죽 길거리토스트 돼지주물럭 나시고랭 딤섬 방어회 꿀꽈배기 계란과자 새싹비빔밥 따끈한밥에스팸한조각 새우튀김 버거킹와퍼 삼각김밥 청경채 차슈 한솥도시락 김치가츠나베우동 된장국 라조기 삼선볶음밥 모닝빵 생선전 2프로 호두과자 순대국 무말랭이 나가사끼짬뽕 오모리김치찌개 돈코츠라멘 검은콩두유 디진다돈까스 찰밥'
    lunch = menu.split()

    pick = random.choice(lunch)

    context = {
        'pick': pick,
    }
    
    return render(request, 'lunch.html', context)

def lotto(request, drwno):
    lotto_url = 'https://www.dhlottery.co.kr/common.do'
    drwno = drwno
    pay_load = {
        'method': 'getLottoNumber',
        'drwNo': drwno,
    }
    r = requests.get(lotto_url, params=pay_load)
    lotto_win = []
    lotto_dict = r.json()
    for i in range(1, 7):
        lotto_win.append(lotto_dict[f'drwtNo{i}'])
    bonus_num = lotto_dict['bnusNo']
    ranking = ''
    lotto_result = {
        1: {},
        2: {},
        3: {},
        4: {},
        5: {},
    }

    for i in range(1, 6):
        lotto_random = random.sample(range(1, 46), 6)
        lotto_random.sort()
        lotto_result[i]['numbers'] = lotto_random

        if len(set(lotto_win) & set(lotto_random)) == 6:
            ranking = '1등입니다!'
        elif len(set(lotto_win) & set(lotto_random)) == 5:
            if bonus_num in lotto_random:
                ranking ='2등입니다.'
            else:
                ranking = '3등입니다.'
        elif len(set(lotto_win) & set(lotto_random)) == 4:
            ranking = '4등입니다.'
        elif len(set(lotto_win) & set(lotto_random)) == 3:
            ranking = '5등입니다.'
        else:
            ranking = '꽝!입니다.'
        lotto_result[i]['ranking'] = ranking

    context = {
        # 'lotto_random': lotto_random,
        'lotto_win': lotto_win,
        # 'ranking': ranking,
        'bonus_num': bonus_num,
        'lotto_result': lotto_result,
        'drwno': drwno,
    }

    return render(request, 'lotto.html', context)

def cube(request, number):
    result = number ** 3

    context = {
        'number': number,
        'result': result,
    }

    return render(request, 'cube.html', context)

def profile(request, username):
    username = username

    context = {
        'username': username
    }

    return render(request, 'profile.html', context)

def articles(request):
    fake = Faker()
    fake_articles = []

    for i in range(100):
        fake_articles.append(fake.text())

    context = {
        'fake_articles': fake_articles,
    }

    return render(request, 'articles.html', context)