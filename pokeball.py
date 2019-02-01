#! /usr/bin/python3
import math

def generate(width,height):
    return [[[255,255,255] for i in range(width)] for j in range(height)]

def output(fileName, img):
    out="P3\n"+str(len(img[0]))+" "+str(len(img))+"\n255\n"
    for row in img:
        for pixel in row:
            for color in pixel:
                out+=str(color)+" "
            out+=" "
        out+="\n"
    f=open(fileName,"w")
    f.write(out)
    f.close()

def fadeRing(img,minRad,maxRad,centerRow,centerCol,color):
    for rad in range(minRad,maxRad):
        for row in range(len(img)):
            if(rad**2-(row-centerRow)**2)>=0:
                if(int(round(math.sqrt(rad**2-(row-centerRow)**2)+centerCol))<len(img[row]))and(int(round(math.sqrt(rad**2-(row-centerRow)**2)+centerCol))>=0):
                    img[row][int(round(math.sqrt(rad**2-(row-centerRow)**2)+centerCol))]=color
                if(int(round(-math.sqrt(rad**2-(row-centerRow)**2)+centerCol))<len(img[row]))and(int(round(-math.sqrt(rad**2-(row-centerRow)**2)+centerCol))>=0):
                    img[row][int(round(-math.sqrt(rad**2-(row-centerRow)**2)+centerCol))]=color
    return img

def ring(img,minRad,maxRad,centerRow,centerCol,color):
    for row in range(len(img)):
        for col in range(len(img[row])):
            if (row-centerRow)**2+(col-centerCol)**2>=minRad**2 and (row-centerRow)**2+(col-centerCol)**2<=maxRad**2:
                img[row][col]=color
    return img
    
def rect(img,width,height,TLrow,TLcol,color):
    for row in range(height):
        for col in range(width):
            if TLrow+row<len(img) and TLcol+col<len(img[0]):
                img[TLrow+row][TLcol+col]=color
    return img

img=generate(501,501)
img=ring(img,70,230,250,250,[255,0,0])
img=rect(img,200,20,240,0,[0,0,0])
img=rect(img,200,20,240,300,[0,0,0])
img=rect(img,500,250,260,0,[255,255,255])
img=ring(img,230,250,250,250,[0,0,0])
img=ring(img,50,70,250,250,[0,0,0])
output("pokeball.ppm",img)
