import streamlit as st
import pandas as pd

# Data viz packages
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Load data
stats_df = pd.read_csv("All_stats/media_stats.csv")

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
        edited_stats_df = pd.read_csv("All_stats/media_stats_edited.csv")

        # Define sidebar
        st.sidebar.title("Video Stats")
        page = st.sidebar.radio("Go to", ("Views-Minutes After", "Likes-Durations After", "Comments-Durations After",
        "Likes per Video", "Views per Video", "Comments per Video", "Durations per Video", "Views per Likes", "Uploaded Video Count",
        "Monthly Average Video Mins", "Monthly Average Video Likes", "Subscribers per Video"))

        if page == "Views-Minutes After":
            with channel_details:

                # create a new DataFrame with 'channelName', 'mins_count_after', and 'view_count_after' columns
                view_mins_df = edited_stats_df[['channelName', 'mins_count_after', 'view_count_after']]

                # sort the values by 'like_count_after'
                view_mins_df = view_mins_df.sort_values(by='view_count_after')

                # Calculate the like per minute values
                view_per_min = view_mins_df['view_count_after'] / view_mins_df['mins_count_after']
                view_mins_df['View per Minute'] = view_per_min

                # set the index to 'channelName' column
                view_mins_df = view_mins_df.set_index('channelName')

                # generate a horizontal bar chart using Plotly
                fig = px.bar(view_mins_df, x='view_count_after', y=view_mins_df.index,
                color='mins_count_after', orientation='h',
                title="Channel Views - Total Video Minutes After 6th of Feb",
                color_continuous_scale='Blues', text=view_per_min.round(0))

                fig.update_layout(xaxis_title=None, legend=dict(orientation='h', yanchor='top', y=1.1,
                xanchor='left', x=0.01), legend_title="Minutes",width=800, height=600, yaxis_title=None,
                coloraxis_colorbar=dict(title="Minutes"))

                fig.update_traces(name="Minutes",selector=dict(name="mins_count_after"))

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""

                From the given values, we can conclude that there is a significant variation in the view per minute for different media channels.

The highest view per minute is for BBC News Türkçe, which is more than 39,000 views per minute, followed by Yeni Şafak with more than 39,000 views per minute.

TRT Haber also has a high view per minute with more than 14,000 views per minute.

On the other hand, FOX Haber and CNN Türk have the lowest view per minute, with only 699 and 1361 views per minute, respectively.

Moreover, we can also observe that the minutes count after and view count after do not necessarily correspond to a higher view per minute.

For instance, A Haber has a lower view per minute, even though it has a higher view count after and minutes count after compared to some other channels such as Halktv and SÖZCÜ Televizyonu.

Overall, the view per minute metric provides a better measure of the popularity of a channel, as it considers the engagement of the viewers with the content in a given period.

                """)

                # Add footer to the page
                st.markdown("<p style='text-align: right;'><i><b>* Data collected on 27rd of March 2023</b></i></p>", unsafe_allow_html=True)


        if page == "Likes-Durations After":
            with channel_details:

                # Select columns of interest
                like_mins_df = edited_stats_df[['channelName', 'mins_count_after', 'like_count_after']]

                # sort the values by 'like_count_after'
                like_mins_df = like_mins_df.sort_values(by='like_count_after')

                # Calculate the like per minute values
                like_per_min = like_mins_df['like_count_after'] / like_mins_df['mins_count_after']
                like_mins_df['Like per Minute'] = like_per_min

                # set the index to 'channelName' column
                like_mins_df = like_mins_df.set_index('channelName')

                # generate a horizontal bar chart using Plotly
                fig = px.bar(like_mins_df, x='like_count_after', y=like_mins_df.index,
                color='mins_count_after', orientation='h',
                title="Channel Likes - Total Video Minutes After 6th of Feb",
                color_continuous_scale='Reds', text=like_per_min.round(0))

                fig.update_layout(xaxis_title=None, legend=dict(orientation='h', yanchor='top', y=1.1,
                xanchor='left', x=0.01), legend_title="Minutes",width=800, height=600, yaxis_title=None,
                coloraxis_colorbar=dict(title="Minutes"))

                fig.update_traces(name="Minutes",selector=dict(name="mins_count_after"))

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""

                Based on the data provided, it appears that the channels with the highest "Like per Minute" are Yeni Şafak and BaBaLa TV, with values of 764 and 709, respectively.

On the other hand, the channels with the lowest "Like per Minute" are FOX Haber, CNN TÜRK, and Halktv, with values of 7, 11, and 13, respectively.

In terms of total "Like Count After", Cüneyt Özdemir has the highest value with 761,719 likes, followed by Yeni Şafak with 656,476 likes.

However, in terms of "Minutes Count After", Halktv has the highest value with 58,560.8 minutes, followed by TV100 with 46,025.6 minutes.

Overall, it can be concluded that while some channels may have a higher "Like per Minute" rate, it is important to also consider the total number of minutes and likes, as these values can provide more context and a more comprehensive picture of a channel's performance on YouTube.

                """)

                # Add footer to the page
                st.markdown("<p style='text-align: right;'><i><b>* Data collected on 27rd of March 2023</b></i></p>", unsafe_allow_html=True)


        if page == "Comments-Durations After":
            with channel_details:

                # Select columns of interest
                comments_mins_df = edited_stats_df[['channelName', 'mins_count_after', 'comment_count_after']]

                # sort the values by 'like_count_after'
                comments_mins_df = comments_mins_df.sort_values(by='comment_count_after')

                # Calculate the like per minute values
                comments_per_min = comments_mins_df['comment_count_after'] / comments_mins_df['mins_count_after']
                comments_mins_df['View per Minute'] = comments_per_min

                # set the index to 'channelName' column
                comments_mins_df = comments_mins_df.set_index('channelName')

                # generate a horizontal bar chart using Plotly
                fig = px.bar(comments_mins_df, x='comment_count_after', y=comments_mins_df.index,
                color='mins_count_after', orientation='h',
                title="Channel Comments - Total Video Minutes After 6th of Feb",
                color_continuous_scale='Greens', text=comments_per_min.round(0))

                fig.update_layout(xaxis_title=None, legend=dict(orientation='h', yanchor='top', y=1.1,
                xanchor='left', x=0.01), legend_title="Minutes",width=800, height=600, yaxis_title=None,
                coloraxis_colorbar=dict(title="Minutes"))

                fig.update_traces(name="Minutes",selector=dict(name="mins_count_after"))

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""

                The data shows the number of comments received by different Turkish news channels in a specific time period.

