# imc.py

def calcular_imc(peso: float, altura: float) -> float:
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso e altura devem ser maiores que zero.")
    return round(peso / (altura ** 2), 2)

def classificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25.0:
        return "Peso normal"
    elif imc < 30.0:
        return "Sobrepeso"
    elif imc < 35.0:
        return "Obesidade grau 1"
    elif imc < 40.0:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"
