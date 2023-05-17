#!/bin/bash

c3d WHS_SD_rat_atlas_v4.01.nii.gz -region 244x0x0vox 268x1024x512vox -o WHS-v4.01-right-hemisphere.nii.gz
c3d WHS_SD_rat_atlas_v4.01.nii.gz -region 0x0x0vox 244x1024x512vox -o WHS-v4.01-left-hemisphere.nii.gz

IDS=$(tail -n +16 ./WHS_SD_rat_atlas_v4.01.label | awk '{print $1;}')

for id in $IDS
do
    argsr+=" $id $(expr 10000 + $id)"
    argsl+=" $id $(expr 50000 + $id)"
done

c3d WHS-v4.01-right-hemisphere.nii.gz -replace $argsr -o WHS-v4.01-right-hemisphere-relabeled.nii.gz
c3d WHS-v4.01-left-hemisphere.nii.gz -replace $argsl -o WHS-v4.01-left-hemisphere-relabeled.nii.gz

c3d WHS-v4.01-left-hemisphere-relabeled.nii.gz WHS-v4.01-right-hemisphere-relabeled.nii.gz -tile x -o WHS-v4.01-both-hemispheres-relabeled-xyflip.nii.gz
c3d WHS-v4.01-both-hemispheres-relabeled-xyflip.nii.gz -flip xy -o WHS-v4.01-both-hemispheres-relabeled.nii.gz