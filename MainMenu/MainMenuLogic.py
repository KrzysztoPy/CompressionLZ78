from MainMenu.MainMenuGui import MainMenuGui
import Compression.ConvertToBinary as ConvertToBinary
import Compression.CompressionLZ78 as CompressionLZ78


class MainMenuLogic:
    main_menu_gui = MainMenuGui()
    actual_load_file = main_menu_gui.nothing_load()

    def menu_lo(self):
        self.main_menu_gui.option_menu_gui()
        decision = input("\n Choice option: ")

        if decision == '1':
            CompressionLZ78.compression_lz78_dict(ConvertToBinary.convert_data_from_string_to_binary(
                input("Input text which you want compress: ")))
        if decision == '2':
            path = input("Input path to file which you want compress: ")
            data_to_compress = None
            try:
                data_to_compress = (open(path, "r")).read()
            except OSError as error:
                print(error)
            print(data_to_compress)
            CompressionLZ78.compression_lz78_dict(ConvertToBinary.convert_data_from_string_to_binary(
                data_to_compress))


main_menu = MainMenuLogic()
main_menu.menu_lo()
