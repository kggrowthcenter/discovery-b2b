from navigation import make_sidebar
import streamlit as st
from data_processing import finalize_data
import pandas as pd
import io
import xlsxwriter

st.set_page_config(
    page_title='Test Result',
    page_icon=':🎭:', 
)

make_sidebar()

# Display the title of the app
st.title("🧙‍♂️ Discovery Test Result")

df_creds, df_links, df_b2b, df_final = finalize_data()

df_merged = df_final.copy()

# GI

# Daftar kolom yang akan di-hyperlink
gi_columns = {
    "GI_Creativity Style": "GI_Creativity Style",
    "GI_Curiosity": "GI_Curiosity",
    "GI_Grit": "GI_Grit",
    "GI_Humility": "GI_Humility",
    "GI_Meaning Making": "GI_Meaning Making",
    "GI_Mindset": "GI_Mindset",
    "GI_Purpose in life": "GI_Purpose in Life"
}

# Loop untuk merge & buat hyperlink
for new_col, merge_col in gi_columns.items():
    df_merged = df_merged.merge(
        df_links, left_on=merge_col, right_on="Tipologi", how="left", 
        suffixes=("", f"_{new_col}")  # Tambahkan suffix sesuai GI yang diproses
    )

    # Cari kolom yang sesuai dengan suffix
    link_col = f"Link_{new_col}" if f"Link_{new_col}" in df_merged.columns else "Link"
    tipologi_col = f"Tipologi_{new_col}" if f"Tipologi_{new_col}" in df_merged.columns else "Tipologi"

    # Buat hyperlink
    df_merged[new_col] = df_merged.apply(
        lambda row: f'<a href="{row[link_col]}" target="_blank">{row[tipologi_col]}</a>' 
        if pd.notna(row[link_col]) else row[tipologi_col], 
        axis=1
    )

# LEAN

# Daftar kolom yang akan di-hyperlink
lean_columns = {
    "LEAN_overall": "LEAN_overall",
    "LEAN_Cognitive Felxibility": "LEAN_Cognitive Flexibility",
    "LEAN_Intellectual Curiosity": "LEAN_Intellectual Curiosity",
    "LEAN_Open-Mindedness": "LEAN_Open-Mindedness",
    "LEAN_Personal Learner": "LEAN_Personal Learner",
    "LEAN_Self-Reflection": "LEAN_Self-Reflection",
    "LEAN_Self-Regulation": "LEAN_Self-Regulation",
    "LEAN_Social Astuteness": "LEAN_Social Astuteness",
    "LEAN_Social Flexibility": "LEAN_Social Flexibility",
    "LEAN_Unconventional Thinking": "LEAN_Unconventional Thinking"
}

# Loop untuk merge & buat hyperlink
for new_col, merge_col in lean_columns.items():
    df_merged = df_merged.merge(
        df_links, left_on=merge_col, right_on="Tipologi", how="left", 
        suffixes=("", f"_{new_col}")  # Tambahkan suffix sesuai GI yang diproses
    )

    # Cari kolom yang sesuai dengan suffix
    link_col = f"Link_{new_col}" if f"Link_{new_col}" in df_merged.columns else "Link"
    tipologi_col = f"Tipologi_{new_col}" if f"Tipologi_{new_col}" in df_merged.columns else "Tipologi"

    # Buat hyperlink
    df_merged[new_col] = df_merged.apply(
        lambda row: f'<a href="{row[link_col]}" target="_blank">{row[tipologi_col]}</a>' 
        if pd.notna(row[link_col]) else row[tipologi_col], 
        axis=1
    )

# ELITE

# Daftar kolom yang akan di-hyperlink
elite_columns = {
    "ELITE_overall": "ELITE_overall",
    "ELITE_Empathy": "ELITE_Empathy",
    "ELITE_Motivation": "ELITE_Motivation",
    "ELITE_Self-Awareness": "ELITE_Self-Awareness",
    "ELITE_Self-Regulation": "ELITE_Self-Regulation",
    "ELITE_Social skills": "ELITE_Social skills"
}

