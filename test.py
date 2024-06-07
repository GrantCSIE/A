import os
import shutil
 

# test_img_path = f'E:/AICUP/AI_CUP_testdataset/AI_CUP_testdata/images'
# #test_img_path = f'E:/AICUP/AI_CUP_MCMOT_dataset/train/images'
# folders = os.listdir(test_img_path)
# print(folders)
# weights_path = 'runs/train/yolov7-AICUP6/weights/best.pt'
# for i in folders:
#     cmd = f'python tools/mc_demo_yolov7.py --weights {weights_path} --source {test_img_path}/{i} --device "0" --name "{i}" --fuse-score --agnostic-nms --with-reid --fast-reid-config fast_reid/configs/AICUP/bagtricks_R50-ibn.yml --fast-reid-weights logs/AICUP_115/bagtricks_R50-ibn/model_0058.pth'
#     print(cmd)
#     os.system(cmd)
#     print()



# 存放txt的資料夾
if not os.path.exists(f'./runs/pred_res/test7'):
    os.mkdir(f'./runs/pred_res/test7')

detect_path = f'./runs/detect/test7'
detect_folder = os.listdir(detect_path)
for i in detect_folder:
    files = os.listdir(f'{detect_path}/{i}')
    for f in files:
        if f.split('.')[-1] == 'txt':
            src = f'{detect_path}/{i}/{f}'
            dst = f'./runs/pred_res/test7/{f}'
            shutil.copyfile(src, dst)
