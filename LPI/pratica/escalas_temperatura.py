#Faça um programa em Python3 que receba uma temperatura em Fahrenheit, calcule e imprima o valor convertido para a escala Celsius e para a escala Kelvin, de acordo com as equações de conversão abaixo:

# t_celsius = (t_fahrenheit - 32) * 5/9
# t_kelvin = t_celsius + 273.15


def converteParaCelsius(t_fahrenheit):
    return (t_fahrenheit - 32) * 5/9

def converteParaKelvin(t_celsius):
    return t_celsius + 273.15

def pegaTemperatura():
    t_fahrenheit  = float(input("Digite a temperatura(°F): "));
    if not t_fahrenheit >= -459.67: 
        return print(f'Valor inválido, por favor insira um valor mair que {t_fahrenheit}');
    else :
        t_celsius = converteParaCelsius(t_fahrenheit);
        t_kelvin = converteParaKelvin(t_celsius);
        return print(f'Convertendo {t_fahrenheit} °F temos:\n{t_celsius} °C e {t_kelvin} K');

pegaTemperatura();