from _collections import OrderedDict
import time
from MainMenu.MainMenuGui import MainMenuGui


def compression_lz78_dict(check_input_data_for_convert):
    ZERO = None
    position = None
    dictionary_dict = dict()
    output = list()
    check_input = ''
    print(check_input_data_for_convert.__len__())
    start_time = time.time()
    for i in range(0, check_input_data_for_convert.__len__()):
        check_input += check_input_data_for_convert[i]
        # dictionary_dict empty
        # if dictionary_dict.__len__() == 0:
        #     dictionary_dict[dictionary_dict.__len__()] = check_input
        #     output.append((check_input, ZERO))
        #     check_input = ''
        # if in dictionary not exist such value
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

    print("--- %s seconds ---" % (time.time() - start_time))
    print("Output len: ", output.__len__())
    print("Dict len: ", dictionary_dict.__len__())
    MainMenuGui.compression_complete_gui()
    return output, dictionary_dict
