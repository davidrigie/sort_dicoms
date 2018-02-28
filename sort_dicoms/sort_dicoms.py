#!/usr/bin/env python

import pydicom
import glob
import shutil
import os


def sort_dicoms(rootdir):

    filelist = glob.glob(os.path.join(rootdir, '*.IMA'))

    uid_dict = dict()
    description_dict = dict()

    for i,filename in enumerate(filelist):
        print('checking file {} of {}'.format(i, len(filelist)))
        ds = pydicom.dcmread(filename)
        
        uid_dict[filename] = ds.SeriesInstanceUID
        description_dict[uid_dict[filename]] = ds.SeriesDescription

    uid_set     = set(uid_dict.values())
    dicom_dirs  = dict()

    for uid in uid_set:
        if uid in dicom_dirs:
            dicom_dirs[uid] = dicom_dirs[uid] + '_'
        else:
            dicom_dirs[uid] = os.path.join(rootdir, description_dict[uid])
        
    for i,filename in enumerate(filelist):
        print('Moving file {} of {}'.format(i+1, len(filelist)))
        uid = uid_dict[filename]
        dirname = dicom_dirs[uid]

        if not os.path.isdir(dirname):
            os.mkdir(dirname)
        shutil.move(filename, os.path.join(dirname,os.path.basename(filename)))


        