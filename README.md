## Description
This repository has two apps: 
1. **Data Scraper**. The app collects the lowest and the highest temperatures by day data in Kyiv from [Accuweather](accuweather.com) based on the user's time interval into a CSV file.
2. **Data Visualization**. It makes an interactive graph based on the collected data.

<details>
  <summary>Scraper details</summary>
  The user inputs the interval in months depending on available ones from the app's message.
  So the app creates a CSV file and writes the months list to the first row and labels in the second.
  Then it starts collecting min and max temperatures for every day of each month from the user's interval into a table of the CSV file.
  A source has the data only for a month per page. Therefore URLs for parsing build automatically depending on the input interval. 
  When all of the temperatures are collected - the CSV file will be opened automatically.
</details>
<details>
  <summary>Visualization details</summary>
  You can see two lines on the diagram, a blue one - the lowest temperatures and a red one - the highest temperatures per day.
  The graph is interactive. So you can get information about every point, scale the graph or disable lines.
</details>

## Stack
**Python, Plotly, BeautifulSoup4, CSV**

## Demo
![Animation](https://user-images.githubusercontent.com/44866199/167425414-b3cac685-f7d1-4548-b947-89879351638a.gif)
For the demo example, the chosen interval is April 2021 - October 2021.
