#%%
import sys
import cv2
import os
from pytorch_mef_ssim.pytorch_mef_ssim.MEF_SSIM import mef_ssim

img_dir_path = './pytorch-mef_ssim/seq6'
refImge_dir = './pytorch-mef_ssim/Menters.png'
img_name_list = ["ExposureQS-0.bmp", "ExposureQS-1.bmp", "ExposureQS-2.bmp", "ExposureQS-3.bmp", "ExposureQS-4.bmp"]

img_list = []
for img_path in img_name_list:
    img = cv2.imread(os.path.join(img_dir_path, img_path), 0).astype(np.float64)
    img = np.expand_dims(img,0)
    img_list.append(img)

img_seq = np.concatenate(img_list,0)
img_seq = np.expand_dims(img_seq,0)
img_seq = torch.Tensor(img_seq)

refImg = cv2.imread(refImge_dir,0)
refImg = refImg.astype(np.float64)
refImg = np.expand_dims(refImg,0)
refImg = np.expand_dims(refImg,0)
refImg = torch.Tensor(refImg)

print(mef_ssim(img_seq,refImg))


#%%


#%%
