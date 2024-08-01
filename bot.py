import os
from time import sleep as wait
import json
import pytesseract
import pyautogui as pg
import keyboard
import cv2
import rich
from rich.console import Console
from datetime import datetime
import sys

with open('config.json', 'r') as json_file:
    cfg = json.load(json_file)

def sprint(text, time):
    console.print(text)
    wait(time)

def dprint(text, color):
    nowTime = datetime.now().time()
    console.print(f'[{color}][{nowTime}] {text}')

console = Console()
vallstech = r"""

 ██▒   █▓ ▄▄▄       ██▓     ██▓      ██████ ▄▄▄█████▓▓█████  ▄████▄   ██░ ██ 
▓██░   █▒▒████▄    ▓██▒    ▓██▒    ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▒██▀ ▀█  ▓██░ ██▒
 ▓██  █▒░▒██  ▀█▄  ▒██░    ▒██░    ░ ▓██▄   ▒ ▓██░ ▒░▒███   ▒▓█    ▄ ▒██▀▀██░
  ▒██ █░░░██▄▄▄▄██ ▒██░    ▒██░      ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒▓▓▄ ▄██▒░▓█ ░██ 
   ▒▀█░   ▓█   ▓██▒░██████▒░██████▒▒██████▒▒  ▒██▒ ░ ░▒████▒▒ ▓███▀ ░░▓█▒░██▓
   ░ ▐░   ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ░▒ ▒  ░ ▒ ░░▒░▒
   ░ ░░    ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░░ ░▒  ░ ░    ░     ░ ░  ░  ░  ▒    ▒ ░▒░ ░
     ░░    ░   ▒     ░ ░     ░ ░   ░  ░  ░    ░         ░   ░         ░  ░░ ░
      ░        ░  ░    ░  ░    ░  ░      ░              ░  ░░ ░       ░  ░  ░
     ░                                                      ░                

"""

pause = [False]

def pauseFunc():
    if pause[0] == False:
        pause[0] = True
        dprint('Перерыв работы', 'yellow')
    else:
        pause[0] = False
        dprint('Продолжаем работу!', 'yellow')
def exitFunc():
    pause[0] = True
    dprint('Завершаю работу...', 'blue')
    wait(2)
    os.system('cls')
    console.print(vallstech)
    print('-' * 100 + '\n')
    dprint('Работа завершена!', 'green')
    os._exit(os.EX_OK)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def gta5rp_shveika():
    buttons = {
        "w": "images/shveika/w.png",
        "a": "images/shveika/a.png",
        "s": "images/shveika/s.png",
        "d": "images/shveika/d.png",
    }

    usp = cfg['bot']['untilStartLoop'] # UntilStartLoop

    os.system('cls')

    console.print(vallstech)
    print('-' * 50 + 'BOT-LOGS' + '-'  * 50)
    print('\n')
    dprint(f'Работа начнётся через {usp} секунды...', 'blue')
    wait(usp)

    while True:
        isWork = False

        if pause[0] == False:
            try:
                a = pg.locateOnScreen(buttons['w'], confidence=cfg['bot']['confidence'])
                keyboard.send('w')
                dprint('Нажал W', 'purple')
                isWork = True
            except: pass
            try:
                a = pg.locateOnScreen(buttons['a'], confidence=cfg['bot']['confidence'])
                keyboard.send('a')
                dprint('Нажал A', 'purple')
                isWork = True
            except: pass
            try:
                a = pg.locateOnScreen(buttons['s'], confidence=cfg['bot']['confidence'])
                keyboard.send('s')
                dprint('Нажал S', 'purple')
                isWork = True
            except: pass
            try:
                a = pg.locateOnScreen(buttons['d'], confidence=cfg['bot']['confidence'])
                keyboard.send('d')
                dprint('Нажал D', 'purple')
                isWork = True
            except: pass
            try:
                w_done = pg.locateOnScreen('images/shveika/w_done.png', confidence=cfg['bot']['confidence'])
                dprint('Трудовое законодательство запрещает Вам сегодня работать больше', 'red')
                dprint('Бот остановлен', 'yellow')
                pause[0] = True
                isWork = False
            except:
                dprint('Начал работу!', 'green')
                keyboard.send('e')
                isWork = False

            wait(cfg['bot']['sDelay'])


def gta5rp_luckSpin():
    def on_label_exists():
        ttw = cfg['bot']['phoneSpeed'] # TimeToWait
        dprint('Колесо удачи доступно!', 'green')
        
        keyboard.send('up')
        wait(ttw)
        pg.click(pg.locateOnScreen('images/safari.png', confidence=cfg['bot']['confidence']))
        wait(ttw)
        pg.click(pg.locateOnScreen('images/d_casino.png', confidence=cfg['bot']['confidence']))
        wait(ttw)
        pg.click(pg.locateOnScreen('images/lucky_spin.png', confidence=cfg['bot']['confidence']))
        wait(ttw)
        try:
            spin_button = pg.locateOnScreen('images/spin_button.png', confidence=cfg['bot']['confidence'])
            pg.click(spin_button)
            wait(20)
            if cfg['bot']['screenshotWins'] == True:
                nowTime = datetime.now().time()
                pg.screenshot(f'data/{nowTime}.png')
            wait(ttw)
        except pg.ImageNotFoundException: print('[⛔] spin_button.png not found!')
        keyboard.send('esc')

    usp = cfg['bot']['untilStartLoop'] # UntilStartLoop

    os.system('cls')

    console.print(vallstech)
    print('-' * 50 + 'BOT-LOGS' + '-'  * 50)
    print('\n')
    dprint(f'Работа начнётся через {usp} секунды...', 'blue')
    wait(usp)
    while True:
        if pause[0] == False:
            try:
                pg.locateOnScreen('images/spin_label.png', confidence=.7)
                on_label_exists()
            except pg.ImageNotFoundException:
                dprint('Колесо удачи не доступно', 'red')
                keyboard.send(cfg['bot']['key'])
            wait(cfg['bot']['delay'])

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def start():
    os.system('cls')
    print(vallstech)

    mlp = 50

    wait(cfg['bot']['animation'])
    sprint('-' * mlp + 'ВЫБЕРИТЕ-МОД' + '-' * mlp, cfg['bot']['animation'])
    sprint('\n[green]Авто колесо удачи: 1', cfg['bot']['animation'])
    sprint('[green]Авто швейка: 2', cfg['bot']['animation'])
    sprint('[red]Авто схемы: 3', cfg['bot']['animation'])
    sprint('\n' + '-' * mlp * 2, cfg['bot']['animation'])
    mode = input('\nМод: ')

    return mode

def main():
    def error(errorCode):
        os.system('cls')
        print(vallstech)
        print('-' * 100)
        console.print('[red]\n[⛔] Error!\n    [⛔] Error code: #' + str(errorCode))
        wait(cfg['bot']['errorTime'])
        main()

    mode = start()
    if not mode.isnumeric():
        error(cfg['error']['modeIsString'])

    match mode:
        case '1':
            gta5rp_luckSpin()
        case '2':
            gta5rp_shveika()
        case '3':
            error(cfg['error']['modeIsNotWorking'])
        case _ :
            error(cfg['error']['notFoundedMode'])
            
keyboard.add_hotkey(cfg['bot']['pauseKey'], pauseFunc)
keyboard.add_hotkey(cfg['bot']['exitKey'], exitFunc)

if __name__ == '__main__':
    main()