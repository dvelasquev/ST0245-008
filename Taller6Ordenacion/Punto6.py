futbolistasTup = [(1, "Casillas"), (15, "Ramos"), (3, "Pique"), (5, "Puyol"), (11, "Capdevila"),  (14, "Xabi Alonso"), (16, "Busquets"), (8, "Xavi Hernandez"), (18, "Pedrito"), (6, "Iniesta"), (7, "Villa")]
futbolistasTup.sort(key=lambda futbolista: futbolista[0])
print(futbolistasTup)

primerpunto = [4,7,11,4,9,5,11,7,3,5]
primerpunto.sort (key=lambda numero: numero)
print(primerpunto)

segundopunto = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,6,6,6,7,7,7,8,9] 
segundopunto.sort (key=lambda numero: numero)
print(segundopunto)

tercerpunto = [6,5,3,1,8,7,2,4]
tercerpunto.sort (key=lambda numero: numero)
print(tercerpunto)

# https://time.com/collection/best-inventions-2019/
MejoresInventos = [(50,'LightPhone2'),(21,'BoseFrames'), (90,'Wave'), (100,'ECOncrete'),(85,'RoliLumi'),(47,'RoybiRobot'), (100,'LightSail2'),(94,'AeroFarms')]
MejoresInventos.sort(key=lambda Inventos: Inventos)
print(MejoresInventos)