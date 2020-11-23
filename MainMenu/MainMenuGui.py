def give_text_gui():
    return 'Input text which you want compress: '


def option_menu_gui():
    available_action = ('Input text from console.', 'Give path to file.', 'Decompression', 'Exit.')

    for i, option in enumerate(available_action):
        print(i + 1, '.', option)


def give_path_gui():
    return '\nInput path to file which you want compress Example path: C:\\Desktop\\My File\\myTextFile.txt\nPath:'


def enter_path_where_save_output_data_gui():
    return '\nInput path when you want save output data. Example path: C:\\Desktop\\My File \n' \
           'Skip file name and add a \\ character to the end\nPath:'


def file_name_output_txt_gui():
    return '\\output.txt'


def save_output_file_complete_gui():
    return '\nWriting output to file was successful!\n'


def enter_path_where_save_dictionary_data_gui():
    return '\nInput path when you want save dictionary data. Example path: C:\\Desktop\\My File \n' \
           'Skip file name and add a \\ character to the end\nPath:'


def file_name_dictionary_txt_gui():
    return '\\dictionary.txt'


def save_dictionary_file_complete_gui():
    return '\nWriting dictionary to file was successful!\n'


def enter_path_where_save_decompressed_data_gui():
    return '\nInput path when you want save decompressed data. Example path: C:\\Desktop\\My File \n' \
           'Skip file name and add a \\ character to the end\nPath:'


def which_save_to_file_gui():
    print('\nWant save output data and dictionary to file?\n 1.Yes \n 2.No')


def get_output_data_to_decompressed():
    return '\nEnter path to output data to decompressed:\n'


def get_dictionary_data_to_decompressed():
    return '\nEnter path to dictionary data to decompressed:\n'


def which_save_decompressed_file_gui():
    print('\nWant save decompressed data to file?\n 1.Yes \n 2.No')


def file_name_decompressed_txt_gui():
    return '\\decompressed.txt'


def save_decompressed_file_complete_gui():
    return '\nWriting decompressed to file was successful!\n'


def compression_complete_gui():
    return '\nCompression successful!\n'

# Ala ma kota, ma również i pieska. Raka też ma ale o tym nie wie.
#C:\Users\Kriss\Desktop\Testy LZ78