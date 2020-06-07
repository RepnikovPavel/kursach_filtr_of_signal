import numpy as np
import os

def write_filtr(vector_of_filtr, path):

    file_with_id1 = open(path + "\\unic_tmp_id.txt", "a")
    if os.stat(path + "\\unic_tmp_id.txt").st_size == 0:
        file_with_id1.write("0")
    file_with_id1.close()

    file_with_id2 = open(path + "\\unic_tmp_id.txt", "r")
    id = file_with_id2.read()
    file_with_id2.close()

    # тут запись кусочка дорожки с нужными данными

    np.save(path + "\\" + "vec_" + id,vector_of_filtr)

    # и в конце увеличиваем id на 1

    tmp_int_id = int(id)
    tmp_int_id += 1
    new_id = str(tmp_int_id)
    file_with_id3= open(path + "\\unic_tmp_id.txt", "w" )
    file_with_id3.write(new_id)
    file_with_id3.close()