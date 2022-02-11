from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def title():
    return "Миссия Колонизация Марса"


@app.route('/index')
def slogan():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def advertising():
    return '''Человечество вырастает из детства.</br>

Человечеству мала одна планета.</br>

Мы сделаем обитаемыми безжизненные пока планеты.</br>

И начнем с Марса!</br>
Присоединяйся!</br>'''


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}" alt="здесь должна была быть картинка, но не нашлась">
                    <br>
                    <p1>Вот она какая, красная планета!</p1>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8081, host='127.0.0.1')
