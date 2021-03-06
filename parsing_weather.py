import requests

s_city = "Kherson,UA"
city_id = 706448
appid = "bf92102ecd82d3994af53c403681fbd1"


def Weather_day():
    try:
        res = requests.get("https://api.openweathermap.org/data/2.5/forecast/",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        result1 = []
        for i in data['list'][:9]:
            date = i['dt_txt'][10:16]
            result1.append(date)
        return result1
    except Exception as e:
        print("Exception (forecast):", e)
        pass


def Weather_temp():
    try:
        res = requests.get("https://api.openweathermap.org/data/2.5/forecast/",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        result2 = []
        for i in data['list'][:9]:
            date = i['main']['temp']
            result2.append(round(date))
        return result2
    except Exception as e:
        print("Exception (forecast):", e)
        pass
