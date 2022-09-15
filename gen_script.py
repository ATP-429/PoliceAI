import os

number = 1000
maxxangle = 1.0
maxyangle = 1.0
maxzangle = 1.7
width = 24
height = 24
positive = "knife_dataset/knife_rev.png"
info = "positives2/positives2.txt"

# GENERATE POSITIVES BY RANDOM PLACEMENT OF KNIVES IN NEGATIVE IMAGES [BACKGROUNDS]
cmd = f"opencv_createsamples -img {positive} -bg negatives.txt -num {number} -bgcolor 255 -bgthresh 8 -maxxangle {maxxangle} -maxyangle {maxyangle} -maxzangle {maxzangle} -info {info}"
os.system(cmd)
#cmd = f"opencv_createsamples -info positives2/positives2.txt -vec positives/positives.vec -num {number} -w {width} -h {height}"
os.system(cmd)

#opencv_traincascade -data output3 -vec positives/positives.vec -bg negatives.txt -numPos 1000 -numNeg 1500 -numStages 10 -precalcValBufSize 6000 -precalcIdxBufSize 6000 -featureType HAAR -w 24 -h 24 -minHitRate 0.95 -maxFalseAlarmRate 0.05

#f0 = open('positives.txt', 'w')
#for i in range(N):
#    f = open(f'{i:04}.txt', 'r')
#    f0.write(f.read())
#    f.close()
#   
#f0.close()

