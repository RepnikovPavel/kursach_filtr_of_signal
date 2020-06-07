import os
import numpy as np

def write_data_to_folder_and_metka_to_text(folder_path, metrki_path,target_data,metka):

    #читаем  предыдущий id ( номер сэмпла) если его нет то создаем нулевой id
    path_data = folder_path
    file_with_id1 = open(path_data + "\\unic_tmp_id.txt", "a" )
    if os.stat(path_data + "\\unic_tmp_id.txt").st_size == 0:
        file_with_id1.write("0")
    file_with_id1.close()

    file_with_id2 = open(path_data + "\\unic_tmp_id.txt", "r" )
    id= file_with_id2.read()
    file_with_id2.close()

    #тут запись кусочка дорожки с нужными данными

    np.save( folder_path + "\\" + "sample_" + id, target_data)

    #создаем текстовый файлик и записываем туда метку

    path_metka = metrki_path +"\\metka_" + id + ".txt"
    file_with_metki = open(path_metka , "a")
    file_with_metki.write(metka)
    file_with_metki.close()

    # и в конце увеличиваем id на 1

    tmp_int_id = int(id)
    tmp_int_id += 1
    new_id = str(tmp_int_id)
    file_with_id3= open(path_data + "\\unic_tmp_id.txt", "w" )
    file_with_id3.write(new_id)
    file_with_id3.close()









