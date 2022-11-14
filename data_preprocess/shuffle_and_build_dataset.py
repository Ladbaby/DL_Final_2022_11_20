import os
import random
import shutil
from tqdm import tqdm

# shuffle

input_dir_train = "./datasets_no_test/train/labels_no_chinese/"# '../datasets_no_test/210618/formulas_labels/'
# input_dir_test = "./datasets_no_test/test/labels_no_chinese/"
input_dir_val = "./datasets_no_test/dev/labels_no_chinese/"
output_dir = './data/CROHME/formulas/'

image_input_dir_train = "./datasets_no_test/train/images/"# '../data/210618/formulas_images/'
# image_input_dir_test = "./datasets_no_test/test/images/"
image_input_dir_val = "./datasets_no_test/dev/images/"
image_output_dir = './data/CROHME/images/'

if not os.path.isdir(output_dir):
    os.mkdir(output_dir)
if not os.path.isdir(image_output_dir):
    os.mkdir(image_output_dir)
    os.mkdir(image_output_dir + 'images_train/')
    os.mkdir(image_output_dir + 'images_val/')
    os.mkdir(image_output_dir + 'images_test/')

# label_name_list_train = os.listdir(input_dir_train)
# label_name_list_test = os.listdir(input_dir_test)
# label_name_list_val = os.listdir(input_dir_val)
# random.shuffle(label_name_list)

# total_num = len(label_name_list)
# train_num = int(0.7 * total_num)
# val_num = int(0.1 * total_num)
# test_num = total_num - train_num - val_num

# total_num = 76253
# train_num = int(0.7 * total_num)
# val_num = int(0.1 * total_num)
# test_num = total_num - train_num - val_num

train_list = os.listdir(input_dir_train) # []
val_list = os.listdir(input_dir_val)
# test_list = os.listdir(input_dir_test)

# for i in range(total_num):
#     if i < train_num:
#         train_list.append(label_name_list[i])
#     elif i < train_num + val_num:
#         val_list.append(label_name_list[i])
#     else:
#         test_list.append(label_name_list[i])

with open(output_dir + 'train.formulas.norm.txt', 'w', encoding='utf-8') as f1:
    for i in tqdm(range(len(train_list))):
        train_label_name = train_list[i]
        image_name = train_label_name[:-4] + '.png'
        shutil.copy(image_input_dir_train + image_name, image_output_dir + 'images_train/' + str(i) + '.png')
        with open(input_dir_train + train_label_name, 'r', encoding='utf-8') as f2:
            line = f2.read()
            f1.write(line + '\n')

with open(output_dir + 'val.formulas.norm.txt', 'w', encoding='utf-8') as f1:
    for i in tqdm(range(len(val_list))):
        val_label_name = val_list[i]
        image_name = val_label_name[:-4] + '.png'
        shutil.copy(image_input_dir_val + image_name, image_output_dir + 'images_val/' + str(i) + '.png')
        with open(input_dir_val + val_label_name, 'r', encoding='utf-8') as f2:
            line = f2.read()
            f1.write(line + '\n')

# with open(output_dir + 'test.formulas.norm.txt', 'w', encoding='utf-8') as f1:
#     for i in tqdm(range(len(test_list))):
#         test_label_name = test_list[i]
#         image_name = test_label_name[:-4] + '.png'
#         shutil.copy(image_input_dir_test + image_name, image_output_dir + 'images_test/' + str(i) + '.png')
#         with open(input_dir_test + test_label_name, 'r', encoding='utf-8') as f2:
#             line = f2.read()
#             f1.write(line + '\n')

# shuffle end