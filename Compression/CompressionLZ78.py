from _collections import OrderedDict


def compression_lz78_dict(check_input_data_for_convert):
    ZERO = None
    position = None
    dictionary_dict = dict()
    output = list()
    check_input = ''

    for i in range(0, check_input_data_for_convert.__len__()):
        check_input += check_input_data_for_convert[i]
        # dictionary_dict empty
        if dictionary_dict.__len__() == 0:
            dictionary_dict[dictionary_dict.__len__()] = check_input
            output.append((check_input, ZERO))
            check_input = ''
        # if in dictionary not exist such value
        elif check_input not in dictionary_dict.values():
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

    # decompression_lz78(output, dictionary_dict)
    return output, dictionary_dict
