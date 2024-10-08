import streamlit as st
import show

if "key" not in st.session_state:
    st.session_state["key"] = "value"
if "select_cov" not in st.session_state:
    st.session_state["select_cov"] = None
if "select_er" not in st.session_state:
    st.session_state["select_er"] = None

st.set_page_config(
    page_title="Outperforming Indexes",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title(":chart: Outperforming the Indexes")
st.markdown(" Data from Yahoo Finance ")


with st.sidebar:

    st.title("Options")

    select_index = st.selectbox(
        "Choose Index",
        (
            "None",
            "S&P 500",
            "Nasdaq 100",
            "Dow Jones Industrial Average",
            "FTSE 100",
            "DAX PERFORMANCE-INDEX",
            "CAC 40",
            "Nikkei 225",
            "HANG SENG INDEX",
        ),
    )

    st.session_state.select_cov = (
        st.selectbox(
            "Select Covariance",
            ("Sample", "Constant Correlation", "Shinkage"),
            ["Sample", "CCM", "Shinkage"].index(st.session_state["select_cov"]),
        )
        if st.session_state.select_cov is not None
        else "Sample"
    )
    # st.session_state.user_choices["Select Covariance"] = select_cov
    st.session_state.select_er = (
        st.selectbox(
            "Select Expected Return",
            ("Average", "Exponentially Weighted Average"),
            ["Average", "EWA"].index(st.session_state["select_er"]),
        )
        if st.session_state.select_er is not None
        else "Average"
    )
    select_er = st.session_state.select_er
    select_cov = st.session_state.select_cov

match select_index:
    case "None":
        # TODO: Starting page
        st.write("Choose index you want to ouperform")

    case "S&P 500":
        index_name = "^GSPC"
        components_returns_url = 0

        st.write("S&P 500 historical data:")

        show.show_index_historical_data(index_name)
        show.show_stats(index_name)
        show.growth_plot(index_name)

    case "Nasdaq 100":
        index_name = "^IXIC"
        components_returns_url = 1

        st.write("Nasdaq Composite historical data:")

        show.show_index_historical_data(index_name)
        show.show_stats(index_name)
        show.growth_plot(index_name)

    case "Dow Jones Industrial Average":
        index_name = "^DJI"
        components_returns_url = 2

        st.write("Dow Jones Industrial Average historical data:")

        show.show_index_historical_data(index_name)
        show.show_stats(index_name)
        show.growth_plot(index_name)

    case "FTSE 100":
        index_name = "^FTSE"
        components_returns_url = 3

        st.write("FTSE 100 historical data:")

        show.show_index_historical_data(index_name)
        show.show_stats(index_name)
        show.growth_plot(index_name)

    case "DAX PERFORMANCE-INDEX":
        index_name = "^GDAXI"
        components_returns_url = 4
        st.write("DAX PERFORMANCE-INDEX historical data:")

        show.show_index_historical_data(index_name)
        show.show_stats(index_name)
        show.growth_plot(index_name)

    case "CAC 40":
        index_name = "^FCHI"
        components_returns_url = None
        st.write("CAC 40 historical data:")

        show.show_index_historical_data(index_name)
        show.show_stats(index_name)
        show.growth_plot(index_name)

    case "Nikkei 225":
        index_name = "^N225"
        components_returns_url = None
        st.write("Nikkei 225 historical data:")

        show.show_index_historical_data(index_name)
        show.show_stats(index_name)
        show.growth_plot(index_name)

    case "HANG SENG INDEX":
        index_name = "^HSI"
        components_returns_url = 5
        st.write("HANG SENG INDEX historical data:")

        show.show_index_historical_data(index_name)
        show.show_stats(index_name)
        show.growth_plot(index_name)


match select_cov:
    case "Sample":
        cov = "Sample"
    case "Constant Correlation":
        cov = "CCM"
    case "Shinkage":
        cov = "Shinkage"

match select_er:
    case "Average":
        er = "Average"
    case "Exponentially Weighted Average":
        er = "EWA"


st.session_state["select_cov"] = cov
st.session_state["select_er"] = er
