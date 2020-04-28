import os
from service import *
from exceptions.exceptions import InvalidOptionJsonPasswordParameters


def main():
    os.system('clear')
    banner_menu()
    menu()

    print("{0}Ingrese OK para finalizar de llenar la información.".format(DEFAULT))
    try:
        option = get_user_input_option()
        if str(option).lower() != "ok":
            option = int(option)
            fill_data(option)
            main()
        else:
            fill_password_parameters()
            # max_length = show_prompt_to_input_max_length()
            # min_length = show_prompt_to_input_min_length()
            # min_length, max_length = validate_range_of_length(min_length, max_length)
            # specials = show_prompt_to_input_add_specials()
            # mode_1337 = show_prompt_to_input_mode_1337()

            # generate_passwords_file(min_length, max_length, specials, mode_1337)

    except ValueError:
        main()
    except KeyboardInterrupt as e:
        print(e)
    except InvalidOptionJsonPasswordParameters:
        fill_password_parameters()
    except Exception as e:
        print(e)


def fill_data(option):
    show_prompt_to_input_json_data(option)
    data_entered_by_user = get_user_input_data()
    data_validated = validate_json_data_options(data_entered_by_user, option)

    json_data_options[str(option)]["data"] = data_validated


def fill_password_parameters():
    try:
        os.system('clear')
        banner_menu()
        print("{0}Si desea seguir completando datos ingrese QUIT sin comillas.{1}".format(DEFAULT, DEFAULT))
        show_password_parameters()
        print("{0}Si desea modificar algun parámetro ingrese un número de opción.{1}".format(DEFAULT, DEFAULT))
        print("{0}Para finalizar, ingrese OK.{1}".format(DEFAULT, DEFAULT))
        option = get_user_input_option()
        if str(option).lower() != "ok":
            if str(option).lower() == "quit":
                main()
            else:
                show_prompt_to_input_json_parameters(option)
                data_entered_by_user = get_user_input_data()
                data_validated = validate_json_password_parameters(data_entered_by_user, option)

                json_password_parameters[str(option)]["data"] = data_validated
                validate_range_of_length()
                fill_password_parameters()
        else:
            banner_menu()
            print()
            print("{0}Generar".format(RESET))
    except InvalidOptionJsonPasswordParameters:
        fill_password_parameters()
    except ValueError:
        fill_password_parameters()


if __name__ == '__main__':
    main()
