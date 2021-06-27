float x = 100;
float y = 0;
float alpha = 0;

void setup() {
  size(800, 800);
  frameRate(60);
}

void draw() {
  translate(400, 400);
  strokeWeight(2);
  line(0, -350, 0, 350);
  line(-350, 0, 350, 0);
  strokeWeight(4);
  scale(1,-1);
  rotate(alpha);
  point(x * (1 + alpha/PI), y);
  alpha += PI/240;
}
