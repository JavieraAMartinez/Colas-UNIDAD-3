class Cola:
    def __init__(self):
        self.cola = []

    def agregar(self, elemento):
        self.cola.append(elemento)

    def eliminar(self):
        return self.cola.pop(0)

    def esta_vacia(self):
        return len(self.cola) == 0

    def tamanio(self):
        return len(self.cola)

def main():
    colas = {
        "1": Cola(),
        "2": Cola(),
        "3": Cola()
    }

    while True:
        opcion = input("Ingrese C para agregar un cliente o A para atender un cliente: ").strip().upper()
        if opcion not in ("C", "A"):
            print("Opción inválida.")
            continue

        if opcion == "C":
            numero_servicio = input("Ingrese el número de servicio (1, 2 o 3): ").strip()
            if numero_servicio not in ("1", "2", "3"):
                print("Número de servicio inválido.")
                continue

            cola = colas[numero_servicio]
            numero_atencion = cola.tamanio() + 1
            cola.agregar(numero_atencion)
            print(f"Cliente con número de atención {numero_atencion} en la cola {numero_servicio}.")

        elif opcion == "A":
            numero_servicio = input("Ingrese el número de servicio (1, 2 o 3): ").strip()
            if numero_servicio not in ("1", "2", "3"):
                print("Número de servicio inválido.")
                continue

            cola = colas[numero_servicio]
            if cola.esta_vacia():
                print(f"No hay clientes en la cola {numero_servicio}.")
                continue

            numero_atencion = cola.eliminar()
            print(f"Llamando al cliente con número de atención {numero_atencion} de la cola {numero_servicio}.")

if __name__ == "__main__":
    main()


