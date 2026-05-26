import pyautogui as at
def aperta_tab(qtd):
    for i in range(qtd):
        at.press("tab")
        at.sleep(0.01)

at.hotkey("win","r")
at.write("chorme", 0.2)
at.press("enter")
at.write("www.instagram.com", 0.1)
at.press("enter")
email = at.prmpt("Digite o seu e-mail: ")
at.write(email, 0.1)
at.press("tab")
senha = at.prompt("Digite sua senha: ")
at.write(senha, 0.1)
at.press("enter")


at.hotkey("win","r")
at.write("chorme", 0.2)
at.press("enter")
at.write("www.tiktok.com", 0.1)
at.press("enter")
at.sleep(5)
email = at.prompt("Digite o seu e-mail: ")
at.write(email, 0.1)
aperta_tab(1)
senha = at.prompt("Digite sua senha do tiktok: ")
at.write(senha, 0.1)
at.press("enter")