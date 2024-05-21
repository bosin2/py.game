import time
import random
import os
import ctypes
from turtle import speed
import datetime
import threading



#터미널위치를임의로지정
class COORD(ctypes.Structure):
        _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

#좌표임의로생성
class SMALL_RECT(ctypes.Structure):
    _fields_ = [("Left", ctypes.c_short),
                ("Top", ctypes.c_short),
                ("Right", ctypes.c_short),
                ("Bottom", ctypes.c_short)]
#콘솔창 영역 설정
def set_console_size(width, height):
    STD_OUTPUT_HANDLE = -11
    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    if handle != -1:
        ctypes.windll.kernel32.SetConsoleScreenBufferSize(handle, COORD(width, height))
        rect = SMALL_RECT(0, 0, width - 1, height - 1)
        ctypes.windll.kernel32.SetConsoleWindowInfo(handle, True, ctypes.byref(rect))
        
#커서 위치 수정해주는코드
kernel32 = ctypes.windll.kernel32
def move_cursor(x,y):
    class COORD(ctypes.Structure):
        _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]
        

    coord = COORD()
    coord.X = x
    coord.Y = y
    kernel32.SetConsoleCursorPosition(kernel32.GetStdHandle(-11), coord)

#글씨 지워주는 함수
def clear():
    os.system('cls')
 
    
#글씨에 색입히기
def color_print(text, color):
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m',
        'pink': '\033[95m',
        'gray' : '\033[90m'
        
    }
    color_code = colors.get(color.lower())
    if color_code:
        print(color_code + text + colors['reset'])
    else:
        print("Invalid color")
#핑크색        
def color_print2(text):
    color_code = "\033[38;2;255;192;203m"
    reset_code = "\033[0m"
    print(color_code + text + reset_code)
    
#rgb값으로 출력하는거    
def color_print3(text, r, g, b):
    color_code = f"\033[38;2;{r};{g};{b}m"
    reset_code = "\033[0m"
    print(color_code + text + reset_code)


        
#색입힌글씨하나씩출력     
def color_print_slow(text, color):
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',  
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m',
        'pink': '\033[95m',
        'sky' : '\033[36m'
    }
    color_code = colors.get(color.lower())
    if color_code:
        for char in text:
            print(color_code + char, end='', flush=True)
            time.sleep(0.1)
        print(colors['reset'])
    else:
        print("Invalid color")
        


#글자 한글자씩 출력해주는 함수
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.06)

def print_slow2(text,speed):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
        
def print_at(text,x,y):
    for char in text:
        print(char, end='',flush=True)
        time.sleep(0.04)
        

#시험
def test():
    clear()
    move_cursor(0,5)
    print_slow("벌써 시험을 보는 기간이 왔습니다... 과연 준영이의 점수는 ! ?\n")
    print("\n")
    if total_brain >= 200 and total_code >= 180:
         color_print_slow("만점이다 !! 열심히 공부한 보람이 ! ! !ヾ(≧▽≦*)o\n","sky")
         print("\n")
         print_slow("다 들어와, 해커톤? 정올올림피아드? ICPC? 다 이겨주지")
         print("\n")
         print_slow("준영이가 미쳤다 ! ! ! 하지만 그럴 만도 하다 ! 자신감 넘쳐 ! 멋있다 !")
         print("\n")
         print_slow("준영이는 여러 대회에 나가 상금도 타오고 장학금도 받았다 ! 교수님들의 무한 러브콜 ! !")
         print("\n")
         stress(-50)
         money(80)
         total_proheart1(20)
         total_proheart2(20)
         time.sleep(1)
         
    elif total_brain >= 180 and total_code >= 160:
         color_print_slow("으아 아쉽게 만점을 놓쳤다... 하지만 잘 했다 !(｡･∀･)ﾉﾞ\n","sky")
         print("\n")
         print_slow("나이스 ㅋㅋㅋ 과탑 기다려라 송선? 최유민? 그 누가 와도 내가 이길자신 있어, 어")
         print("\n")
         print_slow("준영이는 미쳐 날뛴다... 장학금도 받았다 ! 교수님들이 관심을 가진다...")
         print("\n")
         stress(-30)
         money(30)
         total_proheart1(10)
         total_proheart2(10)
         time.sleep(1)
         
    elif total_brain >= 150 and total_code >= 130:
         color_print_slow("이정도면 만족할만한 점수 !(～￣▽￣)～\n","sky")
         print("\n")
         print_slow("\"와 너무 잘봤네 나 혹시 천재인가 ?\"\n")
         print("\n")
         print_slow("준영이는 기쁘다 ! 스트레스가 20 해소되었다 !")
         stress(-20)
         time.sleep(1)
         
    elif total_brain >= 120 and total_code >= 100:
         color_print_slow("열심히 한정도 ~ ( •ω • )y\n","sky")
         print("\n")
         print_slow("괜찮은데? 열심히 했어, 어")
         print("\n")
         print_slow("스트레스가 10 해소되었다 !")
         stress(-10)
         time.sleep(1)
         
    elif total_brain >= 100 and total_code >= 80:
         color_print_slow("조금만 더 열심히 해볼까 ? 화이팅 !\n","sky")
         print("\n")
         print_slow("이정도면 그래도 아직 괜찮아, 어")
         print("\n")
         print_slow("준영이는 마음이 괜찮은것 같다 !")
         time.sleep(1)
         
    elif total_brain >= 80 and total_code >= 70:
         color_print_slow("아쉽다 （；´д｀）ゞ 조금만 더 열심히 해보자 !\n","sky")
         print("\n")
         print_slow("나름 열심히 한건데... 그래도 괜찮아 열심히 하면 되지, 어")
         print("\n")
         print_slow("스트레스 10을 받았다")
         stress(10)
         time.sleep(1)
         
    elif total_brain >= 60 and total_code >= 40:
         color_print_slow("준영아 공부는 중요한 거야 ! ＞﹏＜\n","sky")
         print("\n")
         print_slow("\"나름 열심히 한건데...\"")
         print("\n")
         print_slow("스트레스 20을 받았다")
         stress(20)
         time.sleep(1)
         
    elif total_brain >= 40 and total_code >= 30:
         color_print_slow("또 시간을 돌려주지는 않는다고 ! ヽ（≧□≦）ノ\n","sky")
         print("\n")
         print_slow("\"나름 열심히 한건데...\"")
         stress(20)
         print_slow("스트레스 20을 받았다")
         print("\n")
         time.sleep(1)
         
    elif total_brain >= 20 and total_code >= 10:
         color_print_slow("공부를 어떻게 한건지 궁금해지는 점수다...（；´д｀）ゞ\n","sky")
         print("\n")
         print_slow("솔직히 공부를 별로 안했기에 스트레스를 받지 않았다")
         print("\n")
         time.sleep(1)
    else:
         print_slow("대체 뭘 한걸까...(⊙_⊙)？\n")
         print("\n")
         print_slow("너무 어이가 없어서 아무 생각도 안든다. . . 아무 타격도 받지 않았다")
         print("\n")
         time.sleep(1)

    main_menu()
    

