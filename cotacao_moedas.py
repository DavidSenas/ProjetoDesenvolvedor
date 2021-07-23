import requests
from tkinter import *
from datetime import date
def cambio():
    dados = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    retorno = dados.json()
    cotação = (f'''
    Dollar = RS {retorno['USDBRL']['bid']}
    Euro = R$ {retorno['EURBRL']['bid']}
    Bitcoin = R$ {retorno['BTCBRL']['bid']}''')
    valores_moedas["text"] = cotação
janela = Tk()
janela.geometry('200x200')
janela.title('Cotação de moedas')
data = date.today()
Data = Label(janela, text=data)
Data.grid(column=0, row=4)
inf = Label(janela, text='Cotação em tempo real')
inf.grid(column=0, row=0)
bot = Button(janela, text='Clique para cotar', command=cambio)
bot.grid(column=0, row=3)
valores_moedas = Label(janela, text="")
valores_moedas.grid(column=0, row=5)
janela.mainloop()