The values represents the average number of comments received per minute for each channel.

BBC News Türkçe and Yeni Şafak received the highest and lowest number of comments per minute, respectively.

The BBC News Türkçe's high engagement rate may be attributed to its reputation as a credible and impartial news source.

Yeni Şafak's low engagement rate could be due to a lack of trust in the news source or a smaller audience.

CNN TÜRK, FOX Haber, Habertürk, and TV100 received the lowest number of comments per minute, which could indicate lower audience engagement with these channels.

The channels that received a higher number of comments per minute than others, such as Yeni Şafak and BBC News Türkçe, could benefit from further analysis of their content and engagement strategies to determine what factors contribute to their higher engagement rates.

Meanwhile, the channels with lower engagement rates could use this information to improve their content and engagement strategies to increase their audience's interest and engagement.

                """)

                # Add footer to the page
                st.markdown("<p style='text-align: right;'><i><b>* Data collected on 27rd of March 2023</b></i></p>", unsafe_allow_html=True)


        if page == "Likes per Video":
            with channel_details:

                # generate a horizontal bar chart using Plotly
                fig = px.bar(data_frame=edited_stats_df.sort_values('like_per_video_after', ascending=False),
                x="channelName", y="like_per_video_after", color='video_count_after', color_continuous_scale='Viridis',
                title="Channel Likes per Video After 6th of Feb")

                # fig.update_traces(name="Up to 27/03/23",selector=dict(name="like_per_video_after"))

                fig.update_layout(coloraxis_colorbar=dict(title="Videos"), xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
                width=800, height=600,yaxis_title=None)

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""

                The table shows the number of videos uploaded and the average number of likes per video for 15 different Turkish news channels.

The highest number of videos uploaded after 6th of February was by CNN TÜRK, with a total of 2438 videos. The second highest number of videos was uploaded by TV100 with a total of 1970 videos.

The channel with the lowest number of videos was BaBaLa TV with only 5 videos. When it comes to the average number of likes per video, BaBaLa TV had the highest average with 14,414 likes per video,

followed by Nevşin Mengü with an average of 6065 likes per video. The channel with the lowest average number of likes per video was A Haber with an average of 192 likes per video.

It is interesting to note that some of the channels with a lower number of videos uploaded, such as BBC News Türkçe and TRT Haber, had relatively high average numbers of likes per video.

This suggests that these channels may have a more engaged audience, with viewers who are more likely to engage with and appreciate the content that is uploaded.

                """)

                # Add footer to the page
                st.markdown("<p style='text-align: right;'><i><b>* Data collected on 27rd of March 2023</b></i></p>", unsafe_allow_html=True)

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

                fig.update_traces(name="Up to 27/03/23",selector=dict(name="view_per_video"))

                fig.update_layout(xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
                width=800, height=600,yaxis_title=None)

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""

                The graph shows the number of views per video for different Turkish news channels before and after February 6th, 2023.

Before February 6th, 2023, the channel with the highest number of views per video was BaBaLa TV with 1,321,335 views per video. After the natural disaster the channel with the highest number of views per video was BBC News Türkçe with 410,318 views per video, followed by BaBaLa TV with 189,987 views per video.

On the other hand, A Haber had the lowest number of views per video before and after the earthquake.

