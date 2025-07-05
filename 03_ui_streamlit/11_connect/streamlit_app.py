# streamlit_app.py

import streamlit as st
from sqlalchemy import text  

#Create the SQL connection to pets_db as specified in your secrets file.
conn = st.connection('pets_db', type='sql')

#Insert some data with conn.session.
with conn.session as s:
    s.execute(text('CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);')) #must be wrapped in text
    s.execute(text('DELETE FROM pet_owners;'))
    pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
    for k in pet_owners:
        s.execute(
            text('INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);'),

            params=dict(owner=k, pet=pet_owners[k])
        )
    s.commit()

#Query and display the data you inserted
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)

'''
Make secrets.toml in .streamlit
Connect by 
    [connections.pets_db]
    url = "sqlite:////mnt/c/Users/danny/Downloads/Gen-AI-Bootcamp/03_ui_streamlit/11_connect/pets.db"
Text must be wrapped because SQLAlchemy 2.0+ no longer allows passing raw SQL strings directly to execute(). 
You must wrap the SQL in text() to mark it explicitly as a SQL statement.

Why Does it need secrets.toml (for privacy reasons)
Why is session needed to insert the data (to act as communicator for the database)
'''

