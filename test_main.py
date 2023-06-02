import unittest
from unittest import mock
from io import StringIO
from main import *

class CadastroUser(unittest.TestCase):
    @mock.patch('builtins.input')
    def test_cadastrar_usuario(self, mock_input):
        mock_input.side_effect = ['usuario1', 'senha1']
        usuarios = []
        cadastrar_usuario(usuarios)
        self.assertEqual(len(usuarios), 1)
        self.assertEqual(usuarios[0]['usuario'], 'usuario1')
        self.assertEqual(usuarios[0]['senha'], 'senha1')

        mock_input.side_effect = ['usuario2', 'senha2']
        cadastrar_usuario(usuarios)
        self.assertEqual(len(usuarios), 2)
        self.assertEqual(usuarios[1]['usuario'], 'usuario2')
        self.assertEqual(usuarios[1]['senha'], 'senha2')

        # Testar escrita no arquivo
        with open('usuarios.txt') as arquivo:
            conteudo = arquivo.read()
            self.assertIn('Usuario: usuario1 Senha: senha1', conteudo)
            self.assertIn('Usuario: usuario2 Senha: senha2', conteudo)

    @mock.patch('builtins.input')
    def test_fazer_login(self, mock_input):
        usuarios = [
            {'usuario': 'user1', 'senha': 'pass1'},
            {'usuario': 'user2', 'senha': 'pass2'},
        ]

        mock_input.side_effect = ['user1', 'pass1']
        self.assertTrue(fazer_login(usuarios))

        mock_input.side_effect = ['user2', 'pass2']
        self.assertTrue(fazer_login(usuarios))

        mock_input.side_effect = ['user3', 'pass3']
        self.assertFalse(fazer_login(usuarios))

        mock_input.side_effect = ['user1', 'pass2']
        self.assertFalse(fazer_login(usuarios))

class TestApp(unittest.TestCase):
    def test_pagina_inicial_opcao_1(self):
        with mock.patch('builtins.input', return_value='1'):
            with mock.patch('sys.stdout', new=StringIO()) as fake_output:
                pagina_inicial()
        self.assertEqual(fake_output.getvalue().strip(), '====PÁGINA INICIAL=====\n1 - Voltar para página de login')

    def test_pagina_inicial_opcao_2(self):
        with mock.patch('builtins.input', side_effect=['2']):
            with mock.patch('sys.stdout', new=StringIO()) as fake_output:
                with self.assertRaises(SystemExit) as cm:
                    pagina_inicial()
        self.assertEqual(cm.exception.code, None)
        self.assertEqual(fake_output.getvalue().strip(), '====PÁGINA INICIAL=====\n2 - Sair do sistema\nVocê saiu do sistema!')

    def test_main_opcao_1(self):
        with mock.patch('builtins.input', return_value='1'):
            with mock.patch('sys.stdout', new=StringIO()) as fake_output:
                main()
        self.assertEqual(fake_output.getvalue().strip(), 'Bem vindo ao NossoApp\nEscolha uma das opções abaixo\n1 - Fazer cadastro')

    def test_main_opcao_2_valido(self):
        usuarios = ['usuario1', 'usuario2']
        with mock.patch('builtins.input', return_value='2'), mock.patch('builtins.print') as fake_print:
            with mock.patch('sys.stdout', new=StringIO()) as fake_output:
                with mock.patch('builtins.input', side_effect=usuarios), mock.patch('sys.stdout', new=StringIO()) as fake_output2:
                    main()
        fake_print.assert_called_with('====PÁGINA INICIAL=====\n1 - Voltar para página de login')
        self.assertEqual(fake_output2.getvalue().strip(), 'Você saiu do sistema!')

    def test_main_opcao_2_invalido(self):
        usuarios = ['usuario1', 'usuario2']
        with mock.patch('builtins.input', return_value='2'), mock.patch('builtins.print') as fake_print:
            with mock.patch('sys.stdout', new=StringIO()) as fake_output:
                with mock.patch('builtins.input', side_effect=usuarios + ['usuario3']), mock.patch('sys.stdout', new=StringIO()) as fake_output2:
                    main()
        fake_print.assert_not_called()
        self.assertEqual(fake_output2.getvalue().strip(), 'Opção inválida, digite novamente.')

    def test_main_opcao_3(self):
        with mock.patch('builtins.input', return_value='3'):
            with mock.patch('sys.stdout', new=StringIO()) as fake_output:
                with self.assertRaises(SystemExit):
                    main()
        self.assertEqual(fake_output.getvalue().strip(), 'Você saiu do sistema!')

if __name__ == '__main__':
    main()
