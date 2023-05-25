v = float(input("Informe o valor: "))
t = float(input("Informe a taxa: "))
t2 = float(input("Informe o tempo: "))

p = v + (v * (t/100) * t2)

print(f"Prestacao: {p}")