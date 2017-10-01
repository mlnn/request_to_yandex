import requests


def translate_it(text, lng):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """

    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20171001T174454Z.9858f29bec848f69.edc9fd9cf15c4820a406ffd4b6ab6bd57c19ba20'

    params = {
        'key': key,
        'lang': lng + '-ru',
        'text': text,
    }

    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))


def open_file(lng):
    with open(lng + '.txt', encoding='UTF8') as f:
        text = f.read()
    return text


def write_file(text, lng):
    with open(lng.upper() + '-RU.txt', mode='w', encoding='UTF8') as f:
        f.write(text)
    print('Переведенный с языка {} на русский файл сохранен под именем {}-RU.txt'.format(lng, lng))

if __name__ == '__main__':
    languages = ['DE', 'ES', 'FR']
    for language in languages:
        text = open_file(language)
        translate_text = translate_it(text, language.lower())
        write_file(translate_text, language)
    print('Переведено сервисом «Яндекс.Переводчик» http://translate.yandex.ru/')  # в соответствии с требованиями
    # Яндекса
