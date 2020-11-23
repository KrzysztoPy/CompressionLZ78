import MainMenu.MainMenuGui as MainMenuGui
import Compression.ConvertDataToSave as ConvertDataToSave
import time


def compression_lz78(check_input_data_for_convert):
    ZERO = None
    position = None
    dictionary_dict = dict()
    output = list()
    check_input = ''
    # print(check_input_data_for_convert.__len__())
    start_time = time.time()
    results = list()
    for i in range(0, check_input_data_for_convert.__len__()):
        check_input += check_input_data_for_convert[i]
        # dictionary_dict empty
        if check_input not in dictionary_dict.values():
            # which have remembered value
            if position is None:
                dictionary_dict[dictionary_dict.__len__()] = check_input
                output.append((check_input, ZERO))
                check_input = ''
            else:
                dictionary_dict[dictionary_dict.__len__()] = check_input
                output.append((check_input[-1], position))
                check_input = ''
                position = None
        else:
            if i < check_input_data_for_convert.__len__() - 1:
                position = [key for key, value in dictionary_dict.items() if check_input == value]
                position = int(position[0])
            # if remembered value is last value in the converted string
            elif i == check_input_data_for_convert.__len__() - 1:
                output.append((check_input, ZERO))

        # results.append(['Count: %s' % check_input_data_for_convert.__len__(),
        #                 "--- %s seconds ---" % (time.time() - start_time),
        #                 "Output len: %i" % output.__len__(),
        #                 "Dict len: %i" % dictionary_dict.__len__()])
    MainMenuGui.compression_complete_gui()
    output, dictionary_dict = ConvertDataToSave.convert_data_to_save(output, dictionary_dict)
    return output, dictionary_dict
