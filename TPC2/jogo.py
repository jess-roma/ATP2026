import random
print("""
████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████▀▄▄████████████████████████████
██▀▄─██▄─▄▄▀█▄─▄█▄─█─▄█▄─▄█▄─▀█▄─▄█─█─██▀▄─████─▄▄─███▄─▀█▄─▄█▄─██─▄█▄─▀█▀─▄█▄─▄▄─█▄─▄▄▀█─▄▄─█ █
██─▀─███─██─██─███▄▀▄███─███─█▄▀─██─▄─██─▀─████─██─████─█▄▀─███─██─███─█▄█─███─▄█▀██─▄─▄█─██─█▄█
▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▀▀▀▄▀▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▀▄▀▄▄▀▄▄▀▀▀▄▄▄▄▀▀▀▄▄▄▀▀▄▄▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▄▀

Seja bem vindo(a) ao jogo de adivinhar o número entre 1 e 100!
""")
menu= "m"

while menu=="m":
    per= input("\n\nPretendes adivinhar (1) ou ser adivinhado (2)? (1/2): ")
    while per!="1" and per!="2":
        print("\n>> Resposta inválida! ❌")
        per= input("\nPretendes adivinhar (1) ou ser adivinhado (2)? (1/2): ")
        

    if per=="1":
        r= random.randint(1,100)
        g = int(input("\n> Escreve o teu palpite: "))
        tent=1
        while g!=r:
             while g<1 or g>100:
                print("\n>> Resposta inválida! ❌")
                print("\nEscolhe um número entre 1 e 100.")
                g = int(input("> Escreve o teu palpite: "))
             if g>r:
                print("""\nO número que pensei é Menor!👇 
Tenta outra vez...""")
                g= int(input("> Escreve o teu palpite: "))
                tent+=1
             elif g<r:
                print("""\nO número que pensei é Maior!👆 
Tenta outra vez...""")
                g= int(input("> Escreve o teu palpite: "))
                tent+=1
        print(f"""\n\n>>> Acertaste em {tent} tentativa(s)! O número gerado era mesmo {r}! 🎉
            
            """)

    else:
         ls=100
         li=1
         g= random.randint(li,ls)
         print("\nPensa num número entre 1 e 100 e diz-me... 🤔")
         gg= int(input(f"\n> O teu número é maior (1), menor (2) ou igual (3) a '{g}'? (1/2/3): "))
         tent=1

    
         while gg!=3:
            while gg!=1 and gg!=2 and gg!=3:
                print("\n>> Resposta inválida! ❌")
                gg= int(input(f"\n> O teu número é maior (1), menor (2) ou igual (3) a '{g}'? (1/2/3): "))
            while gg==1:
                li= g+1
                if li>ls:
                    tent=1
                    print("\n>> Lógica inválida! ❌ Vamos tentar outra vez...")
                    li=1
                    ls=100
                    g= random.randint(li,ls)
                    gg= int(input(f"\n> O teu número é maior (1), menor (2) ou igual (3) a '{g}'? (1/2/3): ")) 

                else:
                    tent+=1
                    g= random.randint(li,ls)
                    gg= int(input(f"\n> O teu número é maior (1), menor (2) ou igual (3) a '{g}'? (1/2/3): "))
                 
            while gg==2:
                ls= g-1
                if li>ls:
                    tent=1  
                    print("\n>> Lógica inválida! ❌ Vamos tentar outra vez...")
                    li=1
                    ls=100
                    g= random.randint(li,ls)
                    gg= int(input(f"\n> O teu número é maior (1), menor (2) ou igual (3) a '{g}'? (1/2/3): "))        
                else:
                    tent+=1
                    g= random.randint(li,ls)
                    gg= int(input(f"\n> O teu número é maior (1), menor (2) ou igual (3) a '{g}'? (1/2/3): "))
         if gg==3 and tent==1:
             print(f"""\n\n>>> Então o número era '{g}'! Precisei de 1 tentativa(s) para o adivinhar... 🎉
        
                      """)


         else:
             print(f"""\n\n>>> Então o número era '{g}'! Precisei de {tent} tentativa(s) para o adivinhar... 🎉

              """)

        
    menu= input("\n> Queres voltar ao menu (m) ou sair (s)? ")
    while menu!="s" and menu!="m":
        print("\n>> Resposta inválida! ❌")
        menu= input("\n> Queres voltar ao menu (m) ou sair (s)? ")
        


print("""\n\n That's all folks! 👋🐷

""")