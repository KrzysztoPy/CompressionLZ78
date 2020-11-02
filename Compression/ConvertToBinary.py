class ConvertToBinary:

    @staticmethod
    def convert_data_from_string_to_binary(data_compression):
        input_data_converted_to_binary = bin(int.from_bytes(data_compression.encode(), 'big'))[2:]
        input_data_converted_to_binary = ConvertToBinary.adding_zeros(input_data_converted_to_binary)
        return input_data_converted_to_binary

    @staticmethod
    def adding_zeros(input_data_converted_to_binary):
        if input_data_converted_to_binary.__len__() % 8:
            input_data_converted_to_binary = input_data_converted_to_binary[::-1]
            for i in range(0, 8 - (input_data_converted_to_binary.__len__() % 8)):
                input_data_converted_to_binary += '0'
        return input_data_converted_to_binary[::-1]
