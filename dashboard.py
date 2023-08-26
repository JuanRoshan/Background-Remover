# import streamlit as st
# import plotly_express as px
# import pandas as pd
# import os
# import warnings
# import numpy as np
# import matplotlib.animation as animation
# import matplotlib.pyplot as plt
# import time
# import random


# warnings.filterwarnings("ignore")


# st.set_page_config(page_title="superstore!!!", page_icon=":bar_chart:", layout="wide")

# st.title(" :bar_chart: Class 12 Report Analysis")
# st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

# f1 = st.file_uploader(":file_folder: upload a file", type=(["csv","txt","xlsx","xls"]))
# if f1 is not None:
#     filename = f1.name
#     st.write(filename)
#     df = pd.read_csv(filename, encoding="ISO-8859-1")
# else:
#     os.chdir(r"C:\Users\juanr\OneDrive\Desktop\files")
#     df = pd.read_csv("addresses.csv", encoding="ISO-8859-1")





# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=["a", "b", "c"])

# st.bar_chart(chart_data)


# st.image("https://www.stuttgarter-nachrichten.de/media.media.099d6fff-4603-4e3f-9ad2-6892d828f829.original1024.jpg", caption="This is Andrew Tate", width=500, use_column_width=400, clamp=False, channels="RGB", output_format="auto")


# #not 
# fig, ax = plt.subplots()

# max_x = 1
# max_rand = 5

# x = np.arange(0, max_x)
# ax.set_ylim(0, max_rand)
# line, = ax.plot(x, np.random.randint(0, max_rand, max_x))
# the_plot = st.pyplot(plt)

# def init():  # give a clean slate to start
#     line.set_ydata([np.nan] * len(x))

# def animate(i):  # update the y values (every 1000ms)
#     line.set_ydata(np.random.randint(0, max_rand, max_x))
#     the_plot.pyplot(plt)

# init()
# for i in range(100):
#     animate(i)
#     time.sleep(0.1)
























# #not
# df = px.data.gapminder()  
# fig = px.scatter_geo(df, locations="iso_alpha", color="continent", hover_name="country", size="pop",
#                animation_frame="year", projection="natural earth")
# fig.show()





import streamlit as st
import pandas as pd
import plotly_express as px 
import base64
from io import StringIO, BytesIO
from streamlit_webrtc import webrtc_streamer, RTCConfiguration
import av 
import cv2





cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

class VideoProcessor:
	def recv(self, frame):
		frm = frame.to_ndarray(format="bgr24")

		faces = cascade.detectMultiScale(cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY), 1.1, 3)

		for x,y,w,h in faces:
			cv2.rectangle(frm, (x,y), (x+w, y+h), (0,255,0), 3)

		return av.VideoFrame.from_ndarray(frm, format='bgr24')

webrtc_streamer(key="key", video_processor_factory=VideoProcessor,
				rtc_configuration=RTCConfiguration(
					{"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
					)
	)





def generate_excel_download_link(df):
    # Credit Excel: https://discuss.streamlit.io/t/how-to-add-a-download-excel-csv-function-to-a-button/4474/5
    towrite = BytesIO()
    df.to_excel(towrite, encoding="utf-8", index=False, header=True)  # write to BytesIO buffer
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="data_download.xlsx">Download Excel File</a>'
    return st.markdown(href, unsafe_allow_html=True)


def generate_html_download_link(fig):
    # Credit Plotly: https://discuss.streamlit.io/t/download-plotly-plot-as-html/4426/2
    towrite = StringIO()
    fig.write_html(towrite, include_plotlyjs="cdn")
    towrite = BytesIO(towrite.getvalue().encode())
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:text/html;charset=utf-8;base64, {b64}" download="plot.html">Download Plot</a>'
    return st.markdown(href, unsafe_allow_html=True)



st.set_page_config(page_title='Report Card Analysis')
st.title('Report Card Analysis 📈')
st.subheader('Feed your Report Card(Excel format)')

uploaded_file = st.file_uploader('Choose a XLXS file',type='xlsx')
if uploaded_file:
    st.markdown('---')
    df = pd.read_excel(uploaded_file,engine='openpyxl')
    st.dataframe(df)
    groupby_column = st.selectbox(

        'What do you want to analyze?',
        ( 'Chemistry', 'C.SC', 'Math','English'),
    )
    
    
    # st.image("https://www.stuttgarter-nachrichten.de/media.media.099d6fff-4603-4e3f-9ad2-6892d828f829.original1024.jpg", caption="He needs to escape the matrix", width=500, use_column_width=400, clamp=False, channels="RGB", output_format="auto")

    

    output_columns = ['Month', 'Marks'] 
    df_grouped = df.groupby(by=[groupby_column], as_index=False) [output_columns].sum()

    # fig = px.line(df, x="Month", y="Marks", title='Student progress')
    # fig.show()


    



    
    fig = px.bar(
        df_grouped,
        x='Month',
        y='Marks',
        color='Marks',
        color_continuous_scale = ['red', 'yellow','green'],
        template='plotly_white',
        title= f'<b>Monthly Progress of Student </b>',
        # animation_frame="Marks", animation_group="Month"

    )
    
    st.plotly_chart(fig)

    



    


    


    
































































    

    # fig = px.bar(df_grouped, x="Month", y="Marks", color="Attendance", color_continuous_scale = ['red', 'yellow','green'],

    #  animation_frame="Marks", animation_group="Month")
    # fig.show()








    # st.subheader('Downloads:')
    # generate_excel_download_link(df_grouped)
    # generate_html_download_link(fig)




