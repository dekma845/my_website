# из библиотеки фласк мы импортируем класс фласк и функцию рендера шаблонов
from flask import Flask, render_template

# создаем объект класса фласк
app = Flask(__name__)

# декаратор который обрабатывает маршрут 
@app.route('/')# декарато -  старшая функция
def index():# Создаём функцию
    return render_template('index.html') # return возвращает отрендаренный шаблон



# Запускаем сервер
if __name__ == '__main__':
    app.run(debug=True)