#일정 돌아가는 개월
month = 3


#일정 돌아가는 년도
year = 2024


#스탯
total_brain = 10
total_health = 50
total_stress = 0
total_code = 0
total_money = 50


#교수님 호감도
total_proheart1 = 0
total_proheart2 = 0


#교수님 만나기 
meet_pro = 0


#교수님 만남 분기
total_end_meet_pro1 = 0
total_end_meet_pro2 = 0

def end_meet_pro1(amount):
    global total_end_meet_pro1
    total_end_meet_pro1 += amount
    
    
def end_meet_pro2(amount):
    global total_end_meet_pro2
    total_end_meet_pro2 += amount
    


#애니메이션테스트
def ani(week):
    frames = [
        "■ □ □ □",
        "■ ■ □ □",
        "■ ■ ■ □",
        "■ ■ ■ ■ 마지막 주다 !"
    ]
    move_cursor(5, 5)
    print(frames[week])
    
#스케쥴 리스트 생성
scheduleList = []


#일정 증감
def schedule_UpDown():
    global total_brain, total_code, total_health, total_money, total_stress, scheduleList, month, year, meet_pro, end_meet_pro
    clear()
    for i in range(0,3):
        
        if scheduleList[i] == '알바 가기':
            for week in range(0,4):
                m, h, s = week_UpDown1()
                clear()
                move_cursor(5,5)
                ani_thread = threading.Thread(target=ani, args=(week,))
                ani_thread.start()
                ani_thread.join()
                move_cursor(0, 10)
                print_at(f"{week+1}주째...  알바를 하면서...\n"+
                                "\n"+
                                f"소지금이 {m}원 올랐다!\n"+
                                "\n"+
                                f"체력이 {h} 올랐다 !\n"+
                                "\n"+
                                f"스트레스가 {s} 올랐다 !\n",0,10)
                
                
                
                
        elif scheduleList[i] == '운동 하기':
            for week in range(0,4):
                h, s = week_UpDown2()
                clear()
                move_cursor(5,5)
                ani_thread = threading.Thread(target=ani, args=(week,))
                ani_thread.start()
                ani_thread.join()
                move_cursor(0,10)
                print_at(f"{week+1}주째...\n" +
                           "\n" +
                           "운동을 하면서...\n"  +
                           "\n" +
                           f"체력이 {h} 올랐다 !\n" +
                           "\n" +
                           f"스트레스가 {-s} 내렸다 !\n",0,10)

        elif scheduleList[i] == '일반 공부':
            for week in range(0,4):
                b, s, h = week_UpDown3()
                clear()
                move_cursor(5,5)
                ani_thread = threading.Thread(target=ani, args=(week,))
                ani_thread.start()
                ani_thread.join()
                move_cursor(0,10)
                print_at(f"{week+1}주째...\n" +
                            "\n" +
                            "일반 공부를 하면서...\n" +
                            "\n" +
                            f"지능이 {b} 올랐다 !\n"  +
                            "\n" +
                            f"스트레스가 {s} 올랐다 !\n" + 
                            "\n" +
                            f"체력이 {-h} 내렸다 !\n",0,10)

        elif scheduleList[i] == '코딩 공부':
            for week in range(0,4):
                c, h, s = week_UpDown4()
                clear()
                
                move_cursor(5,5)
                ani_thread = threading.Thread(target=ani, args=(week,))
                ani_thread.start()
                ani_thread.join()
                move_cursor(0,10)
                print_at(f"{week+1}주째...\n" +
                            "\n" +
                            "코딩 공부를 하면서...\n" +
                            "\n" +
                            f"코딩 실력이 {c} 올랐다 !\n" +
                            "\n" +
                            f"체력이 {-h} 내렸다 !\n" +
                            "\n" +
                            f"스트레스가 {s} 올랐다 !\n",0,10)
            
        elif scheduleList[i] == '재밌게 놀기':
            for week in range(0,4):
                m, h, s = week_UpDown5()
                clear()
                
                move_cursor(5,5)
                ani_thread = threading.Thread(target=ani, args=(week,))
                ani_thread.start()
                ani_thread.join()
                move_cursor(0,10)
                print_at(f"{week+1}주째...\n" +
                            "\n" +
                            "놀면서..."
                            "\n" +
                            f"소지금이 {-m}원 내렸다 !\n"
                            "\n" +
                            f"체력이 {h} 올랐다 !\n"
                            "\n" +
                            f"스트레스가 {-s} 내렸다 !\n",0,10)

    print("\n")
    print_slow("모든 일정이 끝났습니다 ! 그동안의 밥값이 차감됐습니다 !\n")
    print("\n")
    print_slow("노력하느라 고생했던 스트레스가 올라갑니다...\n")
    print("\n")
    print_slow2("집으로 돌아가는 중. . .\n\n",0.15)


#밥 값(밥값 랜덤으로변경바람)
    money(-5)
    stress_RandomUp()
   
#교수님 만나기 초기화
    meet_pro -= 1
    
 

#일정 돌릴 때마다 3개월씩 증가
    month += 3 

