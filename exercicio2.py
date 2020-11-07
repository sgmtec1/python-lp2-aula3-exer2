'''
Preencha um dicionário com os dados de 5 alunos.
- Solicite os dados ao usuário
- Utilize como chave o nome do aluno e como valor uma lista
com três notas.
Percorra o dicionário e exiba a média de cada aluno.
'''

alunos = {} # dicionario

'''
for a in range(5):
    nome = input("Nome: ")
    n1 = float(input("Nota: "))
    n2 = float(input("Nota: "))
    n3 = float(input("Nota: "))
    lista = [n1, n2, n3]  
    alunos[nome] = lista
'''
for a in range(5): #define 5 alunos
    nome = input("Nome: ")#entro com nome 5 alunos
    lista = []#crio a lista
    for i in range(3):                  # define 3 espaços de memoria para 3 notas, preenche lista com as notas
        nota = float(input("Nota: "))# pergunto quais notas
        lista.append(nota)
    alunos[nome] = lista#criando a chave do nome na lista
    
print('Os alunos são:', alunos)

for a in alunos:
    lista = alunos[a]           # acessa a lista de notas
    media = sum(lista) / len(lista)
    print("Nome:", a, " - Media:", media)

