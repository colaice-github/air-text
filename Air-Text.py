from pyperclip import copy
from tkinter import *
from tkinter.messagebox import showinfo


def encrypt(str):
    result = ''
    for char in str:
        code_point = ord(char)
        binary_string = format(code_point, 'b')
        morse_style_string = binary_string.replace(
            '0', 'ㅤ').replace('1', '‭')
        result += morse_style_string + ' '
    return result


def decrypt(str):
    result = ''
    morse_style_strings = str.split(' ')
    for morse_style_string in morse_style_strings:
        if morse_style_string:
            binary_string = morse_style_string.replace(
                'ㅤ', '0').replace('‭', '1')
            code_point = int(binary_string, 2)
            char = chr(code_point)
            result += char
    return result


app = Tk()
app.title('空气文字')
app.resizable(0, 0)
entry = Entry(app)


def start(*args):
    message = entry.get()
    try:
        d = decrypt(message)
    except:
        d = None
    showinfo('提示', f'解密\n{d}\n加密\n[{encrypt(message)}]\n按下确定复制加密结果')
    copy(encrypt(message))


entry.bind('<Return>', start)
entry.pack(fill=BOTH, expand=True)
app.mainloop()
