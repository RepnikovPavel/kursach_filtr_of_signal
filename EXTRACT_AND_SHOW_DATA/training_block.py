import tensorflow as tf
from tensorflow.python.ops.signal.fft_ops import fft, ifft
#
import numpy as np
from write_filtr2file import *
import time

from matplotlib.backends.backend_pdf import PdfPages

def training(samples, labels, canvas):
    shape_1 = np.shape(samples)[0]
    shape_2 = np.shape(samples)[1]

    for i in range(len(labels)):
        labels[i] = int(labels[i])

    labels = np.array(labels, dtype=np.float32)
    np.reshape(labels, (shape_1, 1))

    tf.compat.v1.disable_eager_execution()

    # задание тренируемого значения V и вычислительного графа.
    # обратите внимание, что вычисления фурье образа должно идти по строкам, т.к на входе матрица их сэмплов(батч)

    # задаем "веса"
    V = tf.Variable(shape_2 * [1.0], dtype=tf.float32, name="filtr_vector", trainable=True)

    # задаем вход x и выход output с вычислительным узлом tf.norm(...)

    batch_size = 16
    # зададим датасет в виде списка, чтобы было удобно его перемешивать

    x = tf.compat.v1.placeholder(tf.float32, [batch_size, shape_2], "data")

    output = tf.norm(tf.abs(ifft(tf.multiply(fft(tf.complex(x / tf.norm(x, axis=0), 0.)), tf.complex(V, 0.)))),
                     axis=1) / tf.norm(x)

    # задаем столбец меток для бача и функцию ошибки
    target = tf.compat.v1.placeholder(tf.float32, batch_size, "labels")
    cost = tf.reduce_mean(tf.pow(tf.pow(output, 2) - target, 2))

    optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.1)

    gvs = optimizer.compute_gradients(cost)
    # нужно обрезать градиенты, если они вдруг "взорвутся"
    capped_gvs = [(tf.clip_by_value(grad, -1., 1.), var) for grad, var in gvs]

    train_op = optimizer.apply_gradients(capped_gvs)

    # для контроля времени тренировки
    start_time = time.time()

    with tf.compat.v1.Session() as sess:
        sess.run(V.initializer)

        epoch = 8000

        losses = np.zeros(epoch)

        for i in range(epoch):


            if batch_size == shape_1:
                batch_of_samples = samples
                batch_of_labels = labels
            else:
                random_indeces= np.random.randint(0, shape_1 - batch_size)
                batch_of_samples = samples[random_indeces :random_indeces+batch_size]
                batch_of_labels = labels[random_indeces : random_indeces+batch_size]

            losses[i] = sess.run(cost, {x: batch_of_samples, target: batch_of_labels})
            sess.run(train_op, {x: batch_of_samples, target: batch_of_labels})

        tmp_V = V.eval()

    #  и фиксируем затраченное время
    elapsed_time = time.time() - start_time

    #запишем обученный вектор на диск:

    path_for_filtr="D:\\samples_for_kursach\\filter_vector"
    write_filtr(tmp_V, path_for_filtr)

    # теперь визуализируем, как шла тренировка
    canvas.axes.set_xticks([])
    canvas.axes.set_yticks([])
    canvas.axes.set_title("time spent on training: " + str(elapsed_time)[:5] + "  sek" + "        batch size "+ str(batch_size))

    canvas.axes = canvas.fig.add_subplot(121)
    canvas.plot_linear_signal(np.arange(epoch), losses)
    canvas.axes.set_xlabel('number of epochs')
    canvas.axes.set_ylabel('Loss')
    # canvas.axes.set_yscale("log")

    canvas.axes = canvas.fig.add_subplot(122)

    disc = 1000
    freq = np.fft.fftfreq(shape_2, disc)

    output_V = tmp_V[: -int(shape_2 / 2)]
    freq = freq[freq >= 0]


    canvas.plot_linear_signal(freq * disc, output_V)
    canvas.axes.set_xlabel('Hz')
    canvas.axes.set_ylabel('filter vector')

    #запишем фигуру в pdf

    file_with_id2 = open(path_for_filtr + "\\unic_tmp_id.txt", "r")
    id = file_with_id2.read()
    file_with_id2.close()

    id  = int(id) - 1

    tmp_pdf_file = PdfPages(path_for_filtr + "\\vec_" + str(id) + ".pdf")
    tmp_pdf_file.savefig(canvas.fig)
    tmp_pdf_file.close()






