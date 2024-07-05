# Se va a crear un programa que organice y actualice los historiales médicos

medical_cost = {}

medical_cost['Marina'] = 6607.0
medical_cost['Vinay'] = 3225.0

medical_cost.update({'Connie':8886.0, 'Isaac': 16444.0, 'Valentina': 6420.0})

# Calcular el coste médico de cada paciente
total = 0
for cost in medical_cost.values():
    total += cost
media = total / len(medical_cost)
print('La media del coste es: ',media)

names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]

zipped_ages = zip(names,ages)

names_to_ages = {key:value for key, value in zipped_ages}
print(names_to_ages)

