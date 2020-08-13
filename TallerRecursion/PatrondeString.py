string = input("Ingrese una palabra para realizar un patrón triangular: ")

a = 1
for i in string:
    print(string[0:a],end=" ")
    a+=1
    print()

