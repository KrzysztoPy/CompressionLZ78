import MainMenu.MainMenuGui as MainMenuGui


def save_file(answer, save_data, file_name, success_info):
    while True:
        path = input(answer)
        if not path:
            continue
        try:
            tmp_path = path + file_name
            output_file = (open(tmp_path, "w", encoding='utf-8'))
            output_file.write(save_data)
            output_file.close()

            print(success_info)
            break
        except OSError as error:
            print(f'Writing {file_name} to the file has failed')
            print(f'Type error: ', error)


def simply_get_data_from_file_to_convert():
    while True:
        path = input(MainMenuGui.give_path_gui())
        try:
            return (open(path, "r", encoding='utf-8')).read()
        except OSError as error:
            print('\n', error)


def get_data_from_file_with_split(answer, file_name):
    path = input(answer)
    try:
        tmp_path = path + file_name
        output_file = (open(tmp_path, "r", encoding='utf-8'))
        output_data_from_file = output_file.read()
        output_file.close()

        return output_data_from_file.split('\\')

    except OSError as error:
        print(error)


# def save_file_after_compressed(output_and_dictionary_dict):
#     while True:
#         path = input(MainMenuGui.file_path_for_compressed_data_gui())
#         if not path:
#             continue
#         try:
#             tmp_path = path + MainMenuGui.file_name_output_txt_gui()
#             output_file = (open(tmp_path, "w", encoding='utf-8'))
#             output_file.write(output_and_dictionary_dict[0].__str__())
#             output_file.close()
#
#             tmp_path = path + "dx2"
#             dict_file = (open(tmp_path, "w", encoding='utf-8'))
#             dict_file.write(output_and_dictionary_dict[1].__str__())
#             dict_file.close()
#
#             MainMenuGui.save_output_file_complete_gui()
#             break
#         except OSError as error:
#             print(error)
#
#
# def save_file_after_decompressed(decompressed_data):
#     while True:
#         path = input(MainMenuGui.enter_path_where_save_output_data_gui())
#         if not path:
#             continue
#         try:
#             tmp_path = path + MainMenuGui.file_name_output_txt_gui()
#             output_file = (open(tmp_path, "w", encoding='utf-8'))
#             output_file.write(decompressed_data)
#             output_file.close()
#
#             MainMenuGui.save_output_file_complete_gui()
#             break
#         except OSError as error:
#             print(error)
#
#
# def get_data_from_output_data():
#     path = input(MainMenuGui.get_output_data_to_decompressed())
#     try:
#         tmp_path = path + MainMenuGui.file_name_output_txt_gui()
#         output_file = (open(tmp_path, "r", encoding='utf-8'))
#         output_data_from_file = output_file.read()
#         output_file.close()
#
#         return output_data_from_file.split(',')
#
#     except OSError as error:
#         print(error)
#
#
# def get_data_from_dictionary():
#     path = input(MainMenuGui.get_dictionary_data_to_decompressed())
#     try:
#         tmp_path = path + MainMenuGui.file_name_dictionary_txt_gui()
#         dictionary_file = (open(tmp_path, "r", encoding='utf-8'))
#         dictionary_from_file = dictionary_file.read()
#         dictionary_file.close()
#         return dictionary_from_file.split(',')
#
#     except OSError as error:
#         print(error)
#
#
# def save_decompressed_data_to_file(decompressed_data):
#     while True:
#         path = input(MainMenuGui.enter_path_where_save_output_data_gui())
#         if not path:
#             continue
#         try:
#             tmp_path = path + MainMenuGui.name_file_with_decompressed_data_gui()
#             output_file = (open(tmp_path, "w", encoding='utf-8'))
#             output_file.write(decompressed_data)
#             output_file.close()
#
#             MainMenuGui.save_output_file_complete_gui()
#             break
#         except OSError as error:
#             print(error)


def save_statistic_to_file(self):
    statistic_file = 'C:\\Users\\Kriss\\Desktop\\Ojciec\\statistic.txt'
    file = None
    try:
        file = open(statistic_file, 'w', encoding='utf-8')
        for i in self.results:
            for j in i:
                file.write((j.__str__()) + '\n')
            file.write('\n')
    except IOError as e:
        print(e)
    finally:
        file.close()
    print('END!!!')
