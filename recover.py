import os
import json

dirpath = os.path.abspath(os.curdir)
print(dirpath)
keyIndex = [0, 2, 3, 4, 5, 6 ,7]
for file in os.listdir(dirpath+'/json_data/'):
    # 打开新json文件，读取数据
    filepath = dirpath+'/json_data/' + file
    with open(filepath, encoding='utf-8') as f:
        json_data = json.load(f)
        keypoints_n = json_data['people'][0]['pose_keypoints_2d']

    # 打开旧json文件，读取数据
    filepath = dirpath+'/output/' + file
    with open(filepath, encoding='utf-8') as f:
        json_data = json.load(f)
        if len(json_data['people']):
            keypoints_o = json_data['people'][0]['pose_keypoints_2d']

    # 如果旧json未检测到人，手动添加
    if len(json_data['people']) == 0:
        json_data['people'].append({'pose_keypoints_2d':[0 for i in range(18*3)]})
    
    # 修改旧json数据并存储
    for ind in keyIndex:
        o_ind = keyIndex.index(ind)
        json_data['people'][0]['pose_keypoints_2d'][3*ind] = keypoints_n[o_ind][0]
        json_data['people'][0]['pose_keypoints_2d'][3*ind+1] = keypoints_n[o_ind][1]
        json_data['people'][0]['pose_keypoints_2d'][3*ind+2] = keypoints_n[o_ind][2]
    filepath = dirpath+'/json_data_n/' + file
    with open(filepath, 'w+') as f:
        json.dump(json_data, f)

