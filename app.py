import streamlit as st
import pandas as pd

# Data viz packages
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Load data
stats_df = pd.read_csv("media_stats/media_stats.csv")

# Define page layout
header = st.container()
dataset = st.container()
features = st.container()
channel_details = st.container()

# Define sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "Top 10 Videos by Like Count and View Count","Google Developers Console"))

if page == "Home":
    with header:
        st.title("How Turkish News Media's YouTube Stats Stack Up: Exploring the Data on My Streamlit App")
        st.markdown("In this tutorial, we'll explore how to use the YouTube API with Python to interact with one of the world's largest video-sharing platforms,which boasts billions of daily users uploading, viewing, and commenting on videos. By the end of this tutorial, you'll know how to automate various tasks using the YouTube API.")

    with features:
        st.header("")
        st.text("")

    with dataset:
        st.subheader("YouTube Stats of Turkish News Media in YouTube")

        # add radio button to select between the two graphs
        graph_choice = st.radio("Select graph", options=["Views-Total Videos", "Subscribers-Total Videos"])

        # display the selected graph
        if graph_choice == "Views-Total Videos":
            fig = px.bar(data_frame=stats_df.sort_values('views', ascending=False),
                          x="channelName", y="views", color='totalVideos', title="Views-Total Videos")
        else:
            fig = px.bar(data_frame=stats_df.sort_values('subscribers', ascending=False),
                          x="channelName", y="subscribers", color='totalVideos', title="Subscribers-Total Videos")
        st.plotly_chart(fig)

if page == "Google Developers Console":
    with header:
        st.header("However, before we jump into the code,we'll need to create a project in the Google Developers Console and obtain an API key.")

        st.subheader("Step 1: Set Up a Project in the Google Developers Console")
        st.text("""
                To use the YouTube API with Python, you first need to create a project in the Google Developers Console and obtain an API key. Here are the steps:
                1. Go to the Google Developers Console (https://console.developers.google.com/).
                2. Click on the project drop-down menu at the top of the screen and select "New Project" or an existing project that you want to use for the API.
                3. Enter a name for your project and click on the "Create" button.
                4. Once the project is created, click on the hamburger menu at the top-left corner of the screen and select "APIs & Services" > "Library" from the navigation menu.
                5. In the search bar, type "YouTube Data API" and click on the result.
                6. Click on the "Enable" button to enable the API for your project""")

        st.subheader("Step 2: Obtain the API Key")
        st.text("""
                1. Next, click on the "Create Credentials" button to create a new set of credentials for your project.
                2. Select "API key" as the type of credentials and choose the "Restricted key" option.
                3. Set up any necessary restrictions for your API key, such as IP address or HTTP referrers.
                4. Click on the "Create" button to generate your API key.
                5. The API key will be displayed. Copy the key and keep it safe.""")

        st.subheader("Step 3: Install the Google API Client Library for Python")
        st.text("""
                The Google API Client Library for Python makes it easy for developers to access Google APIs.To install the library, run the following command in your terminal or command prompt:
                    pip install --upgrade google-api-python-client

                """)

        st.subheader("Step 4: Make API Requests")
        st.text("""
                Now that we have the API key and the library installed, we can start making API requests. Here’s a simple example that retrieves the details of a video:

                    from googleapiclient.discovery import build

                    api_service_name = "youtube"
                    api_version = "v3"
                """)

        st.subheader("Step 5: Get credentials and create an API client")
        st.text("""
                In this example, the build function creates a YouTube service object that we can use to make API requests. The videos().list() method retrieves the details of a video, and the execute() method sends the request and returns the response. Note: Replace YOUR_API_KEY with your own API key.

                    youtube = build(
                    api_service_name, api_version, developerKey=api_key)

                    def get_channel_stats(youtube, channel_ids):

                    all_data = []
                    request = youtube.channels().list(
                        part="snippet,contentDetails,statistics",
                        id=','.join(channel_ids)
                    )
                    response = request.execute()

                    # loop through items
                    for item in response['items']:
                        data= {'channelName': item['snippet']['title'],
                            'subscribers': item['statistics']['subscriberCount'],
                            'views': item['statistics']['viewCount'],
                            'totalVideos': item['statistics']['videoCount'],
                            'playlistId': item['contentDetails']['relatedPlaylists']['uploads']
                            }

                        # Check if the channel has any subscriber milestone
                        if 'bulletin' in item['contentDetails']:
                            milestone = item['contentDetails']['bulletin']['resource']
                            if milestone['kind'] == 'youtube#subscription':
                                data['milestoneDate'] = milestone['publishedAt']
                                data['milestoneSubscribers'] = milestone['metadata']['subscriberCount']

                        all_data.append(data)

                    return(pd.DataFrame(all_data))
                        """)

        st.subheader("Step 6: Analyze the Response")
        st.text("""
        The response is a JSON object that contains the details of the video, including the title, description, view count, like count, and more.
        Here’s a simple example that prints the title and view count of the video:

        By following these easy steps, you can now begin using the YouTube API with Python to streamline various tasks and collect valuable information about videos, channels, playlists, and beyond. Moreover, the API provides additional functionality such as:

        * Search for videos: You can use the search.list method to search for videos based on keywords, location, language, and other criteria.

        * Retrieve channel details: You can use the channels.list method to retrieve information about a channel, including the number of subscribers, videos, and views.

        * Retrieve playlist details: You can use the playlists.list method to retrieve information about a playlist, including the videos, title, and description.

        The YouTube API and Python provide a wide range of possibilities for automation, data gathering, and feature creation. Whether you want to build a tool to analyze videos or automate repetitive tasks, the API and the Google API Client library can help you achieve your goals.

        By utilizing the capabilities of the YouTube API and Python, you can create innovative and robust applications that can assist in automating tasks, gathering data, and adding new functionalities to your projects. However, it is essential to adhere to the API's terms of service and usage guidelines and to obtain an API key from the Google Cloud Console to ensure ethical and responsible use.
                """)

