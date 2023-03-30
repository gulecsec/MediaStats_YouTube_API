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
st.sidebar.title("Main Pages")
page = st.sidebar.radio("", ("Home", "Google Developers Console", "Top 10 Videos by Like Count and View Count","Turkish News Media's YouTube Stats"))

if page == "Home":
    with header:
        st.title("How Turkish News Media's YouTube Stats Stack Up")
        st.subheader("Exploring the Data on My Streamlit App")
        st.markdown("In this tutorial, we'll explore how to use the YouTube API with Python to retrieve and analyze the statistics of channels on one of the world's largest video-sharing platforms. Specifically, we'll focus on 15 channels affected by the earthquake that occurred in Turkey on February 6th, 2023. By comparing the statistics of these channels, we can gain insight into the impact of the earthquake on the YouTube community and learn how to use the YouTube API to automate various tasks related to channel analysis.")


    with dataset:
        # add radio button to select between the two graphs
        graph_choice = st.radio("Select graph", options=["Total number of Views & Total number of Videos", "Total number of Subscribers & Total number of Videos"])

        # display the selected graph
        if graph_choice == "Total number of Views & Total number of Videos":
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
        st.markdown("This page aims to assist you in obtaining an API key, making requests using the YouTube API with Python, and analyzing the results. It is important to note that before proceeding, you will need to create a project in the Google Developers Console and obtain an API key. With this information, we will explore how to use the YouTube API to gather video statistics of channels after the 6th of February 2023 earthquake in Turkey to compare values between channels.")

        st.subheader("Step 1: Set Up a Project in the Google Developers Console")
        st.markdown("""
                To use the YouTube API with Python, you first need to create a project in the Google Developers Console and obtain an API key. Here are the steps:
                1. Go to the Google Developers Console (https://console.developers.google.com/).
                2. Click on the project drop-down menu at the top of the screen and select "New Project" or an existing project that you want to use for the API.
                3. Enter a name for your project and click on the "Create" button.
                4. Once the project is created, click on the hamburger menu at the top-left corner of the screen and select "APIs & Services" > "Library" from the navigation menu.
                5. In the search bar, type "YouTube Data API" and click on the result.
                6. Click on the "Enable" button to enable the API for your project""")

        st.subheader("Step 2: Obtain the API Key")
        st.markdown("""
                1. Next, click on the "Create Credentials" button to create a new set of credentials for your project.
                2. Select "API key" as the type of credentials and choose the "Restricted key" option.
                3. Set up any necessary restrictions for your API key, such as IP address or HTTP referrers.
                4. Click on the "Create" button to generate your API key.
                5. The API key will be displayed. Copy the key and keep it safe.""")

        st.subheader("Step 3: Install the Google API Client Library for Python")
        st.markdown("""
        The Google API Client Library for Python makes it easy for developers to access Google APIs.To install the library, run the following command in your terminal or command prompt:
                """)
        st.code("pip install --upgrade google-api-python-client")

        st.subheader("Step 4: Make API Requests")
        st.markdown("""
                Now that we have the API key and the library installed, we can start making API requests. Here’s a simple example that retrieves the details of a video:
                """)
        st.code("""
        from googleapiclient.discovery import build
api_service_name = 'youtube'
api_version = 'v3'
                """)

        st.subheader("Step 5: Get credentials and create an API client")
        st.markdown("""
                In this example, the build function creates a YouTube service object that we can use to make API requests. The videos().list() method retrieves the details of a video, and the execute() method sends the request and returns the response. Note: Replace YOUR_API_KEY with your own API key.""")

        st.code("""
        youtube = build(api_service_name, api_version, developerKey=api_key)

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
        st.markdown("""
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
        st.title("Detailed YouTube Stats of Turkish News Media's")

        # Load Each Channel Data
        edited_stats_df = pd.read_csv("All_stats/media_stats_edited.csv")

        # Define sidebar
        st.sidebar.title("Detailed Stats")
        page = st.sidebar.radio("", ("Views-Minutes After", "Likes-Minutes After", "Comments-Minutes After",
        "Likes per Video", "Views per Video", "Comments per Video", "Durations per Video", "Views per Likes", "Number of Videos After",
        "Monthly Minutes After", "Monthly Likes After", "Monthly Views After", "Monthly Comments After","Daily Uploaded Video","Subscribers per Video"))

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
                title="Top Channels by Views per Minute: Analyzing Total Video Minutes After 6th of Feb",
                color_continuous_scale='Blues', text=view_per_min.round(0), labels={'text': 'Views per Min'})

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


        if page == "Likes-Minutes After":
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
                title="Top Channels by Likes per Minute: Analyzing Total Video Minutes After 6th of Feb",
                color_continuous_scale='Reds', text=like_per_min.round(0), labels={'text': 'Likes per Min'})

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


        if page == "Comments-Minutes After":
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
                title="Top Channels by Comments per Minute: Analyzing Total Video Minutes After 6th of Feb",
                color_continuous_scale='Greens', text=comments_per_min.round(0), labels={'text': 'Comments per Min'})

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
                title="Total Likes per Video for Each Channel Uploaded After February 6th", labels={'text': 'Likes per Min'})

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
                fig = px.bar(view_per_video_df, barmode='group', title="Total Views per Video for Each Channel Uploaded After February 6th")

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
                title="Total Comments per Video for Each Channel Uploaded After February 6th")

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
                title="Total Minutes per Video for Each Channel Uploaded After February 6th")

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

                # generate a horizontal bar chart using Plotly
                fig = px.bar(data_frame=edited_stats_df.sort_values('view_per_like_after', ascending=False),
                x="channelName", y="view_per_like_after", color='view_count_after', color_continuous_scale='Inferno',
                title="Total Views per Like for Each Channel Uploaded After February 6th")

                fig.update_layout(coloraxis_colorbar=dict(title="Views"), xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
                width=800, height=600,yaxis_title=None)

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""Looking at the bar chart above:

