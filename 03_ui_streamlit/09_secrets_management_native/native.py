import streamlit as st

# Everything is accessible via the st.secrets dict:

st.write("DB username:", st.secrets["db_username"]) #set db_username and db_password in secrets.toml file in .streamlit folder
st.write("DB password:", st.secrets["db_password"])

# And the root-level secrets are also accessible as environment variables:

import os

st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
) # this checks if os usernmane = secrets username. Use export db_username="" as command for setting username