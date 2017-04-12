# File to play around
#import package
import tensorflow as tf

#create a constant node
"""
node1=tf.constant(3.0,tf.float32)
node2=tf.constant(4.0)
#print the node
print(node1,node2)
sess=tf.Session()
print(sess.run([node1,node2]))
"""
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)