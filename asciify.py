#prog to convert pixels in images to ascii characters

from PIL import Image
# My own mapping of grayscale intensities to ASCII chars
ASCII= [ '#', '@', '%', '&', 'G', 'B', 'V', '/', ':', ',', '.']

# Step 1: Open the image using PILLOW library
def open_img(img_path):
    img=None
    try:
        img=Image.open(img_path)
        return img
    except e:
        print("---Error in opening image---",e)
        print("---Check the file path---",img_path)
        return None

# Step 2: Convert the image to grayscale since the pixels after conversion contain the intesity(brightness)
def to_grayscale(img):
    return img.convert('L')

# Step 3: Change the ascpect ratio of the Image to match the ascpect ratio of the Font
def change_aspect_ratio(img):
    new_width=100
    (org_width,org_height)=img.size
    asp_ratio=org_height/float(org_width)
    new_height=int(asp_ratio*new_width)
    img=img.resize((100,100))#If the img is distorted try changing the H,W manually to correct it.
    return img

#Step 4:Map each pixel to an ASCII char by diving the range 0-255 to n levels of intensity
def pixel_to_ascii(img):
    lvl=25
    pixels=list(img.getdata())
    ascii_img=[ASCII[int(pixel/lvl)] for pixel in pixels]
    return "".join(ascii_img)

#Step 5: Modify the ascii_img to be printable or writable to a file
def disp_img(ascii_img):
    new_width=100
    l=len(ascii_img)
    disp_img_ascii=[ascii_img[i:i+new_width] for i in range(0,l,new_width)]
    return "\n".join(disp_img_ascii)

def asciify(img_path):
    img=open_img(img_path)
    if img==None:
        return None
    else:
        img=to_grayscale(img)
        img=change_aspect_ratio(img)
        ascii_img=pixel_to_ascii(img)
        disp_img_ascii=disp_img(ascii_img)
        return disp_img_ascii
if __name__=='__main__':
    import sys

    #count=0
    #ascii_str=[]
    img_path = sys.argv[1]
    disp_img_ascii=asciify(img_path)
    if disp_img_ascii!=None:
        f=open(img_path+'ascii.txt','w+')
        f.write(disp_img_ascii)
        f.close()
