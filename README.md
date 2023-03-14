# EndoDepth-estimation

This is the reference PyTorch implementation for training and testing depth estimation models using the method described in "Self-supervised monocular depth estimation for gastrointestinal endoscopy"

This code is for non-commercial use; please see the license file for terms.

If you find our work useful in your research please consider citing our paper.

# Setup:

We have ran our experiments under CUDA 11.0, CuDNN 8.0 and Ubuntu 20.04.3. We recommend create a virtual environment with Python 3.6 using Anaconda conda create -n endodepth python=3.6 and install the dependencies as

pip install torch==1.7.0+cu110 torchvision==0.8.0+cu110 torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html

# 其它依赖库:
pip3 install -r path/to/Endo-Depth-and-Motion/requirements.txt

# 
