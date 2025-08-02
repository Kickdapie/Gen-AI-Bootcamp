import streamlit as st
import plotly.graph_objects as go

st.title('Agent App')

left_col, right_col = st.columns(2)

with left_col:
    st.subheader('Conversation')

with right_col:
    fig = go.Figure(go.Scattermapbox())
    fig.update_layout(
        mapbox=dict(
            accesstoken="",
            center=go.layout.mapbox.Center(
                lat=24,
                lon=-73
            )
        ),
        margin=dict(l=0, r=0, t=0, b=0),
    )
    st.plotly_chart(
        fig,
        config={"displayModeBar": False},
        use_container_width=True,
        key="plotly",
    )

st.chat_input(
    placeholder='Ask your question here',
    key="input_user_msg"
)