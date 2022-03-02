import sys
import json
import io
import torch
import numpy as np
import os
import argparse
from tqdm import tqdm
from base_pose_3d.base_model import LinearModel, weight_init
from torch.autograd import Variable
from base_pose_3d.data_process import unNormalizeData
import matplotlib.gridspec as gridspec
from base_pose_3d.camera import *
import matplotlib.pyplot as plt
from base_pose_3d.vis import *

current_path = os.path.dirname(__file__)
camera_path=os.path.join(current_path,"parameters",'metadata.xml')
checkpoint_path=os.path.join(current_path,"parameters",'ckpt_best.pth.tar')
stat_3d_path=os.path.join(current_path,"parameters", 'stat_3d.pth.tar')
stat_2d_path=os.path.join(current_path,"parameters", 'stat_2d.pth.tar')


dim_to_use= np.array([0,  1,  2,  3,  4,  5,  6,  7, 12, 13, 14, 15, 16, 17, 24, 25, 26,
       27, 30, 31, 34, 35, 36, 37, 38, 39, 50, 51, 52, 53, 54, 55])
#将openpose-25 2d格式关键点，转化为hm-36 格式2d关键点
def normalize_data(hm36_data,data_mean,data_std,dim_to_use):
    hm36_data=hm36_data[dim_to_use]
    mu=data_mean[dim_to_use]
    stddev = data_std[dim_to_use]
    normalized = np.divide((hm36_data-mu),stddev)
    return normalized
def covert_op_to_hm(op_kp_2d):
    order=[15,13,25,26,27,17,18,19,0,1,2,3,6,7,8]
    hm36_item=np.zeros([32,2])
    for i in range(len(order)):
        hm36_item[order[i]]=op_kp_2d[i]
    #set spin
    hm36_item[12]=(op_kp_2d[1]+op_kp_2d[8])/2
    hm36_item=hm36_item.flatten()
    return hm36_item
#将2d关键点转化为3d关键点
def convert_2d_to_3d(pose_pts):
    device ="cuda:0" if torch.cuda.is_available() else "cpu:0"    
    stat_3d = torch.load(stat_3d_path)
    stat_2d = torch.load(stat_2d_path,encoding="latin1")
    model = LinearModel()
    #load weight
    ckpt = torch.load(checkpoint_path)
    model.load_state_dict(ckpt['state_dict'])
    model.eval()
    model.to(device)
    #加载摄像头参数，这里是手动指定的
    rcams = load_cameras(camera_path)
    R, T, f, c, k, p, name=rcams[(9,2)]
    hm36_pts=covert_op_to_hm(pose_pts)
    n_hm36_pts=normalize_data(hm36_pts,stat_2d["mean"],stat_2d["std"],dim_to_use)
    inps=n_hm36_pts
    inputs = Variable(torch.tensor(inps.reshape(1,32)).to(torch.float32).to(device))
    outputs = model(inputs)
    p3d = unNormalizeData(outputs.cpu().detach().numpy(), stat_3d['mean'], stat_3d['std'], stat_3d['dim_use'])
    return p3d
def convert_2d_to_3d_batch(batch_pose_pts,width,height):

    batch_3d_pts=[]
    for i in tqdm(range(len(batch_pose_pts)),desc="convert 2d to 3d:"):
        batch_pose_pts_scale=(batch_pose_pts[i].reshape(25,2)+1)*0.5
        batch_pose_pts_scale[:,0] = batch_pose_pts_scale[:,0]*width
        batch_pose_pts_scale[:,1] = batch_pose_pts_scale[:,1]*height       
        pts_3d=convert_2d_to_3d(batch_pose_pts_scale)
        batch_3d_pts.append(pts_3d)
    return np.array(batch_3d_pts)







    

