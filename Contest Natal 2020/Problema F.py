from datetime import timedelta
from datetime import date

revolucoes = int(input())
ano_um = 365.25*revolucoes
jupiter = int(11.9*ano_um)
saturno = int(29.6*ano_um)
data = date(2020, 12, 21)

print(f"Dias terrestres para Jupiter = {jupiter}")
print(f"Data terrestre para Jupiter: {data + timedelta(days=jupiter)}")
print(f"Dias terrestres para Saturno = {saturno}")
print(f"Data terrestre para Saturno: {data + timedelta(days=saturno)}")
