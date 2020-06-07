import numpy as np
import pandas as pd


def read_data_bronnitsy():
    # копка лопатой и хотьба
    # в файле 2lop_12 и 2lop_13 вообще нету записанных каналов 141 (либо сбита нумеровка при записи ,либо еще что-то)
    # fl1='D:\\database_for_kursach\\2013.11.18.Bronnitsy\\'+'pes_8'+'\\'
    fl2 = 'D:\\database_for_kursach\\2013.11.18.Bronnitsy\\' + '2lop_9' + '\\'
    fl3 = 'D:\\database_for_kursach\\2013.11.18.Bronnitsy\\' + '2lop_9' + '\\'
    fl4 = 'D:\\database_for_kursach\\2013.11.18.Bronnitsy\\' + '2lop_9' + '\\'
    fl5 = 'D:\\database_for_kursach\\2013.11.18.Bronnitsy\\' + '2lop_9' + '\\'
    fl6 = 'D:\\database_for_kursach\\2013.11.18.Bronnitsy\\' + '2lop_10' + '\\'
    # fl7='D:\\database_for_kursach\\2013.11.18.Bronnitsy\\'+'2lop_11'+'\\'
    # fl8='D:\\database_for_kursach\\2013.11.18.Bronnitsy\\'+'2lop_12'+'\\'
    fl9 = 'D:\\database_for_kursach\\2013.11.18.Bronnitsy\\' + '2lop_13' + '\\'
    fls = [fl2, fl3, fl4, fl5, fl6, fl9]

    # tt1= 'хотьба'
    tt2 = 'копка'
    tt3 = 'копка'
    tt4 = 'копка'
    tt5 = 'копка'
    tt6 = 'копка'
    # tt7='копка'
    # tt8='копка'
    tt9 = 'копка'
    tts = [tt2, tt3, tt4, tt5, tt6, tt9]

    # ti1='21:22 - 21:26'
    ti2 = '21:27:00 - 21:31:00'
    ti3 = '21:27:00- 21:31:00'
    ti4 = '21:27:00 - 21:31:00'
    ti5 = '21:27:00 - 21:31:00'
    ti6 = '21:26:00 - 21:36:00'  # в файле было указано только одно число 21:31 поэтому возьму+- 5сек для начала
    # ti7='21:32 - 21:34'
    # ti8='21:35 - 21:37'
    ti9 = '21:37:00 - 21:40:00'
    tis = [ti2, ti3, ti4, ti5, ti6, ti9]

    # nk1=-1 #номер канала не указан
    nk2 = 170
    nk3 = 106
    nk4 = 281
    nk5 = 287
    nk6 = 141
    # nk7=141
    # nk8=141
    nk9 = 141
    nks = [nk2, nk3, nk4, nk5, nk6, nk9]

    d = {'filename': fls, 'type_of_target': tts, 'time_interval_of_target': tis, 'nomer_kanala': nks}
    table = pd.DataFrame(data=d)

    for i in range(len(table.values)):
        table.filename[i] += str(table.nomer_kanala[i]) + '.dnew'

    def read_as_binary_file_all_file(filename):
        with open(filename, 'rb') as bytestream:
            buffer = bytestream.read()
            data = np.frombuffer(buffer, dtype=np.uint32).astype(np.uint32)
            bytestream.close
        return data

    tmp_x = []
    for i in range(len(table.values)):
        tmp = read_as_binary_file_all_file(table.filename[i])
        tmp_x.append(tmp)

    table.drop(['filename'], axis='columns', inplace=True)
    table.drop(['nomer_kanala'], axis='columns', inplace=True)

    table['data'] = tmp_x

    neworder = ['data', 'type_of_target', 'time_interval_of_target']
    table = table.reindex(columns=neworder)

    return table