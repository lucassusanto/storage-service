import os

from UsersModel import *

class File_Controller():
    def __init__(self, username):
        self.username = username
        self.path = 'storage/' + username + '/'

    def createFile(self, filePath, content):
        path = self.path + filePath

        if os.path.isfile(path):
            return 1

        user = Users_Model()
        fileSize = len(content)
        
        if user.canAddFile(self.username, fileSize) == False:
            return 2

        with open(path, "w") as f:
            f.write(content)

        user.updateUsedSpace(self.username, fileSize)

        return 0

    def deleteFile(self, filePath):
        path = self.path + filePath

        if not os.path.isfile(path):
            return 1

        Users_Model().updateUsedSpace(self.username, -os.path.getsize(path))
        os.remove(path)

        return 0

    def openFile(self, filePath):
        path = self.path + filePath

        if not os.path.isfile(path):
            return 1, ""

        f = open(path, "r")
        content = f.read()
        f.close()

        return 0, content

    def listFile(self, folderPath):
        path = self.path + folderPath

        if not os.path.isdir(path):
            return 1, ""

        lists = []

        for _, _, files in os.walk(path):  
            for filename in files:
                lists.append(filename)

        return 0, lists

    def createDir(self, folderPath):
        path = self.path + folderPath

        if os.path.isdir(path):
            return 1

        os.makedirs(path)

        return 0
    
    def deleteDir(self, folderPath):
        path = self.path + folderPath

        if not os.path.isdir(path):
            return 1

        os.rmdir(path)

        return 0

    def listDir(self, folderPath):
        path = self.path + folderPath

        if not os.path.isdir(path):
            return 1, ""

        lists = []

        for _, dirs, _ in os.walk(path):  
            for dirname in dirs:
                lists.append(dirname)

        return 0, lists

    def moveFile(self, srcFile, dstFolder):
        fileName = srcFile.split('/')[-1]
        src = self.path + srcFile
        des = self.path + dstFolder

        if not os.path.isfile(src):
            return 1

        if not os.path.isdir(des):
            return 2

        des = des + '/' + fileName
        os.rename(src, des)

        return 0

    def moveDir(self, srcFolder, dstFolder):
        folderName = srcFolder.split('/')[-1]
        src = self.path + srcFolder
        des = self.path + dstFolder

        if not os.path.isdir(src) or not os.path.isdir(des):
            return 1

        des = des + '/' + folderName
        os.rename(src, des)

        return 0