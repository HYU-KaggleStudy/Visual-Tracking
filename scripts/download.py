from urllib import request
from zipfile import ZipFile
from os import remove

targets = ["http://cvlab.hanyang.ac.kr/tracker_benchmark/seq/Dog.zip"]

for tar in targets:
    name = "./train/" + tar.split('/')[-1]
    print ('Download', name)
    request.urlretrieve(tar, name)
    print ('Extract', name)
    zip = ZipFile(name, 'r')
    zip.extractall("./train")
    zip.close()
    remove(name)
    print (name, 'done!')

