def reverse_palabra(Palabra,num):
    if num>0:
        print(Palabra[num],end='')
        reverse_palabra(Palabra,num-1)
    elif num == 0:
        print (Palabra[0])

str = input ("Ingrese una cadena de caracteres: ")
print("La cadena invertida es: ")
reverse_palabra(str,len(str)-1)