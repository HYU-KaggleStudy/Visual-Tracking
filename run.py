from os import listdir
from os.path import isfile, join
import cv2
import re
import math

import numpy as np
from darkflow.net.build import TFNet

options = {
    "model": "cfg/v1/yolo-full.cfg", 
    "load": "bin/yolo-full.weights",
    "threshold": 0.1
}

data = '../test/'
tfnet = TFNet(options)

# Utils
center = lambda tar: ((tar[0] + tar[2]) / 2, (tar[1] + tar[3]) / 2)
overlap = lambda tar, obj: tar[0] < obj[0] and obj[0] < tar[2] and tar[1] < obj[1] and obj[1] < tar[3]
distance = lambda tar, obj: math.sqrt((tar[0] - obj[0])**2 + (tar[1] - obj[1])**2)
tuplize = lambda tar: ((tar[0], tar[1]), (tar[2], tar[3]))


with open(data + 'groundtruth_rect.txt') as f:
    a = list(map(lambda line: list(map(int, re.split(';|,| |\t', line.replace('\n', '')))), f.readlines()))
    box = (a[0][0], a[0][1], a[0][0] + a[0][2], a[0][1] + a[0][3])
# Set target object
objects = [{
    'class': None,
    'position': box,
    'follow': True,
    'begin': None,
    'skip': [],
    'end': None,
}]

# Debug
loss = 0

# Process
for b, file in zip(a, sorted(listdir(data + "img"))):
    if not isfile(join(data + "img", file)): continue
    img = cv2.imread(join(data + "img", file))

    updated = [False] * len(objects)
    for result in tfnet.return_predict(img):
        rect = (result['topleft']['x'],result['topleft']['y'],result['bottomright']['x'],result['bottomright']['y'])
        update = False
        for i, obj in enumerate(objects):
            if overlap(rect, center(obj['position'])) and (result['label'] == obj['class'] or not obj['class']):
                if not obj['class']:
                    obj['class'] = result['label']
                    obj['begin'] = file
                obj['position'] = rect
                update = True
                updated[i] = True
        if not update:
            objects.append({
                'class': result['label'],
                'position': rect,
                'follow': False,
                'begin': file,
                'skip': [],
                'end': None,
            })

    for update, obj in zip(updated, objects):
        if not update:
            obj['skip'].append(file)

    # Showcase
    print (file, '=======================')
    print (objects)
    cv2.rectangle(img, *tuplize(objects[0]['position']), (0,121, 255), 3)
    cv2.imwrite(join(data + 'out', file), img)
