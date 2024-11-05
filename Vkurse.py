from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Combobox
import requests
import json


def update_currency_label(event):
    cur = currency_box.get()
    name = currencies[cur]
    currency_label.config(text=name)


def update_crypto_label(event):
    cryp = crypto_box.get()
    name = cryptocurrency[cryp]
    crypto_label.config(text=name)


def exchange_rate():
    cur = currency_box.get()
    cryp = crypto_box.get()
    if cur and cryp:
        try:
            url = f'https://api.coingecko.com/api/v3/simple/price?ids={cryp}&vs_currencies={cur}'
            headers = {'accept': 'application/json'}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            json_info = json.loads(response.text)
            price = json_info[cryp.lower()][cur.lower()]
            result_label.config(text=f'Стоимость 1 {cryp} составляет {price} {cur}')
        except Exception as e:
            mb.showerror('Ошибка', f'{e}')


currencies = {'USD': 'Американский доллар',
              'EUR': 'Евро',
              'RUB': 'Российский рубль'}
cryptocurrency = {'Bitcoin': 'Биткойн',
                  'Ethereum': 'Эфириум',
                  'Litecoin': 'Лайткоин',
                  'Dogecoin': 'Догикойн',
                  }

window = Tk()
window.title('Курс обмена криптовалют')
window.geometry('400x200')

Label(text="Валюта:").grid(row=0, column=0, padx=10, pady=10)
currency_box=Combobox(values=list(currencies.keys()))
currency_box.grid(row=0, column=1, padx=10, pady=10)
currency_box.bind('<<ComboboxSelected>>', update_currency_label)
currency_label = Label()
currency_label.grid(row=1, column=1)

Label(text="Криптовалюта:").grid(row=2, column=0, padx=10, pady=10)
crypto_box=Combobox(values=list(cryptocurrency.keys()))
crypto_box.grid(row=2, column=1, padx=10, pady=10)
crypto_box.bind('<<ComboboxSelected>>', update_crypto_label)
crypto_label = Label()
crypto_label.grid(row=3, column=1)

Button(window, text='Получить курс обмена', command=exchange_rate).grid(row=4, column=1)

result_label = Label()
result_label.grid(row=5, column=1, padx=5, pady=5)

window.mainloop()
