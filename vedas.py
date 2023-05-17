import numpy as np
import pandas as pd
import datetime
import streamlit as st

st.set_page_config(page_title='Vedas Transcription', layout="wide", initial_sidebar_state="auto", menu_items=None)
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
#st.markdown(hide_menu_style, unsafe_allow_html=True)

def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

# KrutiDev to Unicode function
def kd2u(krutidev_substring):
    
    modified_substring = krutidev_substring
    
    array_one = ["ñ","Q+Z","sas","aa",")Z","ZZ","‘","’","“","”",
    
    "å",  "ƒ",  "„",   "…",   "†",   "‡",   "ˆ",   "‰",   "Š",   "‹", 
    
    "¶+",   "d+", "[+k","[+", "x+",  "T+",  "t+", "M+", "<+", "Q+", ";+", "j+", "u+",
    "Ùk", "Ù", "Dr", "–", "—","é","™","=kk","f=k",  
    
    "à",   "á",    "â",   "ã",   "ºz",  "º",   "í", "{k", "{", "=",  "«",   
    "Nî",   "Vî",    "Bî",   "Mî",   "<î", "|", "K", "}",
    "J",   "Vª",   "Mª",  "<ªª",  "Nª",   "Ø",  "Ý", "nzZ",  "æ", "ç", "Á", "xz", "#", ":",
    
    "v‚","vks",  "vkS",  "vk",    "v",  "b±", "Ã",  "bZ",  "b",  "m",  "Å",  ",s",  ",",   "_",
    
    "ô",  "d", "Dk", "D", "[k", "[", "x","Xk", "X", "Ä", "?k", "?",   "³", 
    "pkS",  "p", "Pk", "P",  "N",  "t", "Tk", "T",  ">", "÷", "¥",
    
    "ê",  "ë",   "V",  "B",   "ì",   "ï", "M+", "<+", "M",  "<", ".k", ".",    
    "r",  "Rk", "R",   "Fk", "F",  ")", "n", "/k", "èk",  "/", "Ë", "è", "u", "Uk", "U",   
    
    "i",  "Ik", "I",   "Q",    "¶",  "c", "Ck",  "C",  "Hk",  "H", "e", "Ek",  "E",
    ";",  "¸",   "j",    "y", "Yk",  "Y",  "G",  "o", "Ok", "O",
    "'k", "'",   "\"k",  "\"",  "l", "Lk",  "L",   "g", 
    
    "È", "z", 
    "Ì", "Í", "Î",  "Ï",  "Ñ",  "Ò",  "Ó",  "Ô",   "Ö",  "Ø",  "Ù","Ük", "Ü",
    
    "‚",    "ks",   "kS",   "k",  "h",    "q",   "w",   "`",    "s",    "S",
    "a",    "¡",    "%",     "W",  "•", "·", "∙", "·", "~j",  "~", "\\","+"," ः",
    "^", "*",  "Þ", "ß", "(", "¼", "½", "¿", "À", "¾", "A", "-", "&", "&", "Œ", "]","~ ","@"]
    
    array_two = ["॰","QZ+","sa","a","र्द्ध","Z","\"","\"","'","'",
    
    "०",  "१",  "२",  "३",     "४",   "५",  "६",   "७",   "८",   "९",   
    
    "फ़्",  "क़",  "ख़", "ख़्",  "ग़", "ज़्", "ज़",  "ड़",  "ढ़",   "फ़",  "य़",  "ऱ",  "ऩ",    
    "त्त", "त्त्", "क्त",  "दृ",  "कृ","न्न","न्न्","=k","f=",
    
    "ह्न",  "ह्य",  "हृ",  "ह्म",  "ह्र",  "ह्",   "द्द",  "क्ष", "क्ष्", "त्र", "त्र्", 
    "छ्य",  "ट्य",  "ठ्य",  "ड्य",  "ढ्य", "द्य", "ज्ञ", "द्व",
    "श्र",  "ट्र",    "ड्र",    "ढ्र",    "छ्र",   "क्र",  "फ्र", "र्द्र",  "द्र",   "प्र", "प्र",  "ग्र", "रु",  "रू",
    
    "ऑ",   "ओ",  "औ",  "आ",   "अ", "ईं", "ई",  "ई",   "इ",  "उ",   "ऊ",  "ऐ",  "ए", "ऋ",
    
    "क्क", "क", "क", "क्", "ख", "ख्", "ग", "ग", "ग्", "घ", "घ", "घ्", "ङ",
    "चै",  "च", "च", "च्", "छ", "ज", "ज", "ज्",  "झ",  "झ्", "ञ",
    
    "ट्ट",   "ट्ठ",   "ट",   "ठ",   "ड्ड",   "ड्ढ",  "ड़", "ढ़", "ड",   "ढ", "ण", "ण्",   
    "त", "त", "त्", "थ", "थ्",  "द्ध",  "द", "ध", "ध", "ध्", "ध्", "ध्", "न", "न", "न्",    
    
    "प", "प", "प्",  "फ", "फ्",  "ब", "ब", "ब्",  "भ", "भ्",  "म",  "म", "म्",  
    "य", "य्",  "र", "ल", "ल", "ल्",  "ळ",  "व", "व", "व्",   
    "श", "श्",  "ष", "ष्", "स", "स", "स्", "ह", 
    
    "ीं", "्र",    
    "द्द", "ट्ट","ट्ठ","ड्ड","कृ","भ","्य","ड्ढ","झ्","क्र","त्त्","श","श्",
    
    "ॉ",  "ो",   "ौ",   "ा",   "ी",   "ु",   "ू",   "ृ",   "े",   "ै",
    "ं",   "ँ",   "ः",   "ॅ",  "ऽ", "ऽ", "ऽ", "ऽ", "्र",  "्", "?", "़",":",
    "‘",   "’",   "“",   "”",  ";",  "(",    ")",   "{",    "}",   "=", "।", ".", "-",  "µ", "॰", ",","् ","/"]
    
    array_one_length = len(array_one)
    
    # Specialty characters
    
    # Move "f"  to correct position and replace
    modified_substring = "  " + modified_substring + "  "
    position_of_f = modified_substring.rfind("f")
    while (position_of_f != -1):    
        modified_substring = modified_substring[:position_of_f] + modified_substring[position_of_f+1] + modified_substring[position_of_f] +  modified_substring[position_of_f+2:]
        position_of_f = modified_substring.rfind("f",0, position_of_f - 1 ) # search for f ahead of the current position.
    modified_substring = modified_substring.replace("f","ि")
    modified_substring = modified_substring.strip()
    
    # Move "half R"  to correct position and replace
    modified_substring = "  " + modified_substring + "  "
    position_of_r = modified_substring.find("Z")
    set_of_matras =  ["‚",    "ks",   "kS",   "k",     "h",    "q",   "w",   "`",    "s",    "S", "a",    "¡",    "%",     "W",   "·",   "~ ", "~"]
    while (position_of_r != -1):    
        modified_substring = modified_substring.replace("Z","",1)
        if modified_substring[position_of_r - 1] in set_of_matras:
            modified_substring = modified_substring[:position_of_r - 2] + "j~" + modified_substring[position_of_r - 2:]
        else:
            modified_substring = modified_substring[:position_of_r - 1] + "j~" + modified_substring[position_of_r - 1:]
        position_of_r = modified_substring.find("Z")
    modified_substring = modified_substring.strip()
    
    # Replace ASCII with Unicode
    for input_symbol_idx in range(0, array_one_length):
        modified_substring = modified_substring.replace(array_one[input_symbol_idx ] , array_two[input_symbol_idx] )
    
    
    return modified_substring


