import functools
# functions


def divide(parameter): return functools.reduce(lambda a, b: a/b, parameter)
def inserir_input(parameter): return parameter.extend(input().split(" "))
def vira_int(parameter): return int(parameter)
def parse_int(parameter): return list(map(int, parameter))
# ____________________


# var
valores_string = []
i = 0
entradas = int(input())
# ____________________

while i < entradas:
    try:
        inserir_input(valores_string)
        array_int = parse_int(valores_string)
        result = divide(array_int)
        print(f"{result:.1f}")
    except ZeroDivisionError:
        print(f"divisao impossivel")
    finally:
        i += 1
        valores_string = []
