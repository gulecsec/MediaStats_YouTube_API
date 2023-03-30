<html>
<head>

</head>
<body>
  <h1>YouTube Stats of Turkish News Media</h1>
  <p>This project aims to analyze the popularity and engagement of YouTube channels belonging to Turkish news media by scraping their statistics. Additionally, it creates a word cloud of the top 50 most used words in the titles of the channel's videos to provide further insights.</p>
  <h2>Data Collection and Analysis</h2>
  <p>The project uses the YouTube Data API v3 to scrape data for the channels of Turkish news media. The scraped data includes information about the number of views, likes, durations, and comments for each video, as well as statistics about the channel itself, such as subscriber count and total views. The data is then analyzed to gain insights about the performance and engagement of the channels.</p>
  <h2>Usage</h2>
  <p>To use the application:</p>
  <ol>
    <li>Clone this repository.</li>
    <li>Install the required packages by running <code>pip install -r requirements.txt</code> in your terminal.</li>
    <li>Run <code>python app.py</code> in your terminal.</li>
    <li>Open <code>http://localhost:8501</code> in your web browser.</li>
    <li>Select a YouTube channel from the dropdown list.</li>
    <li>View the statistics and word cloud for the selected channel.</li>
  </ol>
  <h2>Credits</h2>
  <p>Base Code is inspired by <a href="https://github.com/thu-vu92/youtube-api-analysis">thu-vu92</a>.</p>
  <p>Word cloud generated using the WordCloud package in Python.</p>
  <p>Data scraped using the googleapiclient and pandas packages in Python.</p>
  <p>Web application built using the streamlit package in Python.</p>
  <p>Data Visualization designed using the plotly.express package in Python.</p>
</body>
</html>
