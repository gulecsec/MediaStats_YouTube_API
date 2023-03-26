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
channel_details = st.container()

# Define sidebar
st.sidebar.title("Pages")
page = st.sidebar.radio("Go to", ("Home", "Google Developers Console", "Top 10 Videos by Like Count and View Count","Turkish News Media's YouTube Stats"))

if page == "Home":
    with header:
        st.title("How Turkish News Media's YouTube Stats Stack Up: Exploring the Data on My Streamlit App")
        st.markdown("In this tutorial, we'll explore how to use the YouTube API with Python to interact with one of the world's largest video-sharing platforms,which boasts billions of daily users uploading, viewing, and commenting on videos. By the end of this tutorial, you'll know how to automate various tasks using the YouTube API.")


    with dataset:
        # add radio button to select between the two graphs
        graph_choice = st.radio("Select graph", options=["Views-Total Videos", "Subscribers-Total Videos"])

        # display the selected graph
        if graph_choice == "Views-Total Videos":
            fig = px.bar(data_frame=stats_df.sort_values('views', ascending=False),
                          x="channelName", y="views", color='totalVideos')

        else:
            fig = px.bar(data_frame=stats_df.sort_values('subscribers', ascending=False),
                          x="channelName", y="subscribers", color='totalVideos')

        fig.update_layout(coloraxis_colorbar=dict(title="Total Videos"), xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
            width=800, height=600,yaxis_title=None)

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
                # create a new DataFrame with 'channelName', 'duration_count_after', and 'view_count_after' columns
                view_count_df = edited_stats_df[['channelName', 'duration_count_after', 'view_count_after']]

                # set the index to 'channelName' column
                view_count_df = view_count_df.set_index('channelName')

                # generate a horizontal bar chart using Plotly
                fig = px.bar(view_count_df, barmode='group', title="Views-Video Durations After 6th of Feb")

                fig.update_traces(name="Durations",selector=dict(name="duration_count_after"))

                fig.update_traces(name="Views",selector=dict(name="view_count_after"))

                fig.update_layout(xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
                width=800, height=600,yaxis_title=None)

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""

                Based on the analysis of the data, it can be concluded that the number of videos uploaded by a news media channel does not necessarily have a direct correlation with the number of views received.

                For example, the "Habertürk TV" channel has received the highest number of views after the data was collected, but has uploaded only 40 videos, which is lower than the number of videos uploaded by some of the other channels.

                It is important to note that the number of views received by a channel is influenced by many factors, such as the quality of the content, the relevance of the topics covered, and the promotion of the channel.
                """)

        if page == "Likes-Video Durations After":
            with channel_details:

                # create a new DataFrame with 'channelName', 'duration_count_after', and 'like_count_after' columns
                like_count_df = edited_stats_df[['channelName', 'duration_count_after', 'like_count_after']]

                # set the index to 'channelName' column
                like_count_df = like_count_df.set_index('channelName')

                # generate a horizontal bar chart using Plotly
                fig = px.bar(like_count_df, barmode='group', title="Likes-Video Durations After 6th of Feb")

                fig.update_traces(name="Durations",selector=dict(name="duration_count_after"))

                fig.update_traces(name="Likes",selector=dict(name="like_count_after"))

                fig.update_layout(xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
                width=800, height=600,yaxis_title=None)

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""

                Based on the analysis of the durations and likes counts calculated from the data, the following channels stand out:

Halktv: with a duration_count_after of 3,212,914 and a like_count_after of 665,555, it has the highest number of both metrics among all channels analyzed. Its duration_count_after is 150% higher than the second highest, TV100, and its like_count_after is almost 300% higher than the second highest, Cüneyt Özdemir.

TV100: with a duration_count_after of 2,580,813 and a like_count_after of 482,840, it has the second highest number of both metrics among all channels analyzed.

CNN TÜRK: with a duration_count_after of 3,109,924 and a like_count_after of 558,924, it has the third highest duration_count_after and the fourth highest like_count_after among all channels analyzed.

Cüneyt Özdemir: with a duration_count_after of 588,527 and a like_count_after of 715,635, it has the third highest like_count_after among all channels analyzed.

Yeni Şafak: with a duration_count_after of 34,365 and a like_count_after of 620,847, it has a high like_count_after considering its low duration_count_after.

These results suggest that Halktv and TV100 are the most successful channels in terms of both video duration and likes, while Cüneyt Özdemir, CNN TÜRK, and Yeni Şafak also have relatively high numbers in terms of likes. It should be noted that these conclusions are based on a limited set of metrics and should be interpreted with caution.                """)

        if page == "Comments-Video Durations After":
            with channel_details:

                # create a new DataFrame with 'channelName', 'duration_count_after', and 'like_count_after' columns
                comment_count_df = edited_stats_df[['channelName', 'comment_count_after', 'like_count_after']]

                # set the index to 'channelName' column
                comment_count_df = comment_count_df.set_index('channelName')

                # generate a horizontal bar chart using Plotly
                fig = px.bar(comment_count_df, barmode='group', title="Comments-Video Durations After 6th of Feb")

                fig.update_traces(name="Comments",selector=dict(name="comment_count_after"))

                fig.update_traces(name="Likes",selector=dict(name="like_count_after"))

                fig.update_layout(xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
                width=800, height=600,yaxis_title=None)

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""

                The table above shows the like count and comment count for various Turkish news channels. Among the channels, TV100 has the highest like count with 482,840 likes, followed by Halktv with 665,555 likes and CNN TÜRK with 558,924 likes. On the other hand, Habertürk has the lowest like count with only 32,148 likes.

