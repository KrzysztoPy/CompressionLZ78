from MainMenu.MainMenuGui import MainMenuGui
from TextFromConsole.TextFromConsoleLogic import TextFromConsoleLogic
from Compression.ConvertToBinary import ConvertToBinary


class MainMenuLogic(MainMenuGui, TextFromConsoleLogic):
    actual_load_file = MainMenuGui.nothing_load()

    def menu_lo(self):
        MainMenuGui.option_menu_gui()
        decision = input("\n Choice option: ")

        if decision == 1:
            ConvertToBinary.convert_data_from_string_to_binary(input("Input text which you want compress: "))
