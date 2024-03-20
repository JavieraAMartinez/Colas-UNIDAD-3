class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0, item)

    def avanzar(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)


def sumar_colas(cola1, cola2):
    resultado = Cola()
    while not cola1.esta_vacia() and not cola2.esta_vacia():
        resultado.agregar(cola1.avanzar() + cola2.avanzar())

    while not cola1.esta_vacia():
        resultado.agregar(cola1.avanzar())
    while not cola2.esta_vacia():
        resultado.agregar(cola2.avanzar())

    return resultado


def main():
    cola1 = Cola()
    cola2 = Cola()

    numeros1 = input("Ingrese números para la primera cola separados por espacios: ").split()
    numeros2 = input("Ingrese números para la segunda cola separados por espacios: ").split()

    for num in numeros1:
        cola1.agregar(int(num))
    for num in numeros2:
        cola2.agregar(int(num))

    cola_resultado = sumar_colas(cola1, cola2)

    print("La suma de las colas es:")
    while not cola_resultado.esta_vacia():
        print(cola_resultado.avanzar())


if __name__ == "__main__":
    main()
