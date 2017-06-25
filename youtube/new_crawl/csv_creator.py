import scipy.misc
import os
import re

os.chdir('video')

folders = os.listdir(os.getcwd())

for video in folders:
    if os.path.isfile(video):
        continue
    images = os.listdir(os.getcwd() + '/' + str(video))
    if len(images) == 0:
        continue
    current_path = os.getcwd() + "/" + str(video)
    print("current path: " + str(current_path))
    f = open(current_path + "/testcsv.csv", 'w')
    f_time_stamp = open(current_path + "/time_stamps.csv", 'w')
    f.write('emotion,pixels,Usage\n')
    for i in images:
        if not i.endswith('.jpg'):
            continue
        image_file_name = current_path + "/" + i
        img_array = scipy.misc.imread(image_file_name)
        time_stamp =re.findall(r'\d+', i)[0]
        time_stamp = time_stamp.lstrip('0')
        f_time_stamp.write(str(time_stamp) + '\n')
        s = img_array.reshape(1,-1)[0]
        s = ["%.2f" % number for number in s]
        ss=""
        for ii in s:
            ss+=' '+ii
        #s=s[2:-2]
        s=ss
        a=int(0)
        f.write(str(a)+','+s+",Training\n")
    f.close()
    f_time_stamp.close()