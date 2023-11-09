#Aluno: Lucas Praia and Andrey Borges

import random

def display(sala):
    print(sala)

coletar = 10

sala = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]
print("A sala está suja")
display(sala)

x =0
y= 0

while x < 4:
    while y < 4:
        sala[x][y] = random.choice([0,1])
        y+=1
    x+=1
    y=0

print("Antes de limpar a sala, vou detectar todas as sujeiras.")
display(sala)
x =0
y= 0
z=0
while x < 4:
    while y < 4:
        if sala[x][y] == 1:
            print("Aspirar esse local agora,",x, y)
            sala[x][y] = 0
            print("Limpo", x, y)
            z+=1
        y+=1
    x+=1
    y=0

    if coletar == 10:
     break
pro= (100-((z/16)*100))
print("Agora a sala está limpa. Obrigado por usar : Praia Robot")
display(sala)
print('performance=',pro,'%')