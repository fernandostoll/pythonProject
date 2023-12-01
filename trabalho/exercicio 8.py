import os
import shutil

os.chdir(r'C:\Users\fernando.silva8\Desktop')

#PARA ZIP UM PASTA
origem = 'foi zipado'

#arquivo_zip = 'foi zipado'
destino = 'desktop'

#shutil.make_archive(arquivo_zip, 'zip', '.', origem)
shutil.unpack_archive(origem, destino)