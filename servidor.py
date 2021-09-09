class Servidor:

    def __init__(self, umax: int):
        self.umax: int = umax
        self.usuarios = []

    def adiona_usuario_servidor(self, usuario: object):
        self.usuarios.append(usuario)

