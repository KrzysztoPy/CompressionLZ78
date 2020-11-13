class MainMenuGui:

    @staticmethod
    def give_text_gui():
        return 'Input text which you want compress: '

    @staticmethod
    def nothing_load():
        return 'Actual load path: Empty'

    @staticmethod
    def option_menu_gui():
        available_action = ('Input text from console.', 'Give path to file.', 'Decompression', 'Exit.')

        print('\n', MainMenuGui.nothing_load(), '\n')
        for i, option in enumerate(available_action):
            print(i + 1, '.', option)

    def actual_load_file_gui(self):
        pass

    @staticmethod
    def give_path_gui():
        return '\nInput path to file which you want compress\nExample path: C:\\Desktop\\My File\\myTextFile.txt\nPath:'

    @staticmethod
    def file_path_for_compressed_data_gui():
        return '\nInput path when you want save compressed data.\nExample path: C:\\Desktop\\My File \n' \
               'Skip file name and add a \\ character to the end\nPath:'

    @staticmethod
    def name_file_with_data_compressed_dictionary_gui():
        return '\\dictionary.txt'

    @staticmethod
    def name_file_with_data_output_after_compressed_gui():
        return '\\output.txt'

    @staticmethod
    def compression_complete_gui():
        print('\nCompression LZ78 complete!\n')

    @staticmethod
    def save_file_complete_gui():
        return '\nSave the output and the dictionary as a txt file to the indicated location!'
