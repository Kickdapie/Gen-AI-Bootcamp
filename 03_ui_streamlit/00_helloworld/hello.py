import streamlit as st
st.title("Text Display")
st.write("Write content")
st.text("Text content...")
st.markdown("# Markdown content")
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.title("Title content")
st.header("Header content")
st.subheader("Sub header content")
st.code("[i for i in range(1,10)]")

st.title("Data Display")

import pandas as pd

df : pd.DataFrame = pd.DataFrame({"Col1":[1,2,3],
                                "Col2":['a','b','c']})

# st.write(df)
# st.table(df)
# st.json(df.to_dict())
# st.metric('My metric', 42, 2)

st.title("Display Media")
st.video("https://youtu.be/_OVnXw2ldog?si=2qsVAd3WdTUAlRVH")
st.image("flag.png")
st.audio("whistle.mp3")