#12개월 넘어가면 1년 더하고 3월로 설정
    if month == 15:
        year += 1 
        month = 3 

    if month == 9 or month == 3:
        tuition()
        
    #시험 
    for i in range(month, 16, 6):
        test()
    
    main_menu()
     
#등록금 함수
def tuition():
    if total_money >= 50:
        money(-50)
        print_slow("벌써 한 학기가 지났어요 등록금 50원이 차감됩니다 〒▽〒 \n\n")
    elif total_money < 50:   
        print_slow("등록금을 낼 돈이 부족해... 이러면 학교를 다닐 수 없어. . .")
        death()
        


#시험의 일주일단위 능력치 증감
def week_UpDown0():
    plus1 = stress_RandomUp()
    plus2 = brain_RandomUp()
    return plus1, plus2

#알바 가기의 일주일단위 능력치 증감
def week_UpDown1():
    plus1 = money_RandomUp()
    plus2 = health_RandomUp()
    plus3 = stress_RandomUp()
    return plus1, plus2, plus3 

#운동 하기의 일주일단위 능력치 증감 
def week_UpDown2():
    plus1 = health_RandomUp()
    plus2 = stress_RandomDown()
    return plus1, plus2

#일반 공부의 일주일단위 능력치 증감
def week_UpDown3():
    plus1 = brain_RandomUp()
    plus2 = stress_RandomUp()
    plus3 = health_RandomDown()
    return plus1, plus2, plus3

#코딩 공부의 일주일단위 능력치 증감
def week_UpDown4():
    plus1 = code_RandomUp()
    plus2 = health_RandomDown()
    plus3 = stress_RandomUp()
    return plus1, plus2, plus3

#재밌게 놀기의 일주일단위 능력치 증감
def week_UpDown5():
    plus1 = money_RandomDown()
    plus2 = health_RandomUp()
    plus3 = stress_RandomDown()
    return plus1, plus2, plus3

#스탯 랜덤 증가
def brain_RandomUp():
    global total_brain
    if 0 <= total_brain <=999:
        plus = random.randint(1,5)
        total_brain += plus
        return plus
    
def health_RandomUp():
    global total_health
    if total_health >0:
        plus = random.randint(1,5)
        total_health += plus
        return plus
    elif total_health <= 0:
        death()

def stress_RandomUp():
    global total_stress
    plus = random.randint(1,5)
    if total_stress < 0:
        fix_stress()
        total_stress += plus
        return plus
    elif total_stress + plus >= 100:
        death()
    else :
        total_stress += plus
        return plus

def code_RandomUp():
    global total_code
    if 0 <= total_code <= 999:
        plus = random.randint(1,5)
        total_code += plus
        return plus
    
def money_RandomUp():
    global total_money
    if total_money >=0:
        plus = random.randint(1,5)
        total_money += plus
        return plus
        
#스탯 랜덤 감소
def brain_RandomDown():
    global total_brain
    if 0 <= total_brain <=999:
        minus = random.randint(-5,-1)
        total_brain += minus
        return minus
    
def health_RandomDown():
    global total_health
    minus = random.randint(-5,-1)
    if total_health + minus >0:
        total_health += minus
        return minus
    elif total_health + minus <= 0:
        death()

def stress_RandomDown():
    global total_stress
    minus = random.randint(-5,-1)
    if total_stress + minus < 0:
        fix_stress()
        return minus
    elif total_stress + minus >= 100: 
        death()
    else :
        total_stress += minus
        return minus
    
def code_RandomDown():
    global total_code
    if 0 <= total_code <= 999:
        minus = random.randint(-5,-1)
        total_code += minus
        return minus
    
def money_RandomDown():
    global total_money
    minus = random.randint(-5,-1)
    if total_money + minus < 0:
        fix_money()
        return minus
    elif total_money + minus >= 0:
        total_money += minus
        return minus
    
    #소지금이 0원 이하로 내려가지 않게 하는 코드
def fix_money():
    global total_money
    total_money = 0

#스탯 증감들
def brain(amount):
    global total_brain
    if 0 <= total_brain <= 999:
        total_brain += amount

def health(amount):
    global total_health
    if total_health + amount >0:
        total_health += amount
    elif total_health + amount <= 0:
        death()

def stress(amount):
    global total_stress
    if total_stress + amount < 0:
        fix_stress()
    elif total_stress + amount >=0:
        total_stress += amount
        if total_stress >= 100: 
            death()
    #스트레스가 0이하로 내려가지 않게 하는 코드
def fix_stress():
    global total_stress
    total_stress = 0

    
def code(amount):
    global total_code
    if 0 <= total_code <= 999:
        total_code += amount
    

def money(amount):
    global total_money
    if total_money >=0:
        total_money += amount

    #교수님 호감도 증감

    #박교수님 호감도
def proheart1():
    global total_proheart1
    if total_proheart1 >= 0:
        plus1 = random.randint(1, 5)
        return plus1

    #김교수님 호감도
def proheart2():
    global total_proheart2
    if total_proheart2 >= 0:
        plus2 = random.randint(5, 10)
        return plus2

    #게임 진행하는 코드
def main():
    start_game()
    choice = input("< 시작하기(y)\n")

    if (choice == 'y'):
        start_intro()
        time.sleep(1)
        
        main_menu()
    else:
        def print_slow(text):
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.08)
        print_slow(" 시작하기 싫으세요?\n")
        main()

    #스트레스 100이상일때 & 체력0 이하될때 게임오버
def death():
    clear()
    def print_slow(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.1)
    move_cursor(0,20)
    color_print_slow(
        "준영이는 스트레스로 병에 걸려 생을 마감했습니다...\n"+
        "\n"+
        "농담이고요. 당신이 준영이를 혹사시켜서 자퇴했습니다.\n"+
        "\n"+
        "하하 이것도 농담이에요. 준영이는 안좋은 선택을 했어요. 당신, 때문에.\n"+
        "\n"+
        "이거 다 거짓말인거 아시죠? 아무튼 준영이는 더 이상 무리 ㅠ3ㅠ\n"+
        "\n"+
        "다음에는 열심히 해보세요 ^_^. 당신의 이야기는 여기까지. 바이바이\n",
        "red"
        )
    color_print("                                                                       ","red")
    color_print("     ##                         ##                                  ## ","red") 
    color_print("     ##    ####     ####        ##             ####    #####        ## ","red") 
    color_print("  #####   ##  ##       ##    #####            ##  ##   ##  ##    ##### ","red") 
    color_print(" ##  ##   ######    #####   ##  ##            ######   ##  ##   ##  ## ","red") 
    color_print(" ##  ##   ##       ##  ##   ##  ##            ##       ##  ##   ##  ## ","red") 
    color_print("  #####    ####     #####    #####             ####    ##  ##    ##### ","red") 
                                                                        

    exit()

  #게임시작프린트
