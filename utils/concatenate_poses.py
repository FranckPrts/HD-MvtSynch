#!/usr/bin/env python
# coding=utf-8
# @author Franck Porteous <franck.porteous@proton.me>

#%% 
import glob
import json
import numpy as np

data_path = "../SyncSamples/"
save_path = "../SyncSamples/long_format/"
examples = ["A/", "B/", "C/", "D/"]
cameras = ["HD1", "HD2", "HD3", "HD4"]
poses_dim = 75

for ex in examples:
    for cam in cameras:
        print("\nDoing : ", ex, cam)
        files = glob.glob("{}{}*{}.poses".format(data_path, ex, cam))
        avail_samples = len(files)
        if avail_samples > 2:

            allArrays = np.zeros([poses_dim])
            nb_sampl = 0
            
            for filename in files:
                f = open(filename,"r")
                file = json.load(f) 
                f.close()

                nb_sampl += len(file['poses'])

                for sample in range(len(file['poses'])):
                    allArrays = np.column_stack([allArrays, file['poses'][sample]['data']])
            
            # Pop out the first column of zeros we made when init the arr
            allArrays = allArrays[:,1:]

            # Save the array
            np.save("{}{}_{}_concatenated_poses.npy".format(save_path, ex[:1], cam), allArrays)
            print("\tConcatenated {} files.".format(avail_samples))
        else:
            print("\tNot enought files to do apply concatenation.")
            pass

print("Done.")
# %%
