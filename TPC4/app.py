print(""" 
  >>> Menu <<<

(1) Criar Lista
(2) Ler Lista
(3) Soma
(4) Média
(5) Maior
(6) Menor
(7) está ordenada por ordem crescente
(8) está ordenada por ordem decrescente
(9) Procura um elemento
(0) Sair""")

o=input("Escolhe uma opção: ")
menu=['1','2','3','4','5','6','7','8','9','0']

import random
l=[]

#1
def randomLista(n):
    return  [random.randint(1,100) for _ in range (n)]

#2
def lerLista(n):
    l=[]
    contador=0
    while contador<n:
        x=int(input("Digita o número que pretendes adicionar: "))
        l.append(x)
        contador+=1
    return l

#3
def soma(l):
    soma=0
    for elem in l:
        soma+=elem
    return soma

#4
def media(l):
    soma=0
    for elem in l:
        soma+=elem
        media=soma/len(l)
    return media

#5
def maior(l):
    maior=l[0]
    for elem in l:
        if elem>maior:
            maior=elem
    return maior

#6
def menor(l):
    menor=l[0]
    for elem in l:
        if elem<menor:
            menor=elem
    return menor

#7 e 8
def estaOrdenado(l,o):
    if o=="C":
        i=0
        x=True
        while i<len(l)-1:
            if l[i]>l[i+1]:
                x=False
            i+=1
    elif o=="D":
        i=0
        x=True
        while i<len(l)-1:
            if l[i]<l[i+1]:
                x=False
            i+=1
    return x

#9
def procurar(l,n):
    i=0
    p=[]
    for elem in l:
        if elem==n:
            p.append(i)
        i+=1
    return p

while o!='0':
    while not (o in menu) or len(o)!=1:
        print("\n>> Opção inválida. Escolha entre os números do Menu.")
        print(""" 
  >>> Menu <<<

(1) Criar Lista
(2) Ler Lista
(3) Soma
(4) Média
(5) Maior
(6) Menor
(7) está ordenada por ordem crescente
(8) está ordenada por ordem decrescente
(9) Procura um elemento
(0) Sair""")

        o=input("Escolhe uma opção: ")

    if o=='1':
        n= int(input("\n> Quantos números queres na lista: "))
        l= randomLista(n)
        print(f"\n>>> A tua lista é: {l}")
    elif o=='2':
        n= int(input("\n> Quantos números pretendes adicionar: "))
        l= lerLista(n)
        print(f"\n>>> A lista que criste ficou: {l}")
    elif o== '3':
        print(f"\n> A soma dos elementos da tua lista é: {soma(l)}")
    elif o== '4':
        print(f"\n> A média da tua lista é: {media(l):.2f}")
    elif o== '5':
        x = maior(l)
        print(f"\n> O maior elemento da tua lista é: {x}")
    elif o== '6':
        print(f"\n> O menor elemento da tua lista é: {menor(l)}")
    elif o== '7':
        vereficar= estaOrdenado(l,'C')
        if vereficar== True:
            print("\n> A tua lista está ordenada por ordem crescente!")
        else:
            print("\n> A tua lista NÃO está ordenada por ordem crescente.")
    elif o== '8':
        vereficar= estaOrdenado(l,'D')
        if vereficar== True:
            print("\n> A tua lista está ordenada por oredem descrescente!")
        else:
            print("\n> A tua lista NÃO se encontra ordenada por oredem decrescente.")
    elif o== '9':
        n=int(input("\n> Qual é o número que pretendes procurar: "))
        c= len(procurar(l,n))
        if c== 0:
            print(f"\n>> O número {n} aparece {c} vezes, nas seguintes posições: [-1].")
        else:    
            print(f"\n>> O número {n} aparece {c} vezes, nas seguintes posições: {procurar(l,n)}.")
    print(""" 
  >>> Menu <<<

(1) Criar Lista
(2) Ler Lista
(3) Soma
(4) Média
(5) Maior
(6) Menor
(7) está ordenada por ordem crescente
(8) está ordenada por ordem decrescente
(9) Procura um elemento
(0) Sair""")

    o=input("Escolhe uma opção: ")

print("\n >> That's all folks! <<")