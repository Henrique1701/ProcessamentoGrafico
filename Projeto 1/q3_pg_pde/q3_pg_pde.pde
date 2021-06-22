float a, b; //<>//
float r = -20;
float rAux = -20;
float x = -20;
float pos = 0.1f;
boolean posAux1 = false;
boolean posAux2 = true;

void strokeTest(float r, float x, float step){
    a = 240 +  r * cos(pos/8);
    b = 320 +  r * sin(pos/8);
    stroke(155, 0, 0);
    fill(155,0,0);
    ellipse(a, b, 3, 3);
    strokeCap(ROUND);

    pos+=step;
}

void setup(){
  size(480, 640);

}
void draw(){
  line(width/2, height, width/2, 0);
  stroke(0, 0, 255);
  line(0, height/2, width, height/2);
  stroke(0, 255, 0);
  strokeTest (r, x, -0.1);

  if(a > (width/2) && posAux2 != posAux1){
    posAux1 = true;
  }
   
   if(a < (width/2) && posAux2 != posAux1){
    posAux1 = false;
  }

  if(posAux2 == posAux1){
     if(r != (2 * r)){
       r = r + (rAux/120);
     }
     else{
       posAux2 = !posAux2;
       rAux = 4 * rAux;
     }
  }

}
