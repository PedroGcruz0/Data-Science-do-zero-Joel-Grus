import algebra_linear as agb
import gradiente_descendente as gdd
meus_vetores = [
    [1, 2],  # Vetor A
    [3, 4],  # Vetor B
    [5, 6]   # Vetor C
]

lista = ['A', 'B', 'C', 'D', 'E']
print (agb.soma_varios(meus_vetores))


l1 = meus_vetores[0]
l2 = meus_vetores[1]

print (agb.diferenca(l1,l2))


print(agb.multiplicar_escalar(5,l2))


print(agb.calcula_media(meus_vetores))

print(agb.produto_escalar(l1,l2))

print(agb.soma_quadrados(l1))

print(agb.distancia(l1,l2))

print(list(gdd.minibatches(lista,2)))