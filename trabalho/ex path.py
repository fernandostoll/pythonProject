import os
path = r'C:\Users\fernando.silva8\Downloads\teste.os\teste6'
#check se existe
if os.path.exists(path):
    print('o caminho existe.')
    #encontrar nome do arquivo
    file_name = os.path.basename(path)
    print('nome do arquivo: ', file_name)
    #encontrar parte do diretorio
    directory = os.path.dirname(path)
    print('diretorio:', directory)
else:
    print('o caminho não existe')