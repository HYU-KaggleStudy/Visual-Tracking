import argparse
import re
from pathlib import Path
from operator import methodcaller
from os import makedirs
from xml.etree.ElementTree import Element, SubElement, ElementTree, tostring

from dicttoxml import dicttoxml

parser = argparse.ArgumentParser(description="Annotation converter")
parser.add_argument('filename', type=str, help='filename to convert')

args = parser.parse_args()

path = Path(args.filename)
if not path.exists():
    print ('File', args.filename, 'not exists')
    exit()

# default meta data
width = 320
height = 240
depth = 3

dx = [-1, 0, 1, 0, 0]
dy = [0, -1, 0, 1, 0]

with open(str(path), 'r') as f:
    # update split function for custom split method
    annotations = map(lambda line: list(map(int, re.split(';|,| |\t', line.replace('\n', '')))), f.readlines())

    for index, annotation in enumerate(annotations, 1):
        filename = path.parent / 'annotations' / ('%04d.xml' % index)
        try:
            makedirs(str(filename.parent))
        except:
            pass
        root = Element("annotation")
        SubElement(root, "folder").text = str(path.parent)
        SubElement(root, "filename").text = filename.name + '.jpg'
        SubElement(root, "segmented").text = "0"
        size = SubElement(root, "size")
        SubElement(size, "width").text = str(width)
        SubElement(size, "height").text = str(height)
        SubElement(size, "depth").text = str(depth)
        source = SubElement(root, "source")
        SubElement(source, "database").text = "http://cvlab.hanyang.ac.kr/tracker_benchmark/datasets.html"
        for d in range(5):
            obj = SubElement(root, "object")
            SubElement(obj, "name").text = path.parent.name
            SubElement(obj, "pose").text = "Left"
            SubElement(obj, "truncated").text = "0"
            SubElement(obj, "difficult").text = "0"
            box = SubElement(obj, "bndbox")
            SubElement(box, "xmin").text = str(annotation[0] + dx[d])
            SubElement(box, "ymin").text = str(annotation[1] + dy[d])
            SubElement(box, "xmax").text = str(annotation[0] + annotation[2] + dx[d])
            SubElement(box, "ymax").text = str(annotation[1] + annotation[3] + dy[d])
        ElementTree(root).write(str(filename))