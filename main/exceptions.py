#Excepciones personalizadas

class CasillaOcupada(Exception):
    def __init__(self, message="La casilla seleccionada ya está ocupada por otra de tus piezas. Intentelo de nuevo."):
        self.message = message
        super().__init__(self.message)


class PiezaNoExiste(Exception):
    def __init__(self, message="No hay pieza en esa casilla. Intentelo de nuevo."):
        self.message = message
        super().__init__(self.message)

class MismaCasilla(Exception):
    def __init__(self, message="No puede mover una pieza a su misma casilla. Intentelo de nuevo."):
        self.message = message
        super().__init__(self.message)

class ColorIncorrecto(Exception):
    def __init__(self, message="La pieza seleccionada no es de tu color. Intentelo de nuevo."):
        self.message = message
        super().__init__(self.message)

class MovimientoInvalido(Exception):
    def __init__(self, message="El movimiento no es válido. Intentelo de nuevo."):
        self.message = message
        super().__init__(self.message)