def start_game():
    clear()
    set_console_size(100, 50)
    def print_slow(text):
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.06)
    print("                                                                                                              ")
    color_print2("   ■■■■■■         ■■■■■■                      ■■■■■■         ■■■■■■   ")
    color_print2("   ■                             ■                      ■                             ■   ")
    color_print2("   ■                             ■                      ■                             ■   ")
    color_print2("   ■■■■■■                   ■                      ■■■■■■                   ■   ")
    color_print2("                       ■■■■■■■                                         ■■■■■■■  ")
    color_print2("  ■■■■■■■         ■                              ■■■■■■■         ■            ")
    color_print2("        ■               ■                                    ■               ■            ")
    color_print2("        ■               ■                                    ■               ■            ")
    color_print2("        ■               ■■■■■■                          ■               ■■■■■■  ")
    print("\n")
    color_print2("  ■■■■■    ■        ■        ■                      ■       ■                     ■")
    color_print2("          ■    ■        ■        ■                 ■■■■■■  ■       ■■■■■■  ■")
    color_print2("          ■    ■        ■■■■■■                  ■      ■   ■■         ■■      ■")
    color_print2("  ■■■■■■■■        ■        ■                  ■      ■   ■          ■  ■   ■■")
    color_print2("  ■            ■        ■        ■                    ■■■     ■        ■      ■   ■")
    color_print2("  ■            ■        ■■■■■■                                                      ■")
    color_print2("  ■■■■■    ■                                        ■■■■■             ■■■■■   ")
    color_print2("                ■      ■■■■■■■■                          ■             ■      ■   ")
    color_print2("                                                                  ■             ■■■■■   ")
    print("\n")
    color_print2("    ■■■■■■■        ■■■■■■          ■■■■■  ■  ■          ■■■■■■      ")
    color_print2("      ■      ■                    ■              ■      ■  ■          ■                ")
    color_print2("      ■      ■          ■■■■■■              ■■■■■  ■          ■■■■■■      ")
    color_print2("      ■      ■          ■                      ■  ■    ■  ■          ■                ")
    color_print2("    ■■■■■■■        ■■■■■■          ■      ■  ■  ■          ■■■■■■      ")
    color_print2("                                                                                              ")
    color_print2("                               ■                      ■■■■■          ■■■■■■■■   ")
    color_print2("    ■■■■■■■       ■■■■■■■                        ■                             ")
    color_print2("                                                               ■                             ")
    time.sleep(1)
    print_slow("     ver. 교수님과의 러브러브 만남\n")
    
    #인트로
def start_intro():
    def print_slow(text):
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.03)
    clear()     
    move_cursor(1,10)
    print_slow(
        "준영이 : 아 큰일났다 망했다 아 시험 어떡하지 \n" +
    "\n" +
    " \033[36m *수뭉이요정* :힘들어하는 준영이의 목소리를 듣고 요정 등장 !\033[0m \n" +
    "\n" +
    " 준영이 : 아 깜짝아 아 뭐야 아 이게 뭐지 벌레인가 \n" +
    "\n" +
    " \033[36m *수뭉이요정* : 준영아! 걱정마! 내가 첫날로 시간을 되돌려줄게\033[0m \n" + 
    "\n" +
    " 준영이 : 아 진짜 아 진짜 그러면 좋겠다 \n" +
    "\n" +
    " \033[36m *수뭉이요정* : 웅 !\033[0m \n" + 
    "\n" +
    " 준영이 : 어어? 갑자기 머리가 (시야가 핑 돈다)\n" +
    "\n" +
    " 준영이 : 아 안돼 시험 망치고 죽다니...(털석)\n" +
    "\n" +
    " \033[36m *수뭉이요정* : 후후...이번엔 열심히해 준영아 ! \033[0m\n" +
    "\n" +
    " 이 때 들은 말을 끝으로 나는 정말로 입학 첫날로 돌아왔다... \n" +
    "\n" +
    " 준영이 : 수뭉이는... 실존했구나. 사랑해요 상명대! \n\n")
   
    

    #인트로 후 메인메뉴
def main_menu():
    clear()
    global meet_pro
    def print_slow(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.08)
    move_cursor(0,10)

    print_date()

    print("\n")
    print(" ___________메인 메뉴___________\n")
    print(" |                              |\n")
    print(" | > 스케쥴 표 (a)              |\n")
    print(" |                              |\n")
    print(" | > 교수님 만나기 (s)          |\n")
    print(" |                              |\n")
    print(" | > 자판기 (d)                 |\n")
    print(" |                              |\n")
    print(" | > 스탯 확인 (f)              |\n")
    print(" |______________________________|\n")
    print("\n")
    choice = input("무엇을 하시겠습니까? : \n")
    if choice == 'a':
        schedule()
    elif choice == 's' and meet_pro == 0:
        professor()
    elif choice == 's' and meet_pro == 1:
        print("\n")
        print_slow("교수님은 한 번 씩만 만날 수 있는 것 같다... \n")
        time.sleep(1)
        print("\n")
        main_menu()
    elif choice == 'd':
        store()
    elif choice == 'f':
        status()
    else:
        print_slow("제대로 선택 하세요.\n")
        main_menu()


#날짜 출력 함수
def print_date():
    global month, year
    print_slow2(f"오늘은 {year}년 {month}월 1일 입니다（￣︶￣）\n",0.04)
    

    #스케쥴 메뉴
