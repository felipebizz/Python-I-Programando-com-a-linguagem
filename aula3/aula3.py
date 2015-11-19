#Lista
#Tuplas
#Dicionarios

tipos_convite = ['vip', 'normal', 'meia', 'cortesia']

print('tipos_convite :', tipos_convite)

print('Adicionando elemento na lista')
tipos_convite.append('penetra')


convites_com_valor = ('meia', 30, 'vip', 60, 'normal', 40, 'cortesia', 0)
print('TUPLA :', convites_com_valor)


convites_com_valor = {'meia': 30, 'vip': 60, 'normal': 40, 'cortesia': 0}
print('DICIONARIO :', convites_com_valor)

print('Meia :', convites_com_valor['meia'])

print('VIP: ', convites_com_valor['vip'])

print(convites_com_valor.keys())

print(convites_com_valor.values())

#Convertendo lista para tuplas
estados = ('RJ', 'SP') + tuple(['MG', 'ES'])

print(type(estados))

numeros = [10, 5, 2, 30, 1]
print('MAX: ', max(numeros))
print('MIN: ', min(numeros))

nomes = ('felipe', 'flávio', 'fabio')
print('ODERNAR :', sorted(nomes))


materias_com_peso = {'Equações Diofantinas': 3, 'Álgebra Relacional': 2, 'Português instrumental': 4}

print('materias_com_peso :', materias_com_peso)
pesos = tuple(materias_com_peso.values())
print(pesos)


