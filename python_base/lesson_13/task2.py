def print_name(func):
    def wrapper():
        print('Привет')
        func()
        print('Пока')
    return wrapper

@print_name
def welcome():
    print('Nastya')

welcome()
