from PIL import Image
# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('file')
# parser.add_argument('-o','--output')
# parser.add_argument('--width',type = int,default=80)
# parser.add_argument('--height',type = int,default=80)
#
# args =parser.parse_args()
#
# IMG = args.file
# WIDTH = args.width
# HEIGHT =args.height
# OUTPUT = args.output

IMG = '1.png'

OUTPUT = input('enter name:\n')

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ''
    length =len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__=='__main__':

    im = Image.open(IMG)
    wid,het = im.size
    if wid > 150:
        trans = wid / 150
        wid =150
        het = int(het /trans)
    print(wid,'*',het)
    WIDTH = wid
    HEIGHT = het
    input("press anykey to continue\n")
    # Image.Nearest 是个int
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)

    txt = " "*50

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
        txt += " "*50
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt","w") as f:
            f.write(txt)


