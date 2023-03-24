import streamlit as st
import pandas as pd

# Data viz packages
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Load data
stats_df = pd.read_csv("media_stats.csv")

# Define page layout
header = st.container()
dataset = st.container()
features = st.container()
channel_details = st.container()

# Define sidebar
st.sidebar.title("Pages")
page = st.sidebar.radio("Go to", ("Home", "Google Developers Console", "Top 10 Videos by Like Count and View Count","Turkish News Media's YouTube Stats"))

if page == "Home":
    with header:
        st.title("How Turkish News Media's YouTube Stats Stack Up: Exploring the Data on My Streamlit App")
        st.markdown("In this tutorial, we'll explore how to use the YouTube API with Python to interact with one of the world's largest video-sharing platforms,which boasts billions of daily users uploading, viewing, and commenting on videos. By the end of this tutorial, you'll know how to automate various tasks using the YouTube API.")

    with features:
        st.header("")
        st.text("")

    with dataset:
        # st.subheader("")

        # add radio button to select between the two graphs
        graph_choice = st.radio("Select graph", options=["Views-Total Videos", "Subscribers-Total Videos"])

        # display the selected graph
        if graph_choice == "Views-Total Videos":
            fig = px.bar(data_frame=stats_df.sort_values('views', ascending=False),
                          x="channelName", y="views", color='totalVideos')

        else:
            fig = px.bar(data_frame=stats_df.sort_values('subscribers', ascending=False),
                          x="channelName", y="subscribers", color='totalVideos')


        fig.update_layout(coloraxis_colorbar=dict(title="Total Videos"))

        fig.update_layout(xaxis_title=None)
        fig.update_layout(yaxis_title=None)

        st.plotly_chart(fig)

if page == "Google Developers Console":
    with header:
        st.title("Channel Details")
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

