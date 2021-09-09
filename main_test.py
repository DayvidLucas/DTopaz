import unittest
from main import valida_entrada, carrega_dados
from servidor import Servidor
from usuario import Usuario


class MyTestCase(unittest.TestCase):

    def test_entrada_ttask_correta(self):
        ttask = valida_entrada(5, 2, [1, 2])
        self.assertEqual(ttask, "EXECUTA")

    def test_entrada_ttask_incorreta(self):
        ttask_abaixo = valida_entrada(0, 2, [1, 2])
        ttask_acima = valida_entrada(11, 2, [1, 2])
        self.assertEqual(ttask_abaixo, f"Maximo de ttask deve estar entre 1 e 10 -> Valor: {0}")
        self.assertEqual(ttask_acima, f"Maximo de ttask deve estar entre 1 e 10 -> Valor: {11}")

    def test_arquivo_sem_entrada_incorreta(self):
        sem_entrada = valida_entrada(4, 2, [])
        self.assertEqual(sem_entrada, "Arquivo sem nenhuma entrada:")

    def test_entrada_umax_incorreta(self):
        umax_abaixo = valida_entrada(4, 0, [1, 2])
        umax_acima = valida_entrada(4, 11, [1, 2])
        self.assertEqual(umax_abaixo, f"Maximo de Usuario deve estar entre 1 e 10 -> Valor: {0}")
        self.assertEqual(umax_acima, f"Maximo de Usuario deve estar entre 1 e 10 -> Valor: {11}")

    def test_entrada_saida(self):
        retorno_correto = [3, 4, 5, 4, 3, 3, 3, 3, 2, 0, 9]
        response = []
        carrega_dados("input_test.txt", "output_test.txt")
        arquivo = open("output_test.txt", "r")
        for linha in arquivo:
            response.append(int(linha.strip()))
        arquivo.close()
        print(self.assertEqual(retorno_correto, response))
        self.assertEqual(retorno_correto, response)

    def test_adiciona_usuario_servidor(self):
        s = Servidor(2)
        novo_usuario = Usuario(4)
        s.adiona_usuario_servidor(novo_usuario)
        self.assertIn(novo_usuario, s.usuarios)


if __name__ == '__main__':
    unittest.main()
