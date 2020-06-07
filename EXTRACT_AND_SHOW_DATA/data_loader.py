import extract_bronnitsy
import extract_bryansk

import pandas as pd
import numpy as np


class main_class(object):

    def __init__(self):
        self.data1 = extract_bronnitsy.read_data_bronnitsy()  # тут 6
        self.data2 = extract_bryansk.read_data_bryansk()  # тут 104
        self.data = pd.concat([self.data1, self.data2], ignore_index=True)
        self.samples = []

    def fill_samples(self):
        class sample(object):
            def __init__(self, data_tt_time):
                self.data = data_tt_time[0]
                self.mark = data_tt_time[1]
                self.time = data_tt_time[2]
                self.i1 = 0
                self.i2 = 0
                self.target_data = []

            def prepare_sample(self):  # запись начинается с нулевого моента времени

                RATE = 1000

                s1, s2 = self.time.split("-")
                m1, s1, ms1 = s1.split(":")
                m2, s2, ms2 = s2.split(":")
                t1 = np.float16(m1) * 60 + np.float16(s1) + np.float16(ms1) / 100
                t2 = np.float16(m2) * 60 + np.float16(s2) + np.float16(ms2) / 100
                i_begin = np.uint64(np.around(RATE * t1))
                i_end = np.uint64(np.around(RATE * t2))
                self.i1 = i_begin
                self.i2 = i_end
                self.target_data = self.data[self.i1:self.i2]

        # пока обрабатываю только брянск
        for i in range(len(self.data2.values)):
            tmp = sample(self.data2.loc[i])
            tmp.prepare_sample()
            self.samples.append(tmp)
