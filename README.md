<!DOCTYPE html>
<html>
<head>

</head>
<body>
  <h1>YouTube Stats of Turkish News Media</h1>
  <p>This project aims to analyze the popularity and engagement of 15 YouTube channels belonging to Turkish news media by scraping their statistics.</p>

  <h2>Data Collection and Analysis</h2>
  <p>The project uses the YouTube Data API v3 to scrape data for the channels of Turkish news media. The scraped data includes information about the number of views, likes, durations, and comments for each video, as well as statistics about the channel itself, such as subscriber count and total views. The data is then analyzed to gain insights about the performance and engagement of the channels.</p>

  <h2>Usage</h2>
  <ol>
    <li>Clone this repository.</li>
    <li>Install the required packages by running <code>pip install -r requirements.txt</code> in your terminal.</li>
    <li>Run <code>python app.py</code> in your terminal.</li>
    <li>Open <code>http://localhost:8501</code> in your web browser.</li>
    <li>Select a YouTube channel from the dropdown list.</li>
    <li>View the statistics and word cloud for the selected channel.</li>
  </ol>

  <h2>View the App</h2>
  <p>You can also view the analysis of the YouTube channels by using my Streamlit app. Please click <a href="https://gulecsec-mediastats-youtube-api-app-f7eqyr.streamlit.app/">here</a> to access the app.</p>

  <h2>Credits</h2>
  <p>Special thanks to <a href="https://github.com/thu-vu92">Thu.</a> This project is inspired by <a href="https://github.com/thu-vu92/youtube-api-analysis">thu-vu92's YouTube API Analysis project</a>.</p>
  <p>The data is scraped using the googleapiclient and pandas packages in Python.</p>
  <p>The web application is built using the streamlit package in Python.</p>
  <p>The data visualization is designed using the plotly.express package in Python.</p>
</body>
</html>
