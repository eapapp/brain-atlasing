#!/bin/bash

c3d annotation_10_Slicer.nii.gz -region 0x0x570vox 1320x800x570vox -o AMBA-2022-right-hemisphere.nii.gz
c3d annotation_10_Slicer.nii.gz -region 0x0x0vox 1320x800x570vox -o AMBA-2022-left-hemisphere.nii.gz

RIGHT=$(cat ./relabel-pattern.txt | awk '{print $1 " " $2;}')
LEFT=$(cat ./relabel-pattern.txt | awk '{print $1 " " $3;}')

argsr="${RIGHT//$'\n'/' '}"
argsl="${LEFT//$'\n'/' '}"

c3d AMBA-2022-right-hemisphere.nii.gz -replace $argsr -o AMBA-2022-right-hemisphere-relabeled.nii.gz
c3d AMBA-2022-left-hemisphere.nii.gz -replace $argsl -o AMBA-2022-left-hemisphere-relabeled.nii.gz

c3d AMBA-2022-left-hemisphere-relabeled.nii.gz AMBA-2022-right-hemisphere-relabeled.nii.gz -tile z -o AMBA-2022-both-hemispheres-relabeled.nii.gz
c3d AMBA-2022-both-hemispheres-relabeled.nii.gz -orient ASR -flip z -info -o AMBA-2022-both-hemispheres-relabeled-reoriented.nii.gz
