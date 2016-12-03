
import os
f=open('a.txt')
line=f.read()
print line
f.close()
print '*************'
f=open('a.txt')
while True:
	line=f.readline()
	if line:
		print line
	else:
		break
f.close()
print '*************'
f=open('a.txt','r')
for line in f.readlines():
	print line

#http://blog.csdn.net/google19890102/article/details/49428153