float x, y;
float xSpeed, ySpeed;

void setup(){
  size(640, 480);
   
  x = 0;
  y = 100;
  
  xSpeed = 5;
  ySpeed = 3;
  

}

void draw(){
  background(155);
  fill(#FF0000); //red
  rect(0, 315, width, 200);
  fill(#0085ca); //blue
  circle(x, y, 30);
  
  x = x + xSpeed;
  y = y + ySpeed;
  
  ySpeed = ySpeed + 0.5f;
  
  if(x >= width){
    xSpeed = -xSpeed;
  }else if(x <= 0){
    xSpeed = -xSpeed;
  }
  
  if(y >= 300){
    ySpeed = -ySpeed + 0.5f;
    y = 300;
    
  }else if(y <= 0){
    ySpeed = -ySpeed;
  }

}
