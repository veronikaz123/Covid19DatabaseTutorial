let table;

function preload() {
  table = loadTable('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv', 'csv','header');
}

function setup() {
  createCanvas(windowWidth, windowHeight);
	background(100);
	text('antal rækker: ' + table.getRowCount(),600,400);
	text('antal søjler: ' + table.getColumnCount(),600,420);
  Italy = table.findRow('Italy','Country/Region');
  print(Italy);
  print(Object.keys(Italy));
  print(Italy.table.columns[4]);
  print(Italy.get(2));

}

function draw(){

}