if page == "Turkish News Media's YouTube Stats":
    with channel_details:
        st.title("Turkish News Media's YouTube Stats")

        # Load Each Channel Data
        edited_stats_df = pd.read_csv("media_stats_edited.csv")

        # Define sidebar
        st.sidebar.title("Video Stats")
        page = st.sidebar.radio("Go to", ("Views-Video Durations After", "Likes-Video Durations After", "Comments-Video Durations After",
        "Likes per Video", "Views per Video", "Comments per Video", "Durations per Video", "Views per Likes", "Uploaded Video Count",
        "Monthly Average Video Mins", "Monthly Average Video Likes", "Subscribers per Video"))

        if page == "Views-Video Durations After":
            with channel_details:
                st.title("")

            # create a new DataFrame with 'channelName', 'duration_count_after', and 'view_count_after' columns
            view_count_df = edited_stats_df[['channelName', 'duration_count_after', 'view_count_after']]

            # set the index to 'channelName' column
            view_count_df = view_count_df.set_index('channelName')

            # generate a horizontal bar chart using Plotly
            fig = px.bar(view_count_df, barmode='group', title="Views-Video Durations After 6th of Feb")

            fig.update_layout(xaxis_title=None)
            fig.update_layout(yaxis_title=None)

            fig.update_traces(name="Durations",selector=dict(name="duration_count_after"))

            fig.update_traces(name="Views",selector=dict(name="view_count_after"))

            fig.update_layout(legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="")

            # display the chart
            st.plotly_chart(fig)

        if page == "Likes-Video Durations After":
            with channel_details:
                st.title("")

            # create a new DataFrame with 'channelName', 'duration_count_after', and 'like_count_after' columns
            like_count_df = edited_stats_df[['channelName', 'duration_count_after', 'like_count_after']]

            # set the index to 'channelName' column
            like_count_df = like_count_df.set_index('channelName')

            # generate a horizontal bar chart using Plotly
            fig = px.bar(like_count_df, barmode='group', title="Likes-Video Durations After 6th of Feb")

            fig.update_layout(xaxis_title=None)
            fig.update_layout(yaxis_title=None)

            fig.update_traces(name="Durations",selector=dict(name="duration_count_after"))

            fig.update_traces(name="Likes",selector=dict(name="like_count_after"))

            fig.update_layout(legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
            width=800, height=600)

            # display the chart
            st.plotly_chart(fig)


        if page == "Comments-Video Durations After":
            with channel_details:
                st.title("")

            # create a new DataFrame with 'channelName', 'duration_count_after', and 'like_count_after' columns
            comment_count_df = edited_stats_df[['channelName', 'comment_count_after', 'like_count_after']]

            # set the index to 'channelName' column
            comment_count_df = comment_count_df.set_index('channelName')

            # generate a horizontal bar chart using Plotly
            fig = px.bar(comment_count_df, barmode='group', title="Comments-Video Durations After 6th of Feb")

            fig.update_layout(xaxis_title=None)
            fig.update_layout(yaxis_title=None)

            # display the chart
            st.plotly_chart(fig)

        if page == "Likes per Video":
            with channel_details:
                st.title("")

            # create a new DataFrame with 'channelName', 'like_per_video_after', and 'like_coulike_per_video_beforent_after' columns
            like_per_video_df = edited_stats_df[['channelName', 'like_per_video_after', 'like_per_video_before']]

            # set the index to 'channelName' column
            like_per_video_df = like_per_video_df.set_index('channelName')

            # generate a horizontal bar chart using Plotly
            fig = px.bar(like_per_video_df, barmode='group', title="Likes per Video Before & After")

            fig.update_layout(xaxis_title=None)
            fig.update_layout(yaxis_title=None)

            # display the chart
            st.plotly_chart(fig)

        if page == "Views per Video":
            with channel_details:
                st.title("")

            # create a new DataFrame with 'channelName', 'view_per_video_after', and 'view_per_video_before' columns
            view_per_video_df = edited_stats_df[['channelName', 'view_per_video_after', 'view_per_video_before']]

            # set the index to 'channelName' column
            view_per_video_df = view_per_video_df.set_index('channelName')

            # generate a horizontal bar chart using Plotly
            fig = px.bar(view_per_video_df, barmode='group', title="Views per Video Before & After")

            fig.update_layout(xaxis_title=None)
            fig.update_layout(yaxis_title=None)

            # display the chart
            st.plotly_chart(fig)

        if page == "Comments per Video":
            with channel_details:
                st.title("")

            # create a new DataFrame with 'channelName', 'comment_per_video_after', and 'comment_per_video_before' columns
            comment_per_video_df = edited_stats_df[['channelName', 'comment_per_video_after', 'comment_per_video_before']]

            # set the index to 'channelName' column
            comment_per_video_df = comment_per_video_df.set_index('channelName')

            # generate a horizontal bar chart using Plotly
            fig = px.bar(comment_per_video_df, barmode='group', title="Comments per Video Before & After")

            fig.update_layout(xaxis_title=None)
            fig.update_layout(yaxis_title=None)

            # display the chart
            st.plotly_chart(fig)

        if page == "Durations per Video":
            with channel_details:
                st.title("")

            # create a new DataFrame with 'channelName', 'duration_per_video_after', and 'duration_per_video_before' columns
            duration_per_video_df = edited_stats_df[['channelName', 'duration_per_video_after', 'duration_per_video_before']]

            # set the index to 'channelName' column
            duration_per_video_df = duration_per_video_df.set_index('channelName')

            # generate a horizontal bar chart using Plotly
            fig = px.bar(duration_per_video_df, barmode='group', title="Durations per Video Before & After")

            fig.update_layout(xaxis_title=None)
            fig.update_layout(yaxis_title=None)

            # display the chart
            st.plotly_chart(fig)

        if page == "Views per Likes":
            with channel_details:
                st.title("")

            # create a new DataFrame with 'channelName', 'view_per_like_after', and 'view_per_like_before' columns
            view_per_like_df = edited_stats_df[['channelName', 'view_per_like_after', 'view_per_like_before']]

            # set the index to 'channelName' column
            view_per_like_df = view_per_like_df.set_index('channelName')

            # generate a horizontal bar chart using Plotly
            fig = px.bar(view_per_like_df, barmode='group', title="Views per Likes Before & After")

            fig.update_layout(xaxis_title=None)
            fig.update_layout(yaxis_title=None)

            # display the chart
            st.plotly_chart(fig)

        if page == "Uploaded Video Count":
            with channel_details:
                st.title("")

            # create a new DataFrame with 'channelName', 'video_count_after', and 'video_count_before' columns
            video_count_df = edited_stats_df[['channelName', 'video_count_after', 'video_count_before']]

            # set the index to 'channelName' column
            video_count_df = video_count_df.set_index('channelName')

            # generate a horizontal bar chart using Plotly
            fig = px.bar(video_count_df, barmode='group', title="Uploaded Video Count Before & After")

            fig.update_layout(xaxis_title=None)
            fig.update_layout(yaxis_title=None)

            # display the chart
            st.plotly_chart(fig)

        if page == "Monthly Average Video Mins":
            with channel_details:
                st.title("")

            # create a new DataFrame with 'channelName', 'avg_monthly_total_mins_after', and 'avg_monthly_total_mins_before' columns
            avg_monthly_mins_df = edited_stats_df[['channelName', 'avg_monthly_total_mins_after', 'avg_monthly_total_mins_before','avg_monthly_total_mins']]

            # set the index to 'channelName' column
            avg_monthly_mins_df = avg_monthly_mins_df.set_index('channelName')

            # generate a horizontal bar chart using Plotly
            fig = px.bar(avg_monthly_mins_df, barmode='group', title="Monthly Average Video Mins Before & After")

            fig.update_layout(xaxis_title=None)
            fig.update_layout(yaxis_title=None)

            # display the chart
            st.plotly_chart(fig)

        if page == "Monthly Average Video Likes":
            with channel_details:
                st.title("")

            # create a new DataFrame with 'channelName', 'avg_monthly_total_mins_after', and 'avg_monthly_total_mins_before' columns
            avg_monthly_likes_df = edited_stats_df[['channelName', 'avg_monthly_total_likes_after', 'avg_monthly_total_likes_before','avg_monthly_total_likes']]

            # set the index to 'channelName' column
            avg_monthly_likes_df = avg_monthly_likes_df.set_index('channelName')

            # generate a horizontal bar chart using Plotly
            fig = px.bar(avg_monthly_likes_df, barmode='group', title="Monthly Average Video Likes Before & After")

            fig.update_layout(xaxis_title=None)
            fig.update_layout(yaxis_title=None)

            # display the chart
            st.plotly_chart(fig)

        elif page == "Subscribers per Video":
            with channel_details:
                st.title("")

            # create a new DataFrame with 'channelName', 'avg_monthly_total_mins_after', and 'avg_monthly_total_mins_before' columns
            sub_video_df = edited_stats_df[['channelName', 'subscribers_per_video']]

            # set the index to 'channelName' column
            sub_video_df = sub_video_df.set_index('channelName')

            # generate a horizontal bar chart using Plotly
            fig = px.bar(sub_video_df, barmode='group', title="Subscribers Count per Video ")

            fig.update_layout(xaxis_title=None)
            fig.update_layout(yaxis_title=None)

            # display the chart
            st.plotly_chart(fig)

