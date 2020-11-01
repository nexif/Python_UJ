while True:
    userInput = input('Podaj liczbę lub wpisz \'stop\' by zakończyć')
    if userInput == "stop":
        print('Program kończy działanie')
        break

    try:
        number = int(userInput)
    except ValueError:
        print("Podana wartość nie jest liczbą")
    else:
        print(number, ' do trzecieg potęgi to ', number ** 3)