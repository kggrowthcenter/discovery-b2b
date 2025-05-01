import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import toml
import pymysql


@st.cache_resource()
def fetch_data_creds():
    secret_info = st.secrets["sheets"]
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(secret_info, scope)
    client = gspread.authorize(creds)
    
    # Open the spreadsheet
    spreadsheet = client.open('Discovery Test Result - Dashboard Credentials')
    
    # Fetch Sheet1 (Main Data)
    sheet1 = spreadsheet.sheet1
    data1 = sheet1.get_all_records()
    df_creds = pd.DataFrame(data1)

    # Fetch Sheet2 (Typology Report Links)
    sheet2 = spreadsheet.get_worksheet(1)  # Index 1 refers to the second sheet
    data2 = sheet2.get_all_records()
    df_links = pd.DataFrame(data2)

    # Fetch Sheet3 (B2B)
    sheet3 = spreadsheet.get_worksheet(2)  # Index 2 refers to the third sheet
    data3 = sheet3.get_all_records()
    df_b2b = pd.DataFrame(data3)

    return df_creds, df_links, df_b2b  # Return both DataFrames

def fetch_data_discovery():
    try:
        connection_kwargs = {
            'host': st.secrets["discovery"]["host"],
            'port': st.secrets["discovery"]["port"],
            'user': st.secrets["discovery"]["user"],
            'password': st.secrets["discovery"]["password"],
            'database': st.secrets["discovery"]["database"],
            'cursorclass': pymysql.cursors.DictCursor,
        }
        conn = pymysql.connect(**connection_kwargs)

        with open('query_discovery.sql', 'r') as sql_file:
            query = sql_file.read()

        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return pd.DataFrame(rows)
    except Exception as e:
        st.error(f"An error occurred while fetching data from Discovery: {e}")
        return pd.DataFrame()
