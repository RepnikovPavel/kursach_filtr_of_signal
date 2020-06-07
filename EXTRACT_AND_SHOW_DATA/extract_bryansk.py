import numpy as np
import pandas as pd


def read_data_bryansk():
    class example(object):
        def __init__(self, type_of_target, time_of_interaction, channels_list, filename):

            self.tt = type_of_target
            self.time = time_of_interaction
            self.channels = channels_list
            self.fl = filename

        def preparing_example(self):
            N = len(self.channels)

            fls = []
            for i in range(N):
                fls.append(self.fl + str(self.channels[i]) + '.vtd')

            tts = [self.tt] * N

            tis = [self.time] * N
            nks = self.channels

            # d = {'filename': fls, 'type_of_target': tts, 'time_interval_of_target': tis, 'nomer_kanala': nks}
            d = {'filename': fls, 'type_of_target': tts, 'time_interval_of_target': tis}
            return d

    fl = 'D:\\database_for_kursach\\bryansk_2011_04_14\\data\\'

    list11 = list(range(468, 489, 1))
    list12 = list(range(804, 825, 1))
    channel_list1 = list11 + list12
    time1 = '13:48:16-13:49:23'
    tt1 = 'хотьба'

    list21 = list(range(468, 485, 1))
    list22 = list(range(807, 824, 1))
    channel_list2 = list21 + list22
    time2 = '13:49:58-13:50:55'
    tt2 = 'хотьба'

    channel_list3 = [668, 623]
    time3 = '13:52:42-13:56:14'
    tt3 = 'копка'

    channel_list4 = [668, 623]
    time4 = '13:44:29-13:48:32'
    tt4 = 'копка'

    list51 = list(range(670, 678, 1))
    list52 = list(range(614, 622, 1))
    channel_list5 = list51 + list52
    time5 = '13:41:41-13:42:09'
    tt5 = 'хотьба'

    channel_list6 = [621, 669]
    time6 = '13:37:56-13:41:07'
    tt6 = 'копка'

    channel_list7 = list(range(498, 504, 1))
    time7 = '13:25:14-13:25:30'
    tt7 = 'хотьба'

    a1 = example(tt1, time1, channel_list1, fl)
    x1 = pd.DataFrame(a1.preparing_example())

    a2 = example(tt2, time2, channel_list2, fl)
    x2 = pd.DataFrame(a2.preparing_example())

    a3 = example(tt3, time3, channel_list3, fl)
    x3 = pd.DataFrame(a3.preparing_example())

    a4 = example(tt4, time4, channel_list4, fl)
    x4 = pd.DataFrame(a4.preparing_example())

    a5 = example(tt5, time5, channel_list5, fl)
    x5 = pd.DataFrame(a5.preparing_example())

    a6 = example(tt6, time6, channel_list6, fl)
    x6 = pd.DataFrame(a6.preparing_example())

    a7 = example(tt7, time7, channel_list7, fl)
    x7 = pd.DataFrame(a7.preparing_example())

    table = pd.concat([x1, x2, x3, x4, x5, x6, x7], ignore_index=True)

    def read_as_binary_file_all_file(filename):
        with open(filename, 'rb') as bytestream:
            buffer = bytestream.read()
            data = np.frombuffer(buffer, dtype=np.uint32).astype(np.uint32)
            bytestream.close
        return data

    tmp_x = []
    for i in range(len(table.values)):
        tmp_data = read_as_binary_file_all_file(table.values[i][0])
        tmp_x.append(tmp_data)


    table.drop(['filename'], axis='columns', inplace=True)
    table['data'] = tmp_x

    neworder = ['data', 'type_of_target', 'time_interval_of_target']
    table = table.reindex(columns=neworder)

    return table
