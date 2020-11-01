def is_valid_roman_number(roman_number):

    #Mogą występować tylko symbole I,V,X,L,C,D,M
    valid_symbols = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
    for i in roman_number:
        if i in valid_symbols:
           continue
        else:
            return False

    #Obok siebie nie może stać więcej niż 3 te same znaki (I, X, C, M)
    counter = 1
    for index, value in enumerate(roman_number):
        if (index + 1) < len(roman_number) and value == roman_number[index + 1] and value in ['I', 'X', 'C', 'M']:
            counter = counter + 1
        else: 
            counter = 1

        if counter > 3:
            return False

        # warunek 2: Obok siebie nie mogą stać dwa znaki: V, L, D.
        if (index + 1) < len(roman_number) and value in ['V', 'L', 'D'] and roman_number[index + 1] in ['V', 'L', 'D']:
            return False

    return True

def roman2int(s):
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_value = 0
        for i in range(len(s)):
            if i > 0 and roman_values[s[i]] > roman_values[s[i - 1]]:
                int_value += roman_values[s[i]] - 2 * roman_values[s[i - 1]]
            else:
                int_value += roman_values[s[i]]
        return int_value


if __name__ == "__main__":
    input_value = str(input('"Podaj liczbę w systemie rzymskim:'))


    assert (is_valid_roman_number(input_value) == True), 'Wprowadzona wartość nie jest poprawną liczbą rzymską'

    print(roman2int(input_value))
