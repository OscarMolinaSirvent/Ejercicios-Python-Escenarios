class Calculadora:
    def __init__(self,v_interno = 0):
        self.v_interno = v_interno

    def __verificar_entero(self, n):
        if not isinstance(n, int):
            raise ValueError(f"El valor de {n} no es de tipo entero")
        
    def suma(self,n):
        try:
            self.__verificar_entero(n)
            self.v_interno = self.v_interno + n
        except ValueError as e:
            print(e)

    def resta(self,n):
        try:
            self.__verificar_entero(n)
            self.v_interno = self.v_interno - n
        except ValueError as e:
            print(e)
    def multiplicacion(self,n):
        try:
            self.__verificar_entero(n)
            self.v_interno = self.v_interno * n
        except ValueError as e:
            print(e)
    def division(self,n):
        try:
            self.__verificar_entero(n)
            if n == 0:
                raise ValueError("No se puede dividir por cero")
        except ValueError as e:
            print(e)
    def set(self,valor):
        try:
            self.__verificar_entero(valor)
            self.v_interno = valor
        except ValueError as e:
            print(e)
    def reset(self):
        self.v_interno = 0

    def get_resultado(self):
        return self.v_interno
    
Calculado = Calculadora()
Calculado.suma(10)
print(Calculado.get_resultado())
Calculado.reset()
Calculado.division(20)
print(Calculado.get_resultado())
Calculado.suma(10)
print(Calculado.get_resultado())
Calculado.resta(10)
print(Calculado.get_resultado())
Calculado.set(100)
Calculado.multiplicacion(100)
print(Calculado.get_resultado())