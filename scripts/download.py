from urllib import request
from pathlib import Path
from zipfile import ZipFile
from os import remove

targets = ["http://cvlab.hanyang.ac.kr/tracker_benchmark/seq/Dog.zip",
"http://cvlab.hanyang.ac.kr/tracker_benchmark/seq/Car2.zip"]

objs = []
for tar in targets:
    objs.append(Path(tar).stem)
    path = Path("./train/") / Path(tar).name
    print ('Download', str(path))
    request.urlretrieve(tar, str(path))
    print ('Extract', str(path))
    zip = ZipFile(str(path), 'r')
    zip.extractall("./train")
    zip.close()
    remove(str(path))
    print (str(path), 'done!')

with open('labels.txt', 'w') as f:
    f.write('\n'.join(objs))

