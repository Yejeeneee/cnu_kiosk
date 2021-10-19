###################
## 키오스크 프로그램 MAIN 조작부(콘솔 프로그래밍 Console Programming)
## 개발자 : 권예진
## 일자 : 2021.10.13
##################
# view => consle
# controller => python
# model => List, Dict

## ※ 조건
## 사용자는 최대로 버거 1개, 사이드 1개, 음료 1개를 주문할 수 있습니다.

# 메뉴와 가격표
burger_name = {1: '새우 버거', 2: '치즈 버거', 3: '치킨 버거'}
side_name = {1: '감자튀김', 2: '치즈스틱'}
drink_name = {1: '코카콜라', 2: '커피', 3: '주스'}

burger_price = {1: '3500', 2: '4000', 3: '4500'}
side_price = {1: '1500', 2: '2000'}
drink_price = {1: '1000', 2: '1200', 3: '1500'}

#고객 기록 주문 저장
menu_save = {}  #고객 주문 메뉴 기록
price_save = {}  #고객 주문 금액 기록

####################
## 1. 메인 메뉴 선택##
####################

print('■■■■■■■■■■■■■■■■■■■')
print('■■ ==CNU 버거(ver 01.==')
print('■■ CNU 버거에 방문해주셔서 감사합니다')
print('■■■■■■■■■■■■■■■■■■■')
print('□■ 메뉴')
print('□■ 1. 햄버거 세트')
print('□■ 2. 햄버거 단품')
print('□■ 3. 사이드 메뉴')
print('□■ 4. 음료')
print('■■■■■■■■■■■■■■■■■■■')

# 사용자로부터 메뉴(번호) 입력
# 1~4번 메뉴 선택
while True:
    print('■■ 원하시는 메뉴의 번호를 입력해주세요')
    menu_num = int(input('>>번호:')) #사용자로부터 주문 menu 입력

    if menu_num >= 1 and menu_num <= 4:
        break
    else:
        print('#MSG: 1~4의 번호만 입력해주세요 :)')

####################
## 2. 세부 메뉴 선택##
####################

if menu_num == 1:
    print('■■■■■■■■■■■■■■■■■■■')
    print('□■ BURGER MENU')
    print('□■ 1. 새우 버거 : 3,500원')
    print('□■ 2. 치즈 버거 : 4,000원')
    print('□■ 3. 치킨 버거 : 4,500원')
    while True:
        print('■■ 원하시는 메뉴의 번호를 입력해주세요')
        choice_num = int(input('>>번호:'))
        if choice_num >= 1 and choice_num <=3:
            menu_save['burger'] = burger_name[choice_num]  #사용자가 선택한 버거 메뉴 기록
            price_save['burger'] = burger_price[choice_num]  #사용자가 선택한 버거 메뉴의 가격 기록
            break
        else:
            print('MSG: 1~3의 번호만 입력해주세요 :)')

    print('■■■■■■■■■■■■■■■■■■■')
    print('□■ SIDE MENU')
    print('□■ 1. 감자튀김 : 1,500원')
    print('□■ 2. 치즈스틱 : 2,000원')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요')
    while True:
            choice_num2 = int(input('>>번호:'))
            if choice_num2 >= 1 and choice_num2 <= 2:
                menu_save['side'] = side_name[choice_num2]
                price_save['side'] = side_price[choice_num2]
                break
            else:
                print('MSG: 1~2의 번호만 입력해주세요 :)')

    print('■■■■■■■■■■■■■■■■■■■')
    print('□■ DRINK MENU')
    print('□■ 1. 코카 콜라 : 1,000원')
    print('□■ 2. 커피 : 1,200원')
    print('□■ 3. 주스 : 1,500원')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요')
    while True:
        choice_num3 = int(input('>>번호:'))
        if choice_num3 >= 1 and choice_num3 <= 3:
            menu_save['drink'] = drink_name[choice_num3]
            price_save['drink'] = drink_price[choice_num3]
            break
        else:
            print('MSG: 1~3의 번호만 입력해주세요 :)')


elif menu_num == 2:
    print('■■■■■■■■■■■■■■■■■■■')
    print('□■ BURGER MENU')
    print('□■ 1. 새우 버거 : 3,500원')
    print('□■ 2. 치즈 버거 : 4,000원')
    print('□■ 3. 치킨 버거 : 4,500원')
    while True:
        print('■■ 원하시는 메뉴의 번호를 입력해주세요')
        choice_num = int(input('>>번호:'))
        if choice_num >= 1 and choice_num <= 3:
            menu_save['burger'] = burger_name[choice_num]  # 사용자가 선택한 버거 메뉴 기록
            price_save['burger'] = burger_price[choice_num]  # 사용자가 선택한 버거 메뉴의 가격 기록
            break
        else:
            print('MSG: 1~3의 번호만 입력해주세요 :)')


elif menu_num == 3:
    print('■■■■■■■■■■■■■■■■■■■')
    print('□■ SIDE MENU')
    print('□■ 1. 감자튀김 : 1,500원')
    print('□■ 2. 치즈스틱 : 2,000원')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요')
    while True:
            choice_num2 = int(input('>>번호:'))
            if choice_num2 >= 1 and choice_num2 <= 2:
                menu_save['side'] = side_name[choice_num2]
                price_save['side'] = side_price[choice_num2]
                break
            else:
                print('MSG: 1~2의 번호만 입력해주세요 :)')


elif menu_num == 4:
    print('■■■■■■■■■■■■■■■■■■■')
    print('□■ DRINK MENU')
    print('□■ 1. 코카 콜라 : 1,000원')
    print('□■ 2. 커피 : 1,200원')
    print('□■ 3. 주스 : 1,500원')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요')
    while True:
        choice_num3 = int(input('>>번호:'))
        if choice_num3 >= 1 and choice_num3 <= 3:
            menu_save['drink'] = drink_name[choice_num3]
            price_save['drink'] = drink_price[choice_num3]
            break
        else:
            print('MSG: 1~3의 번호만 입력해주세요 :)')

# 고객 주문 완료
print(menu_save)
print(price_save)

#################################
## 3. 주문 메뉴와 금액 정산 및 출력##
#################################

# Total 주문 금액 계산
total_price = 0  # Total 주문 금액

for price in price_save.values():
    total_price += price

print('■■■■■■■■■■■■■■■■■■■■■■■')
print('■■고객님이 주문하신 메뉴는')
for i, menu in enumerate(menu_save.values()):
    print('□■ {}. {}'.format(i+1, menu))
print('■■ 으로 총 주문 금액은 {}원 입니다.'.format(total_price))
print('■■■■■■■■■■■■■■■■■■■■■■■')
print('■■ 이용해주셔서 감사합니다. 또 방문해주세요.')
print('■■■■■■■■■■■■■■■■■■■■■■■')