def schedule():
    clear()
    global total_brain, total_code, total_health, total_money, total_stress, scheduleList
    def print_slow(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
    move_cursor(0,5)
    print_slow(" 준영이의 세 달을 정해주세요 !\n")
    print_slow("    <일정 3개를 선택하면 됩니다 ! >\n")
    print(" ____________________일 정_______________________\n")
    print(" |                                               |\n")
    print(" |             > 1. 알바 가기                    |\n")
    print(" |        [소지금 up, 체력 up, 스트레스 up]      |\n")
    print(" |                                               |\n")
    print(" |             > 2. 운동 하기                    |\n")
    print(" |        [체력 up, 스트레스 down]               |\n")
    print(" |                                               |\n")
    print(" |             > 3. 일반 공부                    |\n")
    print(" |        [지능 up, 스트레스 up, 체력 down]      |\n")
    print(" |                                               |\n")
    print(" |             > 4. 코딩 공부                    |\n")
    print(" |        [코딩실력 up, 체력 dowm, 스트레스 up]  |\n")
    print(" |                                               |\n")
    print(" |             > 5. 재밌게 놀기                  |\n")
    print(" |        [소지금 down, 체력 up, 스트레스 down]  |\n")
    print(" |                                               |\n")
    print(" |_______________________________________________|\n")

    
    #리스트 비우기
    empty_scheduleList()

    while len(scheduleList) != 3:

        choice = input("메뉴로 돌아가기(a): \n")
        if choice == 'a' or choice == 'A':
            main_menu()

        elif choice == '1':
            print("알바 가기를 선택하셨습니다.\n")
            scheduleList.append('알바 가기')
        
        elif choice == '2':
            print("운동 하기를 선택하셨습니다.\n")
            scheduleList.append('운동 하기')
        
        elif choice == '3':
            print("일반 공부를 선택하셨습니다.\n")
            scheduleList.append('일반 공부')

        elif choice == '4':
            print("코딩 공부를 선택하셨습니다.\n")
            scheduleList.append('코딩 공부')

        elif choice == '5':
            print("재밌게 놀기를 선택하셨습니다.\n")
            scheduleList.append('재밌게 놀기')
        else:
            def print_slow(text):
                for char in text:
                    print(char, end='', flush=True)
                    time.sleep(0.08)
            print_slow("제대로 입력하시라고요.\n")

    #세 달 정했으면 일정 증감 함수로 GO
    schedule_UpDown()

# 스케쥴 표 선택 시 리스트 비우기
def empty_scheduleList():
    global scheduleList
    scheduleList = []
    
    
#교수만나기메뉴
def professor():
    clear()
    def print_slow(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.09)
    move_cursor(0,5)
    print(" ____________연구실 앞____________\n")
    print("|                                |\n")
    print("| > 박교수님 만나러 가기 (1)     |\n")
    print("|                                |\n")
    print("| > 김교수님 만나러 가기 (2)     |\n")
    print("|                                |\n")
    print("| > 메뉴로 돌아가기 (3)          |\n")
    print("|                                |\n")
    print("|________________________________|\n")
    print("\n")
    choice = input(" 무엇을 하시겠습니까? : \n")
    

    #교수님 선택
    if choice == '1':
        professor1()
    elif choice == '2':
        professor2()
    elif choice == '3':
        main_menu()
    else:
        print_slow("\033[36m다시 입력하세요. 제발!!\033[0m\n")
        professor()
        
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.08)

