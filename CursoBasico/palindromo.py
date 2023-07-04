# Palindromo es basicamente verificar que una palabra se escriba igual, al derecho y al revez.

#Paso 1. Definir la funcion run.

# strip

def palindromo(palabra):
    palabra = palabra.lower();
    palabra = palabra.replace(" ","");
    palabra_invertida = palabra[::-1];

    print("la palabra invertida es: "+palabra_invertida)
    if palabra_invertida==palabra:
        return True;
    else:
        return False;


def run():
    frase = input("Digite la palabra aleatoria: ");
    sicumple = palindromo(frase);
    if sicumple:
        print("La palabra si cumple Dx.");
    else:
        print("La palabra no cumple: Dx. ");    




if __name__== "__main__":
    run();

