import os
from service import *


def main():
    os.system('clear')
    banner_menu()
    menu()
    print(menu())

    print("{0}Ingrese OK para finalizar de llenar la información.".format(DEFAULT))
    try:
        option = get_user_input_option()
        if str(option).lower() != "ok":
            option = int(option)
            add_data(option)
            # main()
        # else:
    except ValueError:
        main()
    except KeyboardInterrupt as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
