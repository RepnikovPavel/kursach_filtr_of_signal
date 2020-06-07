import os
import numpy as np

# self.samples, self.labels = load_all_samples_and_labels(data_path, metki_path)
def load_all_samples_and_labels(data_path, metki_path): #так как данных мало, то никаких batches и онлайн подгрузки данных не будет. просто грузим все разом

    #все выполняется только если что-то записано:
    # if os.stat(data_path).st_size != 0 and  os.stat(metki_path).st_size != 0:

    #читаем  id

    file_with_id = open(data_path + "\\unic_tmp_id.txt", "r" )
    id= file_with_id.read()
    file_with_id.close()
    tmp_int_id =  int(id)

    number_of_samples = tmp_int_id #в штуках

    tmp_list= []

    for i in range(number_of_samples):
        tmp_list.append(np.load(data_path + "\\sample_"+str(i)+".npy"))

    samples= np.array(tmp_list)

    #теперь грузим метки:

    list_with_labels = []

    for i in range(number_of_samples):
        tmp_file_with_metka = open(metki_path + "\\metka_" + str(i) +".txt","r")
        tmp_metka = tmp_file_with_metka.read()
        list_with_labels.append(tmp_metka)
        tmp_file_with_metka.close()

    return samples , list_with_labels















