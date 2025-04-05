# из библиотеки фласк мы импортируем класс фласк и функцию рендера шаблонов
from flask import Flask, render_template, request, session
from utils.parser import get_url
from tasks import *

# создаем объект класса фласк
app = Flask(__name__)
app.secret_key = "ae0b2d9fa7cff80ed78dfcc"

# декаратор который обрабатывает маршрут 
@app.route('/')# декарато -  старшая функция
@app.route('/home')
def index():# Создаём функцию
    return render_template('index.html') # return возвращает отрендаренный шаблон
  

# декоратор который обрабатывает кнопки
@app.route('/<variable>', methods=['GET', 'POST']) #функция принимает путь по умолчанию+переменная
def battons(variable): #функия кнопки обробаетывает переменную 
    """
    для примера используется логическое ветвление 
    
    """
    if request.method == 'POST': #если сайт получает данные 
        # Получаем значение из текстового поля
        session['data'] = request.form.get('input_data') #сохраняет их в словарь под ключом дата

        return render_template('/2.html', data=session.get('data')) #возвращает эту же страничку с дополнительной переменной дата

    else:
        if variable == "1": # если перенная равна "1"
            return render_template("/1.html") # то функция возвращает путь к первой страничке
        elif variable == "2": # также переменная равна "2"
            return render_template("/2.html") # то функия возвращает вторую страничку
        elif variable == "3": # также переменная равна "3"
            links = get_url()
            return render_template("/3.html", links=links) # то функия возвращает третью страничку
        else: # иначе означает, то что если ни одно из выше перечисленных условий не исполненно
            return "Страница не найдена!!!!!!"  # то возвращает текущий сценарий
        # при необходимости else можно не использовать в таком случае скрипт будет исполняться без альтернативной логики


@app.route('/rgb')
def rgb():
    return task1()

@app.route('/max_number')
def max_number(n1 = 1, n2 = 3, n3 = 3):
    if n2 > n1:

        return "n2 < n1"
    else:
        return "max_number я "



@app.route('/earth')
def earth():
    return render_template('/earth.html') # return возвращает отрендаренный шаблон

@app.route('/EM-solenoid')
def em_solenoid():
    return render_template('/EM-solenoid.html')

@app.route('/general-relativity')
def general_relativity():
    return render_template('/general-relativity.html')






# Запускаем сервер
if __name__ == '__main__':
    app.run(debug=True)