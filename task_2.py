import urllib.request
from bs4 import BeautifulSoup
from threading import *
from time import time, sleep


def weather():
    url = 'https://defis.ua/pam-jat--ta-nosii-informacii/ssd-nakopichuvachi/?page=3'
    # Створення запиту з заголовком User-Agent
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/91.0.4472.124 Safari/537.36'
        }
    )

    try:
        # Виконання запиту
        with urllib.request.urlopen(req) as response:
            html = response.read()
        # Парсинг HTML-вмісту за допомогою BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        # Знаходження всіх елементів 'temperature-value'
        temperature_elements = soup.find_all('temperature-value')

        for temperature in temperature_elements:
            # Отримання значення атрибуту 'value'
            temperature_value = temperature.get('value')
            # Отримання текстового вмісту тегу
            temperature_text = temperature.text
            print(f"Temperature value (from attribute): {temperature_value}")
            return int(temperature_value)

    except urllib.error.HTTPError as e:
        print(f'HTTPError: {e.code}')
    except urllib.error.URLError as e:
        print(f'URLError: {e.reason}')
    except Exception as e:
        print(f'Error: {e}')


def benz_cost():
    url = 'https://index.minfin.com.ua/ua/markets/fuel/'
    req_benz = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/91.0.4472.124 Safari/537.36'
        }
    )

    try:
        with urllib.request.urlopen(req_benz) as response:
            html = response.read()

        soup = BeautifulSoup(html, 'html.parser')

        td_element = soup.find('td', {'align': 'right'})
        if td_element:
            big_element = td_element.find('big')
            if big_element:
                value = big_element.text.strip()
                print(f'BENz cost: {value} grivniya.')
            else:
                print('Big element not found')
        else:
            print('TD element not found')

    except urllib.error.HTTPError as e:
        print(f'HTTPError: {e.code}')
    except urllib.error.URLError as e:
        print(f'URLError: {e.reason}')
    except Exception as e:
        print(f'Error: {e}')


def dollar_cost():
    url = 'https://www.rbc.ua/rus/currency/USD'
    req_benz = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/91.0.4472.124 Safari/537.36'
        }
    )

    try:
        with urllib.request.urlopen(req_benz) as response:
            html = response.read()

        soup = BeautifulSoup(html, 'html.parser')

        colspan_element = soup.find('td', {'colspan': '2'})
        if colspan_element:
            dollar_value = colspan_element.text.strip()
            print(f'Dollar cost: {dollar_value} grivniya.')
        else:
            print('TD element not found')

    except urllib.error.HTTPError as e:
        print(f'HTTPError: {e.code}')
    except urllib.error.URLError as e:
        print(f'URLError: {e.reason}')
    except Exception as e:
        print(f'Error: {e}')


def measure_average_time(function, repeats=5):
    total_time = 0
    for i in range(repeats):
        start_time = time()
        function()
        end_time = time()
        total_time += (end_time - start_time)
    return total_time / repeats


# Вимірювання середнього часу послідовно
print("Sequential execution:")
average_weather_time = measure_average_time(weather)
average_benz_time = measure_average_time(benz_cost)
average_dollar_time = measure_average_time(dollar_cost)

print(f"Average weather time: {average_weather_time} seconds")
print(f"Average benz time: {average_benz_time} seconds")
print(f"Average dollar time: {average_dollar_time} seconds")

# Вимірювання середнього часу паралельно
print("\nParallel execution:")


def measure_parallel_time(functions, repeats=5):
    total_time = 0
    for i in range(repeats):
        start_time = time()
        threads = [Thread(target=func) for func in functions]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        end_time = time()
        total_time += (end_time - start_time)
    return total_time / repeats


average_parallel_time = measure_parallel_time([weather, benz_cost, dollar_cost])
print(f"Average parallel time: {average_parallel_time} seconds")


'''
def return_five_tims():
    i = 0
    temperature_sum = 0
    while i < 5:
        x1 = time()
        temperature_value = weather()
        if temperature_value is not None:
            temperature_sum += temperature_value
        i += 1
        x2 = time()
        print(x2 - x1)


return_five_tims()

weather()
benz_cost()
dollar_cost()
'''
