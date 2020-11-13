from MainMenu.MainMenuGui import MainMenuGui
import Compression.ConvertToBinary as ConvertToBinary
import Compression.CompressionLZ78 as CompressionLZ78


class MainMenuLogic:
    main_menu_gui = MainMenuGui()
    actual_load_file = main_menu_gui.nothing_load()

    def menu_lo(self):
        while True:
            self.main_menu_gui.option_menu_gui()
            decision = input("\n Choice option: ")

            if decision == '1':
                CompressionLZ78.compression_lz78_dict(
                    ConvertToBinary.convert_data_from_string_to_binary(
                        input(MainMenuGui.give_text_gui())))
            elif decision == '2':
                # self.save_file_after_compressed(
                #     CompressionLZ78.compression_lz78_dict(
                #         ConvertToBinary.convert_data_from_string_to_binary(
                #             self.open_path_file_to_convert()), None))

                self.save_file_after_compressed(
                    CompressionLZ78.compression_lz78_dict(
                        self.open_path_file_to_convert()))

            elif decision == '4':
                exit()

    def open_path_file_to_convert(self):
        while True:
            path = input(MainMenuGui.give_path_gui())
            try:
                return (open(path, "r", encoding='utf-8')).read()
            except OSError as error:
                print('\n', error)

    def save_file_after_compressed(self, output_and_dictionary_dict):
        while True:
            path = input(MainMenuGui.file_path_for_compressed_data_gui())
            if not path:
                continue
            try:
                tmp_path = path + MainMenuGui.name_file_with_data_output_after_compressed_gui()
                output_file = (open(tmp_path, "w", encoding='utf-8'))
                output_file.write(output_and_dictionary_dict[0].__str__())
                output_file.close()

                tmp_path = path + MainMenuGui.name_file_with_data_compressed_dictionary_gui()
                dict_file = (open(tmp_path, "w", encoding='utf-8'))
                dict_file.write(output_and_dictionary_dict[1].__str__())
                dict_file.close()

                MainMenuGui.save_file_complete_gui()
                break

            except OSError as error:
                print(error)


main_menu = MainMenuLogic()
main_menu.menu_lo()
