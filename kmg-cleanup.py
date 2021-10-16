
# Keep  only accepted folders

import os
import shutil

def cleanup(dirName):
    # List comprehension to enter
    # all directories to list

    #L = [(root, dirs, files) for root, dirs, files, in os.walk(dirName)]
    folders = os.listdir(dirName)

    for folder in folders:
        try:
             more = os.listdir(dirName+"/"+folder)
             for tmp in more:
                 if tmp == 'Solution.py':
                     x = dirName+"/"+folder +"/"+ tmp
                     y =  dirName+"/"+folder +"/"+ folder+".py"
                     os.rename(x,y)
        except:
            pass

if __name__=="__main__":
    cleanup("/Users/kmg/projects/kmg-leetcode")