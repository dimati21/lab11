
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import math

app = Flask(__name__)

@app.route('/')
def hello():
    str ='''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask_calc</title>
</head>
<body>
    <p>Для базовых функций калькулятора вводить значения с помощью /default/</p>
    <p>Функционал:</p>
    <p>1.Сложение (Пример: https://dimati2143.pythonanywhere.com/default/1+1)</p>
    <p>2.Вычитание (Пример: https://dimati2143.pythonanywhere.com/default/1-1)</p>
    <p>3.Умножение (Пример: https://dimati2143.pythonanywhere.com/default/1*1)</p>
    <p>4.Деление (Пример: https://dimati2143.pythonanywhere.com/default/1:1)</p>
    <p>5.Квадратный корень (Пример: https://dimati2143.pythonanywhere.com/default/sqrt4)</p>
    <p>6.Степень (Пример: https://dimati2143.pythonanywhere.com/default/2**2)</p>
    <p>2.Для тригонометрических функций калькулятора вводить значения с помощью /trig/</p>
    <p>Функционал:</p>
    <p>1.Синус (Пример: https://dimati2143.pythonanywhere.com/trig/sin1)</p>
    <p>2.Косинус (Пример: https://dimati2143.pythonanywhere.com/trig/cos1)</p>
    <p>3.Тангенс (Пример: https://dimati2143.pythonanywhere.com/trig/tg1)</p>
    <p>4.Котангенс (Пример: https://dimati2143.pythonanywhere.com/trig/ctg1)</p>
    <p>5.Арксинус (Пример: https://dimati2143.pythonanywhere.com/trig/asin1)</p>
    <p>6.Арккосинус (Пример: https://dimati2143.pythonanywhere.com/trig/acos1)</p>
</body>
</html>
'''
    return str

@app.route('/default/<do>')
def calc_default(do:str) -> str:
    try:
        if ":" in do:
            do = do.replace(":","/")
        elif "sqrt" in do:
            do = do.replace("sqrt", "")
            if do.isnumeric():
                return f"sqrt({do}) = {str(math.sqrt(float(do)))}"
            else:
                return "Ошибка"
        return f"{do} = {str(eval(do))}"
    except:
        return "Некорректный ввод"


@app.route('/trig/<do>')
def calc_trig(do: str) -> str:
    try:
        if 'acos' in do:
            do = do.replace("acos", "")
            if -1 <= float(do) <= 1:
                return f"acos({do}) = {str(math.acos(float(do)))}"
            else:
                return "Некорректное значение"
        elif 'asin' in do:
            do = do.replace("asin", "")
            if -1 <= float(do) <= 1:
                return f"asin({do}) = {str(math.asin(float(do)))}"
            else:
                return "Некорректное значение"
        elif 'cos' in do:
            do = do.replace("cos", "")
            return f"cos({do}) = {str(math.cos(float(do)))}"
        elif 'sin' in do:
            do = do.replace("sin", "")
            return f"sin({do}) = {str(math.sin(float(do)))}"
        elif 'ctg' in do:
            do = do.replace("ctg", "")
            return f"ctg({do}) = {str(math.cos(float(do) / math.sin(float(do))))}"
        elif 'tg' in do:
            do = do.replace("tg", "")
            return f"tg({do}) = {str(math.tan(float(do)))}"
        return "Такого действия нет"
    except:
        return "Некорректный ввод"

