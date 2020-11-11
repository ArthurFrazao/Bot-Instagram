from botinstagram import InstagramBot
import getpass, time

usuario = input("Nome de usuario: ")
senha = getpass.getpass('Senha: ')
perfil = input("Pesquisar perfil: ")

instaBot = InstagramBot(usuario, senha)
instaBot.maximizar_janela()
instaBot.login()
instaBot.abrir_perfil(perfil)
instaBot.curtir_sem_parar()
instaBot.fechar()