from collections import Counter
import PySimpleGUI as sg


def isChinese(ch):
    return '\u4e00' <= ch <= '\u9fff'


def countChinese(text):
    cnt = 0
    for ch in text:
        if isChinese(ch):
            cnt += 1
    return cnt


def chineseStat(text):
    cnt = Counter()
    for ch in text:
        if isChinese(ch):
            cnt[ch] += 1
    res = '\n'.join('%s：\t%d' % (ch, freq) 
    for ch, freq in sorted(cnt.items(), key=lambda x:x[1], reverse=True))
    sg.popup_scrolled(res, title='字频统计', font=('宋体', 15))

def output(text):
    window['out'].update(text)


tab1_layout =  [[sg.Button('字数统计'),sg.Button('字频统计') ]]    

tab2_layout = [[sg.T('This is inside tab 2')],    
               ]

layout = [ [sg.TabGroup([[sg.Tab('通用', tab1_layout, tooltip='tip'), sg.Tab('Tab 2', tab2_layout)]], 
    tooltip='TIP2', expand_x=True)],
            [sg.Text('', key='out')],
            [sg.Multiline(key='main')]
        ]

window = sg.Window('文本整理器', layout, font=("宋体", 15), resizable=True,
        finalize=True, size=(1000, 1000))
window['main'].expand(expand_x=True, expand_y=True)

while True:
    event, values = window.read()
    if event == None:
        break
    elif event in ('字数统计'):
        output('汉字：%d' % (countChinese(values['main'])))
    elif event in ('字频统计'):
        chineseStat(values['main'])

window.close()
