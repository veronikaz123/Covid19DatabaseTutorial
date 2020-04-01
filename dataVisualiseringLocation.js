/*
Iterere over kolonne navnene og antallet af smittede i Italien
*/

let table;
let count=5;

function preload() {
  table = loadTable('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv', 'csv','header');
}

function setup() {
  createCanvas(windowWidth,windowHeight);
  background(0,100,200);
  Italy = table.findRow('Italy','Country/Region');
  head = table.columns;
  textSize(60);
  fill(200);
  frameRate(10);
}

function draw(){
  background(0,100,200);
  lat = table.getColumn('Lat');
  long = table.getColumn('Long');
  print(long[1]);
  for (i=0;i<200;i++){
    ellipse(400-long[i]*2,400-lat[i]*2,5,5);
  }
  noLoop();
}
