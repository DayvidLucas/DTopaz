from servidor import Servidor
from usuario import Usuario


class ServidorHelper:

    def __init__(self, ttask: int):
        self.servidores = []
        self.ttask = ttask
        self.custo: int = 0
        self.retorno = []

    def valida_servidor_vazio(self, entradas: int, umax: int, arquivo_saida):
        for quantidade_entradas in entradas:
            while quantidade_entradas > 0:
                adicionado = False
                if len(self.servidores) == 0:
                    servidor = Servidor(umax)
                    servidor.adiona_usuario_servidor(Usuario(self.ttask))
                    self.servidores.append(servidor)
                else:
                    for servidor in self.servidores:
                        if len(servidor.usuarios) < umax:
                            servidor.adiona_usuario_servidor(Usuario(self.ttask))
                            adicionado = True
                            break
                    if not adicionado:
                        servidor = Servidor(umax)
                        servidor.adiona_usuario_servidor(Usuario(self.ttask))
                        self.servidores.append(servidor)
                quantidade_entradas -= 1
            self.valida_ciclo(arquivo_saida)
        while self.servidores:
            self.valida_ciclo(arquivo_saida)
        arquivo_saida.write("0\n")
        arquivo_saida.write(f"{self.custo}\n")

    def valida_ciclo(self, arquivo_saida):

        if len(self.servidores) != 0:
            self.retorno = []
            servidor_remover = []

            for servidor in self.servidores:
                usuario_remover = []
                self.custo += 1
                quantidade_usuarios = 0

                for usuario in servidor.usuarios:
                    quantidade_usuarios += 1
                    usuario.ciclo -= 1
                    if usuario.ciclo == 0:
                        usuario_remover.append(usuario)

                if len(usuario_remover) > 0:
                    servidor.usuarios = list(set(servidor.usuarios) - set(usuario_remover))
                self.retorno.append(quantidade_usuarios)

                if len(servidor.usuarios) == 0:
                    servidor_remover.append(servidor)
            if len(servidor_remover) > 0:
                self.servidores = list(set(self.servidores) - set(servidor_remover))
            arquivo_saida.write(f"{str(self.retorno)[1:-1]}\n")
