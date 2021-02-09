import requests

if __name__ == "__main__":

    print("Сервис httpbin.org позволяет тестировать запросы.\n"
          "Наличие переданных параметров в ответе означает, "
          "что сервер их принял и обработал.")

    # ---------------------------------------------------------------
    print("\n1. Простой GET-запрос и отображение результата")
    r = requests.get("https://httpbin.org/")
    # или используя метод r = requests.request("GET", "httpbin.org/")

    print("URI:", r.url)
    print("\nСтатус и сообщение:", r.status_code, r.reason)
    print("\nЗаголовки:")
    for key in sorted(r.headers):
        print("  - {}: {}".format(key, r.headers[key]))
    print("\nКодировка:", r.encoding)
    print("\nПервые 500 символов тела сообщения: ")
    print(r.text[:500])

    # ---------------------------------------------------------------
    print("\n2. Передача параметров")
    my_params = {"key1": "value1", "key2": "value2"}
    r = requests.get("http://httpbin.org/get", params=my_params)
    print("URI с параметрами:", r.url)
    print(r.text)
    print("Ответ как json:", r.json())

    # ---------------------------------------------------------------
    print("\n3. Закачка файлов")
    r = requests.get("https://httpbin.org/image/jpeg")
    if r.status_code == requests.codes.ok:  # 200
        with open("1.jpeg", "wb") as fh:
            fh.write(r.content)
        print("Файл сохранен!")

    # ---------------------------------------------------------------
    print("\n4. Произвольные заголовки запроса")
    headers = {"user-agent": "my-app/0.0.1"}
    r = requests.get("https://httpbin.org/get", headers=headers)
    print(r.text)

    # ---------------------------------------------------------------
    print("\n5. Простой POST-запрос")
    data = {"data1": "value1", "data2": "value2", "data3": "value3"}
    r = requests.post("http://httpbin.org/post", data=data)
    print(r.text)

    # ---------------------------------------------------------------
    print("\n6. POST-запрос отправка файла")
    files = {"file": open("1.jpeg", "rb")}
    r = requests.post("http://httpbin.org/post", files=files)
    print(r.text)
