# import libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
stats_df = pd.read_csv("media_stats/media_stats.csv")

# Define page layout
header = st.container()
navigation = st.container()
channel_stats = st.container()

# Define navigation items
nav_items = ["All Channels"] + list(stats_df["channelName"].unique())

# Define helper function to get channel data
def get_channel_data(channel_name):
    if channel_name == "All Channels":
        return stats_df
    else:
        return stats_df[stats_df["channelName"] == channel_name]

# Define pages
def show_homepage():
    with header:
        st.title("How Turkish News Media's YouTube Stats Stack Up: Exploring the Data on My Streamlit App")
        st.markdown("In this tutorial, we'll explore how to use the YouTube API with Python to interact with one of the world's largest video-sharing platforms, which boasts billions of daily users uploading, viewing, and commenting on videos. By the end of this tutorial, you'll know how to automate various tasks using the YouTube API.")

    with navigation:
        st.sidebar.title("Navigation")
        selection = st.sidebar.radio("Go to", nav_items)

    with channel_stats:
        if selection == "All Channels":
            fig1 = px.bar(data_frame=stats_df.sort_values('views', ascending=False),
                          x="channelName", y="views",color='totalVideos', title="Views-Total Videos")
            st.write(fig1)

            fig2 = px.bar(data_frame=stats_df.sort_values('subscribers', ascending=False),
                          x="channelName", y="subscribers",color='totalVideos', title="Subscribers-Total Videos")
            st.write(fig2)
        else:
            channel_data = get_channel_data(selection)

            fig1 = px.bar(data_frame=channel_data.sort_values('views', ascending=False),
                          x="month", y="views",color='totalVideos', title=f"{selection} Views-Total Videos")
            st.write(fig1)

            fig2 = px.bar(data_frame=channel_data.sort_values('subscribers', ascending=False),
                          x="month", y="subscribers",color='totalVideos', title=f"{selection} Subscribers-Total Videos")
            st.write(fig2)

def show_channel_stats():
    with header:
        st.title("Channel Stats")

    with navigation:
        st.sidebar.title("Navigation")
        selection = st.sidebar.radio("Go to", nav_items)

    with channel_stats:
        channel_data = get_channel_data(selection)

        fig1 = px.bar(data_frame=channel_data.sort_values('views', ascending=False),
                      x="month", y="views",color='totalVideos', title=f"{selection} Views-Total Videos")
        st.write(fig1)

        fig2 = px.bar(data_frame=channel_data.sort_values('subscribers', ascending=False),
                      x="month", y="subscribers",color='totalVideos', title=f"{selection} Subscribers-Total Videos")
        st.write(fig2)

# Run app
if __name__ == "__main__":
    page = st.sidebar.selectbox("Select a page", ["Homepage", "Channel Stats"])
    if page == "Homepage":
        show_homepage()
    elif page == "Channel Stats":
        show_channel_stats()

    # # selected_media =
    # selected_year = st.sidebar.selectbox("Select Year", [""] + years, index=0)
    # selected_month = st.sidebar.selectbox("Select Month", [""] + months, index=0)
    # if selected_year != "" and selected_month != "":
    #     filtered_df = stats_df.loc[(stats_df["Year"]==selected_year) & (stats_df["Month"]==selected_month)]
    # else:
    #     filtered_df = stats_df
    # # if st.session_state.get('refresh', False):
    # #     selected_year = ""
    # #     selected_month = ""
    # #     st.session_state['refresh'] = False
    # # if selected_year != "" and selected_month != "":
    # #     filtered_df = video_df.loc[(video_df["Year"]==selected_year) & (video_df["Month"]==selected_month)]
    # # else:
    # #     filtered_df = video_df

    # st.session_state.selected_year = selected_year
    # st.session_state.selected_month = selected_month

    # # if st.button("Refresh"):
    # #     st.session_state['refresh'] = True
    # #     st.experimental_rerun()

    # # Display the DataFrame
    # st.write(filtered_df)
