class CompressionLZ78:
    ZERO = None

    def __init__(self, copy_binary_data):
        self.copy_binary_data = copy_binary_data

    dictionary = []

    def compression_lz78(self):
        actual_choice_object = ''
        last_position = None
        for i in range(0, self.copy_binary_data):
            actual_choice_object += self.copy_binary_data[i]
            if actual_choice_object not in self.dictionary:
                self.dictionary.append(actual_choice_object, self.ZERO)
                actual_choice_object = ''
            elif actual_choice_object in self.dictionary:
                actual_choice_object, last_position = actual_choice_object, self.dictionary.index(
                    self.copy_binary_data[i])
