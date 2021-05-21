from enums.TipoUsuario import TipoUsuario
from model.Usuario import Usuario


class UsuarioService:

    def __init__(self):
        pass

    def consultarUsuario(self, nomeUsuario):
        lista_usuario = [
            Usuario("Filipe", "dsa54d4a5d4sa5", TipoUsuario.ADMIN.value),
            Usuario("Daniel", "115esa15sd15as1d", TipoUsuario.COMUM.value),
            Usuario("Douglas", "dsa45dsa45d4as54das", TipoUsuario.COMUM.value),
            Usuario("Rafael", "14sad54asd523", TipoUsuario.COMUM.value),
        ]

        for usuarioLista in lista_usuario:
            if(usuarioLista.nome == nomeUsuario):
                return usuarioLista

        return None