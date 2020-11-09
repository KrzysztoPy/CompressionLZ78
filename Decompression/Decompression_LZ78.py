def decompression_lz78(output_data, dictionary):
    decompressed_data = ''
    for value, position in output_data:
        if position is not None:
            decompressed_data += (value + dictionary.get(position))
            position = None
        else:
            decompressed_data += value
    print('Should be: ', '01000001', 'My lz78: ', decompressed_data)