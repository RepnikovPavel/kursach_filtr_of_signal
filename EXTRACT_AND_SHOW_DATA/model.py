# import tensorflow as tf
# # from tensorflow.python.ops.signal.fft_ops import rfft
# # from tensorflow.python.ops.signal.fft_ops import irfft
# from numpy.fft import rfft, rfftfreq
#
# class Model(object):
#     def __init__(self, dataset_samples):
#         length_of_V =len(rfft(dataset_samples[20]))
#         length_of_dataset = tf.shape(dataset_samples)[0]
#         self.V = tf.random.normal(
#             shape=[length_of_dataset][length_of_V], mean=0.0, stddev=1.0, dtype=tf.dtypes.float32
#         )
#         print(length_of_dataset)
#         print(length_of_V)
#
#     def __call__(self, x):
#         return tf.norm(irfft(tf.multiply(rfft(x), self.V))) / tf.norm(x)
#
#
# def loss(target_y, predicted_y):
#     return tf.reduce_mean(tf.pow(tf.pow(predicted_y, 2) - target_y, 2))
