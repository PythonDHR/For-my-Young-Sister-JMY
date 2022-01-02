import pyautogui#导入pyautogui模块
import win32api

pyautogui.FAILSAFE = False

while True:
    ac = pyautogui.alert(text="hola amigo",title="贾明洋",button="谢谢",root=None,timeout=10000)#用alert方法打招呼
    if not len(ac) == None:
        break
    else:
        pyautogui.alert(text="我生气了",title="不能取消哦",timeout=10)
        continue

while True:
    b = pyautogui.prompt(text="What is your name?",title="不能小于2个符号，多于10个符号",default="")
    if not b == None:
        if 2 < len(b) < 10:
            break
    else:
        continue

while True:
    a = pyautogui.password(text="What is your password?",title="不能小于6个符号，多于18个符号",default="",mask="*")#获取密码
    if not a == None:
        if 6 < len(a) < 18:
            break
    else:
        continue

print(a)#打印密码

while True:
    d = pyautogui.confirm(text="订阅我的bilibili频道吧",title="Subscribe to us",buttons=["进入","再见"])
    if not d == None:
        if d == "进入":
            pyautogui.alert(text="Ok,出发",title="Let's begin",timeout=1000)
            break
        if d == "再见":
            pyautogui.alert(text="你没有拒绝的权利哦",title="Let's begin",timeout=1000)
            break
    else:
        pyautogui.alert(text="你这是什么意思？",title="let's begin,too.",timeout=1000)
        break

win32api.ShellExecute(1,"open","file:///D:/DHR's%20Python%20Program/htmla.html","","",1)