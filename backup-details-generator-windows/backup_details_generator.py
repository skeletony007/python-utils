## import needed libraries
from genericpath import isdir, isfile
from shutil import copyfileobj, copytree
from os.path import isdir
import sys
from datetime import datetime

def add_backup_details(file_name): ## adds backup details ('-backup-%d-%m-%Y_%H.%M.%S.%f') to file/directory path
    
    ## find where the file name extrension starts (and if there is one) using linear search
    dot=False                      ## records if there is a file name extension
    for i in range(len(file_name)):
        if(file_name[i]=="."):
            dot=True
            dot_index=i            ## record position of dot
        if(file_name[i]==" "):     ## file name extensions cannot contain spaces
            dot=False

    ## get the details to add to file name
    details=datetime.now().strftime("-backup-%d-%m-%Y_%H.%M.%S.%f")[0:30]

    ## add the details to the file name
    if(dot):                       ## e.g. "prefs-backup-17-05-2022_20.41.42.35.js"
        file_name=file_name[0:dot_index]+details+file_name[dot_index:len(file_name)]
    else:                          ## e.g. "prefs.j s-backup-17-05-2022_20.41.42.35"
        file_name=file_name+details

    return file_name               ## output file name with details

## Backup files/directories (main process)
print("New files and folders:")     ## debugging log
for i in sys.argv[1:len(sys.argv)]:    ## loop through all arguments -should be file paths -index 0 is to launch this script
    src_path=str(i)
    dst_path=add_backup_details(src_path)
    if(isdir(src_path)):            ## for directories or "folders"
        copytree(src_path, dst_path)
        print("folder "+dst_path)              ## debugging log
    if(isfile(src_path)):           ## for files (with/without extensions)
        src_file=open(src_path,"rb")
        dest_file=open(dst_path,"wb")
        copyfileobj(src_file,dest_file)
        print("file   "+dst_path)              ## debugging log
