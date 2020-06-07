import numpy as np

def load_briansk(file_path,ot,do):
    fl= file_path
    fls = []
    for i in range(ot,do + 1 ,1): #включительно do
        fls.append(fl + str(i) + '.vtd')

    def read_as_binary_file_all_file(filename):
        with open(filename, 'rb') as bytestream:

            buffer = bytestream.read()
            data = np.frombuffer(buffer, dtype=np.float32).astype(np.float64)
            bytestream.close
        return data

    tmp_x = []
    for i in range(len(fls)):
        tmp_data = read_as_binary_file_all_file(fls[i])
        tmp_x.append(tmp_data)

    tmp_x = np.array(tmp_x)


    #print(np.max(tmp_x), '\n',np.min(tmp_x))
    return tmp_x





def load_bronnitsy(file_path, ot, do):
    fl= file_path
    fls = []
    for i in range(ot,do + 1 ,1): #включительно do
        fls.append(fl + str(i) + '.dnew')

    def read_as_binary_file_all_file(filename):
        with open(filename, 'rb') as bytestream:

            buffer = bytestream.read()
            data = np.frombuffer(buffer, dtype=np.float32).astype(np.float64)
            bytestream.close
        return data

    tmp_x = []
    for i in range(len(fls)):
        tmp_data = read_as_binary_file_all_file(fls[i])
        tmp_x.append(tmp_data)

    tmp_x = np.array(tmp_x)

    # tmp_x = tmp_x[:,19000: ]

    #print(np.max(tmp_x), '\n',np.min(tmp_x))
    return tmp_x