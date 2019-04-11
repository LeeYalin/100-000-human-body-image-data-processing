import os
import json

dirpath = os.path.abspath(os.curdir)
print(dirpath)
for file in os.listdir(dirpath+'/json_data/'):
    filepath = dirpath+'/json_data/'+file
    kk = []
    with open(filepath, encoding='utf-8') as f:
        json_data = json.load(f)
        for t in range(len(json_data['people'])):
            keypoints = json_data['people'][t]['pose_keypoints_2d']
            kk.append(keypoints)
        size = json_data['people'][0]['size']
    with open(dirpath+'/keypoints8.txt', 'a+') as f:
        print(file[0:6])
        f.write(file[0:6]+' ')
        f.write(str(size[1])+' ')
        f.write(str(size[0])+': ')
        for ii in range(len(kk)):
            p_num = 0
            p_8=0
            for point in kk[ii]:
                p_8 +=1
                if p_8<9:
                    if point[2]:
                        
                        f.write(str(int(point[0]))+' ')
                        f.write(str(int(point[1]))+' ')
                        f.write('2 ')
                        p_num += 1
                    else:
                        f.write('0 0 0 ')
            f.write(str(p_num)+' ')
            point0 = kk[ii][8]
            point1 = kk[ii][9]
            a_x = (point0[0] +point1[0])/2
            a_y = (point0[1] +point1[1])/2
            f.write(str(int(a_x)) +' '+ str(int(a_y)) +';')
        f.write('\n')
