from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



def init():
   glClearColor(0.0,0.0,0.0,1.0)
   glColor3f(0.0,0.0,1.0)
   glPointSize(2.0)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   gluOrtho2D(-100,100,-100,100)

def plot(x,y):
  glBegin(GL_POINTS)
  glVertex2i(x,y)
  glEnd()
  glFlush()

def plotpolar(xc, yc, x, y):
    plot ( x + xc, y + yc)
    plot ( x + xc, -y + yc)  
    plot ( -x + xc, -y + yc)  
    plot ( -x + xc, y + yc)  
    plot ( y + xc, x + yc)  
    plot ( y + xc, -x + yc)  
    plot ( -y + xc, -x + yc)  
    plot ( -y + xc, x +yc)  
   
   

 
def polar( xc, yc, r):
  x= 0
  y= r
  d= 3 - 2 * r
  
  
  while x<=y :
    
    if d<0 :
      d = d + 4 * x + 6
    else :
      y = y - 1
      d = d + 4 *( x - y) + 10
     
    
    x = x + 1
    plotpolar (xc, yc,x ,y )
    
def Display():
     glClear(GL_COLOR_BUFFER_BIT)
     polar(30,60,30)
     
def main():
   glutInit()
   glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
   glutInitWindowSize(500,500)
   glutInitWindowPosition(200,200)
   glutCreateWindow("bresenham")
   glutDisplayFunc(Display)
   init()

   glutMainLoop()
 
main()

