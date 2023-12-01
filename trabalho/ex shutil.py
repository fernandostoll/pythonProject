import os
import shutil

os.chdir(r'C:\Users\fernando.silva8\Desktop\biblioteca.shutil\fernando2.txt')

caminho_origem = r'C:\Users\fernando.silva8\Desktop\biblioteca.shutil\fernando2.txt'

caminho_destino = r'\Users\fernando.silva8\Desktop\copiando'

shutil.copyfile(caminho_origem, caminho_destino)