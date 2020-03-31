let table;

function preload() {
  table = loadTable('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv', 'csv','header');
}

function setup() {
  createCanvas(windowWidth, windowHeight);

  print(table.getRowCount() + ' total rows in table');
  print(table.getColumnCount() + ' total columns in table');

  frameRate(20);
  r = 20;
  countries = [96,122,118,139,203];
  colors = ['red','green','black','white','yellow'];
  print(table.findRow('Italy','Country/Region'));
}



function draw(){
  fill(200,20,0);
  //plotLocation();
  plotNumber();
  r+=1;
  if (r>table.getColumnCount()-1){
    r=30;
  }
background(0,100,200,10);
}

function plotNumber(){
  for (i=0;i<countries.length;i++){
    y=float(table.getString(countries[i],int(r)));
    fill(colors[i]);
    ellipse(r*10,600-y*10,20,20);
  }
  }




function plotLocation(){
  c =2
//cycle through the table
for (let r = 1; r < table.getRowCount()-4; r++)
//for (let r = 0; r < 50; r++)
  //for (let c = 0; c < table.getColumnCount(); c++)
  {
  //  print(table.getString(int(r), c));
  //  print(table.getString(r, c+1));
    s = max(int(table.getString(r, table.getColumnCount()-1)),1);
    s = log(s)*4;
    s=4;
    ellipse(map(int(table.getString(r, c+1)),-200,200,0,600),map(int(table.getString(r, c)),-200,200,0,600),s,s);
  }

}
