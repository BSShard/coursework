from PySimpleGUI import *
X,O = 0,0
#створимо задній фон
theme('DarkAmber')
def createLayout():
    global X,O
    dimensions = [2,1]
    display = []

    for i in range(3):
        disp = [Text(" "*14)]
        for j in range(1,4):
            disp.append(Text(background_color = '#bbbbcc',size = (dimensions[0],dimensions[1]),key = f'{i*3+j}',enable_events = True,font = ("Helvetica",25)))
        display.append(disp)
#Створимо основні елементи інтерфейсу
    layout =[ [Text(f"X:{X}\t\tO:{O}",key = 'score',font = ('Cambria',20))],
              [Text(text=" "*23+" Tic Tac Toe",enable_events = True, click_submits = True,key = 'click',font = ('Constantia',12),text_color = "#99CAFF")],
              *display,
              [Text(" "*9),Text("X's turn",size = (20,1),key = 'out',font = ('Leelawadee',12),background_color = "#660066")],
              [Text()],
              [Text(" "*5),Button(button_text = 'RESET BOARD',key = 'resetboard'),Button(button_text = 'RESET SCORE',key = 'resetscore')],
              [],
              [Text(" "*27),Button(button_text = 'QUIT',key = 'quit')]]
    return layout
#Пропишемо, щоб програма слідкувала за ходом гри
gameTable = [[None for i in range(3)] for i in range(3)]

def resetTable():
    global gameTable
    gameTable = [[None for i in range(3)] for i in range(3)]

d = {1:' O',0:' X'}
#Для слідкування за тим, чий хід
curr_player  = 0
#Для слідкування за тим, хто переміг та чи переміг
hasWon = 0

options = [str(i) for i in range(1,10)]
oneGame = True
def reset(window):
    global curr_player,hasWon,oneGame
    hasWon = 0
    oneGame = True
    curr_player = 0
    for i in range(1,10):
        window[f"{i}"].update('')
    resetTable()
#Начислення очків за перемогу тому чи іншому гравцю
def checkWin():
    global gameTable,d,hasWon
    if hasWon == 0:
        for i in range(3):
            if gameTable[0][i] != None:
                if gameTable[0][i] == gameTable[1][i] and gameTable[1][i] ==  gameTable[2][i]:
                    hasWon = 1 if gameTable[0][i] == ' X' else 2
            if gameTable[i][0] != None:
                if gameTable[i][0] == gameTable[i][1] and gameTable[i][1] ==  gameTable[i][2]:
                    hasWon = 1 if gameTable[i][0] == ' X' else 2
        if gameTable[1][1] != None:
            if (gameTable[0][0] == gameTable[1][1] and gameTable[1][1] == gameTable[2][2]) or (gameTable[2][0] == gameTable[1][1] and gameTable[1][1] == gameTable[0][2]):
                hasWon = 1 if gameTable[1][1] == ' X' else 2
    return None
def loop():    
    global curr_player,hasWon,options,gameTable,d,X,O,oneGame
    
    layout = createLayout()
    #Створення вікна гри
    window = Window('Tic Tac Toe', layout,margins = (100,100))

    while True:
        event, values = window.Read()
#Основний функціонал гри
        if event == 'click':
            print('Clicked')
        if oneGame:
            if event in options:
                r,c = divmod(int(event)-1,3)
                if gameTable[r][c] == None:                    
                    gameTable[r][c] = d[curr_player%2]
                    print(event)
                    window[event].update(d[curr_player%2])
                    curr_player+=1
        if event == 'resetboard':
            reset(window)
        checkWin()
        if hasWon:
            if oneGame:
                oneGame = False
                if d[hasWon-1] == ' X':
                    X+=1
                else:
                    O+=1
                window['out'].update(f'{d[hasWon-1]} has won the game!')
        else:
            if curr_player == 9:
                window['out'].update(f"Tied!")
            else:
                window['out'].update(f"{d[curr_player%2].strip()}'s turn")
        
        if event == WINDOW_CLOSED:
            break
            
        if event == 'quit':
            res = popup_yes_no("Do you want to quit?")
            if res.lower() == "yes":
                break
            else:
                pass
        
        if event == 'resetscore':
            X,O = 0,0
        window['score'].update(f"X:{X}\t\tO:{O}")
    window.close()
loop()
        

