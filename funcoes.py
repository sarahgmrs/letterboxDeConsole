from collections import Counter
import ast
import os
from filmes import filmes

def voltar_ao_menu(): #Solicita uma tecla para voltar ao menu principal
    input('\nDigite uma tecla para voltar ao menu principal: ')
    
def exibir_subtitulo(texto):
    os.system('cls')
    linha = '_' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
       
def opc_invalida(): # Exibe mensagem de opção inválida e retorna ao menu principal
    print('Opção inválida!')
    voltar_ao_menu() 

def adicionar_filme():
    exibir_subtitulo('Adicionar novo título')
    titulo = input('Digite o título do filme: ').strip() # Tira o espaço extra no final
    while True:
        try:
            ano = int(input('Ano: '))
            if 1888 <= ano <= 2025: # Validação de ano plausível
                break
            print('Ano inválido! Digite entre 1888 e 2025.')
        except ValueError: # Caso ocorra um erro por uso inadequado de string, etc
            print('Digite um número válido para o ano.')
    diretor = input('Diretor: ').strip()
    genero = input('Gêneros (separado por vígula): ')
    while True:
        try:  
            avaliacao = float(input('Avaliação: '))
            if 0 <= avaliacao <= 10:
                break # Quebra dentro da estrutura if e volta a tentar novamente
            print('Avaliação deve ser entre 0 e 10!')
        except ValueError:
            print('Digite um número válido!')
    adicionar = { # Cria dicionario novo com os inputs 
        'titulo': titulo.title(),
        'ano': ano,
        'diretor': diretor.title(),
        'genero': genero,
        'avaliacao': avaliacao
    }
    print('\nFilme adicionado com sucesso!')
    print(f'Filme: {adicionar['titulo']}\n' f'Ano: {adicionar['ano']}\n' f'Diretor: {adicionar['diretor']}\n' f'Gênero: {adicionar["genero"]}\n' f'Nota: {adicionar['avaliacao']}')
    with open('filmes.py', 'r', encoding='utf-8') as f:
        conteudo = f.read() # Lê a lista importada antes de importar o dicionario
    valor_lista = conteudo.split('=', 1)[1].strip()
    lista_atual = ast.literal_eval(valor_lista)
    lista_atual.append(adicionar)
    novo_conteudo = f'filmes = {repr(lista_atual)}\n'
    with open('filmes.py', 'w', encoding='utf-8') as f: # Sobrescreve o dicionario novo sem perder os itens da lista
        f.write(novo_conteudo)
        voltar_ao_menu()
              
def listar_filmes_por_ano(): # Recebe um ano e retorna uma lista com os títulos dos filmes lançados naquele ano
    while True:
        aux = True 
        anos = int(input('Digite um ano: '))
        print(f'Filmes do ano {anos}:')
        for item in filmes:   
            if anos == item['ano']:
                aux = False 
                exibir_subtitulo('Listando filmes...')
                print(item['titulo'])
        if (aux): 
            print(f'Não há filmes do ano {anos}')    
        while True:
            res = input('Deseja pesquisar novamente? (Y/N)').upper()
            if res == 'Y':
                break # Quebra esse loop while True e volta para o anterior
            elif res == 'N':
                return False
            else:
                print('Digite apenas Y/N')
            voltar_ao_menu()

def media_avaliacoes(): # Calcula e retorna a média das avaliações de todos os filmes
    exibir_subtitulo('Média das avaliações de todos os filmes:')
    soma = 0.0
    for item in filmes:
        soma += item['avaliacao']
    media = soma / len(filmes)    
    print(f'{media:.2f}')
    voltar_ao_menu()
    
def filmes_por_genero(): # Recebe um gênero e retorna uma lista de dicionários contendo título e ano dos filmes que pertencem a esse gênero.
    while True:
        exibir_subtitulo('Filmes por gênero')
        aux = True # Variavel auxiliar que recebece o status se a busca é verdadeira ou falsa
        genero = input('Digite um gênero: ')
        for item in filmes:
            if genero == item['genero']:
                aux = False
                print(item['titulo'] , '|' , item['ano'])
        if (aux):
            print('Gênero não encontrado.')
        while True:
            resposta = input('Deseja pesquisar novamente? (Y/N)').upper()
            if resposta == 'Y':
                break
            elif resposta == 'N':
                return False
            else:
                print('Digite apenas Y/N')
            voltar_ao_menu()    
          
def estatisticas_diretores(): # Retorna um dicionário onde as chaves são os nomes dos diretores e os valores são a quantidade de filmes que eles dirigiram
    exibir_subtitulo('Quantidade de filmes logados por diretor')
    count = Counter(filme['diretor'] for filme in filmes)
    for diretor, quant in count.items(): # .tems() navega mais facilmente pelos itens da lista. quant = variavel que armazena a quantidade de filmes dirigidos por cada diretor
        print(f'{diretor}: {quant} filme(s)')
    voltar_ao_menu()
    
def normalizar_titulos(): # Padroniza todos os títulos dos filmes para que fiquem no formato "Primeira Letra Maiúscula"
    exibir_subtitulo('Todos os títulos')
    for item in filmes:
        titulos = item['titulo'].title()
        print(titulos)
    voltar_ao_menu()
    
def melhor_filme(): # Retorna o título do filme com a maior avaliação
    exibir_subtitulo('Filme mais bem avaliado')
    count = 0.0
    for item in filmes: 
        if count < item['avaliacao']:
            count = item['avaliacao']
            print('Filme mais bem avaliado:', item['titulo'], f'Nota: {count}')
            voltar_ao_menu()
        

        

    
        
        
        
        
        