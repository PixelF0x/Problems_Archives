one = 0
two = 2
suma = 0
while two < 4000000:
    suma = suma + two
    x = two
    two = two*4 + one # Каждое 3 число четное в ряде фибоначчи
    one = x
print(suma)