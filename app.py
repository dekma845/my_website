# из библиотеки фласк мы импортируем класс фласк и функцию рендера шаблонов
from flask import Flask, render_template

# создаем объект класса фласк
app = Flask(__name__)

# декаратор который обрабатывает маршрут 
@app.route('/')# декарато -  старшая функция
def index():# Создаём функцию
    return render_template('index.html') # return возвращает отрендаренный шаблон
  

# декоратор который обрабатывает кнопки
@app.route('/<variable>') #функция принимает путь по умолчанию+переменная
def battons(variable): #функия кнопки обробаетывает переменную 
    """
    для примера используется логическое ветвление 
    
    """
    if variable == "1": # если перенная равна "1"
        return render_template("/1.html") # то функция возвращает путь к первой страничке
    elif variable == "2": # также переменная равна "2"
        return render_template("/2.html") # то функия возвращает вторую страничку
    elif variable == "3": # также переменная равна "3"
        return render_template("/3.html") # то функия возвращает третью страничку
    else: # иначе означает, то что если ни одно из выше перечисленных условий не исполненно
        return "Страница не найдена!!!!!!"  # то возвращает текущий сценарий
    # при необходимости else можно не использовать в таком случае скрипт будет исполняться без альтернативной логики


# Запускаем сервер
if __name__ == '__main__':
    app.run(debug=True)