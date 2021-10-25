# 1. 햄버거 세부 메뉴 선택하는 함수
def choice_burger():
    print('■■■■■■■■■■■■■■■■■■■')
    print('□■ BURGER MENU')
    print('□■ 1. 새우 버거 : 3,500원')
    print('□■ 2. 치즈 버거 : 4,000원')
    print('□■ 3. 치킨 버거 : 4,500원')
    while True:
        print('■■ 원하시는 메뉴의 번호를 입력해주세요')
        choice_num = int(input('>>번호:'))
        if choice_num >= 1 and choice_num <= 3:
            break
        else:
            print('MSG: 1~3의 번호만 입력해주세요 :)')
    return choice_num

# 2. 사이드 세부 메뉴 선택하는 함수
def choice_side():
    print('■■■■■■■■■■■■■■■■■■■')
    print('□■ SIDE MENU')
    print('□■ 1. 감자튀김 : 1,500원')
    print('□■ 2. 치즈스틱 : 2,000원')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요')
    while True:
            choice_num2 = int(input('>>번호:'))
            if choice_num2 >= 1 and choice_num2 <= 2:
                break
            else:
                print('MSG: 1~2의 번호만 입력해주세요 :)')
    return choice_num2

# 3. 음료 세부 메뉴 선택하는 함수
def choice_drink():
    print('■■■■■■■■■■■■■■■■■■■')
    print('□■ DRINK MENU')
    print('□■ 1. 코카 콜라 : 1,000원')
    print('□■ 2. 커피 : 1,200원')
    print('□■ 3. 주스 : 1,500원')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요')
    while True:
        choice_num3 = int(input('>>번호:'))
        if choice_num3 >= 1 and choice_num3 <= 3:
            break
        else:
            print('MSG: 1~3의 번호만 입력해주세요 :)')
    return choice_num3