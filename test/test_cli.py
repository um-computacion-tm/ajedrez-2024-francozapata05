from main.cli import Cliente
import unittest
import os
from main.chess import Chess
from main.exceptions import CasillaOcupada, PiezaNoExiste, MismaCasilla, ColorIncorrecto, MovimientoInvalido, IndexErrorPersonalizada


class TestCli(unittest.TestCase):

    def test_clear_console(self):
        # Verificar que la función limpia la consola en Windows
        os.name = 'nt'
        self.assertEqual(Cliente.clear_console(self), None)
        # Verificar que la función limpia la consola en Linux/macOS
        os.name = 'linux'
        self.assertEqual(Cliente.clear_console(self), None)


    def test_comenzar_iteracion(self):
        cliente = Cliente()
        chess = Chess()
        positions = chess.get_board().get_positions()
        self.assertEqual(cliente.comenzar_iteracion(chess, positions), None)

    def test_buscar_index_error(self):
        cliente = Cliente()
        # Verificamos que se lanza la excepción para el índice 0
        with self.assertRaises(IndexErrorPersonalizada):
            cliente.buscar_index_error(-1)
        # Verificamos que se lanza la excepción para el índice 8
        with self.assertRaises(IndexErrorPersonalizada):
            cliente.buscar_index_error(8)

    def test_detectar_exepcion(self):
        cliente = Cliente()
        # Verificamos que se lanza la excepción para el índice 0
        with self.assertRaises(ColorIncorrecto):
            cliente.detectar_exepcion("ColorIncorrecto")
        # Verificamos que se lanza la excepción para el índice 8
        with self.assertRaises(MovimientoInvalido):
            cliente.detectar_exepcion("MovimientoInvalido")
        with self.assertRaises(CasillaOcupada):
            cliente.detectar_exepcion("CasillaOcupada")
        with self.assertRaises(PiezaNoExiste):
            cliente.detectar_exepcion("PiezaNoExiste")
        with self.assertRaises(MismaCasilla):
            cliente.detectar_exepcion("MismaCasilla")