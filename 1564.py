def copeira(entrada):
    if entrada > 0:
        return "vai ter duas!"
    else:
        return "vai ter copa!"


while True:
    try:
        print(copeira(int(input())))
    except EOFError:
        break
