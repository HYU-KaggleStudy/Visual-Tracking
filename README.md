# Visual Tracking

Based on [YOLO](https://pjreddie.com/darknet/yolo/) with [Tensorflow](https://www.tensorflow.org/)

First of all, init submodule.

```
git submodule init
git submodule update
```

or

clone this repository with `--recursive` option.

And init darkflow as [link](https://github.com/thtrieu/darkflow).

## Dataset

from [CVLab @ Hanyang Univ.](http://cvlab.hanyang.ac.kr/tracker_benchmark/datasets.html) 

use `script/download.py` to download datasets.

```
python3 script/download.py
```

It's create `labels.txt` as the number of downloaded classes.
Past to darkflow and change parameter of `cfg` file.

## Annotation

Convert from given annotation format to YOLO format(`xml`).

use `sciprt/annotation.py` to convert automatically.

```
python3 script/annotation.py train/Dog/groundtruth_rect.txt
```

*default image size 352 x 240 x 3*

## Demo

ready
