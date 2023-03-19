import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
stats_df = pd.read_csv("media_stats/media_stats.csv")

# Define page layout
header = st.container()
dataset = st.container()
features = st.container()
channel_details = st.container()

# Define sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "Channel Details"))

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

elif page == "Channel Details":
    with channel_details:
        st.title("Channel Details")

        # Load data
        co_df = pd.read_csv("media_stats/mediastats_cuneytozdemir.csv")

        # add dropdown to select a channel
        channel_choice = st.selectbox("Select Channel", stats_df["channelName"].unique())
        year_choice = st.selectbox("Select Year", co_df["Year"].sort_values(ascending=False).unique().tolist())
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month_choice = st.selectbox("Select Month", months)

        # years = [i for i in range(2010, 2024)]
        # channels = ["Cuneyt Ozdemir Media", "AHaber"]

        # display the selected graph
        if channel_choice in stats_df["channelName"][0]:
            fig = px.bar(data_frame=co_df.sort_values('viewCount', ascending=False)[0:9],
                          x="channelTitle", y="viewCount", color='viewCount', title="Best Performing Videos")
            fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
        else:
            fig = px.bar(data_frame=co_df.sort_values('viewCount', ascending=False),
                          x="channelTitle", y="likeCount", color='viewCount', title="Subscribers-Total Videos")
        st.plotly_chart(fig)

        # # create a filter for the selected channel
        # channel_filter = stats_df['channelName'] == channel_choice

        # # create a new dataframe with only data for the selected channel
        # channel_stats_df = stats_df[channel_filter]

        # # create a bar chart for the views and subscribers for the selected channel
        # fig1 = px.bar(data_frame=channel_stats_df, x='year', y='views', color='month', title=f"{channel_choice} - Views per Year")
        # st.plotly_chart(fig1)

        # fig2 = px.bar(data_frame=channel_stats_df, x='year', y='subscribers', color='month', title=f"{channel_choice} - Subscribers per Year")
        # st.plotly_chart(fig2)
