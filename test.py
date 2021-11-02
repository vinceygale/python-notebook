# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 09:59:09 2021

@author: vincey
"""

import shutil,os,zipfile
from pathlib import Path
p=Path.cwd()


#shutil.copy(src, dst) 复制源文件到目录文件
#shutil.copy(p/'temp.txt',p/'temp_1.txt')

#shutil.copytree(src, dst) 复制目录（包括文件夹和文件）到目标目录下
#shutil.copytree(p/'test', p/'test_1')

#shutil.move(src, dst) 移动文件到目标文件（相当于剪切&粘贴）
#注意：参数dst所指定的路径必须已经存在，否则会抛出错误，且dst应该是一个带有扩展名的字符串参数，不然会生成一个无扩展名的文件
#shutil.move(p/'temp_1.txt', p/'temp_1.bak')

#os.unlink(path) 删除文件
#os.rmdir(path) 删除文件夹
#shutil.rmtree(path) 删除路径及路径下所有文件及文件夹

"""
for file in Path(p/'test_1').glob('*.txt'):
    #os.unlink(file)
    print(file)

for folderName,subFolders,fileNames in os.walk('D:\\科室内部文档'):
    print('The current forlder is : '+folderName)
    for subFolder in subFolders:
        print(' Subfolder of '+folderName + ' : '+subFolder)
    for fileName in fileNames:
        print('   Files inside '+ folderName+' : '+fileName)
"""

""" 使用zipfile进行文件的压缩和解压缩 """

#
newZip=zipfile.ZipFile('test.zip','w')
p=p/'test'


for path,dir,files in os.walk(p):
    for myFile in files:
        newZip.write(os.path.join(path, myFile))
        print(os.path.join(path,myFile)+' has been ziped!!!')
newZip.close()


myZip=zipfile.ZipFile(Path.cwd()/'test.zip')
for file in myZip.namelist():
    print(file + ' size: '+str(myZip.getinfo(file).file_size)+' compressed size : '+str(myZip.getinfo(file).compress_size))
