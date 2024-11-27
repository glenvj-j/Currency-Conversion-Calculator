# Currency Conversion Calculator
# Created by Glen

import requests # for fetching web
import os
import time

from bs4 import BeautifulSoup

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

symbol = {
'ARS': ['$','Argentine'],
 'AUD': ['$','Australian'],
 'BWP': ['P','Botswanan'],
 'BGN': ['лв','Bulgarian'],
 'BRL': ['R$','Brazilian'],
 'BND': ['$','Brunei'],
 'CAD': ['$','Canadian'],
 'CLP': ['$','Chilean'],
 'CNY': ['¥','Chinese'],
 'COP': ['$','Colombian'],
 'HRK': ['kn','Croatian'],
 'CZK': ['Kč','Czech'],
 'DKK': ['kr','Danish'],
 'EUR': ['€','Euro'],
 'HKD': ['$','Hong Kong'],
 'HUF': ['Ft','Hungarian'],
 'ISK': ['kr','Icelandic'],
 'INR': ['₹','Indian'],
 'IDR': ['Rp','Indonesian'],
 'IRR': ['﷼','Iranian'],
 'ILS': ['₪','Israeli'],
 'JPY': ['¥','Japanese'],
 'KZT': ['лв','Kazakhstani'],
 'KRW': ['₩','South Korean'],
 'MYR': ['RM','Malaysian'],
 'MUR': ['₨','Mauritian'],
 'MXN': ['$','Mexican'],
 'NPR': ['₨','Nepalese'],
 'NZD': ['$','New Zealand'],
 'NOK': ['kr','Norwegian'],
 'OMR': ['﷼','Omani'],
 'PKR': ['₨','Pakistani'],
 'PHP': ['₱','Philippine'],
 'PLN': ['zł','Polish'],
 'QAR': ['﷼','Qatari'],
 'RON': ['lei','Romanian'],
 'RUB': ['₽','Russian'],
 'SAR': ['﷼','Saudi'],
 'SGD': ['$','Singapore'],
 'ZAR': ['R','South African'],
 'LKR': ['₨','Sri Lankan'],
 'SEK': ['kr','Swedish'],
 'USD': ['$','American']}

history = [['USD', 123123.0, 'BWP', 1681350.57, 'USDxBWP'], ['USD', 9090.0, 'BRL', 5292141232.97, 'USDxBRL']]

def history_print():
    print('          ╔══════════════════════╤═══════════════════════╗ ')
    print('          ║ From                 │  To                   ║ ')
    print('          ╠══════════════════════╧═══════════════════════╣ ')
    print('          ║                                              ║')
    for i in history:
        print(f'          ║    {i[0]}\t{round(i[1])}\t--->  {i[2]}  {round(i[3])}  \t ║')
    print('          ║                                              ║')
    print('          ╚══════════════════════════════════════════════╝')


def changecurrency():
    global listofhtml
    global moneyfrom
    while True:
        menu_inside = input("Enter the source currency : ").upper()
        if menu_inside == 'CANCEL' :
            break
        else:
            if menu_inside in symbol.keys():
                print('Currency is Available')
                moneyfrom = menu_inside
                page = requests.get(f"https://www.x-rates.com/table/?from={moneyfrom}&amount=1") #untuk download html
                soup = BeautifulSoup(page.text,'html.parser')

                listofhtml = soup.findAll('a')
                break
            else:
                print('Currency Not Available')
                clear_console()        
                

def converter():
    global moneyfrom
    global moneyto
    global listofhtml

    while True:
        list_currency()
        print()
        moneyto = input("▷ Enter the target currency : ").upper()
        if moneyfrom != moneyto :
            if moneyto in symbol.keys():
                clear_console()
                print()
                while True :
                    try:
                        clear_console()
                        print()
                        userinputmoney = float(input("▷ Enter the amount of money : "))
                        if userinputmoney.is_integer():
                            break
                        else:
                            continue
                    except ValueError:
                        print('Please Input Number not text')
                        time.sleep(2)
                
                x = moneyfrom
                y = moneyto
                checker = x+'&to='+y
                kurs = float([i.get_text() for i in listofhtml if checker in str(i.get('href'))][0])
                Output = round(userinputmoney * kurs,2)


                history.append([moneyfrom,userinputmoney,moneyto,Output]) #,moneyfrom+'x'+moneyto
                clear_console()
                print(f'''
          ╔════════════╤═════════════════════════════════╗
          ║ Conversion │         {moneyfrom}  --->  {moneyto} \t ║
          ╠════════════╧═════════════════════════════════╣
         
                 {symbol[moneyfrom][-2]} {userinputmoney:,}  --->  {symbol[moneyto][-2]} {Output:,}
         
          ╟──────────────────────────────────────────────╢
          ║ Kurs : {round(kurs,4)}\t\t\t\t ║
          ╚══════════════════════════════════════════════╝
''')
                input('Press Enter to Continue ')
                clear_console()
                break
            else:
                print('Currency Not Available')
                time.sleep(2)
                clear_console()
        else :
            print('Cannot convert to the same currency')
            time.sleep(2)
            clear_console()


def list_currency():
    currency_codes = list(symbol.keys())

    rows = [currency_codes[i:i+6] for i in range(0, len(currency_codes), 6)] #skip per 6 jadi biar di bawahnya bisa next nya
    print()
    print('  ╔═══════════════════════════════════════════════════════════════════╗')
    print('  ║                     List of Supported Currency                    ║')
    print('  ╠═══════════════════════════════════════════════════════════════════╣')
    print('  ║                                                                   ║')
    for row in rows:
        # Use 'join' to print the row elements with a fixed width for alignment
        print("  | ".join([f"{code:>8}" for code in row]))
    print('  ║                                                                   ║')
    print('  ╚═══════════════════════════════════════════════════════════════════╝')


def menu():
    print(f'''
          ╔══════════════════════════════════════════════╗
          ║                                              ║
          ║   Welcome to Currency Conversion Calculator  ║
          ║                                              ║
          ╚═══════════════════════╤══════════════════════╝
                 From Currency    ├>   {symbol[moneyfrom][-1]} {moneyfrom}\t\t 
          ╔═══════════════════════╧══════════════════════╗
          ║                                              ║
          ║   1. Start Program                           ║
          ║   2. Change Source Currency                  ║
          ║   3. History                                 ║
          ║   4. Exit                                    ║
          ║                                              ║
          ╠══════════════════════════════════════════════╣
          ║              created by Glen V               ║
          ╚══════════════════════════════════════════════╝
          ''')


#Main Program
def main():
    clear_console()
    global listofhtml
    global moneyfrom
    page = requests.get(f"https://www.x-rates.com/table/?from=USD&amount=1") #default USD
    soup = BeautifulSoup(page.text,'html.parser')
    listofhtml = soup.findAll('a')
    moneyfrom = 'USD'
    while True:
        menu()
        menu_choosen = input("Type the menu you want to run : ")
        if menu_choosen == '1':
            clear_console()
            converter()
        elif menu_choosen == '2':
            clear_console()
            list_currency()
            print()
            changecurrency()
            clear_console()
        elif menu_choosen == '3':
            clear_console()
            print()
            history_print() 
            print()
            input('Press Enter to Continue ')
            clear_console()
        elif menu_choosen == '4':
            break
        else:
            print("Menu doesn't exist")
            input('Press Enter to Continue ')
            clear_console()
        
main()
