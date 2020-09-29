def counting_sort(arr, Mayor, get_Indice):
  counts = [0] * Mayor

  # Contando - O(n)
  for a in arr:
    counts[get_Indice(a)] += 1
  
  # Acumulando - O(k)
  for i, c in enumerate(counts):
    if i == 0:
      continue
    else:
      counts[i] += counts[i-1]

  # Calculando el siguiente Indice - O(k)
  for i, c in enumerate(counts[:-1]):
    if i == 0:
      counts[i] = 0
    counts[i+1] = c

  ret = [None] * len(arr)
  # Ordenando - O(n)
  for a in arr:
    indice = counts[get_Indice(a)]
    ret[indice] = a
    counts[get_Indice(a)] += 1
  
  return ret




def get_digit(n, d):
  for i in range(d-1):
    n //= 10
  return n % 10

def get_num_difit(n):
  i = 0
  while n > 0:
    n //= 10
    i += 1
  return i

def radix_sort(arr, Mayor):
  NumDigitos = get_num_difit(Mayor)
  # O(k(n+k))
  for d in range(NumDigitos):
    
    arr = counting_sort(arr, Mayor, lambda a: get_digit(a, d+1))
  return arr


lista = [4,24,26,3,8,5,45,29,28,17,14]
print (radix_sort(lista,45))