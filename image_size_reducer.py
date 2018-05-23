import os
# print(os.walk('.'))
from shutil import copyfile

from PIL import Image


def compress_image(filepath, file):
    original_file_path = filepath + '/' + file
    oldsize = os.stat(original_file_path).st_size
    picture = Image.open(original_file_path)
    # dim = picture.size
    # li = original_file_path.split('/')[original_file_path.split('/').__len__() - 3:]
    new_file = '/home/rahul/Projects/its_my_design/Content/material/Web Design1/' + file
    if not os.path.exists(os.path.dirname(new_file)):
        os.makedirs(os.path.dirname(new_file))
    picture.save(new_file, "PNG", optimize=True, quality=40)

    newsize = os.stat(new_file).st_size
    percent = (oldsize - newsize) / float(oldsize) * 100
    # if (verbose):
    # print("File compressed from {0} to {1} or {2}%".format(oldsize, newsize, percent))
    return percent


# def compress_video(filepath, file)
#     original_file_path = filepath + '/' + file
#     oldsize = os.stat(original_file_path).st_size
#     li = original_file_path.split('/')[original_file_path.split('/').__len__() - 3:]
#     new_file = '/home/rahul/Projects/its_my_design/Media/Categories1/' + \
#                li[0] + '/' + li[1] + '/' + file
#     os.makedirs(os.path.dirname(new_file))


for root, dirs, files in os.walk("/home/rahul/Projects/its_my_design/Content/material/Web Design/"):
    path = root.split(os.sep)
    # print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        # if root.split('/').__len__() >= 9:
        if file.split('.')[1].lower() in ['jpeg', 'jpg', 'png']:
            print(root + file)
            compress_image(root, file)
            # else:
            #     original_file_path = root + '/' + file
            #
            #     li = original_file_path.split('/')[original_file_path.split('/').__len__() - 3:]
            #     new_file = '/home/rahul/Projects/its_my_design/Media/Categories1/' + \
            #                li[0] + '/' + li[1] + '/' + file
            #     os.makedirs(os.path.dirname(new_file))
            #
            #     copyfile(original_file_path, new_file)
