import mysql.connector
import streamlit as st
import pandas as pd
from datetime import datetime

mydbse = mysql.connector.connect(
    host = 'bg9wpv58aase6fgcsioc-mysql.services.clever-cloud.com',
    user = 'uuzmzajbberam5qy',
    password = 'HcmWyMhQVLzurg9NOWPo',
    database = 'bg9wpv58aase6fgcsioc',
    port = 3306
)

mycursor = mydbse.cursor()
print('Connection established successfully')

# Setting page config
st.set_page_config(page_title="CRUD Queries")

# Author name and current date
st.write("Author: Ramlavan")
st.write(f"Current Date: {datetime.now().strftime('%Y-%m-%d')}")
st.write("")

# Setting title
st.markdown("""<h1 style='margin-top: -5px; margin-bottom: -10px;'>CRUD Operations with MySQL</h1>""", 
            unsafe_allow_html=True)


#Displaying options in sidebar
options = st.selectbox("Select an Operation",('Select','Create','Read','Update','Delete'))


# To perform selected CRUD operation
if options =='Select':
    st.subheader('Select an option')

elif options == 'Create':
    st.subheader('Create a Record')
    name = st.text_input('Enter your Name')
    email = st.text_input('Enter your Email')


    if st.button('Create'):                                                                                
        # SQL Command                            
        sqlcmd = """ INSERT into users          
        (name,email)                                
        values(%s,%s)
        """
        values = (name,email)   
        mycursor.execute(sqlcmd,values)
        mydbse.commit()
        st.success("Record Created Successfully")



elif options == 'Read':
    st.subheader('Read Records')
    mycursor.execute('SELECT * from users')

    rows = mycursor.fetchall()  # Fetches the rows

    for row in rows:
        st.write(row)



elif options == 'Update':
    st.subheader('Update Records')

   # Receive and round the ID input from the user
    id = round(st.number_input("Enter ID", step=1, format="%d"))
    name = st.text_input("Enter New Name")
    email = st.text_input("Enter New Email")

    if st.button("Update"):

        sqlcmd = "update users set name = %s, email = %s where id = %s"
        values = (name,email,id)

        mycursor.execute(sqlcmd,values)
        mydbse.commit()
        st.success("Data updated successfully")




elif options == 'Delete':
    st.subheader("Delete Records")
    id = round(st.number_input("Enter ID", step=1, format="%d"))
    if st.button("Delete"):
        sqlcmd = "delete from users where id = %s"
        values = (id,)
        mycursor.execute(sqlcmd,values)
        mydbse.commit()
        st.success("Data Deleted Successfully")








