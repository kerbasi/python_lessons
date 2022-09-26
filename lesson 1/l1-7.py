# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

def logic_checker(x , y , z):
    return not (x or y or z) == (not x and not y and not z)

for i in range(2):
    for j in range(2):
        for k in range(2):
            print(f"Для значений x={i} y={j} z={k} выражение {'ИСТИННО' if logic_checker(i , j , k) else 'ЛОЖНО'}")