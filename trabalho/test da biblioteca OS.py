import os

#for sistema in os.environ:
#    print(sistema)
# novo_caminho = r'C:\Users\fernando.silva8\Desktop\bibliotecaOS'
# os.chdir(novo_caminho)
# print(novo_caminho)
# os.getcwd()

# os.mkdir('bibliotecaOS') #criar pastas

caminho = r'C:\Users\fernando.silva8\Desktop\2023\setembro\28\manha'
os.chdir(caminho)
#os.makedirs(caminho)
print(os.listdir())
#PARA REMOVER ARQUIVOS
#os.remove('test5.txt')
#os.rmdir('biblioteca')
#PARA RENOMEAR UM ARQUIVO OU DIRETORIO
#os.rename('test5.txt', 'teste2.txt')
#PARA INICIAR UM ARQUIVO
#os.startfile( r'C:\Users\fernando.silva8\Desktop\2023\setembro\28\manha\teste2.txt')

for root, dir, file in os.walk(r'C:\Users\fernando.silva8\Desktop\2023\setembro\28\manha'):
    #print(root) #oara ver a raiz
    #print(dir) #para ver a diretorios
    print(file) #para ver arquivos