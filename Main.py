import webbrowser

import PySimpleGUI as sg

# Buttons, Text inputs, etc.
layout = [  [sg.Text('Welcome to the login simulator! Guess the right password for a surprise!')],
            [sg.InputText('Enter password here', key=('passq'))],
            [sg.Button('Hint', key=('Hint1'))],
            [sg.Button('Continue'), sg.Button('Cancel')]




]

password = "tacocat"

window = sg.Window('Login Riddle Simulator!', layout )

#If statements for the buttons and text inputs and the main loop.

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break


    if event == 'Hint1':
        sg.popup('What word can be spelled the same backwards and fowards?')

    if event == 'Continue':
        if values['passq'] == password:
            sg.popup('You did it!!')
            webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        if values['passq'] != password:
            sg.popup('Wrong password!')

window.close()