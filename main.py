from funcoes import adicionar_filme, listar_filmes_por_ano, media_avaliacoes, filmes_por_genero, estatisticas_diretores, normalizar_titulos, melhor_filme, opc_invalida, exibir_subtitulo
from filmes import filmes    
import os

def menu():
    print('1. Adicionar filme.')
    print('2. Listar filmes por ano.')
    print('3. Média das avaliações. ')
    print('4. Filmes por gênero.')
    print('5. Filmes por diretores.')
    print('6. Todos os títulos.')
    print('7. Melhor filme.')
    print('0. Sair')
    
def titulo():
    print("""
$$\       $$$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$$\  $$$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$\        $$$$$$$\  $$$$$$$$\        $$$$$$\   $$$$$$\  $$\   $$\  $$$$$$\   $$$$$$\  $$\       $$$$$$$$\ 
$$ |      $$  _____|\__$$  __|\__$$  __|$$  _____|$$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |$$  __$$\       $$  __$$\ $$  _____|      $$  __$$\ $$  __$$\ $$$\  $$ |$$  __$$\ $$  __$$\ $$ |      $$  _____|
$$ |      $$ |         $$ |      $$ |   $$ |      $$ |  $$ |$$ |  $$ |$$ /  $$ |\$$\ $$  |$$ |  $$ |      $$ |  $$ |$$ |            $$ /  \__|$$ /  $$ |$$$$\ $$ |$$ /  \__|$$ /  $$ |$$ |      $$ |      
$$ |      $$$$$\       $$ |      $$ |   $$$$$\    $$$$$$$  |$$$$$$$\ |$$ |  $$ | \$$$$  / $$ |  $$ |      $$ |  $$ |$$$$$\          $$ |      $$ |  $$ |$$ $$\$$ |\$$$$$$\  $$ |  $$ |$$ |      $$$$$\    
$$ |      $$  __|      $$ |      $$ |   $$  __|   $$  __$$< $$  __$$\ $$ |  $$ | $$  $$<  $$ |  $$ |      $$ |  $$ |$$  __|         $$ |      $$ |  $$ |$$ \$$$$ | \____$$\ $$ |  $$ |$$ |      $$  __|   
$$ |      $$ |         $$ |      $$ |   $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$  /\$$\ $$ |  $$ |      $$ |  $$ |$$ |            $$ |  $$\ $$ |  $$ |$$ |\$$$ |$$\   $$ |$$ |  $$ |$$ |      $$ |      
$$$$$$$$\ $$$$$$$$\    $$ |      $$ |   $$$$$$$$\ $$ |  $$ |$$$$$$$  | $$$$$$  |$$ /  $$ |$$$$$$$  |      $$$$$$$  |$$$$$$$$\       \$$$$$$  | $$$$$$  |$$ | \$$ |\$$$$$$  | $$$$$$  |$$$$$$$$\ $$$$$$$$\ 
\________|\________|   \__|      \__|   \________|\__|  \__|\_______/  \______/ \__|  \__|\_______/       \_______/ \________|       \______/  \______/ \__|  \__| \______/  \______/ \________|\________|
 """)
    

def main(): 
    while True:
        os.system('cls')
        titulo()
        menu()    
        try:
            opc_menu = int(input('Escolha uma opção do menu: '))
            if opc_menu == 1:
                adicionar_filme()
            elif opc_menu == 2:
                listar_filmes_por_ano()
            elif opc_menu == 3:
                media_avaliacoes()
            elif opc_menu == 4:
                filmes_por_genero()
            elif opc_menu == 5:
                estatisticas_diretores()
            elif opc_menu == 6:
                normalizar_titulos()
            elif opc_menu == 7:
                melhor_filme()
            elif opc_menu == 0:
                exibir_subtitulo('Finalizando o programa.')
                return False
            else:
                opc_invalida()
        except ValueError:
            opc_invalida() 
                
    
if __name__ == '__main__':
    main()    