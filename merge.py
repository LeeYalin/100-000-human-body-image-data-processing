import os
import json

dirpath = os.path.abspath(os.curdir)
print(dirpath)
for file in os.listdir(dirpath+'/json_data/'):
    filepath = dirpath+'/json_data/'+file
    with open(filepath, encoding='utf-8') as f:
        json_data = json.load(f)
        keypoints = json_data['people'][0]['pose_keypoints_2d']
        size = json_data['people'][0]['size']
    with open(dirpath+'/keypoints_pose14.txt', 'a+') as f:
        print(file[0:6])
        f.write('000000'+file[0:6]+' ')
        p_num = 0
        p_14=0
        for point in keypoints:
            p_14 +=1
            if p_14<15:
                if point[2]:
                    f.write(str(int(point[0]))+' ')
                    f.write(str(int(point[1]))+' ')
                    f.write('2 ')
                    p_num += 1
                else:
                    f.write('0 0 0 ')
        f.write(str(p_num)+' 0.00 0.00 ')
        f.write(str(size[0])+'.00 ')
        f.write(str(size[1])+'.00 0 1 ')
        f.write('000000'+file[0:6]+'\n')

