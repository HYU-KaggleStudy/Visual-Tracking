import argparse
from pathlib import Path
from operator import methodcaller
from os import makedirs

from dicttoxml import dicttoxml

parser = argparse.ArgumentParser(description="Annotation converter")
parser.add_argument('filename', type=str, help='filename to convert')

args = parser.parse_args()

path = Path(args.filename)
if not path.exists():
    print ('File', args.filename, 'not exists')
    exit()

# default meta data
width = 352
height = 240
depth = 3

with open(str(path), 'r') as f:
    # update split function for custom split method
    annotations = map(lambda line: list(map(int, line.split())), f.readlines())

    for index, annotation in enumerate(annotations, 1):
        filename = path.parent / 'annotations' / ('%04d.xml' % index)
        try:
            makedirs(str(filename.parent))
        except:
            pass
        with open(str(filename), 'w') as anno:
            anno.write(dicttoxml({
                "folder": str(path.parent),
                "filename": str(filename),
                "size": {
                    "width": width,
                    "height": height,
                    "depth": depth,
                }, "source": {
                    "database": "http://cvlab.hanyang.ac.kr/tracker_benchmark/datasets.html",
                }, "segmented": 0,
                "object": {
                    "name": str(path.parent),
                    "pose": "Left",
                    "truncated": 0,
                    "difficult": 0,
                    "bndbox": {
                        "xmin": annotation[0],
                        "ymin": annotation[1],
                        "xmax": annotation[0] + annotation[2],
                        "ymax": annotation[1] + annotation[3],
                    }
                }
            }, custom_root='annotation', attr_type=False).decode('utf-8'))
