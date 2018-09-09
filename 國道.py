def 收費():
    cash = 0
    Km = int(input('KM = ?'))
    if Km < 0:
        print('Erorr')
        收費()
    if Km <= 20:
        print(cash)
    elif Km <= 200:
        Km -= 20
        cash += Km * 1.2
        print(cash)
    elif Km <= 200:
        cash += 180 * 1.2
        Km -= 200
        cash += Km * 0.8
        print(cash)
收費()
       
