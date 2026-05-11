"""
Semáforo. Leia a cor do semáforo (verde, amarelo ou vermelho) e exiba a ação correspondente:
Siga em frente, Atenção ou Pare.
"""

cor_semaforo = input('cor do semáforo: ')

if cor_semaforo.lower() == 'verde':
    print('Siga em frente!')
elif cor_semaforo.lower() == 'amarelo':
    print('Atenção!')
elif cor_semaforo.lower() == 'vermelho':
    print('Pare!')