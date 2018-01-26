from darkflow.net.build import TFNet
from lib.utils import parse
from lib.img import Image

from os import path, listdir

# Load model
options =  {
    "model": "cfg/yolo-full.cfg", 
    "load": "bin/yolo-full.weights",
    "threshold": 0.1
}
# model = TFNet(options)

# Target dir must contain 
# - `groundtruth_rect.txt`
# - `img` dir contains images
# and line of groundtruth_rect must matches number of images
TARGET_RECTS = 'groundtruth_rect.txt'
TARGET_IMGS = 'img'
target = 'train/BlurCar1/'

with open(path.join(target, TARGET_RECTS)) as f:
    target_rect = parse(f.readline())

for file in sorted(listdir(path.join(target, TARGET_IMGS))):
    img = Image(path.join(target, TARGET_IMGS, file))
    cropped = img.crop(*target_rect)
    cropped.show()
    break
