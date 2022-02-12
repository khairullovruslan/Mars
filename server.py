from flask import Flask, url_for, request

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Миссия Колонизация Марса!</h1>"


@app.route("/index")
def index2():
    return "<h1>И на Марсе будут яблони цвести!</h1>"


@app.route("/promotion")
def promotion():
    return f"""Человечество вырастает из детства.<br>
Человечеству мала одна планета.<br>
Мы сделаем обитаемыми безжизненные пока планеты.<br>
И начнем с Марса!<br>
Присоединяйся!"""


@app.route("/image_mars")
def image_mars():
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <title>Привет, Марс!</title>
                          </head>
                          <body>
                            <h1>Жди нас, Марс!</h1>
                            <img src="{url_for('static', filename='img/mars.jpg')}" alt="здесь должна была быть картинка, но не нашлась">
                            <div>Вот она какая, красная планета</div>
                          </body>
                        </html>"""


@app.route("/promotion_image")
def promotion_image():
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                            <title>Колонизация</title>
                          </head>
                          <body>
                            <h1>Жди нас, Марс!</h1>
                            <img src="{url_for('static', filename='img/mars.jpg')}" alt="здесь должна была быть картинка, но не нашлась">
                            <div class="alert alert-dark" role="alert">
                                Человечество вырастает из детства.
                            </div>
                            <div class="alert alert-success" role="alert">
                                Человечеству мала одна планета.
                            </div>
                            <div class="alert alert-secondary" role="alert">
                                Мы сделаем обитаемыми безжизненные пока планеты.
                            </div>
                            <div class="alert alert-warning" role="alert">
                                И начнем с Марса!
                            </div>
                            <div class="alert alert-danger" role="alert">
                               Присоединяйся!
                            </div>
                          </body>
                        </html>"""


@app.route("/astronaut_selection")
def astronaut_selection():
    pass


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор</title>
                          </head>
                          <body>
                            <h1><center>Анкета претендента<center></h1>
                            <br>
                            <h2><center>на участие в миссии<center></h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" aria-describedby="surnameHelp" placeholder="Введите фамилию" name="surname">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                          <option>Послевузовское</option>
                                        </select>
                                    </div>
                                     <div>Какие у Вас есть профессии?</div>
                                     <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="1" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                     </div>
                                     <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="2" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                                     </div>
                                     <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="3" name="accept">
                                        <label class="form-check-label" for="acceptRules">Пилот</label>
                                     </div>
                                     <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="4" name="accept">
                                         <label class="form-check-label" for="acceptRules">Метеоролог</label>
                                     </div>
                                     <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="5" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label>
                                     </div>
                                     <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="6" name="accept">
                                       <label class="form-check-label" for="acceptRules">Инженер по радиационной защите</label>
                                     </div>
                                     <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="7" name="accept">
                                        <label class="form-check-label" for="acceptRules">Врач</label>
                                     </div>
                                     <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="8" name="accept">
                                       <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                     </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
