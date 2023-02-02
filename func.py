import re
import datetime


def to_fixed(num_obj: float, digits=0):
    """
        :param num_obj: transfer number.
        :param digits: a number of simbols after comma.


        :return: str number
    """
    return f"{num_obj:.{digits}f}"


def get_sum():
    """
    read txt file with balance

    :return: get info from user_info.txt
    """
    with open('file_data/user_info.txt') as file:
        balance = float(file.read())

    return balance


def set_sum(new_balance):
    """
    overwrite txt file with balance

    :param new_balance: file.txt
    """
    with open('file_data/user_info.txt', 'w') as file:
        file.write(str(new_balance))


def show_balance(balance):
    return f"Ваш баланс составляет: {balance} uah"


def put_money(balance):
    """
    :param balance: transfer the balance

    :return: will return the updated balance
    """
    inp_user = input("Enter the amount : ").replace(',', '.')
    inp_user = (re.sub('[^\d+.]', "", inp_user))

    try:
        true_inp_user = float(inp_user)
        true_inp_user = to_fixed(true_inp_user, 2)
        update_balance = float(true_inp_user) + balance
        set_sum(update_balance)

        return f"Операция успешна!\n{show_balance(update_balance)}"
    except ValueError:
        print('Ведите число!')


def choose_currency(balance):
    curr_list = [
        {"usd": 26.93},
        {"eur": 40.56},
    ]
    curr_str = "\n"
    for i in range(len(curr_list)):
        curr_str += f"{i + 1}.{list(curr_list[i].keys())[0]}\n"

    choose = int(input(f"Enter currency: {curr_str}"))
    choose -= 1
    course = list(curr_list[choose].values())[0]
    curr = list(curr_list[choose].keys())[0]

    return f"{round((balance / course), 2)} {curr}"


def user_unset(balance):
    try:
        user_unset_sum = float(input("Введите сумму: ").replace('-', '').replace(',', '.'))

        if user_unset_sum <= balance:
            rest = balance - user_unset_sum
            set_sum(rest)

            return f"Операция успешна!\n{show_balance(rest)}"
        else:
            return "Сумма превышает баланс"
    except ValueError:
        return "Сумма введена не верно!"


def set_log(log):
    with open("file_data/user_log.txt", 'a') as file:
        file.write(log)


def perform_action(action: str, balance):
    """
    :param action: selected user action
    :param balance: current user balance

    :return: the executed function from the internal dictionary
    """
    choose_list = [
        {"id": "1", "text": "choose currency", "func": choose_currency},
        {"id": "2", "text": "put money", "func": put_money},
        {"id": "3", "text": "user unset", "func": user_unset},
        {"id": "4", "text": "show balance", "func": show_balance}
    ]

    for dict_ in choose_list:
        for value in dict_['id']:
            if value == action:
                set_log(f"{dict_['text']} | {datetime.datetime.now()}\n")

                return dict_['func'](balance)

    return "Команда введена не верно. Выберите команду со списка!"
