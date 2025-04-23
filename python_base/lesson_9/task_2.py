def buy_ticket(full_name, age, adult=False):
    if age > 18:
        print('Билет продан')
    elif age < 18 and adult:
        print('Билет продан под присмотром взрослого')
    else:
        print('Нельзя продать билет')
