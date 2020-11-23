def convert_data_to_save(output, dictionary_dict):
    output_data = ''
    dictionary_data = ''

    for i, j in output:
        output_data += i.__str__() + '\\' + j.__str__() + '\\'
    for key, value in dictionary_dict.items():
        dictionary_data += key.__str__() + '\\' + value.__str__() + '\\'
    return output_data[0:output_data.__len__() - 1], dictionary_data[0:dictionary_data.__len__() - 1]
