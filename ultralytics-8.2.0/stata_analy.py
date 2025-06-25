from collections import OrderedDict

# *****************parameters*********************
Baud_list = {1: 4800, 2: 9600, 3: 14400, 4: 19200, 5: 38400, 6: 57600, 7: 115200}
Parity_list = {1: "None", 2: "Odd", 3: "EVEN"}
Stop_bit_list = {1: "1", 2: "2", 3: "1.5", 4: "0.5"}


# ********************************************************
# Description:根据LED的ON/OFF值解析出ASCII码，分隔符为FF+'0'
# Param   IN : binary_string,二进制ASCII码，LED ON/OFF状态
# Return     : 去重之后的通讯参数列表
# ********************************************************
def parse_ascii_binary_with_ff_separator(binary_list_IN):
    binary_string = ''.join([str(item) for item in binary_list_IN])
    # print(binary_string)
    # 结果字符串列表
    ascii_chars = []
    # 分隔符FF+'0'
    delimiter = "111111110"
    values = binary_string.split(delimiter)[1:-1]  # 舍弃掉第一个值和最后一个值
    binary_list = ['0' + value for value in values]  # 在每个值的最左端添加'0'
    # print(binary_list)
    filtered_values = [value for value in binary_list if len(value) % 8 == 0]  # 舍去非8的整数倍的值
    for binary_str in filtered_values:
        # 将二进制字符串拆分为8bit
        binary_chunks = [binary_str[i:i + 8] for i in range(0, len(binary_str), 8)]
        # 将每个8bit数据转成ASCII码，组合成结果字符串
        ascii_char = ''.join([chr(int(chunk, 2)) for chunk in binary_chunks])
        # print(ascii_char)
        # 如果第一个字母是S，则为Slave ID
        if ascii_char[0] == 'S' and len(ascii_char) == 4:
            try:
                slave_id = ascii_char[1:]
            except ValueError:
                slave_id = ascii_char[1:] + "-Unknown value"
            ascii_chars.append(f"Slave_ID: {slave_id}")
        # 如果第一个字母是B，则为Baud_rate
        elif ascii_char[0] == 'B' and len(ascii_char) == 2:
            try:
                Param_key_value = int(ascii_char[1:])
                Param_key = Baud_list.get(Param_key_value, f"{Param_key_value}-Unknown Baud Rate")
            except ValueError:
                Param_key = ascii_char[1:] + "-Unknown Baud Rate"
            ascii_chars.append(f"Baud_rate: {Param_key}")
        # 如果第一个字母是P，则为Parity
        elif ascii_char[0] == 'P' and len(ascii_char) == 2:
            try:
                Param_key_value = int(ascii_char[1:])
                Param_key = Parity_list.get(Param_key_value, f"{Param_key_value}-Unknown Parity")
            except ValueError:
                Param_key = ascii_char[1:] + "-Unknown Parity"
            ascii_chars.append(f"Parity: {Param_key}")
        # 如果第一个字母是D，则为Stop_bits
        elif ascii_char[0] == 'D' and len(ascii_char) == 2:
            try:
                Param_key_value = int(ascii_char[1:])
                Param_key = Stop_bit_list.get(Param_key_value, f"{Param_key_value}-Unknown Stop Bits")
            except ValueError:
                Param_key = ascii_char[1:] + "-Unknown Stop Bits"
            ascii_chars.append(f"Stop_bits: {Param_key}")
        else:
            ascii_chars.append(ascii_char + "-Unknown Data Type")
    # 返回结果去重，不改变原数据的次序
    unique_results = list(OrderedDict.fromkeys(ascii_chars))
    return unique_results

if __name__ =='__main__':
    com_247_19200_EVEN_1= [0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0,
                      1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1,
                      0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0,
                      1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0,
                      1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1]
    com_10__4800_Odd_2 = [1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0,
              0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1,
              1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0,
              0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,
              1, 0, 0, 1, 1, 0, 0]
    com_5_115200_None_05 = [1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1,
                            0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1,
                            1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0,
                            0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0,
                            1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    result = parse_ascii_binary_with_ff_separator(com_5_115200_None_05)
    print(result)