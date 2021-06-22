float x = 300;
float y = 300;
 
float position = 0.1;
 
void circles(float r, float step){
   
  float x1 = x +  r*cos(position);
  float y1 = y +  r*sin(position);
 
  ellipse(x1, y1, 50, 50);
  
  stroke(0, 0, 255);
  strokeCap(ROUND);
  stroke(255, 0, 0);
  x1 = x1 + 25f*cos(position*4);
  y1 = y1 + 25f*sin(position*4);
  fill(255, 0, 0);
  circle(x1, y1, 5);
  
  position+=step; 
}

void setup (){
  size(640, 480);
  frameRate(15);
}
 
void draw (){ 
  background(255);
  fill(255);
  stroke(0, 0, 255);
  ellipse(x, y, 250, 250);
  circles(100, -0.1);
}