## reading in from public google sheet
SHEET_ID = '1pjbBPhh-v5Bo7UXeq0OOXP56XwtnzdkQnLy6GEOjdXE'
SHEET_NAME = 'responses'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)
df.columns = ['Timestamp','Text','Hierarchy','Verse','Meaning','Elucidation','Practical Utility']
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df = df.sort_values(by=['Timestamp','Text','Hierarchy'], ascending=[False,True,True])
dft = df.head(1)

st.markdown("<h1 style='text-align: center;'>Vedas Archive and Transcription</h1>", unsafe_allow_html=True)

st.markdown("## Today's Verse: {} {}".format(dft.Text.values[0], dft.Hierarchy.values[0]))
st.write(dft.Verse.values[0])
st.markdown("### Meaning")
st.write(dft.Meaning.values[0])
st.markdown("### Elucidation")
st.write(dft.Elucidation.values[0])
st.markdown("### Practical Utility in Life")
st.write(dft['Practical Utility'].values[0])


st.markdown('#### Search for Specific Verse or Keyword')
st.write('Search for text below and the verse, meaning, elucidation, and practical utility will be shown below.')
search = st.text_input(label='Press Enter to search', placeholder='Example: searching \'family\' will show relevant teachings')
if search != '':
    dfsidx = []
    for col in df:
        ## get indices of search for each column
        try:
            idx = df[df[col].str.contains(search, case=False)].index.tolist()
            dfsidx = dfsidx + idx
        except: pass
    
    dfs = df[df.index.isin(np.unique(dfsidx))].sort_index()

    for label, row in dfs.iterrows():
        with st.expander('{} {}'.format(row.Text, row.Hierarchy)):
            st.markdown("### Verse")
            st.write(row.Verse)
            st.markdown("### Meaning")
            st.write(row.Meaning)
            st.markdown("### Elucidation")
            st.write(row.Elucidation)
            st.markdown("### Practical Utility")
            st.write(row['Practical Utility'])

## show full df at bottom of page
st.markdown('#### All Verses')
st.dataframe(df[['Text','Hierarchy','Verse','Meaning','Elucidation','Practical Utility']])
## Button for downloading vedas data to CSV
vedas_csv = convert_df(df)
st.download_button("Download all verses in text format", vedas_csv, "vedas.csv", "text/csv", key='download-csv')