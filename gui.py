import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do Application', layout=[[label], [input_box, add_button], [exit_button]])
window.read()
window.close()
