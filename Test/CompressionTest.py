import time

from Compression.ConvertToBinary import ConvertToBinary

# x = open('OjciecChrzestny.txt', 'r', encoding='utf-16')
# data_for_convert = x.read()
data_for_convert = input("Input text which you want compress: ")


class FormatConvertedBin:
    diff_1 = 0

    def my_bin_converter(self, data_for_convert):
        start = int(round(time.time() * 1000))
        converted_data = ''
        for i in range(0, data_for_convert.__len__()):
            converted_data += '{0:08b}'.format(int.from_bytes(data_for_convert[i].encode(), 'big'))
        stop = int(round(time.time() * 1000))
        self.diff_1 = stop - start
        return converted_data


def convert_data_from_string_to_binary_test():
    format_converted_bin = FormatConvertedBin()

    result = ConvertToBinary.convert_data_from_string_to_binary(data_for_convert)
    result_1 = format_converted_bin.my_bin_converter(data_for_convert)

    # print('Time bin solution: ', compression_lz78.diff)
    # print('Time format solution: ', format_converted_bin.diff_1)
    print(result)
    print(result_1)

    assert result == result_1


convert_data_from_string_to_binary_test()
