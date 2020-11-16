from botinstagram import InstagramBot
import getpass, time

"""próximas atualizações:
- incluir no bot opções de seguir perfil e de pesquisar mais de 1 perfil"""

def main():
    usuario = input("Nome de usuario: ")
    senha = getpass.getpass("Senha: ")   
    perfil = input("Pesquisar perfil: ")
    instaBot = InstagramBot(usuario, senha)
    instaBot.maximizar_janela()
    instaBot.login()
    instaBot.abrir_perfil(perfil)
    instaBot.curtir_sem_parar()
    instaBot.fechar()
    
if __name__ == "__main__":
    main()