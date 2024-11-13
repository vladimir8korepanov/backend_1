from flask import Flask, render_template, request #импорт библиотек

app = Flask(__name__) #Инициализация объекта Flask

@app.route('/') #Дерокатор Url
def index(): #Функция которая отрабатывает при вызове декортора 
    name = 'Volodya' #Задание переменных
    age = 666
    return render_template('index.html', name=name, age=age) #Функция для отрисовок

if __name__ == '__main__': #Котнструкция для проверки запуска файла питона
    app.run(debug=True) #Запуск приложения в режиме откладки