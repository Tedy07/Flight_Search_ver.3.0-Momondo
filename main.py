from multiprocessing.managers import Value

print ('\nHello in Flight Search Program ver.3.0 \nMomondo')
#autor programu: Tedy07 ted.k07@gmail.com
# ver produkcyjna Momondo 07.11.2025 r.
# ver.3.1.1.
import webbrowser
import time
from datetime import datetime

menu_options = ('o', 'r', 'x')

while True:
      print()
      print('*** MENU ***')
      print('o = OW One Way Ticket')
      print('r = RT Return Ticket')
      print('x = Exit')
      print()
      print()
      user_input = input('Enter an option: ')

      if user_input in menu_options:
            break
      else:
            print()
            print('Option not available! / Opcja niedostępna!')

# tutaj kończy się menu

if user_input == 'o':
      print ()
      print ('**OW one way ticket**')
      skad=input("Podaj lotnisko wylotu: ")
      dokad=input("Podaj lotnisko docelowe: ")
      data_str=input("Podaj rok miesiac dzień RRRR-MM-DD: ")

      try:
            data=datetime.strptime(data_str, "%Y-%m-%d")
            print (f"Podana data to: {data.strftime('%d-%m-%Y')}")
      except ValueError:
            print("Niepoprawny format")

      lista = ['pl', 'es', 'dk', 'ie']
      # dodatkowe państwa 'de', 'it', 'fr', 'nl', 'no', 'pt', 'ch', 'se', 'cl', 'com.br', 'com.au', 'com', 'com.co', 'mx', 'com.pe', 'com.tr', 'co.uk', 'co.za', 'ca', 'cz', 'ee', 'in', 'at', 'ro',  'fi', 'ua'

      wait_time = 3
      counter=1

      for l in lista:

          webbrowser.get('firefox').open("https://www.momondo."+ l+ "/flight-search/"+ skad+ "-"+ dokad+ "/"+ data_str+"?ucs=1j6tr23&sort=price_a", new=0)
          time.sleep(wait_time)
          wait_time += 2
          # ('firefox')

          print(f"Licznik: {counter}")
          counter+=1

      print ('\nKoniec.')
# koniec pierwszej opcji wyboru OW


elif user_input == 'x':
            print()
            print('See you soon')
            exit()

