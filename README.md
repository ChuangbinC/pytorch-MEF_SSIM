# pytorch-MEF_SSIM

## Installation
1. Clone this repo.
2. Copy "pytorch_ssim" folder in your project.

## Example
```
python3 mef_ssim_test.py
```

# Comparison of Pytorch version and Matlab version						
|                  | Menters | BruceExpoBlend | GGF     | GGIF    | Raman   | Times    |
| ---------------- | ------- | -------------- | ------- | ------- | ------- | -------- |
| pytorch-MEF_SSIM | 0.8702  | 0.8985         | 0.9112  | 0.8711  | 0.8654  | 1.034 s  |
| Matlab-MEF_SSIM  | 0.9372  | 0.9682         | 0.9903  | 0.9405  | 0.9283  | 60.377 s |
| Error            | 0.0670  | 0.0697         | 0.0791  | 0.0694  | 0.0629  |          |
| Error/pytorch-MEF_SSIM                 | 7.700%  | 7.758%         | 8.681%  | 7.967%  | 7.269%  |          |

# Citation
```
@misc{chen2019pytorchmefssim,
    author = {Chuangbin Chen},
    title = {CODE: MEF_SSIM in Pytorch},
    year = {2019},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\url{https://github.com/ChuangbinC/pytorch-MEF_SSIM}}
  }
```
# Note
This is a pytorch implementation of MEF_SSIM and if you find some wrong in the code, PLEASE tell me.
# Reference
+ [pytorch-ssim](https://github.com/Po-Hsun-Su/pytorch-ssim)
+ [Perceptual Quality Assessment for Multi-Exposure Image Fusion](https://ece.uwaterloo.ca/~k29ma/papers/15_TIP_MEF.pdf)
