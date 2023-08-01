import requests as rq

def get_data():
  url = 'https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22'
  response = rq.get(url)
  return response.json()

def filter_data(data, date_str):
  return list(filter(lambda item: item['dt_txt'].startswith(date_str), data['list']))[0]

def main():

  while True:
    print('-: Choose an option :-')
    print('1. Get weather')
    print('2. Get wind speed')
    print('3. Get pressure')
    print('0. Exit')
    choice = int(input('Enter your choice >> '))
    
    if choice in [1, 2, 3]:
      date_str = input("Enter a date (YYYY-MM-DD): ") # 2019-03-27
  
      data = get_data()
      filtered_data = filter_data(data, date_str)

    if choice == 1:
      temp = filtered_data['main']['temp']
      print(f'Temperature : {temp}')

    elif choice == 2:
      wind_speed = filtered_data['wind']['speed']
      print(f'Wind Speed : {wind_speed}')

    elif choice == 3:
      pressure = filtered_data['main']['pressure']
      print(f'Pressure : {pressure}')

    elif choice == 0:
      print('Terminating the program...')
      break

    else:
      print('Invalid input enter again!')

if __name__ == '__main__':
  main()
