/*
Indlæsning af dataset fra URL og print karakteristika.
Se consolen i Chrome View->Developer->JavaScript console.
Der kommer nogen fejlmeddelser som I skal se bort fra.
*/



let table;

function preload() {
  table = loadTable('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv', 'csv','header');
}

function setup() {
	print('antal rækker: ' + table.getRowCount());
	print('antal søjler: ' + table.getColumnCount());
//  Italy = table.findRow('Italy','Country/Region');
//  print(Italy);
//  print(Object.keys(Italy));
//  print(Italy.table.columns);
//  print(Italy.get(2));
}

function draw(){

}
