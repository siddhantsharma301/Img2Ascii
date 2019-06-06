import sys, random, argparse 
import numpy as np 
import math 
from PIL import Image

ASCII_CHARS = '@%#*+=-:. '

def avgLuminosity(image): 
    img = np.array(image) 
    w,h = img.shape 
    return np.average(img.reshape(w * h)) 

def image2Ascii(file, cols, scale): 
    global ASCII_CHARS 
    image = Image.open(file).convert('L') 
    W, H = image.size[0], image.size[1] 
    w = W / cols 
    h = w / scale
    rows = int(H / h) 
    if cols > W or rows > H: 
        print("Image too small for specified cols!") 
        exit(0) 
    ascii_img = [] 
    for j in range(rows): 
        y1 = int(j * h) 
        y2 = int((j +1 ) * h)  
        if j == rows - 1: 
            y2 = H 
        ascii_img.append("") 
        for i in range(cols):  
            x1 = int(i * w) 
            x2 = int((i + 1) * w) 
            if i == cols - 1: 
                x2 = W 
            img = image.crop((x1, y1, x2, y2))
            avg = int(avgLuminosity(img))  
            ascii_img[j] += ASCII_CHARS[int((avg * 9) / 255)] 
    return ascii_img 

def main(): 
    descStr = "Converts an image to ASCII art"
    ap = argparse.ArgumentParser(description = descStr) 
    ap.add_argument('-f', '--file', dest = 'img', required = True) 
    ap.add_argument('-s', '--scale', dest = 'scale', required = False) 
    ap.add_argument('-o', '--out', dest = 'out', required = False) 
    ap.add_argument('-c', '--cols', dest = 'cols', required = False) 
    args = ap.parse_args() 
    img = args.img 
    out = 'out.txt'
    if args.out: 
        out = args.out 
    scale = 0.43
    if args.scale: 
        scale = float(args.scale)
    cols = 80
    if args.cols: 
        cols = int(args.cols)
    ascii_img = image2Ascii(img, cols, scale)
    f = open(out, 'w')
    for row in ascii_img: 
        f.write(row + '\n')
    f.close() 
    print("ASCII art written to %s" % out) 

if __name__ == '__main__': 
    main() 
