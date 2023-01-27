def fibo(number):

    fibonacci = [0,1]

    for n in range(2, (number + 10)):

        fibonacci.append(fibonacci[n-2] + fibonacci[n-1])

    if number in fibonacci:

        return "fibonacci"

    else:

        return "no es fibonacci"

def primo(number):

    for n in range(2, number):

        if (number % n) == 0 and number != n:

            return "no es primo"

    return "es primo"

def par(number):

    if (number % 2) == 0:

        return "es par"

    else:

        return "es impar"


def main():

    number = int(input("Ingrese un número entero positivo: "))

    if number > 0:

        print(f"El número {number}: {primo(number)}, {fibo(number)} y {par(number)}")

    else:

        print("En numero ingresado no se puede evaluar")


if __name__ == "__main__":

    main()
