#import sys
#print(sys.path)
#sys.path.append('/tmp/work/python-ftgl/build/lib.linux-armv7l-2.7')
#sys.path.append('/tmp/work/python-ftgl/build/lib.linux-armv7l-2.7/ftgl')
import ftgl
#from ftgl import ftgl
print(dir(ftgl))
#font = ftgl.FTGLPixmapFont("Arial.ttf")
font = ftgl.FTPixmapFont("/usr/share/fonts/truetype/vlgothic/VL-Gothic-Regular.ttf")
font.FaceSize(72)
font.Render("Hello World!")

