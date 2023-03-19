import streamlit as st
import pandas as pd
import plotly.express as px


header = st.container()
dataset= st.container()
features = st.container()

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
    stats_df = pd.read_csv("media_stats/media_stats.csv")
    fig1 = px.bar(data_frame=stats_df.sort_values('views', ascending=False), x="channelName", y="views",color='totalVideos', title="Views-Total Videos")
    st.write(fig1)

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