In terms of comment count, Halktv has the highest count with 156,956 comments, followed by CNN TÜRK with 126,936 comments and TV100 with 106,354 comments. The lowest comment count is for BaBaLa TV with only 4,377 comments.

It's interesting to note that although TV100 has the highest like count, it has a relatively lower comment count compared to Halktv and CNN TÜRK. This suggests that TV100's content may be more popular or appealing to viewers, but may not necessarily be sparking as much discussion or engagement. Conversely, Halktv and CNN TÜRK's content seems to be generating more conversation and engagement among viewers, despite having lower like counts.

                """)

        if page == "Likes per Video":
            with channel_details:

                # create a new DataFrame with 'channelName', 'like_per_video_after', and 'like_coulike_per_video_beforent_after' columns
                like_per_video_df = edited_stats_df[['channelName', 'like_per_video_after', 'like_per_video_before', 'like_per_video']]

                # set the index to 'channelName' column
                like_per_video_df = like_per_video_df.set_index('channelName')

                # generate a horizontal bar chart using Plotly
                fig = px.bar(like_per_video_df, barmode='group', title="Likes per Video")

                fig.update_traces(name="After",selector=dict(name="like_per_video_after"))

                fig.update_traces(name="Before",selector=dict(name="like_per_video_before"))

                fig.update_traces(name="Up to 23/03/23",selector=dict(name="like_per_video"))

                fig.update_layout(xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
                width=800, height=600,yaxis_title=None)

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""

                Looking at the values, we can see that for some channels like Nevşin Mengü, Cüneyt Özdemir, and A Haber, the like_per_video_after is slightly higher than the like_per_video_before. On the other hand, for channels like BaBaLa TV, FOX Haber, and Habertürk, the like_per_video_after is significantly lower than the like_per_video_before.

For some channels like Yeni Şafak, Anadolu Ajansı, and CNN TÜRK, there is not much difference between the like_per_video_before and like_per_video_after values. However, for channels like Halktv and Erk Acarer, the like_per_video_after values are considerably higher than the like_per_video_before values.

Overall, it is difficult to draw a general conclusion without more context about the channels and their content, but we can see some variation in the changes in average likes per video for different channels.

                """)

        if page == "Views per Video":
            with channel_details:

                # create a new DataFrame with 'channelName', 'view_per_video_after', and 'view_per_video_before' columns
                view_per_video_df = edited_stats_df[['channelName', 'view_per_video_after', 'view_per_video_before', 'view_per_video']]

                # set the index to 'channelName' column
                view_per_video_df = view_per_video_df.set_index('channelName')

                # generate a horizontal bar chart using Plotly
                fig = px.bar(view_per_video_df, barmode='group', title="Views per Video")

                fig.update_traces(name="After",selector=dict(name="view_per_video_after"))

                fig.update_traces(name="Before",selector=dict(name="view_per_video_before"))

                fig.update_traces(name="Up to 23/03/23",selector=dict(name="view_per_video"))

                fig.update_layout(xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
                width=800, height=600,yaxis_title=None)

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""Views per video represent the average number of views per video for each channel, as well as the average number of views per video before and after the period of natural disaster.

Comparing these values for each channel can provide insight into how their viewership has changed over time. For instance, BaBaLa TV had a very high average view count per video before the period, but this dropped significantly after the incident. On the other hand, channels like TRT Haber and FOX Haber saw a significant increase in average view counts per video after the earthquake.

