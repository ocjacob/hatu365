def getWeather(name):
    url = 'http://wthrcdn.etouch.cn/weather_mini'
    response = requests.get(url, {'city': name})
    result = json.loads(response.content.decode())
    print('city:', result.get('data').get('city'))
    data = result.get('data').get('yesterday')
    print(data.get('date'), '\t', data.get('high'), '\t', data.get('low'), '\t', data.get('type'), '\t', data.get('fx'), '\t',
          data.get('fl').replace('<![CDATA[', '').replace(']]>', ''))
    data = result.get('data').get('forecast')
    for i in data:
        print(i.get('date'), '\t', i.get('high'), '\t', i.get('low'), '\t', i.get('type'), '\t', i.get('fengxiang'), '\t',
          i.get('fengli').replace('<![CDATA[', '').replace(']]>', ''))


if __name__ == '__main__':
    print(getWeather('深圳'))
