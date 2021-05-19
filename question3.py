import turtle
import time

def movepen(t,a,b):
	t.penup();
	t.goto(a,b);
	t.pendown();

if __name__ == '__main__':
	color=['pink','purple','blue','green','orange','red','light blue','yellow'];
	length=[];
	size=[];
	for n in range(150,0,-5):
		length.append(n);
	for m in range(60,30,-1):
		size.append(m/3);
	t= turtle.Pen();
	i=0;
	t.speed(10);
	movepen(t,-100,-100);
	while (i<30):
		t.pencolor(color[i%8]);
		t.pensize(size[i]);
		t.fd(length[i]);
		t.left(45);
		i=i+1;
	time.sleep(2);
			