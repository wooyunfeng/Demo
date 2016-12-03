import glob,os
cnt=0
for filename in glob.glob(r'C:\Users\Administrator.USER-20160908DM\Desktop\CSDN_expert\*.jpg'):
    print filename
    print filename[:-4]
    os.rename(filename,filename[:-4])
    cnt=cnt+1
print cnt
