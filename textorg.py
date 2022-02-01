from cmath import exp
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
    totChinese = countChinese(text)
    res = '\n'.join('%s：\t%d\t%.4f%%' % (ch, freq, freq / totChinese * 100) 
    for ch, freq in sorted(cnt.items(), key=lambda x:x[1], reverse=True))
    sg.popup_scrolled(res, title='字频统计', font=('宋体', 15))

def output(text):
    window['out'].update(text)


tab1_layout =  [[sg.Button('字数统计'),sg.Button('字频统计') ]]    

tab2_layout = [[sg.Button('检查引号'), sg.Button('修正引号')],
               ]

layout = [ [sg.TabGroup([[sg.Tab('通用', tab1_layout, tooltip='tip'), sg.Tab('标点', tab2_layout)]], 
    tooltip='TIP2', expand_x=True)],
            [sg.Text('', key='out')],
            [sg.Multiline(key='main')]
        ]

window = sg.Window('文本整理器', layout, font=("宋体", 15), resizable=True,
        finalize=True, size=(1000, 1000))
window['main'].expand(expand_x=True, expand_y=True)

while True:
    event, values = window.read()
    text = values['main']
    if event == None:
        break
    elif event == '字数统计':
        totChinese = countChinese(text)
        uniqueChineseChars = set()
        for ch in text:
            if isChinese(ch):
                uniqueChineseChars.add(ch)
        output("总字数：%d\t不同汉字数：%d" % (totChinese, len(uniqueChineseChars)))
        # output('汉字：%d' % (countChinese(values['main'])))
    elif event == '字频统计':
        chineseStat(text)
    elif event == '检查引号':
        expectLeft = expectLeftc = True
        for c in text:
            if c in '“”':
                if (c == '“') ^ expectLeft:
                    output('不匹配')
                    break
                expectLeft = not expectLeft
            elif c in '‘’':
                if (c == '‘') ^ expectLeftc:
                    output('不匹配')
                    break
                expectLeftc = not expectLeftc
        else:
            output('匹配')
    elif event == '修正引号':
        expectLeft = expectLeftc = True
        textArray = list(text)
        for i, c in enumerate(textArray):
            if c in '“”':
                if expectLeft:
                    textArray[i] = '“'
                else:
                    textArray[i] = '”'
                expectLeft = not expectLeft
            elif c in '‘’':
                if expectLeftc:
                    textArray[i] = '‘'
                else:
                    textArray[i] = '’'
                expectLeftc = not expectLeftc
        window['main'].update(''.join(textArray))
        output('修正完成')
                    
            
window.close()
