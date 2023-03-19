import streamlit as st
import pandas as pd
import plotly.express as px

# Define function to show homepage
def show_homepage():
    st.set_page_config(page_title="MediaStats", page_icon=":tv:", layout="wide")
    st.title("How Turkish News Media's YouTube Stats Stack Up: Exploring the Data on My Streamlit App")
    st.markdown("In this tutorial, we'll explore how to use the YouTube API with Python to interact with one of the world's largest video-sharing platforms, which boasts billions of daily users uploading, viewing, and commenting on videos. By the end of this tutorial, you'll know how to automate various tasks using the YouTube API.")

    # Create navigation sidebar
    navigation = st.sidebar.radio("Navigation", ["Home", "Channel Details"])

    # Show homepage by default
    if navigation == "Home":
        show_stats()
    elif navigation == "Channel Details":
        show_channel_details()

# Define function to show stats page
def show_stats():
    with st.container():
        st.subheader("YouTube Stats of Turkish News Media in YouTube")
        years=[ i for i in range(2010, 2024)]
        months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        channels = ["Cuneyt Ozdemir Media", "AHaber"]
        stats_df = pd.read_csv("media_stats/media_stats.csv")

        fig1 = px.bar(data_frame=stats_df.sort_values('views', ascending=False),
                      x="channelName", y="views",color='totalVideos', title="Views-Total Videos")
        st.write(fig1)

        fig2 = px.bar(data_frame=stats_df.sort_values('subscribers', ascending=False),
                      x="channelName", y="subscribers",color='totalVideos', title="Subscribers-Total Videos")
        st.write(fig2)

# Define function to show channel details page
def show_channel_details():
    with st.container():
        st.subheader("Channel Details")
        channels = ["Cuneyt Ozdemir Media", "AHaber"]
        stats_df = pd.read_csv("media_stats/media_stats.csv")

        for channel in channels:
            channel_stats_df = stats_df[stats_df["channelName"] == channel]
            fig1 = px.bar(data_frame=channel_stats_df, x="monthYear", y="views", title=f"{channel} Views Over Time")
            st.write(fig1)

            fig2 = px.bar(data_frame=channel_stats_df, x="monthYear", y="subscribers", title=f"{channel} Subscribers Over Time")
            st.write(fig2)

# Run app
if __name__ == "__main__":
    show_homepage()
