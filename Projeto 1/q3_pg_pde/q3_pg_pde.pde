float x = 100;
float y = 0;
float alpha = 0;

void setup() {
  size(800, 800);
  frameRate(30);
}

void draw() {
  translate(400, 400);
  scale(1,-1);
  rotate(alpha);
  point(x * alpha, y);
  alpha += PI/120;
}
