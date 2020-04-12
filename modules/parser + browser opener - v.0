

import requests
import webbrowser

url = "https://www.zlomorda.net/"


def httpRequest():
    """ Функция обращается по адресу
        и печатает Статус Код
    """
    # Отправка запроса по адресу
    http_answer = requests.get(url)

    # Получам только номер кода
    http_status_code = http_answer.status_code
    print("Код ответа {}".format(http_status_code))
    statusCodeHelper(http_status_code)


def statusCodeHelper(status_code):
    """ Функция пытается найти страницу с определённым кодам
        для расшифровки. Если страница не найдена, то открывается
        страница с общими данными по кодам статуса.
    """
    user_answer = input("Для информации нажмите ENTER ")
    if user_answer == "":

        # Если был нажат ENTER, тогда программка созда линк на страницу с данным кодом
        url = "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/" + \
            str(status_code)

        # Проверка статуса данного линка
        http_answer = requests.get(url)
        http_status_code = http_answer.status_code

        # Если такой страницы нет, откроется общая страница по кодам статуса
        # Если такая страница есть, тогда программка откроет её в браузере
        if http_status_code == 404:
            webbrowser.open(
                "https://www.tutorialspoint.com/http/http_status_codes.htm", new=2)
        else:
            webbrowser.open(url, new=2)


if __name__ == "__main__":
    httpRequest()