#박교수님 선택
def professor1():
    clear()
    global total_proheart1, total_brain, meet_pro, total_end_meet_pro1
    
    move_cursor(0,5)
    print_slow("준영이 : 박교수님 계세요?\n\n")
    if total_brain > 10:
        if total_end_meet_pro1 == 0:
            meet_pro+=1
            end_meet_pro1(1)
            total_proheart1+=5
            print_slow("박교수님 : 아 준영이 안녕~ 무슨일로 왔니~ ?\n\n")
            print("________________선 택 창________________\n")
            print("|                                       |\n")
            print("| > 1. 그냥요                           |\n")
            print("|                                       |\n")
            print("| > 2. 상담하고 싶은게 있어서 왔어요    |\n")
            print("|_______________________________________|\n")

            choice = input("어떤 대답을 할까? :\n")
            if choice == '1':
                print_slow("박교수님 : 그러니. 내가 좀 바빠서 미안해 (•_•).\"\n")
                print_slow("（ヽ(*。>Д<)o゜쫓겨났다...\n")
                like1 = proheart1()
                total_proheart1 -= like1
                print_slow(f"박교수님의 호감도가 {like1} 내려가서 {total_proheart1}가 되었다 (┬┬﹏┬┬) \n")
                print_slow("돌아가는 중. . .\n")
                time.sleep(1)
                main_menu()
            elif choice == '2':
                print_slow("박 교수님 : 아이고 그렇구나 잠시만, 여기 앉으면 돼~ ^_^\n")
                print("\n")
                print_slow("준영이와 박교수님은 재밌게 대화를 나눴다\n")
                print("\n")
                like1 = proheart1()
                total_proheart1 += like1
                print_slow(f"박교수님의 호감도가 {like1} 올라서 {total_proheart1}가 되었다 ! (｡･∀･)ﾉﾞ)\n")
                print("\n")
                print_slow("돌아가는 중. . .\n")
                time.sleep(1)
                main_menu()
            else:
                print_slow("진짜 그럴거에요?\n")
                main_menu()
                
        elif  total_proheart1 >= 0 and total_end_meet_pro1 >= 1:
             meet_pro+=1
             end_meet_pro1(1)
             print_slow("박교수님 : 아 준영이 안녕~ 오늘은 어쩐일 이야 ~ ?\n\n")
             print("________________선 택 창________________\n")
             print("|                                       |\n")
             print("| > 1. 저번일로 다시 얘기하고 싶어요    |\n")
             print("|                                       |\n")
             print("| > 2. 교수님 보고 싶어서 왔어요        |\n")
             print("|_______________________________________|\n")
             choice = input("어떤 대답을 할까? :\n")
             if choice == '1':
                print_slow("박교수님 : 그러니? 그런데 그때 얘기가 끝났던거 같은데... (•_•).\"\n")
                print_slow("（ヽ(*。>Д<)o゜쫓겨났다...\n")
                like1 = proheart1()
                total_proheart1 -= like1
                print_slow(f"박교수님의 호감도가 {like1} 내려가서 {total_proheart1}가 되었다 (┬┬﹏┬┬) \n")
                print_slow("돌아가는 중. . .\n")
                time.sleep(1)
                main_menu()
             elif choice == '2':
                print_slow("박 교수님 : 어머 (*^▽^*) 잠시만 ~ \n")
                print("\n")
                print_slow("준영이와 박교수님은 재밌게 대화를 나눴다\n")
                print("\n")
                like1 = proheart1()
                total_proheart1 += like1
                print_slow(f"박교수님의 호감도가 {like1} 올라서 {total_proheart1}가 되었다 ! (｡･∀･)ﾉﾞ)\n")
                print("\n")
                print_slow("돌아가는 중. . .\n")
                time.sleep(1)
                main_menu()
             else:
                print_slow("진짜 그럴거에요?\n")
                main_menu()
                
        elif total_proheart1 >= 5 and total_end_meet_pro1 >= 1:
             meet_pro+=1
             end_meet_pro1(1)
             print_slow("박교수님 : 아 준영이 안녕~ 그런데 내가 지금 잠시 바빠서 기다려줄래? (；′⌒`) ?\n\n")
             print("________________선 택 창________________\n")
             print("|                                       |\n")
             print("| > 1. 바쁘시면 다음에 오겠습니다 !     |\n")
             print("|                                       |\n")
             print("| > 2. 싫어요 교수님 보고 갈래요        |\n")
             print("|_______________________________________|\n")
             choice = input("어떤 대답을 할까? :\n")
             if choice == '2':
                print_slow("박교수님 : 그러니? (•_•).\"\n")
                print_slow("（ヽ(*。>Д<)o゜어색한 침묵이 흐른다...\n")
                like1 = proheart1()
                total_proheart1 -= like1
                print_slow(f"박교수님의 호감도가 {like1} 내려가서 {total_proheart1}가 되었다 (┬┬﹏┬┬) \n")
                print_slow("돌아가는 중. . .\n")
                time.sleep(1)
                main_menu()
             elif choice == '1':
                print_slow("박 교수님 : 고마워o(TヘTo) 다음에 꼭 다시와 ~ ! \n")
                print("\n")
                print_slow("준영이는 방을 나왔다 \n")
                print("\n")
                like1 = proheart1()
                total_proheart1 += like1
                print_slow(f"박교수님의 호감도가 {like1} 올라서 {total_proheart1}가 되었다 ! (｡･∀･)ﾉﾞ)\n")
                print("\n")
                print_slow("돌아가는 중. . .\n")
                time.sleep(1)
                main_menu()
             else:
                print_slow("진짜 그럴거에요?\n")
                main_menu()
                
        elif total_proheart1 >= 15 and total_end_meet_pro1 >= 2:
             meet_pro+=1
             end_meet_pro1(1)
             print_slow("박교수님 : 아 준영이 안녕 ! 저번에는 바빠서 미안 (/▽＼) \n\n")
             print("________________선 택 창________________\n")
             print("|                                       |\n")
             print("| > 1. 아니에요 당연히 괜찮죠 저번에는  |\n")
             print("|      그냥 교수님 보고싶어서 왔어요    |\n")
             print("|                                       |\n")
             print("| > 2. 새로 상담하고 싶은게 있어요,,    |\n")
             print("|_______________________________________|\n")
             choice = input("어떤 대답을 할까? :\n")
             if choice == '1':
                print_slow("박교수님 : 그, 그래? 호호... (•_•).\"\n")
                print_slow("（ヽ(*。>Д<)o゜교수님은 부담감을 느끼신다...\n")
                like1 = proheart1()
                total_proheart1 -= like1
                print_slow(f"박교수님의 호감도가 {like1} 내려가서 {total_proheart1}가 되었다 (┬┬﹏┬┬) \n")
                print_slow("돌아가는 중. . .\n")
                time.sleep(1)
                main_menu()
             elif choice == '2':
                print_slow("박 교수님 : 상담은 언제든지 환영이야 ~ (*^▽^*) 잠시만 ~ \n")
                print("\n")
                print_slow("준영이와 박교수님은 재밌게 대화를 나눴다 !\n")
                print("\n")
                like1 = proheart1()
                total_proheart1 += like1
                print_slow(f"박교수님의 호감도가 {like1} 올라서 {total_proheart1}가 되었다 ! (｡･∀･)ﾉﾞ)\n")
                print("\n")
                print_slow("돌아가는 중. . .\n")
                time.sleep(1)
                main_menu()
             else:
                print_slow("진짜 그럴거에요?\n")
                main_menu()
        elif total_proheart1 >= 25 and total_end_meet_pro1 >= 3:
             meet_pro+=1
             end_meet_pro1(1)
             print_slow("박교수님 : 아 준영이 안녕~ 그런데 내가 지금 잠시 바빠서 기다려줄래? (；′⌒`) ?\n\n")
             print("________________선 택 창________________\n")
             print("|                                       |\n")
             print("| > 1. 바쁘시면 다음에 오겠습니다 !     |\n")
             print("|                                       |\n")
             print("| > 2. 싫어요 교수님 보고 갈래요        |\n")
             print("|_______________________________________|\n")
             choice = input("어떤 대답을 할까? :\n")
             if choice == '2':
                print_slow("박교수님 : 그러니? (•_•).\"\n")
                print_slow("（ヽ(*。>Д<)o゜어색한 침묵이 흐른다...\n")
                like1 = proheart1()
                total_proheart1 -= like1
                print_slow(f"박교수님의 호감도가 {like1} 내려가서 {total_proheart1}가 되었다 (┬┬﹏┬┬) \n")
                print_slow("돌아가는 중. . .\n")
                time.sleep(1)
                main_menu()
             elif choice == '1':
                print_slow("박 교수님 : 고마워o(TヘTo) 다음에 꼭 다시와 ~ ! \n")
                print("\n")
                print_slow("준영이는 방을 나왔다 \n")
                print("\n")
                like1 = proheart1()
                total_proheart1 += like1
                print_slow(f"박교수님의 호감도가 {like1} 올라서 {total_proheart1}가 되었다 ! (｡･∀･)ﾉﾞ)\n")
                print("\n")
                print_slow("돌아가는 중. . .\n")
                time.sleep(1)
                main_menu()
             else:
                print_slow("진짜 그럴거에요?\n")
                main_menu()
                
        elif total_proheart1 >= 35 and total_end_meet_pro1 >= 3:
             meet_pro+=1
             end_meet_pro1(1)
             print_slow("박교수님 : 준영아 안보여서 걱정했어 ~ (/▽＼) \n\n")
             print("________________선 택 창________________\n")
             print("|                                       |\n")
             print("| > 1. 시험 준비하느라... 교수님 과제좀 |\n")
             print("|      줄여주세요 제발요 너무 어려워요  |\n")
             print("|                                       |\n")
             print("| > 2. 시험 때문에 바빠서 못왔어요 ㅠㅠ |\n")
             print("|      그래도 코딩은 재밌어서 좋아요    |\n")
             print("|_______________________________________|\n")
             choice = input("어떤 대답을 할까? :\n")
             if choice == '1':
                print_slow("박교수님 : 어머... 그렇구나 미안해 (ToT)/~~~.\n")
                print_slow("（ヽ(*。>Д<)o゜교수님은 상처를 받으신거 같다...\n")
                like1 = proheart1()
                total_proheart1 -= like1
                print_slow(f"박교수님의 호감도가 {like1} 내려가서 {total_proheart1}가 되었다 (┬┬﹏┬┬) \n")
                print_slow("돌아가는 중. . .\n")
                time.sleep(1)
                main_menu()
             elif choice == '2':
                print_slow("박 교수님 : 아이고 시험 때문에 많이 힘들지 ? 그래도 다행이야 코딩을 좋아해줘서 （。＾▽＾） \n")
                print("\n")
                print_slow("준영이 : 괜찮아요 ヾ(•ω•`)o")
                print("\n")
                print_slow("박 교수님 : 별 건 아니고 이거 사탕인데 공부하면서 먹어 ~~ ヾ(^▽^*)))) \n")
                print("\n")
                print_slow("사탕을 받았다 ! \n")
                print("\n")
                print_slow("너무 맛있다... 스트레스가 10 내려갔다 \n")
                print("\n")
                print_slow("준영이와 박교수님은 재밌게 대화를 나눴다 !\n")
                print("\n")
                like1 = proheart1()
                total_proheart1 += like1+5
                print_slow(f"박교수님의 호감도가 {like1+5} 올라서 {total_proheart1}가 되었다 ! (｡･∀･)ﾉﾞ)\n")
                print("\n")
                print_slow("돌아가는 중. . .\n")
                time.sleep(1)
                main_menu()
             else:
                print_slow("진짜 그럴거에요?\n")
                main_menu()
        
    elif total_brain <= 10:
        print_slow("박소영 교수님은 자리에 안계시는 것 같다.\n")
        print("\n")
        print_slow("돌아가는 중. . .")
        time.sleep(1)
        main_menu()
        

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.08)

