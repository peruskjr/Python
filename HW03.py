a, b, c = 3, 4, 5

if a < b:
    print('OK')
else:
    print('NOT OKAY')

if c < b:
    print('OK')
else:
    print ('NOT OKAY')

if a + b == c:
    print ('OK')
else:
    print('NOT OKAY')

if a**2 + b**2 == c**2:
    print ('OK')
else:
    print('NOT OKAY')

import turtle
aScreen = turtle.Screen()
shelly = turtle.Turtle()

color = input('Please enter a color: ')
lineWidth = int(input)('Please enter a line width: ')
lineLength = int(input)('Please enter a line length: ')
shape = input('Please enter a shape: ')

shelly.color(color)
shelly.width(lineWidth)

if shape == 'line':
    shelly.fd(lineLength)
elif shape == 'square':
    shelly.fd(lineLength)
    shelly.rt(90)
    shelly.fd(lineLength)
    shelly.rt(90)
    shelly.fd(lineLength)
    shelly.rt(90)
    shelly.fd(lineLength)
    shelly.rt(90)
elif shape == 'triangle':
    shelly.fw(lineLength)
    shelly.rt(120)
    shelly.fd(lineLength)
    shelly.rt(120)
    shelly.fd(lineLength)
    shelly.rt(120)
else:
    print('Sorry I do not recognize that shape, please specificy either a line, square, or trianlge!')


