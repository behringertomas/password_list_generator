RED, WHITE, CYAN, GREEN, DEFAULT = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m', '\033[0m'

# ------------------------------------
# -- Data Types Available for Input --
# ------------------------------------

STRING = "String"
INT = "int"
SHORT_INT = "short_int"
EMAIL = "Email"
DATE = "Date"
LIST = "List"


json_data_options = {
    "1": {
        "description": "1:- Nombre de la persona",
        "data": None,
        "type": STRING
    },
    "2": {
        "description": "2:- Celular de la persona",
        "data": None,
        "type": INT
    },
    "3": {
        "description": "3:- Apellido de la persona",
        "data": None,
        "type": STRING
    },
    "4": {
        "description": "4:- Nombre de la pareja de la persona",
        "data": None,
        "type": STRING
    },
    "5": {
        "description": "5:- Apodo de la persona",
        "data": None,
        "type": STRING
    },
    "6": {
        "description": "6:- Apellido de la pareja de la persona",
        "data": None,
        "type": STRING
    },
    "7": {
        "description": "7:- Email de la persona",
        "data": None,
        "type": EMAIL
    },
    "8": {
        "description": "8:- Fecha de Nacimiento de la pareja de la persona [dd/mm/yyyy]",
        "data": None,
        "type": DATE
    },
    "9": {
        "description": "9:- Fecha de Nacimiento de la persona [dd/mm/yyyy]",
        "data": None,
        "type": DATE
    },
    "10": {
        "description": "10:- Compañia de trabajo/empleo",
        "data": None,
        "type": STRING
    },
    "11": {
        "description": "11:- Altura de la direccion de la casa de la persona",
        "data": None,
        "type": SHORT_INT
    },
    "12": {
        "description": "12:- Calle donde vive la persona",
        "data": None,
        "type": STRING
    },
    "13": {
        "description": "13:- Otros datos relevantes (Colocarlos separados por comas)",
        "data": None,
        "type": LIST
    }

}


def banner_menu():
    print('''{0}    *******************************************************************************************
    *******************************************************************************************
    *****************************  PASSWORD LIST GENERATOR   **********************************
    *******************************************************************************************
    *******************************************************************************************{1}'''.format(RED, CYAN))


def menu():
    index = 1
    menu = ""
    for option in json_data_options.items():
        menu += option[1]['description']
        if index % 2 == 1:
            if len(str(option[1]['description'])) < 28:
                menu += "\t\t\t\t\t\t"
            else:
                menu += "\t\t\t"
        else:
            menu += "\n"
        index += 1

    return menu


def get_user_input():
    try:
        option = input("{0}[+] Ingrese un numero de opcion : {1}".format(DEFAULT, DEFAULT))
        return option
    except KeyboardInterrupt:
        raise KeyboardInterrupt("\n{0}Se interrumpió la ejecución.{1}".format(RED, RED))
    except Exception as e:
        raise e


def add_data(option):
    try:
        print(json_data_options[str(option)]['description'])
    except ValueError:
        raise ValueError("La opcion ingresada no existe.")
