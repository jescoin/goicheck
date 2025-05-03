import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Back, Style



def again():
    answer = int(input(Fore.YELLOW+'Желаете продолжить? 1/2'))
    if answer == 1:
        check()
    if answer == 2:
        exit()


def check():
    address = input(Fore.BLUE + 'Адрес гоя:')
    url = "https://tonviewer.com/" + address + '?section=tokens'
    try:
        # Отправляем GET-запрос к странице
        response = requests.get(url)
        response.raise_for_status()  # Проверяем на ошибки

        # Создаем объект BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ищем элемент, содержащий "Tether USD SCAM"
        # (этот селектор может потребовать корректировки, если структура страницы изменится)
        scam_element = soup.find(string=lambda text: text and "SCAM" in text)

        if scam_element:
            print(Fore.RED + 'НЕ ГОЙ')
        else:
            print(Fore.GREEN+ "ЭТО ГОЙ, ЕБАШЬ ЕГО!")

        again()


    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к сайту: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
check()
