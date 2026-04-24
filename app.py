import pandas as pd
import streamlit as st

 # --- Page Config ---
st.set_page_config(
    page_title="AAPL Stock Dashboard",
    page_icon="🍎",
    layout="wide"
)

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv('aapl_cleaned.csv', header=[0, 1], index_col=0)
    df.columns = df.columns.get_level_values(0)
    df.index = pd.to_datetime(df.index)
    df.index.name = 'Date'
    return df

df_apple = load_data()


st.title(f"AAPL Stock Dashboard")
st.caption("Apple Inc. · NASDAQ · USD · Daily Data")
st.divider()

with st.expander("📌 About this Dashboard"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Dataset Info")
        st.write("**Ticker:** AAPL (Apple Inc.)")
        st.write("**Exchange:** NASDAQ")
        st.write("**Currency:** USD")
        st.write("**Data Range:** 2016 - 2026")
        st.write("**Total Records:**", len(df_apple))
        st.write("**Frequency:** Daily")

    with col2:
        st.markdown("### 📋 Columns")
        st.write("**Open** — Opening price of the day")
        st.write("**High** — Highest price of the day")
        st.write("**Low** — Lowest price of the day")
        st.write("**Close** — Closing price of the day")
        st.write("**Volume** — Number of shares traded")

    st.divider()

    st.markdown("### 📅 Date Coverage")
    col3, col4, col5 = st.columns(3)
    col3.metric("First Date", str(df_apple.index.min().date()))
    col4.metric("Last Date", str(df_apple.index.max().date()))
    col5.metric("Trading Days", len(df_apple))

    st.divider()

    st.markdown("### 🛠️ Tools Used")
    st.write("- **Python** — Core programming language")
    st.write("- **Pandas** — Data loading and manipulation")
    st.write("- **Streamlit** — Dashboard framework")


    st.divider()
    st.caption("Data sourced from Yahoo Finance. For educational purposes only.")

year = st.number_input("🗓️ Select Year", min_value=2016, max_value=2026, value=2026, step=1)
result = df_apple[df_apple.index.year == year]

# --- Metrics ---
col1, col2, col3 = st.columns(3)
col1.metric("High", result['High'].max().round(2))
col2.metric("Low", result['Low'].min().round(2))
col3.metric("Highest-Close", result['Close'].max().round(2))

st.subheader("AAPL Summary")
if st.checkbox("Show Raw Data"):
    st.dataframe(result.query('Date >= @year'))



st.subheader(f"Apple Stock Key Metrics {year}")
tab1, tab2 = st.tabs(["📈 High Price", "📊 Volume"])
with tab1:
    st.line_chart(result, y=['High'], color=["#27AE60"])
with tab2:
    st.bar_chart(result['Volume'], color= ['#F39C12'])

st.caption("A line chart showing the AAPl High trend for a specific year") 

st.download_button(
    label="⬇️ Download AAPL Data",
    data=df_apple.to_csv().encode('utf-8'),
    file_name="aapl_cleaned.csv",
    mime="text/csv",
    use_container_width=True,
    type="secondary"
)
st.caption("📁 CSV format · All years · Daily frequency")



st.divider()
st.markdown("""
    <div style='text-align: center; padding: 10px;'>
        <p style='color: gray; font-size: 14px;'>Built with ❤️ by <strong>Milton Bedah</strong></p>
        <p>
            <a href='https://github.com/bedahmilton' target='_blank' style='color: #2E86C1; text-decoration: none; margin: 0 10px;'>🐙 GitHub</a>
            <a href='mailto:bedah.dev@gmail.com' style='color: #2E86C1; text-decoration: none; margin: 0 10px;'>📧 EMAIL</a>
        </p>
        <p style='color: gray; font-size: 12px;'>© 2026 All Rights Reserved</p>
    </div>
""", unsafe_allow_html=True)