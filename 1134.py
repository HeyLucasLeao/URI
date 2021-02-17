alcool = 0
gasolina = 0
diesel = 0


def banco_posto(value):
    global alcool
    global gasolina
    global diesel
    if value == 1:
        alcool += 1
    elif value == 2:
        gasolina += 1
    elif value == 3:
        diesel += 1


def loop_pergunta(pergunta):
    if pergunta != 4:
        banco_posto(pergunta)
        loop_pergunta(int(input()))
    if pergunta == 4:
        print(
            f"MUITO OBRIGADO\nAlcool: {alcool}\nGasolina: {gasolina}\nDiesel: {diesel}")


loop_pergunta(int(input()))