Overall, it seems that most channels experienced a decrease in the number of views per video after February 6th, 2023. The only exceptions to this trend were BBC News Türkçe and BaBaLa TV which saw an increase in their views per video.

                """)

                # Add footer to the page
                st.markdown("<p style='text-align: right;'><i><b>* Data collected on 27rd of March 2023</b></i></p>", unsafe_allow_html=True)

        if page == "Comments per Video":
            with channel_details:

                # create a new DataFrame with 'channelName', 'comment_per_video_after', and 'comment_per_video_before' columns
                comment_per_video_df = edited_stats_df[['channelName', 'comment_per_video_after', 'video_count_after']]

                # generate a horizontal bar chart using Plotly
                fig = px.bar(data_frame=edited_stats_df.sort_values('comment_per_video_after', ascending=False),
                x="channelName", y="comment_per_video_after", color='video_count_after', color_continuous_scale='Cividis',
                title="Channel Comments per Video After 6th of Feb")

                # fig.update_traces(name="Up to 27/03/23",selector=dict(name="like_per_video_after"))

                fig.update_layout(coloraxis_colorbar=dict(title="Videos"), xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
                width=800, height=600,yaxis_title=None)

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""

                The graph shows the number of videos uploaded by different news channels on YouTube and the average number of comments per video after the 6th of February 2023.

In terms of the average number of comments per video, the highest number is seen for BaBaLa TV with 923 comments per video followed by BBC News Türkçe with 666 comments per video. Anadolu Ajansı has the lowest number of comments per video with only 12 comments per video on average.

Overall, it appears that BaBaLa TV and BBC News Türkçe are the channels with the most engaged audiences as they have the highest number of comments per video.

However, it is important to note that the number of videos uploaded by these channels is relatively small compared to other channels such as CNN TÜRK and SÖZCÜ Televizyonu, which may have an impact on the comment per video ratio.

                """)

                # Add footer to the page
                st.markdown("<p style='text-align: right;'><i><b>* Data collected on 27rd of March 2023</b></i></p>", unsafe_allow_html=True)

        if page == "Durations per Video":
            with channel_details:

                # generate a horizontal bar chart using Plotly
                fig = px.bar(data_frame=edited_stats_df.sort_values('mins_per_video_after', ascending=False),
                x="channelName", y="mins_per_video_after", color='video_count_after', color_continuous_scale='Cividis',
                title="Minutes per Video After 6th of Feb")

                # fig.update_traces(name="Up to 27/03/23",selector=dict(name="like_per_video_after"))

                fig.update_layout(coloraxis_colorbar=dict(title="Videos"), xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
                width=800, height=600,yaxis_title=None)

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""

                These values represent the number of videos and the average length of those videos for each channel after the selected date range.

The highest number of videos produced after the selected date range was by CNN TÜRK with 2,438 videos, followed by TV100 with 1,970 videos and Halktv with 1,396 videos.

Regarding the average length of videos produced, Nevşin Mengü has the longest average length of videos at 46.2 minutes, followed by Halktv with 41.9 minutes and FOX Haber with 34.4 minutes. On the other hand, TRT Haber has the shortest average video length of 1.6 minutes , followed by Yeni Şafak with 7.8 minutes.

It is important to note that the number of videos produced does not necessarily reflect the quality of content or engagement with the audience.

                """)

                # Add footer to the page
                st.markdown("<p style='text-align: right;'><i><b>* Data collected on 27rd of March 2023</b></i></p>", unsafe_allow_html=True)

        if page == "Views per Likes":
            with channel_details:

                # create a new DataFrame with 'channelName', 'view_per_like_after', and 'view_per_like_before' columns
                view_per_like_df = edited_stats_df[['channelName', 'like_count_after', 'view_per_like_after', 'view_count_after' ]]

                # set the index to 'channelName' column
                view_per_like_df = view_per_like_df.set_index('channelName')

                # generate a horizontal bar chart using Plotly
                fig = px.bar(view_per_like_df, barmode='group', title="Views per Likes")

                fig.update_traces(name="After",selector=dict(name="view_per_like_after"))

                fig.update_traces(name="Before",selector=dict(name="view_per_like_before"))

                fig.update_traces(name="Up to 27/03/23",selector=dict(name="view_per_like"))

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

                fig.update_traces(name="Up to 27/03/23",selector=dict(name="totalVideos"))

                fig.update_layout(xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
                width=800, height=400,yaxis_title=None)

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""

                Looking at the data, we can see that some channels have had significant changes in their video count.

Here are the percentage changes for each channel:
""")
                # Calculate the percentage change for each channel and sort Percentage Change values descending
                edited_stats_df["Percentage Change"] = round(((edited_stats_df["totalVideos"] - edited_stats_df["video_count_before"]) / edited_stats_df["video_count_before"]) * 100,2)
                edited_stats_df = edited_stats_df.sort_values(by="Percentage Change", ascending=False)

                # Create a line chart using Plotly
                fig = px.bar(edited_stats_df, x="channelName", y="Percentage Change", title="", hover_data=["totalVideos", "video_count_before"],
                color='Percentage Change', color_continuous_scale=px.colors.sequential.Plasma)

                fig.update_layout(xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
                width=800, height=600,yaxis_title=None)

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

                fig.update_traces(name="Up to 27/03/23",selector=dict(name="avg_monthly_total_mins"))

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

                fig.update_traces(name="Up to 27/03/23",selector=dict(name="avg_monthly_total_likes"))

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
