cedula = int(input("Ingrese su número de documentación: "))
rol = input("Ingrese su rol dentro de la Universidad (profesor / estudiante): ").lower()
codProd = int(input("Ingrese el codigo del producto a comprar: "))
cantidad = int(input("Ingrese el numero de unidades que desea comprar: "))
precio = int(input("Ingrese el precio del producto: "))
precioProd = 0

if rol == "estudiante":
    precioProd = (precio * cantidad) * 0.5

elif rol == "profesor":
    precioProd = (precio * cantidad) * 0.8

print("El %s con cedula N°%s, debe pagar un total de %s$ por el producto %s" % (rol, cedula, precioProd, codProd))
