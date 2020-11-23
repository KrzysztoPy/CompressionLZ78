def decompression_lz78(output_data, dictionary):
    decompressed_data = ''
    for tuples in output_data:
        for i in range(0, tuples.__len__(), 2):
            if tuples[i + 1] == 'None':
                decompressed_data += tuples[i]
            else:
                decompressed_data += dictionary.get(int(tuples[i + 1])) + tuples[i]

    return decompressed_data