CNN TÜRK has the highest view count after, followed by Habertürk and Halktv.

BaBaLa TV and Anadolu Ajansı have the lowest view count after.

Yeni Şafak has the lowest view per like after, while Habertürk has the highest view per like after.

The view per like after for most channels is around 50-100, indicating that for every like on a video, there are about 50-100 views. However, there are some outliers, like CNN TÜRK with a view per like after of 126.3 and Habertürk with a view per like after of 203.6.

It's worth noting that the view per like after metric could be influenced by factors such as the type of content, engagement rate, and the number of likes on each video. Therefore, it should be taken with a grain of salt and analyzed in conjunction with other metrics.

                """)

                # Add footer to the page
                st.markdown("<p style='text-align: right;'><i><b>* Data collected on 27rd of March 2023</b></i></p>", unsafe_allow_html=True)

        if page == "Number of Videos After":
            with channel_details:

                # create a new DataFrame with 'channelName', 'video_count_after', and 'video_count_before' columns
                video_count_df = edited_stats_df[['channelName', 'video_count_after', 'video_count_before', 'totalVideos']]

                # set the index to 'channelName' column
                video_count_df = video_count_df.set_index('channelName')

                # generate a horizontal bar chart using Plotly
                fig = px.bar(video_count_df, barmode='group', title="Number of Videos Uploaded")

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
                edited_stats_df = edited_stats_df[edited_stats_df['channelName'] != 'SÖZCÜ Televizyonu'] # Exclude SÖZCÜ Televizyonu from the dataframe
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

                # Add footer to the page
                st.markdown("<p style='text-align: right;'><i><b>* Data collected on 27rd of March 2023</b></i></p>", unsafe_allow_html=True)


        if page == "Monthly Minutes After":
            with channel_details:

                # Load data
                monthly_df = pd.read_csv("All_stats/monthly_totals.csv")

                # Pivot the data to create a new DataFrame with columns for each month
                pivoted_df = monthly_df.pivot_table(index='channelName', columns='Month', values='mins_after_per_month')

                # Create a new DataFrame with the monthly_video_count_after values
                monthly_count_df = monthly_df[['channelName', 'Month', 'monthly_video_count_after', 'mins_after_per_month']]

                # Pivot the data to create a new DataFrame with columns for each month
                pivoted_count_df = monthly_count_df.pivot_table(index='channelName', columns='Month', values=['monthly_video_count_after','mins_after_per_month'])

                # Generate a horizontal bar chart using Plotly
                fig = px.bar(pivoted_df, barmode='group', title="Total Minutes of Content in Feb & Mar 2023",
                            labels={'value': 'Minutes'}, color_discrete_sequence=px.colors.sequential.Inferno)

                # Add text to the bars with monthly_video_count_after values
                for i, col in enumerate(pivoted_df.columns):
                    fig.data[i].text = pivoted_count_df['monthly_video_count_after'][col].astype(str)
                    fig.data[i].textposition = 'outside'

                # Customize the layout
                fig.update_layout(xaxis_title=None, yaxis_title=None, legend=dict(orientation='h',
                            yanchor='top', y=1.1, xanchor='left', x=0.01), legend_title="", width=800, height=600)

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""

                The graph above shows the monthly video count and the minutes of content uploaded after the disaster, by various news channels and individual journalists in Turkey.

Looking at the data, it appears that CNN TÜRK and Halktv are the channels with the highest number of videos uploaded in both February and March, with over 1,000 videos per month.

These channels also have a high number of minutes of content uploaded, with Halktv having the highest number of minutes in March. Other channels such as A Haber, Habertürk, and TV100 also have a significant number of videos and minutes uploaded.

On the other hand, some individual journalists such as Cüneyt Özdemir, Nevşin Mengü, and Erk Acarer have lower video and minute counts compared to the news channels. BaBaLa TV has the lowest counts among all channels with only one video uploaded in February and 4 videos uploaded in March.

SÖZCÜ Televizyonu also has a low number of videos uploaded in February but has a significantly high count of videos and minutes uploaded in March.

Overall, the data suggests that there is a considerable variation in the amount of content uploaded by different news channels and individual journalists in Turkey.
                """)

                # Add footer to the page
                st.markdown("<p style='text-align: right;'><i><b>* Data collected on 27rd of March 2023</b></i></p>", unsafe_allow_html=True)

        if page == "Monthly Likes After":
            with channel_details:

                # Load data
                monthly_df = pd.read_csv("All_stats/monthly_totals.csv")

                # Pivot the data to create a new DataFrame with columns for each month
                pivoted_df = monthly_df.pivot_table(index='channelName', columns='Month', values='likes_after_per_month')

                # Create a new DataFrame with the monthly_video_count_after values
                monthly_count_df = monthly_df[['channelName', 'Month', 'monthly_video_count_after', 'likes_after_per_month']]

                # Pivot the data to create a new DataFrame with columns for each month
                pivoted_count_df = monthly_count_df.pivot_table(index='channelName', columns='Month', values=['monthly_video_count_after','likes_after_per_month'])

                # Generate a horizontal bar chart using Plotly
                fig = px.bar(pivoted_df, barmode='group', title="Total Likes on Content Uploaded in Feb & Mar 2023",
                            labels={'value': 'Likes'}, color_discrete_sequence=px.colors.sequential.Inferno)

                # Add text to the bars with monthly_video_count_after values
                for i, col in enumerate(pivoted_df.columns):
                    fig.data[i].text = pivoted_count_df['monthly_video_count_after'][col].astype(str)
                    fig.data[i].textposition = 'outside'

                # Customize the layout
                fig.update_layout(xaxis_title=None, yaxis_title=None, legend=dict(orientation='h',
                            yanchor='top', y=1.1, xanchor='left', x=0.01), legend_title="", width=800, height=600)

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""

                When looking at the number of likes per month, we can see that some channels like Anadolu Ajansı, BBC News Türkçe, and Habertürk had a decrease in the number of likes from February to March. In contrast, other channels such as A Haber, Cüneyt Özdemir, Halktv, and SÖZCÜ Televizyonu had an increase in the number of likes.

