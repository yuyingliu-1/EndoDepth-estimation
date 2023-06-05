# EndoDepth-estimation

This is the reference PyTorch implementation for training and testing depth estimation models using the method described in "Self-supervised monocular depth estimation for gastrointestinal endoscopy"

This code is for non-commercial use; please see the license file for terms.

If you find our work useful in your research please consider citing our paper.

# Setup:

We have ran our experiments under CUDA 11.0, CuDNN 8.0 and Ubuntu 20.04.3. We recommend create a virtual environment with Python 3.6 using Anaconda conda create -n endodepth python=3.6 and install the dependencies as

pip3 install -r path/to/EndoDepth-estimation/requirements.txt

Install PyTorch 1.7.0 accordingly with your Cuda version (see PyTorch website for more alternatives).

pip install torch==1.7.0+cu110 torchvision==0.8.0+cu110 torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html

# DATA
1.UCL dataset
http://cmic.cs.ucl.ac.uk/ColonoscopyDepth/

2.Endoslam dataset
https://github.com/CapsuleEndoscope/EndoSLAM

未完待续。。。

# Reference

1. C. Godard, O. Mac Aodha, M. Firman, G. J. Brostow, Digging into self-supervised monocular depth estimation, in: Proceedings of the IEEE/CVF International Conference on Computer Vision, 2019, pp. 3828–3838.
2. A. Rau, P. Edwards, O. F. Ahmad, P. Riordan, M. Janatka,L. B. Lovat, D. Stoyanov, Implicit domain adaptation with conditional generative adversarial networks for depth prediction in endoscopy, International journal of computer assisted radiology and surgery 14 (7) (2019) 1167–1176.
3. K. B. Ozyoruk, G. I. Gokceler, T. L. Bobrow, G. Coskun,K. Incetan, Y. Almalioglu, F. Mahmood, E. Curto, L. Perdigoto, M. Oliveira, et al., Endoslam dataset and an unsupervised monocular visual odometry and depth estimation approach for endoscopic videos, Medical image analysis 71 (2021) 102058.
  
