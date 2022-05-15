"""
Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада. Считаем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего. Если 3м аргументом передан 0, то вызов должен быть совпадать с задачей 4.
"""

def end_deposit(deposit, month=6, add=0):
    if 1000 <= deposit < 10000:
        if 6 <= month < 12:
            percent = 0.05
        elif 12 <= month < 24:
            percent = 0.06
        elif 24 <= month:
            percent = 0.05
    elif 10000 <= deposit < 100000:
        if 6 <= month < 12:
            percent = 0.06
        elif 12 <= month < 24:
            percent = 0.07
        elif 24 <= month:
            percent = 0.065
    elif 100000 <= deposit < 1000000:
        if 6 <= month < 12:
            percent = 0.05
        elif 12 <= month < 24:
            percent = 0.06
        elif 24 <= month:
            percent = 0.05
    else:
        return
    for _ in range(0, month):
        deposit += deposit * percent / 12
        deposit += add
    return round(deposit, 2)



if __name__ == "__main__":
    print(end_deposit(350000, 27, 5000))
