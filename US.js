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
