# Created: 210313 14:02
# Last edited: 210421 14:02 

import os
import shutil
from tqdm import tqdm


# # 筛除多行的label.txt

input_label_dir = "./datasets_no_test/dev/labels/" # './data/math_210421/formula_labels/'
output_label_dir = "./datasets_no_test/dev/labels_after/" # './data/math_210421/formula_labels_210421/'
multiline_label_dir = "./datasets_no_test/dev/labels_multiline/"

# if not os.path.exists(output_label_dir):
#     os.mkdir(output_label_dir)

# if not os.path.exists(multiline_label_dir):
#     os.mkdir(multiline_label_dir)

# label_name_list = os.listdir(input_label_dir)

# for label_name in tqdm(label_name_list):
#     label_file_name = input_label_dir + label_name
#     with open(label_file_name, 'r', encoding='utf-8') as f1:
#         lines = f1.readlines()
#     # print(lines)
#     if len(lines) > 1:
#         # print("wtf")
#         # print(lines[1])
#         shutil.copy(label_file_name, multiline_label_dir + label_name)
#         continue
#     shutil.copy(label_file_name, output_label_dir + label_name)

# # 筛除多行的label.txt end

# 筛除error mathpix

input_label_dir = output_label_dir
output_label_dir = './datasets_no_test/dev/labels_no_error/'
error_label_dir = './datasets_no_test/dev/labels_error/'

if not os.path.exists(output_label_dir):
    os.mkdir(output_label_dir)

if not os.path.exists(error_label_dir):
    os.mkdir(error_label_dir)

label_name_list = os.listdir(input_label_dir)

for label_name in tqdm(label_name_list):
    label_file_name = input_label_dir + label_name
    with open(label_file_name, 'r', encoding='utf-8') as f1:
        content = f1.read()
    if 'error mathpix' in content:
        shutil.copy(label_file_name, error_label_dir + label_name)
        continue
    shutil.copy(label_file_name, output_label_dir + label_name)

# 筛除error mathpix end