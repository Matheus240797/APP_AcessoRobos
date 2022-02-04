import pyautogui as py
import pydirectinput as pi
from Acessos import lst_robos_homologa, lst_robos_producao, lst_aws

class robo:
    def __init__(self, ambiente, robo):
        py.hotkey('winleft', 'r')
        py.write("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Remote Desktop Connection.lnk")
        pi.press('enter')

        py.sleep(1)
        py.write(lst_aws[ambiente][0])
        pi.press('tab')
        pi.press('space')
        py.sleep(1)

        py.hotkey('shift', 'tab')
        py.sleep(1)
        pi.press('right')
        pi.press('tab')


        pi.press('left', presses=4)
        pi.press('enter')
        py.sleep(3)
        pi.press('tab', presses=2)
        pi.press('enter')
        py.sleep(2)
        pi.press('tab', presses=2)
        pi.press('enter')

        if ambiente == 1:
            py.write(lst_robos_producao[robo][0])
            pi.press('tab')
            py.write(lst_robos_producao[robo][1])
            pi.press('enter')
        if ambiente == 2:
            py.write(lst_robos_homologa[robo][0])
            pi.press('tab')
            py.write(lst_robos_homologa[robo][1])
            pi.press('enter')