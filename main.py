balance = 5000


def one_use():
    user_answer = input('Продолжить работу?\ntype exit/press enter\n_')
    if user_answer == 'exit':
        return False

    return True


while one_use():
    print('Действия пользователя')


def user_unset():
    try:
        user_unset_sum = input("Введите cумму: ")
    except ValueError:
        print("введено не число, оставляем 0")

