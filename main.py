from func import *


def one_use():
    user_answer = input('Продолжить работу?\ntype exit/press enter\n_').lower().strip()
    if user_answer == 'exit':
        return False

    return True


while one_use():
    print('Действия пользователя')

    choose_action = input("1 - Choose currency\n2 - put money\n3 - unset money\n4 - Show balance\nyour choice? : ")

    print(perform_action(choose_action, get_sum()))
