from src.service import STRING, LIST
from exceptions.exceptions import NoDataEntered


def generate_passwords_file(json_data, json_password_parameters):
    try:
        list_of_words = get_all_data_from_json_data(json_data)
        list_of_words = list(filter(None, list_of_words))
        print(list_of_words)
    except NoDataEntered:
        raise NoDataEntered()


def get_all_data_from_json_data(json_data):
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
