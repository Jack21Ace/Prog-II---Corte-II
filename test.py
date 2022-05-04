# Total modulos a recorrer
n:int = 4
#Total distancia a recorrer
totalDistance:int = 26140/4
#Total gasolina por modulo
gasPerModule:int = 4674
#Total gasolina en el vehiculo
vehicleGas:int = 6534
for t in range(n-1):
    print(f"Estación {t}")
    if totalDistance > vehicleGas:
        print(f"Gasolina actual {vehicleGas}")
        vehicleGas = vehicleGas + gasPerModule
        print(f"Gasolina despues de tanquear {vehicleGas}")
    vehicleGas = vehicleGas - totalDistance
    print(f"Distnacia hasta la proxima bomba de gasolina {totalDistance}")
    print(f"Consumo despues de recorrido {vehicleGas}")
print(f'---Gasolina total despues del viaje {vehicleGas}')
