import os
from PIL import Image
def main():
    for filename in os.listdir(os.path.join(os.curdir, "images")):
        if filename.endswith('.jpg'):
            try:
                img = Image.open(os.path.join(os.curdir, "images", filename)) 
                img.verify()  
            except (IOError, SyntaxError) as e:
                try:
                    os.remove(filename)
                    break
                except:
                    pass
        if (os.path.getsize(os.path.join(os.curdir, "images", filename)) < 10000):
            os.remove(os.path.join(os.curdir, "images", filename))
        else:
            print(filename)

main()