Overall, we can see that there is no clear correlation between the number of videos uploaded and the number of likes received. It seems that factors such as content quality, engagement with the audience, and current events play a significant role in determining the number of likes a channel receives.

                """)

                # Add footer to the page
                st.markdown("<p style='text-align: right;'><i><b>* Data collected on 27rd of March 2023</b></i></p>", unsafe_allow_html=True)


        if page == "Monthly Views After":
            with channel_details:

                # Load data
                monthly_df = pd.read_csv("All_stats/monthly_totals.csv")

                # Pivot the data to create a new DataFrame with columns for each month
                pivoted_df = monthly_df.pivot_table(index='channelName', columns='Month', values='views_after_per_month')

                # Create a new DataFrame with the monthly_video_count_after values
                monthly_count_df = monthly_df[['channelName', 'Month', 'monthly_video_count_after', 'views_after_per_month']]

                # Pivot the data to create a new DataFrame with columns for each month
                pivoted_count_df = monthly_count_df.pivot_table(index='channelName', columns='Month', values=['monthly_video_count_after','views_after_per_month'])

                # Generate a horizontal bar chart using Plotly
                fig = px.bar(pivoted_df, barmode='group', title="Total Views on Content Uploaded in Feb & Mar 2023",
                labels={'value': 'Views'}, color_discrete_sequence=px.colors.sequential.Inferno)

                # Add text to the bars with monthly_video_count_after values
                for i, col in enumerate(pivoted_df.columns):
                    fig.data[i].text = pivoted_count_df['monthly_video_count_after'][col].astype(str)
                    fig.data[i].textposition = 'outside'

                # Customize the layout
                fig.update_layout(xaxis_title=None, yaxis_title=None, legend=dict(orientation='h',
                            yanchor='top', y=1.1, xanchor='left', x=0.01), legend_title="", width=800, height=600)

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""

                Based on the data provided, we can observe that the total number of videos produced by each channel decreased in March compared to February, except for SÖZCÜ Televizyonu, Halktv, and CNN TÜRK. However, the views received by these videos decreased more dramatically compared to the reduction in the number of videos produced, especially for channels like Habertürk, Yeni Şafak, and Anadolu Ajansı.

Interestingly, Halktv and SÖZCÜ Televizyonu saw an increase in the number of comments per month in March compared to February, even though the number of videos produced decreased slightly.

Overall, it seems that the viewing trends of Turkish news channels declined in March compared to February, which could be due to a variety of factors such as changes in the news cycle or shifts in audience behavior. However, further analysis would be needed to identify the reasons behind these trends.

                """)

                # Add footer to the page
                st.markdown("<p style='text-align: right;'><i><b>* Data collected on 27rd of March 2023</b></i></p>", unsafe_allow_html=True)

        if page == "Monthly Comments After":
            with channel_details:

                # Load data
                monthly_df = pd.read_csv("All_stats/monthly_totals.csv")

                # Pivot the data to create a new DataFrame with columns for each month
                pivoted_df = monthly_df.pivot_table(index='channelName', columns='Month', values='comments_after_per_month')

                # Create a new DataFrame with the monthly_video_count_after values
                monthly_count_df = monthly_df[['channelName', 'Month', 'monthly_video_count_after', 'comments_after_per_month']]

                # Pivot the data to create a new DataFrame with columns for each month
                pivoted_count_df = monthly_count_df.pivot_table(index='channelName', columns='Month', values=['monthly_video_count_after','comments_after_per_month'])

                # Generate a horizontal bar chart using Plotly
                fig = px.bar(pivoted_df, barmode='group', title="Total Comments on Content Uploaded in Feb & Mar 2023",
                labels={'value': 'Comments'}, color_discrete_sequence=px.colors.sequential.Inferno)

                # Add text to the bars with monthly_video_count_after values
                for i, col in enumerate(pivoted_df.columns):
                    fig.data[i].text = pivoted_count_df['monthly_video_count_after'][col].astype(str)
                    fig.data[i].textposition = 'outside'

                # Customize the layout
                fig.update_layout(xaxis_title=None, yaxis_title=None, legend=dict(orientation='h',
                            yanchor='top', y=1.1, xanchor='left', x=0.01), legend_title="", width=800, height=600)

                # display the chart
                st.plotly_chart(fig)

                st.markdown("""

                Regarding comments, in February, the channel with the highest number of comments was Halktv with a count of 67274 while in March, it was SÖZCÜ Televizyonu with a count of 101034. The channel with the lowest number of comments in February was SÖZCÜ Televizyonu with only 10 comments while in March, it was Habertürk with only 39 comments.

In summary, it seems that in general, Halktv and SÖZCÜ Televizyonu are the channels that have the highest number of comments across the two months. TV100 had the highest number of videos in February while Halktv had the highest number of videos in March. However, it is worth noting that these conclusions are based on only two months' worth of data and may not be indicative of overall trends.

                """)

                # Add footer to the page
                st.markdown("<p style='text-align: right;'><i><b>* Data collected on 27rd of March 2023</b></i></p>", unsafe_allow_html=True)

        if page == "Daily Uploaded Video":
            with channel_details:

                # Load data
                monthly_df = pd.read_csv("All_stats/daily_totals.csv")

                # Create a dictionary to map day names to their respective numeric values
                day_name_to_num = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}

                # Map the pushblishDayName column to their respective numeric values
                monthly_df['day_num'] = monthly_df['pushblishDayName'].map(day_name_to_num)

                # Pivot the data to create a new DataFrame with columns for each channel
                pivoted_df = monthly_df.pivot_table(index='day_num', columns='channelName', values='daily_counts')

                # Rename the index values to the corresponding day names
                pivoted_df.rename(index={1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}, inplace=True)

                # Create a new DataFrame with the daily_counts values
                monthly_count_df = monthly_df[['channelName', 'day_num', 'daily_counts']]

                # Pivot the data to create a new DataFrame with columns for each channel
                pivoted_count_df = monthly_count_df.pivot_table(index='day_num', columns='channelName', values='daily_counts')

                # Rename the index values to the corresponding day names
                pivoted_count_df.rename(index={1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}, inplace=True)

                # Generate a horizontal bar chart using Plotly
                fig = px.bar(pivoted_df, barmode='group', title="Content Uploaded Daily in Feb & Mar 2023",
                            labels={'value': 'Daily Content'}, color_discrete_sequence=px.colors.sequential.Inferno)

                # Customize the layout
                fig.update_layout(xaxis_title=None, yaxis_title=None, legend=dict(orientation='h',
                                            yanchor='top', y=1.1, xanchor='left', x=0.01), legend_title="", width=800, height=600)

                # display the chart
                st.plotly_chart(fig)


                st.markdown("""

                From the given data, we can see that the news channels have varying daily counts of published news articles across different days of the week.

A Haber, CNN TÜRK, Halktv, and TV100 seem to have the highest daily counts of published news articles, whereas BBC News Türkçe, BaBaLa TV, and Habertürk have the lowest.

Furthermore, looking at the days of the week, Tuesday and Thursday seem to have the highest daily counts of published news articles across the majority of the channels, whereas Sunday seems to have the lowest daily counts.

Overall, it is difficult to draw any definitive conclusions from this data without additional information, but we can see that different news channels have different patterns in terms of when they publish their news articles.
                """)

                # Add footer to the page
                st.markdown("<p style='text-align: right;'><i><b>* Data collected on 27rd of March 2023</b></i></p>", unsafe_allow_html=True)


        elif page == "Subscribers per Video":
            with channel_details:

                # create a new DataFrame with 'channelName', 'view_per_video_after', and 'view_per_video_before' columns
                subs_per_video_df = edited_stats_df[['channelName','subscribers', 'subscribers_per_video','totalVideos']]

                fig = px.bar(data_frame=subs_per_video_df.sort_values('subscribers', ascending=True),
                x="subscribers", y="channelName", color='subscribers_per_video', orientation='h',
                color_continuous_scale=px.colors.sequential.Viridis, title = 'Number of Subscribers per Uploaded Video up to 27th of March 2023')

                fig.update_layout(coloraxis_colorbar=dict(title="Subscribers per Video"), yaxis_title=None, xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
                width=800, height=600)


                # display the chart
                st.plotly_chart(fig)

                st.markdown("""

                Looking at the data, it appears that BaBaLa TV has the highest number of subscribers per video, with a whopping 11,152 subscribers per video on average.

BBC News Türkçe comes in second with an average of 189 subscribers per video, followed closely by Cüneyt Özdemir with 312 subscribers per video. On the other hand, Erk Acarer and SÖZCÜ Televizyonu have the lowest number of subscribers per video with only 168 and 37 respectively.

It's interesting to note that some channels with fewer subscribers, such as A Haber and Anadolu Ajansı, have a higher number of subscribers per video than channels with larger subscriber counts like Habertürk and FOX Haber. This suggests that the quality and engagement of the content may be more important than the number of subscribers.

                """)

                # Add footer to the page
                st.markdown("<p style='text-align: right;'><i><b>* Data collected on 27rd of March 2023</b></i></p>", unsafe_allow_html=True)


