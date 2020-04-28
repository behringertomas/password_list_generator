from datetime import datetime
from exceptions.exceptions import InvalidOptionJsonPasswordParameters

RED, WHITE, CYAN, GREEN, DEFAULT, YELLOW_BOLD = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m', '\033[0m', '\033[1;33m'
RESET = '\033[39m'

# ------------------------------------
# -- Data Types Available for Input --
# ------------------------------------

STRING = "String"
INT = "int"
SHORT_INT = "short_int"
EMAIL = "Email"
DATE = "Date"
LIST = "List"
BOOLEAN = "Boolean"

# ------------------------------------
# ---------- Default Values ----------
# ------------------------------------

DEFAULT_MAX_LENGTH = 12
DEFAULT_MIN_LENGTH = 8
DEFAULT_BOOL_ADD_SPECIALS = False
DEFAULT_BOOL_MODE_1337 = False

json_data_options = {
    "1": {
        "description": "1:- Nombre/s de la persona: ",
        "data": None,
        "type": STRING
    },
    "2": {
        "description": "2:- Celular de la persona: ",
        "data": None,
        "type": INT
    },
    "3": {
        "description": "3:- Apellido/s de la persona: ",
        "data": None,
        "type": STRING
    },
    "4": {
        "description": "4:- Nombre/s de la pareja de la persona: ",
        "data": None,
        "type": STRING
    },
    "5": {
        "description": "5:- Apodo/s de la persona: ",
        "data": None,
        "type": STRING
    },
    "6": {
        "description": "6:- Apellido/s de la pareja de la persona: ",
        "data": None,
        "type": STRING
    },
    "7": {
        "description": "7:- Email de la persona: ",
        "data": None,
        "type": EMAIL
    },
    "8": {
        "description": "8:- Fecha de Nacimiento de la pareja de la persona [dd/mm/yyyy]: ",
        "data": None,
        "type": DATE
    },
    "9": {
        "description": "9:- Fecha de Nacimiento de la persona [dd/mm/yyyy]: ",
        "data": None,
        "type": DATE
    },
    "10": {
        "description": "10:- Compañia de trabajo/empleo: ",
        "data": None,
        "type": STRING
    },
    "11": {
        "description": "11:- Altura de la direccion de la casa de la persona: ",
        "data": None,
        "type": SHORT_INT
    },
    "12": {
        "description": "12:- Calle donde vive la persona: ",
        "data": None,
        "type": STRING
    },
    "13": {
        "description": "13:- Número de teléfono fijo de la persona: ",
        "data": None,
        "type": INT
    },
    "14": {
        "description": "14:- Otros datos relevantes (Colocarlos separados por comas): ",
        "data": None,
        "type": LIST
    }

}

json_password_parameters = {
    "1": {
        "description": "1:- Indique máximo length de las contraseñas: ",
        "data": DEFAULT_MAX_LENGTH,
        "type": SHORT_INT
    },
    "2": {
        "description": "2:- Indique mínimo length de las contraseñas: ",
        "data": DEFAULT_MIN_LENGTH,
        "type": SHORT_INT
    },
    "3": {
        "description": "3:- ¿Desea agregarle caracteres especiales a las contraseñas? [y/N]: ",
        "data": DEFAULT_BOOL_ADD_SPECIALS,
        "type": BOOLEAN
    },
    "4": {
        "description": "4:- ¿Desea generar las contraseñas en modo 1337 (Ejemplo: hola = h01@)? [y/N]: ",
        "data": DEFAULT_BOOL_MODE_1337,
        "type": BOOLEAN
    }
}


def banner_menu():
    print('''{0}    *******************************************************************************************
    *******************************************************************************************
    *****************************  PASSWORD LIST GENERATOR   **********************************
    *******************************************************************************************
    *******************************************************************************************{0}'''.format(RED,
                                                                                                             RESET))
    print()


def menu():
    index = 1
    _menu = ""
    _menu += CYAN
    for option in json_data_options.items():
        _menu += str(option[1]['description'])
        length_of_field_description = len(str(option[1]['description']))
        length_of_field_data = 0
        if option[1]['data'] is not None:
            _menu += YELLOW_BOLD
            _menu += str(option[1]['data'])
            _menu += CYAN
            length_of_field_data = len(str(option[1]['data']))

        total_length = length_of_field_description + length_of_field_data
        if index % 2 == 1:
            if total_length < 30:
                _menu += "\t\t\t\t"
            else:
                _menu += "\t\t"
        else:
            _menu += "\n"
        index += 1

    print(_menu)


def show_password_parameters():
    _parameters = ""
    _parameters += CYAN
    for option in json_password_parameters.items():
        _parameters += str(option[1]['description'])
        _parameters += YELLOW_BOLD
        _parameters += str(option[1]['data'])
        _parameters += CYAN
        _parameters += "\n"

    print(_parameters)


def get_user_input_option():
    try:
        option = input("{0}[+] Ingrese un numero de opcion : {1}".format(DEFAULT, DEFAULT))
        return option
    except KeyboardInterrupt:
        raise KeyboardInterrupt("\n{0}Se interrumpió la ejecución.{1}".format(RED, RED))
    except Exception as e:
        raise e


def get_user_input_data():
    try:
        data = input("{0}[+]: {1}".format(DEFAULT, DEFAULT))
        return data
    except KeyboardInterrupt:
        raise KeyboardInterrupt("\n{0}Se interrumpió la ejecución.{1}".format(RED, RED))
    except Exception as e:
        raise e


def show_prompt_to_input_json_data(option):
    try:
        print(json_data_options[str(option)]['description'])
    except ValueError:
        raise ValueError("La opcion ingresada no existe.")


def show_prompt_to_input_json_parameters(option):
    try:
        print(json_password_parameters[str(option)]['description'])
    except ValueError:
        raise InvalidOptionJsonPasswordParameters("La opcion ingresada no existe.")


# ------------------------------------
# ----------- Validations ------------
# ------------------------------------

def validate_json_data_options(data, option):
    try:
        data_validated = validate(data, option, json_data_options)
        return data_validated
    except ValueError as e:
        raise ValueError(e)


def validate_json_password_parameters(data, option):
    try:
        data_validated = validate(data, option, json_password_parameters)
        return data_validated
    except ValueError as e:
        raise InvalidOptionJsonPasswordParameters(e)


def validate(data, option, json):
    try:
        data_string = str(data)
        if len(data_string) <= 0:
            raise ValueError("No se ingresó nada.")

        _type = json[str(option)]['type']

        if _type == STRING:
            try:
                validated_data = validate_string(data_string)
                return validated_data
            except ValueError as e:
                raise ValueError(e)

        elif _type == INT:
            try:
                validated_data = validate_int(data_string)
                return validated_data
            except ValueError as e:
                raise ValueError(e)

        elif _type == SHORT_INT:
            try:
                validated_data = validate_short_int(data_string)
                return validated_data
            except ValueError as e:
                raise ValueError(e)

        elif _type == EMAIL:
            try:
                validated_data = validate_email(data_string)
                return validated_data
            except ValueError as e:
                raise ValueError(e)

        elif _type == DATE:
            try:
                validated_data = validate_date(data_string)
                return validated_data
            except ValueError as e:
                raise ValueError(e)

        elif _type == LIST:
            entered_list = data_string.split(",")
            cleaned_list = []
            for word in entered_list:
                trimmed_word = str(word).strip().capitalize()
                cleaned_list.append(trimmed_word)

            return cleaned_list

        elif _type == BOOLEAN:
            try:
                validated_data = validate_bool(data_string)
                return validated_data
            except ValueError as e:
                raise ValueError(e)

    except Exception:
        raise ValueError("Error en el dato ingresado.")


def validate_range_of_length():
    if json_password_parameters['1']['data'] < json_password_parameters['2']['data']:
        json_password_parameters['1']['data'] = DEFAULT_MAX_LENGTH
        json_password_parameters['2']['data'] = DEFAULT_MIN_LENGTH


def validate_string(data_string):
    for char in data_string:
        if char.isdigit():
            raise ValueError("Se ingresaron caracteres donde van solo numeros.")
    data_capitalized = ""
    list_data_string = data_string.split(" ")
    for word in list_data_string:
        data_capitalized += word.strip().lower().capitalize()
        data_capitalized += " "

    return data_capitalized


def validate_int(data_string):
    try:
        data_int = int(data_string)
        return data_int
    except ValueError:
        raise ValueError("Se ingresaron palabras donde iban numeros.")


def validate_short_int(data_string):
    if len(data_string) > 5:
        raise ValueError("El numero ingresado es demasiado grande.")
    try:
        data_int = validate_int(data_string)
        return data_int
    except ValueError as e:
        raise ValueError(e)


def validate_email(data_string):
    if not data_string.__contains__('@'):
        raise ValueError("El email debe contener @.")
    else:
        emails, sep, tail = data_string.partition("@")
        if len(emails) < 6:
            raise ValueError("Nombre de Email demasiado corto. Debe superar las 6 letras al menos.")
        return data_string


def validate_date(data_string):
    try:
        datetime.strptime(data_string, "%d/%m/%Y")
        return data_string
    except ValueError:
        raise ValueError("Formato de fecha erroneo.")


def validate_bool(data_string):
    if data_string == "y":
        return True
    elif data_string == "n":
        return False
    else:
        raise ValueError("No se ingresó un bool correcto.")
