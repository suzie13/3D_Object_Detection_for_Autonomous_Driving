from __future__ import division
import os
import os.path
import torch
import numpy as np
import cv2
import math


from utils import *


class KittiDataset(torch.utils.data.Dataset):

    def __init__(self, root='D:/3D-Object-Detection-for-Autonomous-Driving/dataset/kitti',set='train',type='velodyne_train'):
        self.type = type
        self.root = root
        self.data_path = os.path.join(root, 'training')
        self.lidar_path = os.path.join(self.data_path, "velodyne/")
        self.image_path = os.path.join(self.data_path, "image_2/")
        self.calib_path = os.path.join(self.data_path, "calib/")
        self.label_path = os.path.join(self.data_path, "label_2/")

        with open(os.path.join(self.data_path, '%s.txt' % set)) as f:
            self.file_list = f.read().splitlines()


    def __getitem__(self, i):

        lidar_file = self.lidar_path + '/' + self.file_list[i] + '.bin'
        calib_file = self.calib_path + '/' + self.file_list[i] + '.txt'
        label_file = self.label_path + '/' + self.file_list[i] + '.txt'
        image_file = self.image_path + '/' + self.file_list[i] + '.png'
        #print(self.file_list[i])

        if self.type == 'velodyne_train':
            
            target = get_target(label_file,calib_file)
            #print(target)
            #print(self.file_list[i])
            
            ################################
            # load point cloud data
            a = np.fromfile(lidar_file, dtype=np.float32).reshape(-1, 4)

            b = removePoints(a,bc)

            data = makeBVFeature(b, bc, 40/512)   # (512, 1024, 3)

            return data , target


    def __len__(self):
        return len(self.file_list)


