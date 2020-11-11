from botinstagram import InstagramBot
import getpass, time

""" Login Instagram """
usuario = input("Nome de usuario: ")
senha = getpass.getpass('Senha: ')
perfil = input("Pesquisar perfil: ")

""" Usuario e Senha do instagram utilizados para fazer login na conta """
instaBot = InstagramBot(usuario, senha)
instaBot.maximizar_janela()
instaBot.login()

""" Perfil que deseja pesquisar """
instaBot.abrir_perfil(perfil)
instaBot.curtir_sem_parar()
instaBot.fechar()
