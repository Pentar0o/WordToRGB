import re
import sys
import time
import hashlib
from PIL import Image, ImageDraw, ImageFont

def colors(s):
    result = hashlib.sha1(s.encode())
    chif=str(int(result.hexdigest(), 16))[0:15]
    rgb=[]

    for i in range(0,15,5):
        color= int(chif[i:i+5])%256
        rgb.append(color)

    return rgb


def cutoup(phrase):

    return re.compile('\w+').findall(phrase)



def main(phrase):
    
    image = Image.new("RGB", (800, 800), "white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("Arial.ttf", 40)

    mots = cutoup(phrase)
    
    y = 0
    
    for mot in mots :
        color = colors(mot)
        print("La Couleur du mot " + mot + " est : " + str(color) )
        draw.text((10, y), mot,fill=(color[0],color[1],color[2]), font=font)
        y += 40

    image.save('test.jpg')


if __name__ == '__main__':
    if len(sys.argv) < 1:
        print('USAGE: {} phrase'.format(sys.argv[0]))
    else:
        t1 = time.time()
        main(sys.argv[1])
        print('Temps de Traitement : %d s'%(time.time()-t1))