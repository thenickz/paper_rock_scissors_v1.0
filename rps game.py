from random import choice
print('\n\tJOKENPÔ\n')

play = str(input('Jogada: '))
lista = ['pedra', 'papel', 'tesoura']
playPedra = play.find(lista[0])
playPapel = play.find(lista[1])
playTesoura = play.find(lista[2])
playPc = choice(lista)
vi = '\033[32mVITÓRIA!!'
de = '\033[31mDERROTA...'
em = '\033[33mEMPATE.'

if playPedra == 0 and playPc == 'tesoura':
    print('O computador jogou', playPc)
    print(vi)
elif playPedra == 0 and playPc == 'papel':
    print('O computador jogou', playPc)
    print(de)
elif playPedra == 0 and playPc == 'pedra':
    print('O computador jogou', playPc)
    print(em)
elif playPapel == 0 and playPc == 'pedra':
    print('O computador jogou', playPc)
    print(vi)
elif playPapel == 0 and playPc == 'tesoura':
    print('O computador jogou', playPc)
    print(de)
elif playPapel == 0 and playPc == 'papel':
    print('O computador jogou', playPc)
    print(em)
elif playTesoura == 0 and playPc == 'papel':
    print('O computador jogou', playPc)
    print(vi)
elif playTesoura == 0 and playPc == 'pedra':
    print('O computador jogou', playPc)
    print(de)
elif playTesoura == 0 and playPc == 'tesoura':
    print('O computador jogou', playPc)
    print(em)

print('\n\033[mFIM DO PROGRAMA')
