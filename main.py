summaProcent = input('Enter the percentage you want : ')
summaProcent = float(summaProcent)
i = 0
while i < 10:
    summa = input('Enter the base cost of the item : ')
    summa = float(summa)
    summaD = ((summa / 100) * summaProcent)
    print(round(summa + summaD,3))
