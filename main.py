import eel
import os
import g4f

@eel.expose
def Russia (display):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":'Проверить на ошибки текст' + display}],
    )
    return response

@eel.expose
def maths (display):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":display + 'на русском'}],
    )
    return response
        
@eel.expose
def Literatura (display):
    response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":'Напиши сочинение на тему' + display + 'на русском'}],
    )
    return response

@eel.expose
def IT (display):
    response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":'Напиши код на тему' + display + 'на языке Python'}],
    )
    return response


eel.init('web')

eel.start('main.html', size=(680, 651))
