#Excepciones personalizadas

class CasillaOcupada(Exception):
    def __init__(self, message="La casilla seleccionada ya está ocupada. Intentelo de nuevo."):
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