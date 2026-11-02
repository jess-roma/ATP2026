def menu():
    print("""
             >> Menu <<
     
     1: Criar uma turma;
     2: Inserir um aluno na turma;
     3: Listar a turma;
     4: Consultar um aluno por id;
     8: Guardar a turma em ficheiro;
     9: Carregar uma turma dum ficheiro;
     0: Sair da aplicação\n""")
    
    o=input("Opção escolhida: ")
    op=['1','2','3','4','8','9','0']
    while o not in op or len(o)!=1:
        print(">> Opção inválida. Escolha entre as opções disponíveis.")
        o=input("Opção escolhida: ")
    return o
turma=[]
#1
def criarTurma(na):
    while na!=0:
        aluno= inserirAluno()
        turma.append(aluno)
        na-=1
    return turma
#2
def inserirAluno():
    nome=input("\n> Insira o nome do aluno/a: ")
    id=int(input(f"> Insira a identificação d@ {nome}: "))

    duplicado=False
    for aluno in turma:
        if aluno[1]==id:
            duplicado=True
    while duplicado==True:
        print("\n>> Essa identificação já existe.")
        id=int(input(f"> Insira a identificação d@ {nome}: "))
        duplicado=False
        for aluno in turma:
            if aluno[1]==id:
                duplicado=True

    notaTPC=int(input(f"> Insira a nota TPC d@ {nome} (1 a 20): "))
    while 1>notaTPC or notaTPC>20:
        print("\n>> Nota inválida!")
        notaTPC=int(input(f"> Insira a nota TPC d@ {nome} (1 a 20): "))
    notaProj=int(input(f"> Insira a nota do projeto d@ {nome} (1 a 20): "))
    while 1>notaProj or notaProj>20:
        print("\n>> Nota inválida!")
        notaProj=int(input(f"> Insira a nota do projeto d@ {nome} (1 a 20): "))
    notaTeste=int(input(f"> Insira a nota do teste d@ {nome} (1 a 20): "))
    while 1>notaTeste or notaTeste>20:
        print("\n>> Nota inválida!")
        notaTeste=int(input(f"> Insira a nota do teste d@ {nome} (1 a 20): "))
    notas=[notaTPC,notaProj,notaTeste]

    aluno=(nome, id, notas)
    print(f"\n >>> {nome} foi adicion@ à turma com sucesso!")
    return aluno
#3
def listarTurma(turma):
    if turma==[]:
        print(">> Não existe uma turma para listar.")
    else:
        for aluno in turma:
            print(f"""
        Nome: {aluno[0]}
        ID: {aluno[1]}
        Nota TPC: {aluno[2][0]}
        Nota Projeto: {aluno[2][1]}
        Nota Teste: {aluno[2][2]}""")
#4
def consultarAluno(turma,idp):
    encontrado=False
    for aluno in turma:
        if aluno[1]==idp:
            print(f"Nome associado a essa identificação: {aluno [0]}")
            encontrado=True
    if encontrado==False:
        print(">> Não existe ninguém com essa identificação!")
#8
def guardar(turma):
    f=open("turma.txt", "w")
    for aluno in turma:
        nome= aluno[0]
        id= aluno[1]
        notaTPC= aluno[2][0]
        notaProj= aluno[2][1]
        notaTeste= aluno[2][2]
        linha= f"{nome}|{id}|{notaTPC},{notaProj},{notaTeste}\n"
        f.write(linha)
    f.close()
    print("\nFicheiro guardado com sucesso!")
#9
def carregar():
    turma=[]
    f=open("turma.txt", "r")
    for linha in f:
        campos= linha.strip().split("|")
        nome=campos[0]
        id=int(campos[1])
        notas=  campos[2].split(",")
        nota1=int(notas[0])
        nota2=int(notas[1])
        nota3=int(notas[2])
        turma.append((nome,id,[nota1,nota2,nota3]))
    f.close()
    print(turma)
    return turma

o=menu()
while o!='0':
    if o=='1':
        na=int(input("Número de alunos que pretende inserir: "))
        turma = criarTurma(na)
    elif o=='2' and len(turma)!=0:
        aluno=inserirAluno()
        turma.append(aluno)
    elif o=='3' and len(turma)!=0:
        listarTurma(turma)
    elif o=='4' and len(turma)!=0:
        idp= int(input("Identificação do aluno que procura: "))
        consultarAluno(turma,idp)
    elif o=='8' and len(turma)!=0:
        turma=guardar(turma)
    elif o=='9':
        carregar()
    else:
        print(">> Não existe nenhuma turma de momento.")
    o=menu()
print("  >> That's all folks! <<")