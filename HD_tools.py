#!/usr/bin/env python
# coding=utf-8
# @author Franck Porteous <franck.porteous@proton.me>

import glob
from this import d
import numpy as np

class all_poses:
    
    """
    Lorem ipsum 
    """

    def __init__(self, path:str, example:str, video_sr):
        
        self.path     = path
        self.example  = example
        self.video_sr = float(video_sr)

        self.cams = self.find_cams()
        self.poses1, self.poses2 = self.load_poses()

    def find_cams(self):
        l = []
        for cam in glob.glob("{}{}*.npy".format(self.path, self.example)):
            l.append(cam.split('/')[3].split('_')[1])
        return l

    def load_poses(self):
        sub1 = np.load("{}{}_{}_concatenated_poses.npy".format(self.path, self.example, self.cams[0]))   
        sub2 = np.load("{}{}_{}_concatenated_poses.npy".format(self.path, self.example, self.cams[1]))   
        print("\n>> Who's data is where?\n\tPoses1 is {}\n\tPoses2 is {}".format(self.cams[0], self.cams[1]))
        return sub1, sub2

    def sw(self, sw_min:float, sw_max:float):
        '''
        Lorem ipsum
        
        Arguments:
            sw_min: float
                Minimum boudary for the sliding window 
            sw_mxn: float
                Maximum boudary for the sliding window
        '''

        sw_min_spl = int(sw_min * self.video_sr)
        sw_max_spl = int(sw_max * self.video_sr)

        print("\n>> Extracting poses time window: [{} - {}] ...".format(sw_min, sw_max))

        sub1 = self.poses1[:,sw_min_spl:sw_max_spl]
        sub2 = self.poses2[:,sw_min_spl:sw_max_spl]
        
        self.po1, self.po2 = sub1, sub2
        
        print(">>> Data extracted.")