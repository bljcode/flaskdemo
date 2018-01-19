import os
import shutil

from datetime import datetime

from logger import getLogger
log = getLogger(__name__)

def saveAppend(src,name,s):
    file_object = open(src + name, 'a+', encoding='utf-8')
    #file_object = open('com/jd/consumeranalysis/ai/tmpwarehouse/' + name, 'a+', encoding='utf-8')
    file_object.writelines(s)

def copyFile(src,dst):
    try:
        #src = "text.txt"
        #dst = "tt/tt3.txt"
        dir1 = os.path.dirname(dst)
        #print("dir1:" + dir1)
        if (os.path.exists(dir1) == False):
            os.makedirs(dir1)
        shutil.copyfile(src,dst)
    except Exception as err:
        log.error(err)

def fileList(src):
    src="tt"
    dict1 = {}
    for filename in os.listdir(src):
        print("filename with full path:" + str(filename))
        if str(filename) == "__init__.py":
            continue
        dict1[filename]={}
        timestamp = os.path.getctime(os.path.join(src, filename))
        date = datetime.fromtimestamp(timestamp)
        ctime = date.strftime('%Y-%m-%d %H:%M:%S')
        dict1[filename]['ctime'] = ctime
        timestamp2 = os.path.getmtime(os.path.join(src, filename))
        date2 = datetime.fromtimestamp(timestamp2)
        mtime = date2.strftime('%Y-%m-%d %H:%M:%S')
        dict1[filename]['mtime'] = mtime
        isdir = os.path.isdir(os.path.join(src, filename))
        dict1[filename]['isdir'] = isdir
    return dict1

if __name__ == "__main__":
    dict = fileList(None)
    for i, j in dict.items():
        print(i, ":\t", j)