It's important to note that these changes in average view counts could be due to a variety of factors, such as changes in content strategy or promotion efforts. Therefore, further analysis would be needed to determine the specific reasons behind these changes.

                """)

        if page == "Comments per Video":
            with channel_details:

                # create a new DataFrame with 'channelName', 'comment_per_video_after', and 'comment_per_video_before' columns
                comment_per_video_df = edited_stats_df[['channelName', 'comment_per_video_after', 'comment_per_video_before', 'comment_per_video']]

                # set the index to 'channelName' column
                comment_per_video_df = comment_per_video_df.set_index('channelName')

                # generate a horizontal bar chart using Plotly
                fig = px.bar(comment_per_video_df, barmode='group', title="Comments per Video")

                fig.update_traces(name="After",selector=dict(name="comment_per_video_after"))

                fig.update_traces(name="Before",selector=dict(name="comment_per_video_before"))

                fig.update_traces(name="Up to 23/03/23",selector=dict(name="comment_per_video"))

                fig.update_layout(xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
                width=800, height=600,yaxis_title=None)

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""Comments per video values show the average number of comments per video for each channel, both before and after the period covered in the data.

Looking at the data, we can see that the channels with the highest comment_per_video are BaBaLa TV, Yeni Şafak, and Halktv, while the channels with the lowest comment_per_video are TRT Haber, Habertürk, and Anadolu Ajansı.

Comparing the values, we can see that some channels have increased their average number of comments per video, while others have decreased.

For example, Halktv and Erk Acarer have both seen a significant increase in the number of comments per video, while TRT Haber, Habertürk, and Anadolu Ajansı have remained relatively consistent.

                """)

        if page == "Durations per Video":
            with channel_details:

                # create a new DataFrame with 'channelName', 'duration_per_video_after', and 'duration_per_video_before' columns
                duration_per_video_df = edited_stats_df[['channelName', 'duration_per_video_after', 'duration_per_video_before', 'duration_per_video']]

                # set the index to 'channelName' column
                duration_per_video_df = duration_per_video_df.set_index('channelName')

                # generate a horizontal bar chart using Plotly
                fig = px.bar(duration_per_video_df, barmode='group', title="Durations per Video")

                fig.update_traces(name="After",selector=dict(name="duration_per_video_after"))

                fig.update_traces(name="Before",selector=dict(name="duration_per_video_before"))

                fig.update_traces(name="Up to 23/03/23",selector=dict(name="duration_per_video"))

                fig.update_layout(xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
                width=800, height=600,yaxis_title=None)

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""

                In terms of percentage increase or decrease, Nevşin Mengü, Cüneyt Özdemir, and FOX Haber have increased their video duration by 47.2%, 24.4%, and 254.8% respectively.

On the other hand, TRT Haber, BBC News Türkçe, and Anadolu Ajansı have decreased their video duration by 76.5%, 181.7%, and 47.4% respectively.

In terms of overall duration, TV100 and Halktv have the longest video duration, while TRT Haber has the shortest.

It is important to note that the duration of a video does not necessarily determine its quality or success on the platform, as there are other factors such as content and engagement that play a significant role.

                """)

        if page == "Views per Likes":
            with channel_details:

                # create a new DataFrame with 'channelName', 'view_per_like_after', and 'view_per_like_before' columns
                view_per_like_df = edited_stats_df[['channelName', 'view_per_like_after', 'view_per_like_before', 'view_per_like']]

                # set the index to 'channelName' column
                view_per_like_df = view_per_like_df.set_index('channelName')

                # generate a horizontal bar chart using Plotly
                fig = px.bar(view_per_like_df, barmode='group', title="Views per Likes")

                fig.update_traces(name="After",selector=dict(name="view_per_like_after"))

                fig.update_traces(name="Before",selector=dict(name="view_per_like_before"))

                fig.update_traces(name="Up to 23/03/23",selector=dict(name="view_per_like"))

                fig.update_layout(xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
                width=800, height=600,yaxis_title=None)

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""

                Based on the observations above, we can conclude that:

The average number of views per like after 2nd Feb 2023 is posted is lower than the overall average and the number of views per like before.

Habertürk has the highest value in both the number of views per like after and overall views per like.

TRT Haber has the highest value in the number of views per like before the video is posted, but this value is not a strong predictor of overall views per like.

In terms of percentages, we can say that the average number of views per like after a video is posted is 107.3% lower than the average number of views per like before the video is posted, and 36.8% lower than the overall average number of views per like.

Additionally, the difference between the highest and lowest values for each column is quite significant, ranging from 12.5% to 757.5%.

                """)

        if page == "Uploaded Video Count":
            with channel_details:

                # create a new DataFrame with 'channelName', 'video_count_after', and 'video_count_before' columns
                video_count_df = edited_stats_df[['channelName', 'video_count_after', 'video_count_before', 'totalVideos']]

                # set the index to 'channelName' column
                video_count_df = video_count_df.set_index('channelName')

                # generate a horizontal bar chart using Plotly
                fig = px.bar(video_count_df, barmode='group', title="Uploaded Video Count")

                fig.update_traces(name="After",selector=dict(name="video_count_after"))

                fig.update_traces(name="Before",selector=dict(name="video_count_before"))

                fig.update_traces(name="Up to 23/03/23",selector=dict(name="totalVideos"))

                fig.update_layout(xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
                width=800, height=600,yaxis_title=None)

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""

                Looking at the data, we can see that some channels have had significant changes in their video count.

