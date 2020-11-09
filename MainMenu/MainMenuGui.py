class MainMenuGui:
    AVAILABLE_ACTION = ('Input text from console.', 'Give path to file.', 'Decompression', 'Exit.')
    empty_path = 'Actual load path: Empty'

    def nothing_load(self):
        return self.empty_path

    def option_menu_gui(self):
        print('\n', self.nothing_load(), '\n')
        for i, option in enumerate(self.AVAILABLE_ACTION):
            print(i + 1, '.', option)

    def option_for_choice_gui(self):
        return self.AVAILABLE_ACTION

    def actual_load_file_gui(self):
        pass
