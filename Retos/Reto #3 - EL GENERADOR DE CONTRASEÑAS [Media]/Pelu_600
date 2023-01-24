import string
import random

caracteres = {"caps" : string.ascii_uppercase, "numbers" : string.digits, "sings" : string.punctuation}
modos = {"caps" : False, "numbers" : False, "sings" : False}

def genera_password(long, modos):

    password = string.ascii_lowercase

    for parameter , condition in modos.items():

        if condition:

            password += caracteres[parameter]

    return "".join(random.choices(password, k = long))


def main():

    longitud = int(input("Establezca el largo de la contraseña: "))

    while longitud < 8 or longitud > 16:

        longitud = int(input("Establezca el largo de la contraseña: "))

    modos["caps"] = input("Desea que la contraseña tenga letras mayúsculas: ")
    modos["numbers"] = input("Desea que la contraseña tenga numeros: ")
    modos["sings"] = input("Desea que la contraseña tenga simbolos: ")

    print(f"La contraseña es: {genera_password(longitud, modos)}")

if __name__ == "__main__":

    main()
