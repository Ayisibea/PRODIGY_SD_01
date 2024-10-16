import PySimpleGUI as sg

# Function to handle temperature conversion
def convert_temperature(temp, unit):
    # Check if the input is a valid number (allowing negatives and decimals)
    if temp.lstrip('-').replace('.', '', 1).isdigit():
        temp1 = float(temp)
        if unit == 'F':
            newTemp = (temp1 - 32) * (5/9)
            return f'{newTemp:.2f} °C'
        elif unit == 'C':
            newTemp = (temp1 * (9/5)) + 32
            return f'{newTemp:.2f} °F'
        else:
            return 'Invalid unit. Use "C" for Celsius or "F" for Fahrenheit.'
    else:
        return 'Invalid temperature input. Please enter a valid number.'

# Layout for the window
layout = [
    [sg.Text('Temperature Converter')],
    [sg.Text('Temperature: '), sg.InputText(key='TEMP')],
    [sg.Text('Unit (C or F): '), sg.InputText(key='UNIT')],
    [sg.Text('Answer: '), sg.Text(size=(20, 1), key='OUTPUT')],
    [sg.Button('Convert'), sg.Button('Cancel')]
]

# Create the Window
window = sg.Window('Temperature Converter', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    
    # Get the temperature and unit from the input fields
    temp_input = values['TEMP']
    unit_input = values['UNIT'].upper()  # Convert to uppercase to handle 'C' and 'F' case-insensitively
    
    # Perform conversion and update output
    result = convert_temperature(temp_input, unit_input)
    window['OUTPUT'].update(result)

# Close the window when done
window.close()
