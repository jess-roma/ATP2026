import random
print('Bem vindo(a) ao jogo "Corrida até aos 100"!')
p= input("""\nEscolhe entre quem vai começar: 
1- Computador 
2- O utilizador
Escolha (1 ou 2): """)
while p!="1" and p!="2":
    print(">> Resposta inválida!")
    p= input("""\nEscolhe entre quem vai começar: 
1- Computador 
2- O utilizador
Escolha (1 ou 2): """)
if p=="1":
    l=[1,12,23,34,45,56,67,78,89,100]
    tt=0
    t=0
    i=0
    while tt<100 and t!=100 and i<len(l):
        nc= l[i]-tt
        t=tt+nc
        if t==100:
            print(f"\n  >> O computador escolheu {nc} chegando aos 100!")
            print("\n   >>> O computador ganhou!")
        else:
            u=int(input(f"\n > O total está {tt}. O computador escolheu o número {nc}. Ficando com um novo total de {t}. Qual é o número que o utilizador escolhe (1 a 10): "))
            while 10<u or u<1:
                print("\n >>> Resposta inválida!")
                u=int(input(f"\n > O total está {tt}. O computador escolheu o número {nc}. Ficando com um novo total de {t}. Qual é o número que o utilizador escolhe (1 a 10): "))
        tt+=nc+u
        i+=1 
    print("FIM DE JOGO!")

else:
    print("\n> Começas tu!")
    u = int(input("\nEscolhe um número: "))
    while 10 < u or u < 1:
        print("\n >>> Resposta inválida!")
        u = int(input("\nEscolhe um número: "))
        
    tt = 0
    t = 0
    i = 0
    nc = 0
    l = [1, 12, 23, 34, 45, 56, 67, 78, 89, 100]

    while t < 100 and tt < 100 and i < len(l):

        tt += nc + u
        if tt == 100:
            print("\n   >>> Chegaste ao 100 e ganhaste!!")
        else:
            if tt in l:
                nc = random.randint(1, 10) 
            else:
                if l[i]>tt:
                    nc = l[i] - tt
                else: 
                    while 10 < u or u < 1:
                        print("\n >>> Resposta inválida!")
                        u = int(input(f"\n > O total está {tt}. O computador escolheu o número {nc}. Ficando com um novo total de {t}. Qual é o número que o utilizador escolhe (1 a 10): "))
                    while tt>100:
                        tt-=(u+nc)
                        print("\n >>> Resposta inválida!")
                        u = int(input(f"\n > O total está {tt}. O computador escolheu o número {nc}. Ficando com um novo total de {t}. Qual é o número que o utilizador escolhe (1 a 10): "))
                        tt += u+nc
            t = tt + nc
            if t == 100:
                print(f"\n  >> O computador escolheu {nc} chegando aos 100!")
                print("\n   >>> O computador ganhou!")
            else:
                max_p = 100 - t
                if max_p > 10:
                    max_p = 10
                u = int(input(f"\n > O total está {tt}. O computador escolheu o número {nc}. Ficando com um novo total de {t}. Qual é o número que o utilizador escolhe (1 a 10): "))
                while u < 1 or u > max_p:
                    print("\n >>> Resposta inválida!")
                    u = int(input(f"\n > O total está {tt}. O computador escolheu o número {nc}. Ficando com um novo total de {t}. Qual é o número que o utilizador escolhe (1 a 10): "))
        i += 1

    print("\nFIM DE JOGO!")