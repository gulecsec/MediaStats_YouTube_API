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

        co_df = pd.read_csv("media_stats/stats_cuneytozdemir.csv")
        cnn_df = pd.read_csv("media_stats/stats_cnnturk.csv")
        tv100_df = pd.read_csv("media_stats/stats_tv100.csv")
        htv_df = pd.read_csv("media_stats/stats_htv.csv")
        ntv_df
        soz_df
        fox_df
        bab_df
        fox_df
        shw_df

        # create a dictionary to store data frames and graph titles for each channel
        channel_data = {
        'Cüneyt Özdemir': {'df': co_df, 'title': 'Cüneyt Özdemir Top Videos by Like Count and View Count'},
        'CNN TÜRK': {'df_df': cnn_df, 'title': 'CNN TÜRK Top Videos by Like Count and View Count'},
        'TV100': {'df': tv100_df, 'title': 'ABC News (Australia) Top Videos by Like Count and View Count'},
        'Habertürk TV': {'df': htv_df, 'title': 'Anadolu Ajansı Top Videos by Like Count and View Count'},
        'NTV': {'df': ntv_df, 'title': 'NTV Top Videos by Like Count and View Count'},
        'SÖZCÜ Televizyonu': {'df': soz_df, 'title': 'SÖZCÜ Televizyonu Top Videos by Like Count and View Count'},
        'Fox News': {'df': fox_df, 'title': 'Fox News Top Videos by Like Count and View Count'},
        'BaBaLa TV': {'df': bab_df, 'title': 'BaBaLa TV Top Videos by Like Count and View Count'},
        'FOX Haber': {'df': fox_df, 'title': 'FOX Haber Top Videos by Like Count and View Count'},
        'Show Ana Haber': {'df': shw_df, 'title': 'Show Ana Haber Top Videos by Like Count and View Count'}
        }






        # add dropdown to select a channel
        channel_choice = st.selectbox("Select Channel", stats_df["channelName"].unique())
        year_choice = st.selectbox("Select Year", co_df["Year"].sort_values(ascending=False).unique().tolist())
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month_choice = st.selectbox("Select Month", months)

        # years = [i for i in range(2010, 2024)]
        # channels = ["Cuneyt Ozdemir Media", "AHaber"]

        # display the selected graph
        if channel_choice == stats_df["channelName"][0]:
            fig1 = px.bar(data_frame=co_df.sort_values('likeCount', ascending=False)[0:9],
                          x="title", y="likeCount", color='viewCount', title="likeCount-viewCount")
            st.plotly_chart(fig1)
        else:
            fig1 = px.bar(data_frame=co_df.sort_values('likeCount', ascending=False),
                          x="title", y="likeCount", color='viewCount', title="likeCount-viewCount")
            st.plotly_chart(fig1)

        # filtered_df = video_df.loc[(video_df["Year"]==selected_year) & (video_df["Month"]==selected_month)]
        # # create a filter for the selected channel
        # channel_filter = stats_df['channelName'] == channel_choice

        # # create a new dataframe with only data for the selected channel
        # channel_stats_df = stats_df[channel_filter]

        # # create a bar chart for the views and subscribers for the selected channel
        # fig1 = px.bar(data_frame=channel_stats_df, x='year', y='views', color='month', title=f"{channel_choice} - Views per Year")
        # st.plotly_chart(fig1)

        # fig2 = px.bar(data_frame=channel_stats_df, x='year', y='subscribers', color='month', title=f"{channel_choice} - Subscribers per Year")
        # st.plotly_chart(fig2)
