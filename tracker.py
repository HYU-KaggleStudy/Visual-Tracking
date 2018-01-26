from darkflow.net.build import TFNet

# Load model
dump(model, open('model.p', 'wb'))

options =  {
    "model": "cfg/yolo-full.cfg", 
    "load": "bin/yolo-full.weights",
    "threshold": 0.1
}
model = TFNet(options)

# Target dir must contain 
# - `groundtruth_rect.txt`
# - `img` dir contains images
# and line of groundtruth_rect must matches number of images
target = '../train/BlurCar1/'