Here are the percentage changes for each channel:""")

                # Calculate the percentage change for each channel and sort Percentage Change values descending
                edited_stats_df["Percentage Change"] = ((edited_stats_df["totalVideos"] - edited_stats_df["video_count_before"]) / edited_stats_df["video_count_before"]) * 100
                edited_stats_df = edited_stats_df.sort_values(by="Percentage Change", ascending=False)

                # Create a line chart using Plotly
                fig = px.bar(edited_stats_df, x="channelName", y="Percentage Change", title="Video Count Changes by Channel", hover_data=["totalVideos", "video_count_before"], color='Percentage Change', color_continuous_scale=px.colors.sequential.Plasma)
                fig.update_layout(yaxis=dict(title="Percentage Change"), xaxis=dict(title="Channel Name"))

                # Display the chart in a Streamlit app
                st.plotly_chart(fig)

                st.markdown("""

These percentages represent the increase or decrease in the number of videos uploaded by each channel before and after the disaster.

Overall, it seems that the majority of channels have had a relatively small change in their video count, with most falling within a range of 1-5% increase or decrease.

However, it's important to note that these changes may not necessarily be significant in the context of each channel's total video count. For example, a 1% increase for a channel with only a few videos may be less significant than a 1% increase for a channel with thousands of videos.