elif page == "Top 10 Videos by Like Count and View Count":
    with channel_details:
        st.header("10 Most Popular Videos based on Likes and Views per Channel")

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

        # get the top 10 videos based on like count
        top10 = df.sort_values('likeCount', ascending=False).iloc[:10]

        # generate plotly graph
        fig = px.bar(data_frame=df.sort_values('likeCount', ascending=False)[0:9],
                    x="title", y="likeCount", color='viewCount', title=channel_data[channel_choice]['title'])

        # format y-axis labels to show thousands
        fig.update_yaxes(tickformat=',.0f')

        fig.update_layout(xaxis={'tickmode': 'array', 'tickvals': []},xaxis_title=None,legend=dict(orientation='h',yanchor='top',y=1.1,xanchor='left',x=0.01),legend_title="",
        width=800, height=600,yaxis_title=None)

        # display plotly graph
        st.plotly_chart(fig)

        # show the list of top 10 videos in a table
        top10_table = top10[['title', 'likeCount','viewCount']].reset_index(drop=True)
        top10_table.index += 1  # start the index from 1 instead of 0

        # set header background color
        top10_table = top10_table.style.set_properties(**{'background-color': '#F0F2F6', 'color': 'black'}, subset=pd.IndexSlice[:, :])

        # display the table
        st.write("Top 10 Video Titles:")
        st.write(top10_table)

        st.markdown("""

        The accuracy of the Top 10 Videos by Like Count and View Count may vary due to daily quotas on YouTube APIs, which can result in incomplete data for channels with a high number of total videos.

The daily quota for YouTube Data API v3 was 10,000 units per day as of September 2021, but this may change at any time. It's important to follow YouTube's official documentation and guidelines to avoid exceeding the quota limit and ensure compliance with their terms of service.

                """)

        # Add footer to the page
        st.markdown("<p style='text-align: right;'><i><b>* Data collected on 27rd of March 2023</b></i></p>", unsafe_allow_html=True)