elif page == "Top 10 Videos by Like Count and View Count":
    with channel_details:
        st.title("Channel Details")

        # Load Each Channel Data
        ahaber_df = pd.read_csv("media_stats/stats_a_haber.csv")
        aa_df = pd.read_csv("media_stats/stats_anadolu_ajansı.csv")
        bab_df = pd.read_csv("media_stats/stats_babala_tv.csv")
        bbc_df = pd.read_csv("media_stats/stats_bbc_news_türkçe.csv")
        cnn_df = pd.read_csv("media_stats/stats_cnn_türk.csv")
        co_df = pd.read_csv("media_stats/stats_cüneyt_özdemir.csv")
        co_df = pd.read_csv("media_stats/stats_erk_acarer.csv")
        fox_df = pd.read_csv("media_stats/stats_fox_haber.csv")
        ht_df = pd.read_csv("media_stats/stats_habertürk.csv")
        h_tv_df = pd.read_csv("media_stats/stats_halktv.csv")
        nev_df = pd.read_csv("media_stats/stats_nevşin_mengü.csv")
        soz_df = pd.read_csv("media_stats/stats_sözcü_televizyonu.csv")
        trt_df = pd.read_csv("media_stats/stats_trt_haber.csv")
        tv_df = pd.read_csv("media_stats/stats_tv100.csv")
        ys_df = pd.read_csv("media_stats/stats_yeni_şafak.csv")


        # create a dictionary to store data frames and graph titles for each channel
        channel_data = {
        'A Haber': {'df': ahaber_df, 'title': 'A Haber Top 10 Videos by Like Count and View Count'},
        'Anadolu Ajansı': {'df': aa_df, 'title': 'Anadolu Ajansı Top 10 Videos by Like Count and View Count'},
        'BaBaLa TV': {'df': bab_df, 'title': 'BaBaLa TV Top 10 Videos by Like Count and View Count'},
        'BBC News Türkçe': {'df': bbc_df, 'title': 'BBC News Türkçe Top 10 Videos by Like Count and View Count'},
        'CNN TÜRK': {'df': cnn_df, 'title': 'CNN TÜRK Top 10 Videos by Like Count and View Count'},
        'Cüneyt Özdemir': {'df': co_df, 'title': 'Cüneyt Özdemir Top 10 Videos by Like Count and View Count'},
        'FOX Haber': {'df': fox_df, 'title': 'FOX Haber Top 10 Videos by Like Count and View Count'},
        'Habertürk': {'df': ht_df, 'title': 'Habertürk Top 10 Videos by Like Count and View Count'},
        'Halktv': {'df': h_tv_df, 'title': 'Halktv Top 10 Videos by Like Count and View Count'},
        'Nevşin Mengü': {'df': nev_df, 'title': 'Nevşin Mengü Top 10 Videos by Like Count and View Count'},
        'SÖZCÜ Televizyonu': {'df': soz_df, 'title': 'SÖZCÜ Televizyonu Top 10 Videos by Like Count and View Count'},
        'TRT Haber': {'df': trt_df, 'title': 'TRT Haber Top 10 Videos by Like Count and View Count'},
        'TV100': {'df': tv_df, 'title': 'TV100 Top 10 Videos by Like Count and View Count'},
        'Yeni Şafak': {'df': ys_df, 'title': 'Yeni Şafak Top 10 Videos by Like Count and View Count'},
        }


        # add dropdown to select a channel
        channel_choice = st.selectbox("Select Channel", stats_df["channelName"].unique())
        year_choice = st.selectbox("Select Year", channel_data[channel_choice]['df']["Year"].sort_values(ascending=False).unique().tolist())
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

        fig.update_layout(xaxis_title=None)
        fig.update_layout(yaxis_title=None)

        fig.update_layout(coloraxis_colorbar=dict(title="Total Views"))

        # display plotly graph
        st.plotly_chart(fig)
