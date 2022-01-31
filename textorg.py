import PySimpleGUI as sg


def isChinese(ch):
    return '\u4e00' <= ch <= '\u9fff'


def countChinese(text):
    cnt = 0
    for ch in text:
        if isChinese(ch):
            cnt += 1
    return cnt


def output(text):
    window['out'].update(text)


layout = [ [sg.Button('字数统计') ],
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

window.close()
