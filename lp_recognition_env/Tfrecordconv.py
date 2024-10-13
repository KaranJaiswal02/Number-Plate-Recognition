import os
import pandas as pd
import tensorflow as tf
from object_detection.utils import dataset_util
from collections import namedtuple
from PIL import Image
import io

# Function to convert CSV row to tf.Example
def create_tf_example(group, path):
    with tf.io.gfile.GFile(os.path.join(path, '{}'.format(group.files)), 'rb') as fid:
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height = image.size

    filename = group.files.encode('utf8')
    image_format = b'jpg'
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    for index, row in group.object.iterrows():
        xmins.append(row['xmin'] / width)
        xmaxs.append(row['xmax'] / width)
        ymins.append(row['ymin'] / height)
        ymaxs.append(row['ymax'] / height)
        classes_text.append(row['text'].encode('utf8'))
        classes.append(1)  # Assuming license_plate is the only class and its label is 1

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    return tf_example

# Function to read CSV and convert to tf.Example
def main():
    path = 'dataset/images'
    examples = pd.read_csv('dataset/annot_file.csv')
    grouped = examples.groupby('files')
    writer = tf.io.TFRecordWriter('dataset/train.record')
    
    for filename, group in grouped:
        group = namedtuple('group', ['files', 'object'])(filename, group)
        tf_example = create_tf_example(group, path)
        writer.write(tf_example.SerializeToString())
    
    writer.close()
    print('Successfully created the TFRecord file.')

if __name__ == '__main__':
    main()
