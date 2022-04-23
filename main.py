# Importando a biblioteca Tkinter
from tkinter import *
from tkinter import ttk
from datetime import datetime
from pytz import timezone
import pyglet

pyglet.font.add_file('digital-7.ttf')


#-- Definindo a paleta de cores
cor1 = '#000000'
cor2 = '#ffffff'
cor3 = '#21c25c'
cor4 = '#eb463b'
cor5 = '#dedcdc'
cor6 = '#3080f0'
cor7 = '#bfeeff'
cor8 = '#26ff1f'

fundo = cor1
cor = cor8

janela = Tk()
janela.title('')
janela.geometry('440x180')
janela.resizable(False, False)
janela.configure(background=fundo)

def relogio():

    tempo = datetime.now(timezone('America/Sao_Paulo'))
   

    hora = tempo.strftime('%H:%M:%S')
    dia_semana = tempo.strftime('%A')
    dia = tempo.day
    mes = tempo.strftime('%B')
    ano = tempo.strftime('%Y')

    l1.config(text=hora)
    l1.after(500, relogio)
    l2.config(text=dia_semana + ' ' + str(dia) + ' de ' + mes + ' de ' + str(ano))

    
l1 = Label(janela, text='', font=('digital-7 100'), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, pady=5, padx=40)
l2 = Label(janela, text='', font=('digital-7 17'), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, pady=5, padx=40)

relogio()
janela.mainloop()
