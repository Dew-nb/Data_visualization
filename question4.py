import turtle
import time

def star(t,length,pcolor,fcolor):
	t.pencolor(pcolor);
	t.seth(36);
	t.fillcolor(fcolor);
	t.begin_fill();
	for i in range(5):
		t.forward(length);
		t.right(72);
		t.forward(length);
		t.left(144);
	t.end_fill();

def rectanger(t,a,b,pcolor,fcolor):
	t.fillcolor(fcolor);
	t.pencolor(pcolor);
	t.begin_fill();
	t.fd(360);
	t.left(90);
	t.fd(80);
	t.left(90);
	t.fd(360);
	t.left(90);
	t.fd(80);
	t.left(90);
	t.end_fill();

def movepen(t,a,b):
	t.penup();
	t.goto(a,b);
	t.pendown();

if __name__ == '__main__':
	t=turtle.Pen();
	#上面的红色矩形
	t.speed(10);
	movepen(t,-180,40);
	rectanger(t,360,80,'red','red');
	#下面的黑色矩形
	movepen(t,-180,-120);
	rectanger(t,360,80,'black','black');
	#绿色的五角星
	movepen(t,-100,-15);
	star(t,15,'green','green');
	movepen(t,70,-15);
	star(t,15,'green','green');
	time.sleep(3);
