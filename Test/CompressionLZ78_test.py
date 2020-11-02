from Compression import CompressionLZ78
from Compression import ConvertToBinary

sample = 'aa_bbb_cccc_ddddd_ee'


def compression_lz78_test():
    result = CompressionLZ78.CompressionLZ78(ConvertToBinary.convert_data_from_string_to_binary(sample))


compression_lz78_test()
