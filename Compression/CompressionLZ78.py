class CompressionLZ78:

    def __init__(self, copy_binary_data):
        self.copy_binary_data = copy_binary_data


    def compression_lz78(self):
        ZERO = None
        dictionary = []
        actual_choice_object = ''
        last_position = None
        for i in range(0, self.copy_binary_data):
            actual_choice_object += self.copy_binary_data[i]
            if actual_choice_object not in dictionary:
                dictionary.append(actual_choice_object, ZERO)
                actual_choice_object = ''
            elif actual_choice_object in dictionary:
                actual_choice_object, last_position = actual_choice_object, dictionary.index(
                    copy_binary_data[i])
