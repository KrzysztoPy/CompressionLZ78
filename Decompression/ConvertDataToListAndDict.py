def convert_to_list(output_data, ):
    convert_output_data = list()

    for i in range(0, output_data.__len__(), 2):
        convert_output_data.append((output_data[i], output_data[i + 1]))
    return convert_output_data


def convert_to_dict(dictionary):
    convert_dictionary = dict()

    for i in range(0, dictionary.__len__(), 2):
        convert_dictionary[int(dictionary[i])] = dictionary[i + 1]

    return convert_dictionary
