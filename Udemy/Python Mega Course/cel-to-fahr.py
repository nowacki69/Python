def cel_to_fahr(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

temperatures = [10, -20, 100]

for temp in temperatures:
    print(cel_to_fahr(temp))
