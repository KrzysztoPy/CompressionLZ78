import Decompression.ConvertDataToListAndDict as ConvertToListAndDict
import OperationOnFile.OperationOnFile as OperationOnFile
import Decompression.Decompression_LZ78 as Decompression


def convert_to_list_and_dict_test():
    output = ['b', None, 'a', None, 'c', '0', 'i', None, 'a', None]
    dictionary = ['0', 'b', '1', 'a', '2', 'bc', '3', 'i']

    result = Decompression.decompression_lz78(
                    ConvertToListAndDict.convert_to_list(OperationOnFile.get_data_from_file_with_split()),
                    ConvertToListAndDict.convert_to_dict(OperationOnFile.get_data_from_dictionary()))
    print(result)
    assert 'babcia' == result


convert_to_list_and_dict_test()