Therefore, while these percentage changes can give us some insight into each channel's recent activity, they should be interpreted with caution and in the context of each channel's overall content strategy.

                """)

        if page == "Monthly Average Video Mins":
            with channel_details:

                # create a new DataFrame with 'channelName', 'avg_monthly_total_mins_after', and 'avg_monthly_total_mins_before' columns
                avg_monthly_mins_df = edited_stats_df[['channelName', 'avg_monthly_total_mins_after', 'avg_monthly_total_mins_before','avg_monthly_total_mins']]

                # set the index to 'channelName' column
                avg_monthly_mins_df = avg_monthly_mins_df.set_index('channelName')

                # generate a horizontal bar chart using Plotly
                fig = px.bar(avg_monthly_mins_df, barmode='group', title="Monthly Average Video Mins")

                fig.update_traces(name="After",selector=dict(name="avg_monthly_total_mins_after"))

                fig.update_traces(name="Before",selector=dict(name="avg_monthly_total_mins_before"))

                fig.update_traces(name="Up to 23/03/23",selector=dict(name="avg_monthly_total_mins"))

                fig.update_layout(xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
                width=800, height=600,yaxis_title=None)

                # display the chart
                st.plotly_chart(fig)

        if page == "Monthly Average Video Likes":
            with channel_details:

                # create a new DataFrame with 'channelName', 'avg_monthly_total_mins_after', and 'avg_monthly_total_mins_before' columns
                avg_monthly_likes_df = edited_stats_df[['channelName', 'avg_monthly_total_likes_after', 'avg_monthly_total_likes_before','avg_monthly_total_likes']]

                # set the index to 'channelName' column
                avg_monthly_likes_df = avg_monthly_likes_df.set_index('channelName')

                # generate a horizontal bar chart using Plotly
                fig = px.bar(avg_monthly_likes_df, barmode='group', title="Monthly Average Video Likes")

                fig.update_layout(xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
                width=800, height=600,yaxis_title=None)

                fig.update_traces(name="After",selector=dict(name="avg_monthly_total_likes_after"))

                fig.update_traces(name="Before",selector=dict(name="avg_monthly_total_likes_before"))

                fig.update_traces(name="Up to 23/03/23",selector=dict(name="avg_monthly_total_likes"))

                # display the chart
                st.plotly_chart(fig)


        elif page == "Subscribers per Video":
            with channel_details:

                # create a new DataFrame with 'channelName', 'avg_monthly_total_mins_after', and 'avg_monthly_total_mins_before' columns
                sub_video_df = edited_stats_df[['channelName', 'subscribers_per_video']]

                # set the index to 'channelName' column
                sub_video_df = sub_video_df.set_index('channelName')

                # generate a horizontal bar chart using Plotly
                fig = px.bar(sub_video_df, barmode='group', title="Subscribers Count per Video ")

                fig.update_traces(name="Subscribers",selector=dict(name="subscribers_per_video"))

                fig.update_layout(xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
                width=800, height=600,yaxis_title=None)

                # display the chart
                st.plotly_chart(fig)

elif page == "Top 10 Videos by Like Count and View Count":
    with channel_details:
        st.title("Channel Details")

        # create a dictionary to store data frames and graph titles for each channel
        channel_data = {
        'A Haber': {'path': 'media_stats/stats_a_haber.csv' ,'title': 'A Haber Top 10 Videos by Like Count and View Count'},
        'Anadolu Ajansı': {'path': 'media_stats/stats_anadolu_ajansı.csv' , 'title': 'Anadolu Ajansı Top 10 Videos by Like Count and View Count'},
        'BaBaLa TV': {'path': 'media_stats/stats_babala_tv.csv' , 'title': 'BaBaLa TV Top 10 Videos by Like Count and View Count'},
        'BBC News Türkçe': {'path': 'media_stats/stats_bbc_news_türkçe.csv' ,'title': 'BBC News Türkçe Top 10 Videos by Like Count and View Count'},
        'CNN TÜRK': {'path': 'media_stats/stats_cnn_türk.csv' , 'title': 'CNN TÜRK Top 10 Videos by Like Count and View Count'},
        'Cüneyt Özdemir': {'path': 'media_stats/stats_cüneyt_özdemir.csv' , 'title': 'Cüneyt Özdemir Top 10 Videos by Like Count and View Count'},
        'Erk Acarer': {'path': 'media_stats/stats_cüneyt_özdemir.csv' , 'title': 'Cüneyt Özdemir Top 10 Videos by Like Count and View Count'},
        'FOX Haber': {'path': 'media_stats/stats_fox_haber.csv' , 'title': 'FOX Haber Top 10 Videos by Like Count and View Count'},
        'Habertürk': {'path': 'media_stats/stats_habertürk.csv' , 'title': 'Habertürk Top 10 Videos by Like Count and View Count'},
        'Halktv': {'path': 'media_stats/stats_halktv.csv' , 'title': 'Halktv Top 10 Videos by Like Count and View Count'},
        'Nevşin Mengü': {'path': 'media_stats/stats_nevşin_mengü.csv' ,'title': 'Nevşin Mengü Top 10 Videos by Like Count and View Count'},
        'SÖZCÜ Televizyonu': {'path': 'media_stats/stats_sözcü_televizyonu.csv' ,'title': 'SÖZCÜ Televizyonu Top 10 Videos by Like Count and View Count'},
        'TRT Haber': {'path': 'media_stats/stats_trt_haber.csv' ,'title': 'TRT Haber Top 10 Videos by Like Count and View Count'},
        'TV100': {'path': 'media_stats/stats_tv100.csv' ,'title': 'TV100 Top 10 Videos by Like Count and View Count'},
        'Yeni Şafak': {'path': 'media_stats/stats_yeni_şafak.csv' ,'title': 'Yeni Şafak Top 10 Videos by Like Count and View Count'},
        }


        # add dropdown to select a channel
        channel_choice = st.selectbox("Select Channel", stats_df["channelName"].unique())

        # get the path and dataframe for the selected channel
        path = channel_data[channel_choice]['path']

        # Load Each Channel Data
        df = pd.read_csv(path)

        # create dropdowns for year and month selection
        years = df['Year'].unique()
        year_choice = st.selectbox("Select Year", sorted(years, reverse=True))
        months = df[df['Year']==year_choice]['Month'].unique()
        month_choice = st.selectbox("Select Month", months)

        # filter the data based on the user's selection
        df = df[(df['Year']==year_choice) & (df['Month']==month_choice)]

        # generate plotly graph
        fig = px.bar(data_frame=df.sort_values('likeCount', ascending=False)[0:9],
                    x="title", y="likeCount", color='viewCount', title=channel_data[channel_choice]['title'])

        # format y-axis labels to show thousands
        fig.update_yaxes(tickformat=',.0f')

        fig.update_layout(xaxis={'tickmode': 'array', 'tickvals': []},xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
        width=800, height=600,yaxis_title=None)

        # display plotly graph
        st.plotly_chart(fig)
