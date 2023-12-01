massa_inicial = float(input('digite a massa inicial em gramas:'))
massa_final = 0.5
tempo = 0

while massa_inicial >= massa_final:
    massa_inicial /= 2
    tempo += 50

print(f'massa inicial|:{massa_inicial:.2f} gramas')
print(f'massa final: {massa_final} gramas')
print(f'tempo necessario: {tempo} segundos')