# Loop untuk merge & buat hyperlink
for new_col, merge_col in elite_columns.items():
    df_merged = df_merged.merge(
        df_links, left_on=merge_col, right_on="Tipologi", how="left", 
        suffixes=("", f"_{new_col}")  # Tambahkan suffix sesuai GI yang diproses
    )

    # Cari kolom yang sesuai dengan suffix
    link_col = f"Link_{new_col}" if f"Link_{new_col}" in df_merged.columns else "Link"
    tipologi_col = f"Tipologi_{new_col}" if f"Tipologi_{new_col}" in df_merged.columns else "Tipologi"

    # Buat hyperlink
    df_merged[new_col] = df_merged.apply(
        lambda row: f'<a href="{row[link_col]}" target="_blank">{row[tipologi_col]}</a>' 
        if pd.notna(row[link_col]) else row[tipologi_col], 
        axis=1
    )

# Astaka

# Daftar kolom yang akan di-hyperlink
astaka_columns = {
    "Astaka_Top 1_typology": "Astaka_Top 1_typology",
    "Astaka_Top 2_typology": "Astaka_Top 2_typology",
    "Astaka_Top 3_typology": "Astaka_Top 3_typology",
    "Astaka_Top 4_typology": "Astaka_Top 4_typology",
    "Astaka_Top 5_typology": "Astaka_Top 5_typology",
    "Astaka_Top 6_typology": "Astaka_Top 6_typology"
}

# Loop untuk merge & buat hyperlink
for new_col, merge_col in astaka_columns.items():
    df_merged = df_merged.merge(
        df_links, left_on=merge_col, right_on="Tipologi", how="left", 
        suffixes=("", f"_{new_col}")  # Tambahkan suffix sesuai GI yang diproses
    )

    # Cari kolom yang sesuai dengan suffix
    link_col = f"Link_{new_col}" if f"Link_{new_col}" in df_merged.columns else "Link"
    tipologi_col = f"Tipologi_{new_col}" if f"Tipologi_{new_col}" in df_merged.columns else "Tipologi"

    # Buat hyperlink
    df_merged[new_col] = df_merged.apply(
        lambda row: f'<a href="{row[link_col]}" target="_blank">{row[tipologi_col]}</a>' 
        if pd.notna(row[link_col]) else row[tipologi_col], 
        axis=1
    )

# Genuine

# Daftar kolom yang akan di-hyperlink
genuine_columns = {
"Genuine_Top 1_typology": "Genuine_Top 1_typology",
"Genuine_Top 2_typology": "Genuine_Top 2_typology",
"Genuine_Top 3_typology": "Genuine_Top 3_typology",
"Genuine_Top 4_typology": "Genuine_Top 4_typology",
"Genuine_Top 5_typology": "Genuine_Top 5_typology",
"Genuine_Top 6_typology": "Genuine_Top 6_typology",
"Genuine_Top 7_typology": "Genuine_Top 7_typology",
"Genuine_Top 8_typology": "Genuine_Top 8_typology",
"Genuine_Top 9_typology": "Genuine_Top 9_typology"
}

# Loop untuk merge & buat hyperlink
for new_col, merge_col in genuine_columns.items():
    df_merged = df_merged.merge(
        df_links, left_on=merge_col, right_on="Tipologi", how="left", 
        suffixes=("", f"_{new_col}")  # Tambahkan suffix sesuai GI yang diproses
    )

    # Cari kolom yang sesuai dengan suffix
    link_col = f"Link_{new_col}" if f"Link_{new_col}" in df_merged.columns else "Link"
    tipologi_col = f"Tipologi_{new_col}" if f"Tipologi_{new_col}" in df_merged.columns else "Tipologi"

    # Buat hyperlink
    df_merged[new_col] = df_merged.apply(
        lambda row: f'<a href="{row[link_col]}" target="_blank">{row[tipologi_col]}</a>' 
        if pd.notna(row[link_col]) else row[tipologi_col], 
        axis=1
    )

# --- Display Data ---

