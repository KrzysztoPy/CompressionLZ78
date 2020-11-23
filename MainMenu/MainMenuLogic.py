from MainMenu.MainMenuGui import MainMenuGui
import Decompression.ConvertDataToListAndDict as ConvertToListAndDict
import Compression.CompressionLZ78 as CompressionLZ78
import OperationOnFile.OperationOnFile as OperationOnFile
import Decompression.Decompression_LZ78 as Decompression


class MainMenuLogic:
    main_menu_gui = MainMenuGui()

    def menu_lo(self):
        while True:
            self.main_menu_gui.option_menu_gui()
            decision = input("\n Choice option: ")

            if decision == '1':
                output_data, dictionary = CompressionLZ78.compression_lz78(
                    input(self.main_menu_gui.give_text_gui()))
                while True:
                    MainMenuGui.which_save_to_file_gui()
                    decision = input("\n Choice option: ")
                    if decision == '1':
                        OperationOnFile.save_file(MainMenuGui.enter_path_where_save_output_data_gui(), output_data,
                                                  MainMenuGui.file_name_output_txt_gui(),
                                                  MainMenuGui.save_output_file_complete_gui)
                        OperationOnFile.save_file(MainMenuGui.enter_path_where_save_dictionary_data_gui(), dictionary,
                                                  MainMenuGui.file_name_dictionary_txt_gui(),
                                                  MainMenuGui.save_dictionary_file_complete_gui)
                        break
                    if decision == '2':
                        break
            elif decision == '2':
                output_data, dictionary = CompressionLZ78.compression_lz78(
                    OperationOnFile.simply_get_data_from_file_to_convert())

                OperationOnFile.save_file(MainMenuGui.enter_path_where_save_output_data_gui(), output_data,
                                          MainMenuGui.file_name_output_txt_gui(),
                                          MainMenuGui.save_output_file_complete_gui())
                OperationOnFile.save_file(MainMenuGui.enter_path_where_save_dictionary_data_gui(), dictionary,
                                          MainMenuGui.file_name_dictionary_txt_gui(),
                                          MainMenuGui.save_dictionary_file_complete_gui())
            elif decision == '3':
                decompressed_data = Decompression.decompression_lz78(
                    ConvertToListAndDict.convert_to_list(
                        OperationOnFile.get_data_from_file_with_split(
                            MainMenuGui.get_output_data_to_decompressed(),
                            MainMenuGui.file_name_output_txt_gui())),
                    ConvertToListAndDict.convert_to_dict(
                        OperationOnFile.get_data_from_file_with_split(
                            MainMenuGui.get_dictionary_data_to_decompressed(),
                            MainMenuGui.file_name_dictionary_txt_gui())))
                while True:
                    MainMenuGui.which_save_decompressed_file_gui()
                    decision = input("\n Choice option: ")
                    if decision == '1':
                        OperationOnFile.save_file(MainMenuGui.enter_path_where_save_decompressed_data_gui(),
                                                  decompressed_data, MainMenuGui.file_name_decompressed_txt_gui(),
                                                  MainMenuGui.save_decompressed_file_complete_gui())
                        break
                    if decision == '2':
                        break
            elif decision == '4':
                exit()

main_menu = MainMenuLogic()
main_menu.menu_lo()
