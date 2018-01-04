from urllib import request
from pathlib import Path
from zipfile import ZipFile
from os import remove

targets = ["http://cvlab.hanyang.ac.kr/tracker_benchmark/seq/Dog.zip"]

for tar in targets:
    path = Path("./train/") / Path(tar).name
    print ('Download', str(path))
    request.urlretrieve(tar, str(path))
    print ('Extract', str(path))
    zip = ZipFile(str(path), 'r')
    zip.extractall("./train")
    zip.close()
    remove(str(path))
    print (str(path), 'done!')

