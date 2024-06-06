arquivo = open("C:/Users/pc/PycharmProjects/Projetos_DIO/05 - Manipulação de Arquivos/lorem.txt", "r")

#print(arquivo.read())
#print(arquivo.readline())
#print(arquivo.readlines())

# iterando em cada linha do arquivo
while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()
