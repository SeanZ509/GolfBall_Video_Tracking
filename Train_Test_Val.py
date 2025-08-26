#File to split the imported Dataset of images and labels - Following Yolo implementation

import os
import shutil
from sklearn.model_selection import train_test_split

image_dir = 'Dataset/all/images'
label_dir = 'Dataset/all/labels'
output_dir = 'Dataset'

os.makedirs(os.path.join(output_dir, 'train', 'images'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'train', 'labels'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'valid', 'images'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'valid', 'labels'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'test', 'images'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'test', 'labels'), exist_ok=True)

images = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]
labels = [f for f in os.listdir(label_dir) if f.endswith('.txt')]

images = [img for img in images if img.replace('.jpg', '.txt') in labels]
train_imgs, test_imgs = train_test_split(images, test_size=0.3, random_state=42)
val_imgs, test_imgs = train_test_split(test_imgs, test_size=0.333, random_state=42)  # 0.333 * 0.3 ≈ 0.1

def copy_files(file_list, src_dir, dest_dir, ext):
    for file in file_list:
        src_file = os.path.join(src_dir, file)
        dest_file = os.path.join(dest_dir, file)
        shutil.copy2(src_file, dest_file)
        label_file = file.replace(ext, '.txt')
        src_label_file = os.path.join(label_dir, label_file)
        dest_label_file = os.path.join(dest_dir.replace('images', 'labels'), label_file)
        shutil.copy2(src_label_file, dest_label_file)

copy_files(train_imgs, image_dir, os.path.join(output_dir, 'train', 'images'), '.jpg')
copy_files(val_imgs, image_dir, os.path.join(output_dir, 'valid', 'images'), '.jpg')
copy_files(test_imgs, image_dir, os.path.join(output_dir, 'test', 'images'), '.jpg')
print("Dataset split completed successfully!")