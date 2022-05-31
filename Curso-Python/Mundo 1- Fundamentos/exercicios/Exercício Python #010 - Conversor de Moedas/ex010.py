real = float(input('quantos reais vc tem? R$ '))
dolar = real/4.13
euro = real/4.80
print('com {:.2f}R$ você pode comprar: {:.2f} US$ '.format(real, dolar))
print('com {:.2f}R$ você pode comprar: {:.2f} €$ '.format(real, euro))
