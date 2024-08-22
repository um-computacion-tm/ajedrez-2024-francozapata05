from main.cli import clear_console
import unittest
import os

class TestCli(unittest.TestCase):

    def test_clear_console(self):
        # Verificar que la función limpia la consola en Windows
        os.name = 'nt'
        self.assertEqual(clear_console(), None)
        # Verificar que la función limpia la consola en Linux/macOS
        os.name = 'linux'
        self.assertEqual(clear_console(), None)