# --- Select Columns to Display ---
selected_columns = [
    "project", "email", "name", "register_date", "GI_date", "GI_overall"] + list(gi_columns.keys()) + \
    ["LEAN_date"] + list(lean_columns.keys()) + ["ELITE_date"] + list(elite_columns.keys()) + \
    ["Astaka_date", "Astaka_Top 1_typology", "Astaka_Top 1_total_score", "Astaka_Top 2_typology", "Astaka_Top 2_total_score", 
    "Astaka_Top 3_typology", "Astaka_Top 3_total_score", "Astaka_Top 4_typology", "Astaka_Top 4_total_score", 
    "Astaka_Top 5_typology", "Astaka_Top 5_total_score", "Astaka_Top 6_typology", "Astaka_Top 6_total_score"] + \
    ["Genuine_date", "Genuine_Top 1_typology", "Genuine_Top 1_total_score", "Genuine_Top 2_typology", "Genuine_Top 2_total_score", 
    "Genuine_Top 3_typology", "Genuine_Top 3_total_score", "Genuine_Top 4_typology", "Genuine_Top 4_total_score", 
    "Genuine_Top 5_typology", "Genuine_Top 5_total_score", "Genuine_Top 6_typology", "Genuine_Top 6_total_score", 
    "Genuine_Top 7_typology", "Genuine_Top 7_total_score", "Genuine_Top 8_typology", "Genuine_Top 8_total_score", 
    "Genuine_Top 9_typology", "Genuine_Top 9_total_score"
]

# --- Filter by Project (Text Input) ---
project_query = st.text_input("📁 Search by Project", "")

df_b2b['email'] = df_b2b['email'].str.lower().str.strip()
df_merged['email'] = df_merged['email'].str.lower().str.strip()
df_b2b['project'] = df_b2b['project'].str.lower().str.strip()
df_merged['project'] = df_merged['project'].str.lower().str.strip()

if project_query:
    df_b2b_project = df_b2b[df_b2b["project"].str.contains(project_query, case=False, na=False)]

    df_merged_subset = df_merged[['email', 'project']].drop_duplicates()

    done_participants = pd.merge(
        df_b2b_project, 
        df_merged_subset, 
        on=['email', 'project'], 
        how='inner'
    )

    not_done_participants = pd.merge(
        df_b2b_project, 
        df_merged_subset, 
        on=['email', 'project'], 
        how='left', 
        indicator=True
    ).query('_merge == "left_only"').drop(columns=['_merge'])

    total_count = len(df_b2b_project)
    done_count = len(done_participants)
    not_done_count = len(not_done_participants)

    # Display metrics column
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Participant", total_count)
    col2.metric("Done", done_count)
    col3.metric("Not Done", not_done_count)

# --- Display done participants ---
if project_query:
    df_merged = df_merged[
        df_merged["project"].fillna("").str.contains(project_query, case=False, na=False)
    ]
    
    # --- Drop columns with all NaN values after selecting columns ---
    df_merged_cleaned = df_merged[selected_columns].dropna(axis=1, how='all')

    # Display the table only if search input is provided
    st.write(f"Showing {len(df_merged_cleaned)} results")

    # Create a buffer to hold the Excel file
    excel_buffer = io.BytesIO()

    # Prepare the Excel export
    def extract_hyperlink(text):
        if isinstance(text, str) and text.startswith('<a href="'):
            start = text.find('href="') + 6
            end = text.find('"', start)
            url = text[start:end]
            
            start_text = text.find('>') + 1
            end_text = text.rfind('</a>')
            display_text = text[start_text:end_text]
            
            return url, display_text
        return None, None

    # Prepare the Excel export
    with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
        df_for_excel = df_merged_cleaned.copy()  # Create a copy of the cleaned DataFrame
        df_for_excel.to_excel(writer, index=False, sheet_name='Test Results')  # Write the DataFrame to Excel
        
        # Access the xlsxwriter workbook and worksheet
        workbook = writer.book
        worksheet = writer.sheets['Test Results']
        
        # Loop through each column and set hyperlinks
        for col_num, column in enumerate(df_for_excel.columns):
            for row_num, value in enumerate(df_for_excel[column]):
                url, display_text = extract_hyperlink(value)
                if url:
                    # Set the hyperlink in the cell if it contains a valid URL
                    worksheet.write_url(row_num + 1, col_num, url, string=display_text)
                    
    # Set the file pointer to the beginning of the buffer
    excel_buffer.seek(0)

    # Offer the file as a download link
    st.download_button(
        label="Download Test Results as Excel",
        data=excel_buffer,
        file_name="test_results.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    st.write(df_merged_cleaned.to_html(escape=False, index=False), unsafe_allow_html=True)
else: 
    st.write("❗ Enter a search query to see results.")

# --- Display not done participants ---
if project_query:
    with st.expander("⏳ Participants Who Have Not Completed the Test"):
        st.write(
            not_done_participants[['project', 'email', 'name']].to_html(index=False, escape=False),
            unsafe_allow_html=True
        )
