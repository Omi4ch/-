import eel
import os
import g4f

@eel.expose
def Russia (display):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":display + 'на русском'}],
        stream=True,
    )
    for message in response:
        print (message,flush=True,end='')

@eel.expose
def maths (display):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":display + 'на русском'}],
        stream=True,
    )
    for message in response:
      print (message,flush=True,end='')
        
@eel.expose
def Literatura (display):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":'Напиши сочинение на тему' + display + 'на русском'}],
        stream=True,
    )
    for message in response:
        print (message,flush = True, end='')

@eel.expose
def IT (display):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":'Напиши код на тему' + display + 'на pythone'}],
        stream=True,
    )
    for message in response:
        print (message,flush = True, end='')


eel.init('C:/Users/egork/OneDrive/Рабочий стол/Хакатон ноябрь 2023/web')

eel.start('main.html', size=(651, 651), port = 8080)