elif page == "Top 10 Videos by Like Count and View Count":
    with channel_details:
        st.title("Channel Details")

        # Load Each Channel Data
        co_df = pd.read_csv("media_stats/stats_cüneyt_özdemir.csv")
        bab_df = pd.read_csv("media_stats/stats_babala_tv.csv")
        ahaber_df = pd.read_csv("media_stats/stats_a_haber.csv")
        aa_df = pd.read_csv("media_stats/stats_anadolu_ajansi.csv")
        bbc_df = pd.read_csv("media_stats/stats_bbc_news_turkce.csv")
        cnn_df = pd.read_csv("media_stats/stats_cnn_turk.csv")
        fox_df = pd.read_csv("media_stats/stats_fox_haber.csv")
        ht_df = pd.read_csv("media_stats/stats_haberturk_tv.csv")
        soz_df = pd.read_csv("media_stats/stats_sozcu_televizyonu.csv")
        



        # create a dictionary to store data frames and graph titles for each channel
        channel_data = {
        'Cüneyt Özdemir': {'df': co_df, 'title': 'Cüneyt Özdemir Top 10 Videos by Like Count and View Count'},
        'BaBaLa TV': {'df': bab_df, 'title': 'BaBaLa TV Top 10 Videos by Like Count and View Count'},
        'A Haber': {'df': ahaber_df, 'title': 'A Haber Top 10 Videos by Like Count and View Count'},
        'Anadolu Ajansi': {'df': aa_df, 'title': 'Anadolu Ajansi Top 10 Videos by Like Count and View Count'},
        'BBC News Turkce': {'df': bbc_df, 'title': 'BBC News Turkce Top 10 Videos by Like Count and View Count'},
        'CNN Turk': {'df': cnn_df, 'title': 'CNN Turk Top 10 Videos by Like Count and View Count'},
        'FOX Haber': {'df': fox_df, 'title': 'FOX Haber Top 10 Videos by Like Count and View Count'},
        'Haberturk': {'df': ht_df, 'title': 'Haberturk Top 10 Videos by Like Count and View Count'},
        'Sozcu Televizyonu': {'df': soz_df, 'title': 'Sozcu Televizyonu Top 10 Videos by Like Count and View Count'},
        'TRT Haber': {'df': trt_df, 'title': 'TRT Haber Top 10 Videos by Like Count and View Count'},
        }

        # add dropdown to select a channel
        channel_choice = st.selectbox("Select Channel", stats_df["channelName"].unique())
        year_choice = st.selectbox("Select Year", co_df["Year"].sort_values(ascending=False).unique().tolist())
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month_choice = st.selectbox("Select Month", months)

        # filter data based on user's selection
        df = channel_data[channel_choice]['df']
        df = df[(df['Year'] == year_choice) & (df['Month'] == month_choice)]

        # generate plotly graph
        fig = px.bar(data_frame=df.sort_values('likeCount', ascending=False)[0:9],
                    x="title", y="likeCount", color='viewCount', title=channel_data[channel_choice]['title'])

        # format y-axis labels to show thousands
        fig.update_yaxes(tickformat=',.0f')

        # remove x-axis tick labels
        fig.update_layout(xaxis={'tickmode': 'array', 'tickvals': []})

        # display plotly graph
        st.plotly_chart(fig)
