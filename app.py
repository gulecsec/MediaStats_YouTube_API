import streamlit as st
import pandas as pd

header = st.container()
dataset= st.container()
features = st.container()

@st.cache_data
def get_data(filename):
    video_df = pd.read_csv(filename)
    return video_df

with header:
    st.title("How Turkish News Media's YouTube Stats Stack Up: Exploring the Data on My Streamlit App")
    st.markdown("In this tutorial, we'll explore how to use the YouTube API with Python to interact with one of the world's largest video-sharing platforms,which boasts billions of daily users uploading, viewing, and commenting on videos. By the end of this tutorial, you'll know how to automate various tasks using the YouTube API.")

with features:
    st.header("")
    st.text("")

with dataset:
    st.subheader("YouTube Stats of Turkish News Media in YouTube")
    years=[ i for i in range(2010, 2024)]

    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    channels = ["Cuneyt Ozdemir Media", "AHaber"]
    video_df = get_data("/workspaces/MediaStats_YouTube_API/mediastats_cuneytozdemir.csv")

    # selected_media =
    selected_year = st.sidebar.selectbox("Select Year", [""] + years, index=0)
    selected_month = st.sidebar.selectbox("Select Month", [""] + months, index=0)
    if selected_year != "" and selected_month != "":
        filtered_df = video_df.loc[(video_df["Year"]==selected_year) & (video_df["Month"]==selected_month)]
    else:
        filtered_df = video_df
    # if st.session_state.get('refresh', False):
    #     selected_year = ""
    #     selected_month = ""
    #     st.session_state['refresh'] = False
    # if selected_year != "" and selected_month != "":
    #     filtered_df = video_df.loc[(video_df["Year"]==selected_year) & (video_df["Month"]==selected_month)]
    # else:
    #     filtered_df = video_df

    st.session_state.selected_year = selected_year
    st.session_state.selected_month = selected_month

    # if st.button("Refresh"):
    #     st.session_state['refresh'] = True
    #     st.experimental_rerun()

    # Display the DataFrame
    st.write(filtered_df)


st.markdown('''

''')

'''
## However, before we jump into the code, we'll need to create a project in the Google Developers Console and obtain an API key.

### Step 1: Set Up a Project in the Google Developers Console
To use the YouTube API with Python, you first need to create a project in the Google Developers Console and obtain an API key. Here are the steps:
1. Go to the Google Developers Console (https://console.developers.google.com/).
2. Click on the project drop-down menu at the top of the screen and select "New Project" or an existing project that you want to use for the API.
3. Enter a name for your project and click on the "Create" button.
4. Once the project is created, click on the hamburger menu at the top-left corner of the screen and select "APIs & Services" > "Library" from the navigation menu.
5. In the search bar, type "YouTube Data API" and click on the result.
6. Click on the "Enable" button to enable the API for your project

### Step 2: Obtain the API Key
1. Next, click on the "Create Credentials" button to create a new set of credentials for your project.
2. Select "API key" as the type of credentials and choose the "Restricted key" option.
3. Set up any necessary restrictions for your API key, such as IP address or HTTP referrers.
4. Click on the "Create" button to generate your API key.
5. The API key will be displayed. Copy the key and keep it safe.

### Step 3: Install the Google API Client Library for Python
The Google API Client Library for Python makes it easy for developers to access Google APIs. To install the library, run the following command in your terminal or command prompt:
pip install --upgrade google-api-python-client

### Step 4: Make API Requests
Now that we have the API key and the library installed, we can start making API requests. Here’s a simple example that retrieves the details of a video:

from googleapiclient.discovery import build

api_service_name = "youtube"
api_version = "v3"

### Step 5: Get credentials and create an API client
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

In this example, the build function creates a YouTube service object that we can use to make API requests. The videos().list() method retrieves the details of a video, and the execute() method sends the request and returns the response.
Note: Replace YOUR_API_KEY with your own API key.

### Step 6: Analyze the Response
The response is a JSON object that contains the details of the video, including the title, description, view count, like count, and more. Here’s a simple example that prints the title and view count of the video:

By following these easy steps, you can now begin using the YouTube API with Python to streamline various tasks and collect valuable information about videos, channels, playlists, and beyond. Moreover, the API provides additional functionality such as:

* Search for videos: You can use the search.list method to search for videos based on keywords, location, language, and other criteria.

* Retrieve channel details: You can use the channels.list method to retrieve information about a channel, including the number of subscribers, videos, and views.

* Retrieve playlist details: You can use the playlists.list method to retrieve information about a playlist, including the videos, title, and description.

The YouTube API and Python provide a wide range of possibilities for automation, data gathering, and feature creation. Whether you want to build a tool to analyze videos or automate repetitive tasks, the API and the Google API Client library can help you achieve your goals.

By utilizing the capabilities of the YouTube API and Python, you can create innovative and robust applications that can assist in automating tasks, gathering data, and adding new functionalities to your projects. However, it is essential to adhere to the API's terms of service and usage guidelines and to obtain an API key from the Google Cloud Console to ensure ethical and responsible use.

'''