#김교수님 선택
def professor2():
    clear()
    global total_proheart2, total_brain, total_code, meet_pro
    meet_pro+=1
    move_cursor(0,5)
    print_slow("준영이 : 김교수님 계세요?\n")
    if total_brain >= 20 and total_code >= 20:
        if total_brain >= 20 and total_code >= 20:
            print_slow("김교수님 : 그래 어떤일로 왔니 ?\n")
            print("________________선 택 창________________\n")
            print("|                                       |\n")
            print("| > 1. 그냥요                           |\n")
            print("|                                       |\n")
            print("| > 2. 상담하고 싶은게 있어서 왔어요    |\n")
            print("|_______________________________________|\n")

            choice = input("어떤 대답을 할까? :\n")
            if choice == '1':
                print_slow("김교수님 : 그래? 할 말 없으면 이만 가자. 바쁘다 바뻐. (¬_¬ ))\n")
                print("\n")
                print_slow("（；´д｀）ゞ쫓겨났다...\n")
                print("\n")
                like2 = proheart2()
                total_proheart2 -= like2
                print(f"김교수님의 호감도가 {like2} 내려가서 {total_proheart2}가 되었다 /(ㄒoㄒ)/~~)\n")
                print("\n")
                print_slow("돌아가는 중. . .\n")
                time.sleep(1)
                main_menu()
            elif choice == '2':
                print_slow("김교수님 : 그래? 여기 앉아봐, 뭐 상담 하려고? o(*￣▽￣*)ブ)\n")
                print("\n")
                print_slow("준영이와 김교수님은 재밌게 대화를 나눴다\n")
                print("\n")
                like2 = proheart2()
                total_proheart2 += like2
                print(f"김교수님의 호감도가 {like2} 올라서 {total_proheart2}가 되었다 ! (｡･∀･)ﾉﾞ)\n")
                print("\n")
                
                print_slow("돌아가는 중. . .\n")
                time.sleep(1)
                main_menu()
            else:
                print_slow("진짜 그럴거에요?\n")
                main_menu()
    
    elif total_brain < 20 or total_code < 20:
        print_slow("김석규 교수님은 자리에 안계시는 것 같다.\n")
        print("\n")
        print_slow("돌아가는 중. . .\n")
        time.sleep(1)
        main_menu()
        
        
    #자판기 메뉴
