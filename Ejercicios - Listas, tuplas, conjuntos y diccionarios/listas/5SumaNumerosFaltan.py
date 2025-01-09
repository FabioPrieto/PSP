numeros = [0, 3, 1, 4, 9]

max_num = max(numeros)
total_sum = sum(range(max_num + 1))
missing_sum = total_sum - sum(numeros)
print("La suma de los números que faltan es:", missing_sum)
