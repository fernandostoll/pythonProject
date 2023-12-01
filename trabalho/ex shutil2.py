import os
import shutil

os.chdir(r'C:\Users\fernando.silva8\Desktop\2023')

origem = r'C:\Users\fernando.silva8\Desktop\2023'
destino = r'C:\Users\fernando.silva8\Desktop\copia'

#shutil.copytree(origem, destino) #cria a pasta
shutil.rmtree(destino) #apaga a pasta