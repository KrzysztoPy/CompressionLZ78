from MainMenu.MainMenuGui import MainMenuGui
import Decompression.ConvertDataToListAndDict as ConvertToListAndDict
import Compression.CompressionLZ78 as CompressionLZ78
import OperationOnFile.OperationOnFile as OperationOnFile
import Decompression.Decompression_LZ78 as Decompression

# main_menu_logic = MainMenuLogic()


# main_menu_logic.menu_lo()


output_and_dictionary_dict = [[('0', None), ('1', None), ('0', 0), ('0', 2), ('1', None)],
                              {0: '0', 1: '1', 2: '00', 3: '000'}]

# result = main_menu_logic.save_file_after_compressed(output_and_dictionary_dict)
# result_1, result_2 = Compression.compression_lz78('babcia')

result_1, result_2 = Decompression.decompression_lz78(
    ConvertToListAndDict.convert_to_list(
        OperationOnFile.get_data_from_file_with_split(
            MainMenuGui.get_output_data_to_decompressed(),
            MainMenuGui.file_name_output_txt_gui())),
    ConvertToListAndDict.convert_to_dict(
        OperationOnFile.get_data_from_file_with_split(
            MainMenuGui.get_dictionary_data_to_decompressed(),
            MainMenuGui.file_name_dictionary_txt_gui())))
print(result_1)
print(result_2)

# save_file_after_compressed_test()
