# 导入需要的模块
from glob import glob
from PIL import Image
import os

# 图片路径
# 使用 glob模块 获得文件夹内所有jpg图像
img_path = glob("/mnt/cd43550d-ff7b-4058-a185-a6b1f0bd96ea/hamlyn_tracking_test_data-20220830T112924Z-001/sim/test/depth/*.png")
path_save = "/mnt/cd43550d-ff7b-4058-a185-a6b1f0bd96ea/hamlyn_tracking_test_data-20220830T112924Z-001/sim/test/depth"


for i, file in enumerate(img_path):
  name = os.path.join(path_save, file)
  im = Image.open(file)
  # im.thumbnail((720,1280))
  reim = im.resize((256, 256))
  print(im.format, reim.size, reim.mode)
  reim.save(name, im.format)
