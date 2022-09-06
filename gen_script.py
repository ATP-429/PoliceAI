import os

number = 3000
maxxangle = 1.0
maxyangle = 1.0
maxzangle = 1.0
width = 24
height = 24
positive = "knife_dataset/0000.png"

# GENERATE POSITIVES BY RANDOM PLACEMENT OF KNIVES IN NEGATIVE IMAGES [BACKGROUNDS]
cmd = f"opencv_createsamples -img {positive} -bg negatives.txt -num {number} -bgcolor 255 -bgthresh 8 -w {width} -h {height} -maxxangle {maxxangle} -maxyangle {maxyangle} -maxzangle {maxzangle} -info positives/positives.txt"
os.system(cmd)

#f0 = open('positives.txt', 'w')
#for i in range(N):
#    f = open(f'{i:04}.txt', 'r')
#    f0.write(f.read())
#    f.close()
#   
#f0.close()