def store():
    clear()
    global total_money, total_brain, total_code, total_health, total_stress
    
    if total_money >= 5:
        move_cursor(0,5)
        print_slow(" 무엇을 마시던 상상이상!! 구매하지 않으면 불행이 옵니다.\n")
        print_slow("    < 숫자를 선택 해 구매하세요! > \n")
        print("____________________________자 판 기_____________________________")
        print("|                                                                |\n")
        print("| > 1. 맛이 좋은 초록 이슬 (5원)                                 |\n")
        print("|       [스트레스 -20, 지능 -5]                                  |\n")
        print("|                 -마시면 기분이 좋아집니다-                     |\n")
        print("|                                                                |\n")
        print("| > 2. 스x피 커피우유 (10원)                                     |\n")
        print("|       [스트레스 +5, 지능 +10]                                  |\n")
        print("|                -저런...잠을 잘자야 키가 커 준영아-             |\n")
        print("|                                                                |\n")
        print("| > 3. 맛이 좋지 않은 사약 한 접시 (15원)                        |\n")
        print("|       [스트레스 +10, 체력 +20]                                 |\n")
        print("|                -사약은 몸에 좋은 재료로 이루어져 있다는 사실-  |\n")
        print("|                                                                |\n")
        print("| > 4. 딸기 맛이 나는 해열제 (10원)                              |\n")
        print("|      [스트레스 -20]                                            |\n")
        print("|                -준영아 힘내! 아프지마 유유.-                   |\n")
        print("|                                                                |\n")
        print("|> 5. 색이알록달록한버섯을우린물 (25원)                          |\n")
        print("|       [스트레스 -10, 코딩실력 +10, 지능 +10, 체력 -20]         |\n")
        print("|                -히히...이거 마시면 나도 코딩을...-             |\n")
        print("|                                                                |\n")
        print("|________________________________________________________________|")

    elif total_money <= 4:
        move_cursor(5,20)
        print_slow(" 돈도 없으면서 뭘 사시려고요 ? 가서 돈벌어와\n")
        main_menu()

    #자판기 메뉴선택
    choice = input(" 무엇을 드시겠어요? 설마 아무것도 마시지 않는건 아니시죠? (y/n) \n")
    if choice == '1':
        if total_money >= 5:
            print(" < 스트레스가 해소되고 지능이 떨어졌다 !>\n")
            print("\n")
            print_slow(" - 이슬은 아이셔가 맛있는데-\n")
            print("\n")
            stress(-20)
            brain(-5)
            money(-5)
            time.sleep(1)
            main_menu()
        elif total_money < 5:
            print_slow(" < 소지금이 부족합니다...[거-지]>\n")
            print("\n")
            time.sleep(1)
            store()

    elif choice == '2': 
        if total_money >= 9:
            print(" < 스트레스를 받고 지능이 올라갔다 !>\n")
            print("\n")
            print_slow(" - 공부 화이팅... 카페인은 조금만-\n")
            print("\n")
            stress(5)
            brain(10)
            money(-10)
            time.sleep(1)
            main_menu()
        elif total_money <= 9:
            print_slow(" < 소지금이 부족합니다...[거-지]>\n")
            print("\n")
            time.sleep(1)
            store()

    elif choice == '3':
        if total_money >= 15:
            print(" < 스트레스를 받고 체력이 올라갔다 !>\n")
            print("\n")
            print_slow(" - 우웩 너무 맛없어!! 하지만 먹는건 준영이다 화이팅! >o< - \n")
            print("\n")
            stress(10)
            health(20)
            money(-15)
            time.sleep(1)
            main_menu()
        elif total_money <= 14:
            print_slow(" < 소지금이 부족합니다...[거-지] >\n")
            time.sleep(1)
            store()
        
    elif choice == '4':
        if total_money >=10:
            print(" < 스트레스가 해소되었다 ! >")
            print("\n")
            print_slow("- 아플때까지 공부하지는 말기로 ㅜㅅㅜ - \n")
            print("\n")
            stress(-20)
            money(-10)
            main_menu()
        elif total_money <= 9:
            print_slow(" < 소지금이 부족합니다...[거-지] >\n")
            time.sleep(1)
            store()
    elif choice == '5':
        if total_money >= 25:
            print(" < 스트레스가 해소되고 체력이 떨어지고 코딩실력과 지능이 올라갔다 ! >\n")
            print("\n")
            print_slow(" - 코딩 능력자가 되기 위해서는 뭐든 할 수 있어... -\n")
            print("\n")
            stress(-10)
            brain(10)
            code(10)
            health(-20)
            money(-25)
            time.sleep(1)
            
            main_menu()
        elif total_money <= 24:
            print_slow(" < 소지금이 부족합니다...[거-지] >\n")
            time.sleep(1)
            store()
        
    elif choice == 'y':
            print_slow(" 아무것도 사지 않으시겠다고요? \n")
            print("\n")
            print_slow(" 그렇다면... <버섯> 을 강제로 먹이겠습니다.\n")
            print("\n")
            print_slow(" 스트레스를 1 받았다. 우웩 \n")
            print("\n")
            stress(1)
            main_menu()
    elif choice == 'n':
            print_slow(" 감사합니다! 자판기 숫자를 선택해서 구매하시면 됩니다! \n")
            print("\n")
            time.sleep(1)
            store()    
    else:
        print_slow(" 뭐하세요? 뭐든 하세요.\n")
        print("\n")
        time.sleep(1)
        store()

    #스탯 메뉴 
def status():
    clear()
    global total_money, total_brain, total_code, total_health, total_proheart1, total_proheart2, total_stress

    move_cursor(0,5)
    print("________________스 탯_________________\n")
    print("|                                     |\n")
    print("| > 지능:{:<28} |".format(total_brain))
    print("|                                     |\n")
    print("| > 체력:{:<28} |".format(total_health))
    print("|                                     |\n")
    print("| > 스트레스:{:<24} |".format(total_stress))
    print("|                                     |\n")
    print("| > 코딩실력:{:<24} |".format(total_code))
    print("|                                     |\n")
    print("| > 소지금:{:<26} |".format(total_money))
    print("|                                     |\n")
    print("| > 박교수님 호감도:{:<17} |".format(total_proheart1))
    print("|                                     |\n")
    print("| > 김교수님 호감도:{:<17} |".format(total_proheart2))
    print("|                                     |\n")
    print("|_____________________________________|\n")
    print("\n")

    
    def print_slow(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.08)
    choice = input("  > 메뉴로 돌아가기 (a): \n")
    if choice == 'a' or choice == 'A':
        main_menu()
    else:
        print_slow(" 제대로 입력하시라고요.\n")
        status()



    


    #main 코드만 실행되게하는 코드(name은 현재 진행중인 코드를 뜻함)
if __name__ == "__main__":
        main()
