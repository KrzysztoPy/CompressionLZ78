from MainMenu.MainMenuLogic import MainMenuLogic

main_menu_logic = MainMenuLogic()
# main_menu_logic.menu_lo()


def save_file_after_compressed_test():
    output_and_dictionary_dict = [[('0', None), ('1', None), ('0', 0), ('0', 2), ('1', None)],
                                  {0: '0', 1: '1', 2: '00', 3: '000'}]

    result = main_menu_logic.save_file_after_compressed(output_and_dictionary_dict)


save_file_after_compressed_test()
