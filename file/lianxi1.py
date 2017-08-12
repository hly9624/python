import os

def sj(rootDir,outPutFile):
    fw = open(outPutFile,'w')

    for dirName in os.listdir(rootDir):
        if os.path.isdir(os.path.join(rootDir,dirName)):
            print 'process in dir:%s'%dirName
            for 
