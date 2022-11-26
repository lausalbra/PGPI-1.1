class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id" : producto.id,
                "nombre" : producto.nombre,
                "precio" : producto.precio,
            }
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"]  = self.carrito
        self.session.modified = True

    def devolver(self, nombre_producto):
        if nombre_producto in self.carrito['nombre_producto']:
            del self.carrito['nombre_producto']
            self.guardar_carrito()