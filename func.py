import re


def to_fixed(num_obj: float, digits=0):
    """
        :param num_obj: transfer number.
        :param digits: a number of simbols after comma.


        :return: str number
    """
    return f"{num_obj:.{digits}f}"


def put_money(balance):
    """
    :param balance: transfer the balance

    :return: will return the updated balance
    """
    inp_user = input("Enter the amount : ").replace(',', '.')
    inp_user = (re.findall(r'-[0-9.,]+|[0-9.,]+', inp_user))
    try:
        true_inp_user = float(inp_user[0])
        true_inp_user = to_fixed(true_inp_user, 2)

        return float(true_inp_user) + balance
    except TypeError:
        print('Ведите число!')


def choose_currency(bal):
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
    print(f"{round((bal / course), 2)} {curr}")