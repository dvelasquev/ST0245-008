def Elementorepetido(List): 
    cont = 0
    num = List[0] 
      
    for i in List: 
        frecuencia = List.count(i) 
        if(frecuencia> cont): 
            cont = frecuencia 
            num = i 
  
    return num 
  
List = [2, 1, 2, 2, 1, 3,15] 
print(Elementorepetido(List)) 