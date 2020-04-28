from src.service import STRING, LIST
from src.service import RED
from exceptions.exceptions import NoDataEntered


def generate_passwords_file(json_data, json_password_parameters):
    try:
        list_of_words = get_all_data_from_json_data(json_data)
        list_of_words = list(filter(None, list_of_words))

        list_of_passwords = cartesian_product(list_of_words)
        # Me quede en modo leet
        print(list_of_passwords)
    except NoDataEntered:
        raise NoDataEntered()
    except KeyboardInterrupt as e:
        raise KeyboardInterrupt(e)


def get_all_data_from_json_data(json_data):
    try:
        data_list = []
        for option in json_data.items():
            data = option[1]['data']
            if data is not None:
                data = str(option[1]['data'])
                _type = str(option[1]['type'])
                if _type == STRING:
                    data_list = data_list + data.split(" ")
                elif _type == LIST:
                    data_list = data_list + option[1]['data']
                else:
                    data_list.append(data)

        if not data_list:
            raise NoDataEntered()

        return data_list
    except KeyboardInterrupt:
        raise KeyboardInterrupt("\n{0}Se interrumpió la ejecución.{1}".format(RED, RED))


def cartesian_product(list_of_words):
    password_list = []
    try:
        for word_1 in list_of_words:
            password_list.append(word_1)
            for word_2 in list_of_words:
                if word_1 != word_2:
                    password_list.append(word_1 + word_2)
        return password_list
    except KeyboardInterrupt:
        raise KeyboardInterrupt("\n{0}Se interrumpió la ejecución.{1}".format(RED, RED))
