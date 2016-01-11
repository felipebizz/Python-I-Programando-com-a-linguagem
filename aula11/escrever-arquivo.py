arquivo_novo = open('arquivo_novo.csv', 'a')
arquivo_novo.write('Felipe lima, Programador, Poliglota \n')
arquivo_novo.close()

#Ou podemos dizer que queremos ler e escrever no arquivo através do flag w+:

#para leitura e escrita (w+)
arquivo = open('arquivo_novo.csv'','w+')

#Com o arquivo aberto, podemos ler uma linha através da função readline():

linha = arquivo.readline()
#E se quisermos ler todas as linhas usaremos um laço:

for linha in arquivo:
    print linha
