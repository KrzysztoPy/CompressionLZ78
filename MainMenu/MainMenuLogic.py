from MainMenu.MainMenuGui import MainMenuGui
from TextFromConsole.TextFromConsoleLogic import TextFromConsoleLogic
import Compression.ConvertToBinary
# import Compression.ConvertToBinary
from Compression.CompressionLZ78 import CompressionLZ78


class MainMenuLogic(TextFromConsoleLogic):
    main_menu_gui = MainMenuGui()
    actual_load_file = main_menu_gui.nothing_load()

    def menu_lo(self):
        self.main_menu_gui.option_menu_gui()
        decision = input("\n Choice option: ")

        if decision == 1:
            Compression.ConvertToBinary.convert_data_from_string_to_binary(
                input("Input text which you want compress: "))
            # CompressionLZ78(
            #     ConvertToBinary.convert_data_from_string_to_binary(input("Input text which you want compress: ")))


main_menu = MainMenuLogic()
main_menu.menu_lo()
