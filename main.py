import streamlit as st
from streamlit_option_menu import option_menu
import yfinance as yf

st.set_page_config(page_title="Tech Stock Analysis",page_icon="📈")
st.markdown(
    """
        <style>
    [data-testid="stSidebarNavLink"]{
        visibility: hidden;
    }
         .reportview-container {
            margin-top: -2em;
        }

        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
        footer {visibility: hidden;}
    [data-testid="collapsedControl"] {
        display: none
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    choose = option_menu("HOME", ["About", "Apple", "Nvidia", "Microsoft","Amazon" ,"Alphabet","Meta Platforms","Tesla","Intel","Oracle",
"SAP","Netflix","AMD","Salesforce","Zoom","Adobe"],icons=['info-circle',"arrow-right","arrow-right","arrow-right","arrow-right","arrow-right","arrow-right","arrow-right","arrow-right","arrow-right","arrow-right","arrow-right","arrow-right","arrow-right","arrow-right","arrow-right"], menu_icon="house", default_index=0,
styles={
        # "container": {"padding": "5!important", "background-color": "#fafafa"},
        # "icon": {"color": "red", "font-size": "25px"},
        # "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        # "nav-link-selected": {"background-color": "#02ab21"},
    })



def About():
    st.title("Tech Stock Analysis")

def Apple():
    st.title("Apple Stock")
    ticker = "AAPL"
    stock = yf.Ticker(ticker)
    info = stock.info
    st.markdown(
    """
        <style>
	      @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap');
	      @import url('https://fonts.googleapis.com/css2?family=Meow+Script&display=swap');
              .st-emotion-cache-13k62yr {
                    background-color: black;
               }
	      .st-emotion-cache-ropwps h1{
		     color: black;
    		     font-family: "Merriweather", serif;
    		     font-weight: 700;
    		     background: white;
    		     width: 50%;
       		     border-radius: 10px;
		     border: 2px solid white;
                     text-align: center;
                     position: relative;
                     top: 50px;
                     left: 10%;
		     text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
                     box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);  
		 
		}
	</style>

    """,unsafe_allow_html=True)
    container = st.container(border=True, height = 300)
    container.write("  ")
    st.markdown(
    """
        <style>
              .st-emotion-cache-c79bx6 {
    			border: 2px solid white;
    			padding: calc(-1px + 1rem);
    			height: 350px;
    			overflow: auto;
    			background-color: grey;
			width: auto;
			}

		.st-emotion-cache-1cvow4s p {
   			color: black;
    			font-size: 1.0em;
			font-weight: 700;
			}

		.st-emotion-cache-7czcpc > img {
   			 border-radius: 0.5rem;
			// border: 4px solid white;
    			 position: relative;
    			 left: 7%;
			}
	</style>

    """,unsafe_allow_html=True)
    container.write(" ")
    col1, col2 = container.columns(2)
    with col1:
        image_url = "https://companiesmarketcap.com/img/company-logos/256/AAPL.webp"
        st.write(" ")
        st.image(image_url, width=260)
        st.write(" ")
    with col2:
        st.write(f"company_name : {info.get("displayName")}")
        st.write(f"rank :    #1")
        st.write(f"Total Market Cap :      {info.get('marketCap')/ 1e9:.2f} B")
        st.write(f"Company Location :      {info.get('country')}")
        st.write(f"Latest Price:           {info.get('currentPrice'):.2f}")
        st.write(f"Change in One Day:      {info.get('regularMarketChangePercent'):.2f}%")
        st.write(f"Change in One Year:     {info.get('52WeekChange'):.2f}%")





def Nvidia():
    st.title("Nvidia Stock")
    ticker = "NVDA"
    stock = yf.Ticker(ticker)
    info = stock.info
    st.markdown(
    """
        <style>
	      @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap');
	      @import url('https://fonts.googleapis.com/css2?family=Meow+Script&display=swap');
              .st-emotion-cache-13k62yr {
                    background-color: green;
               }
	      .st-emotion-cache-ropwps h1{
		     color: green;
    		     font-family: "Merriweather", serif;
    		     font-weight: 700;
    		     background: white;
    		     width: 50%;
       		     border-radius: 10px;
		     border: 2px solid black;
                     text-align: center;
                     position: relative;
                     top: 50px;
                     left: 10%;
		     text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
                     box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
		}

	</style>

    """,unsafe_allow_html=True)
    container = st.container(border=True, height = 300)
    container.write("  ")
    st.markdown(
    """
        <style>
              .st-emotion-cache-c79bx6 {
    			border: 2px solid black;
    			padding: calc(-1px + 1rem);
    			height: 350px;
    			overflow: auto;
    			background-color: white;
			width: auto;
			}

		.st-emotion-cache-1cvow4s p {
   			color: black;
    			font-size: 1.0em;
			font-weight: 700;
			}

		.st-emotion-cache-7czcpc > img {
   			 border-radius: 0.5rem;
			// border: 4px solid white;
    			 position: relative;
    			 left: 7%;
			}
	</style>

    """,unsafe_allow_html=True)
    container.write(" ")
    col1, col2 = container.columns(2)
    with col1:
        image_url = "https://companiesmarketcap.com/img/company-logos/256/NVDA.webp"
        st.image(image_url, width=250)
        st.write(" ")
    with col2:
        st.write(f"company_name : {info.get("displayName")}")
        st.write(f"rank :    #2")
        st.write(f"Total Market Cap :      {info.get('marketCap')/ 1e9:.2f} B")
        st.write(f"Company Location :      {info.get('country')}")
        st.write(f"Latest Price:           {info.get('currentPrice'):.2f}")
        st.write(f"Change in One Day:      {info.get('regularMarketChangePercent'):.2f}%")
        st.write(f"Change in One Year:     {info.get('52WeekChange'):.2f}%")


def Microsoft():
    st.title("Microsoft Stock")
    ticker = "MSFT"
    stock = yf.Ticker(ticker)
    info = stock.info
    st.markdown(
    """
        <style>
	      @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap');
	      @import url('https://fonts.googleapis.com/css2?family=Meow+Script&display=swap');
              .st-emotion-cache-13k62yr {
                    background-color: aqua;
               }
	      .st-emotion-cache-ropwps h1{
		     color: black;
    		     font-family: "Merriweather", serif;
    		     font-weight: 700;
    		     background: white;
    		     width: 70%;
       		     border-radius: 10px;
		     border: 2px solid white;
                     text-align: center;
                     position: relative;
                     top: 50px;
                     left: 10%;
		     text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
                     box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);  
		 
		}

	</style>

    """,unsafe_allow_html=True)
    container = st.container(border=True, height = 300)
    container.write("  ")
    st.markdown(
    """
        <style>
              .st-emotion-cache-c79bx6 {
    			border: 2px solid white;
    			padding: calc(-1px + 1rem);
    			height: 350px;
    			overflow: auto;
    			background-color: black;
			width: auto;
			}

		.st-emotion-cache-1cvow4s p {
   			color: white;
    			font-size: 1.0em;
			font-weight: 700;
			}
		.st-emotion-cache-7czcpc > img {
   			 border-radius: 0.5rem;
			// border: 4px solid white;
    			 position: relative;
    			 left: 7%;
			}
	</style>

    """,unsafe_allow_html=True)
    container.write(" ")
    col1, col2 = container.columns(2)
    with col1:
        image_url = "https://companiesmarketcap.com/img/company-logos/256/MSFT.webp"
        st.image(image_url, width=250)
        st.write(" ")
    with col2:
        st.write(f"company_name : {info.get("displayName")}")
        st.write(f"rank :    #3")
        st.write(f"Total Market Cap :      {info.get('marketCap')/ 1e9:.2f} B")
        st.write(f"Company Location :      {info.get('country')}")
        st.write(f"Latest Price:           {info.get('currentPrice'):.2f}")
        st.write(f"Change in One Day:      {info.get('regularMarketChangePercent'):.2f}%")
        st.write(f"Change in One Year:     {info.get('52WeekChange'):.2f}%")


def Amazon():
    st.title("Amazon Stock")
    ticker = "AMZN"
    stock = yf.Ticker(ticker)
    info = stock.info
    st.markdown(
    """
        <style>
	      @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap');
	      @import url('https://fonts.googleapis.com/css2?family=Meow+Script&display=swap');
              .st-emotion-cache-13k62yr {
                    background-color: #FD9A24;
               }
	      .st-emotion-cache-ropwps h1{
		     color:  black;
    		     font-family: "Merriweather", serif;
    		     font-weight: 700;
    		     background: white;
    		     width: 60%;
       		     border-radius: 10px;
		     border: 2px solid white;
                     text-align: center;
                     position: relative;
                     top: 50px;
                     left: 10%;
		     text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
                     box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
		}

	</style>

    """,unsafe_allow_html=True)
    container = st.container(border=True, height = 300)
    container.write("  ")
    st.markdown(
    """
        <style>
              .st-emotion-cache-c79bx6 {
    			border: 2px solid white;
    			padding: calc(-1px + 1rem);
    			height: 350px;
    			overflow: auto;
    			background-color: grey;
			width: auto;
			}

		.st-emotion-cache-1cvow4s p {
   			color: black;
    			font-size: 1.0em;
			font-weight: 700;
			}
		.st-emotion-cache-7czcpc > img {
   			 border-radius: 0.5rem;
			// border: 4px solid white;
    			 position: relative;
    			 left: 7%;
			}
	</style>

    """,unsafe_allow_html=True)
    container.write(" ")
    col1, col2 = container.columns(2)
    with col1:
        image_url = "https://companiesmarketcap.com/img/company-logos/256/AMZN.webp"
        st.image(image_url, width=250)
        st.write(" ")
    with col2:
        st.write(f"company_name : {info.get("displayName")}")
        st.write(f"rank :    #4")
        st.write(f"Total Market Cap :      {info.get('marketCap')/ 1e9:.2f} B")
        st.write(f"Company Location :      {info.get('country')}")
        st.write(f"Latest Price:           {info.get('currentPrice'):.2f}")
        st.write(f"Change in One Day:      {info.get('regularMarketChangePercent'):.2f}%")
        st.write(f"Change in One Year:     {info.get('52WeekChange'):.2f}%")

def Alphabet():
    st.title("Alphabet Stock")
    ticker = "GOOG"
    stock = yf.Ticker(ticker)
    info = stock.info
    st.markdown(
    """
        <style>
	      @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap');
	      @import url('https://fonts.googleapis.com/css2?family=Meow+Script&display=swap');
              .st-emotion-cache-13k62yr {
                    background-color:  #4285F4;
               }
	      .st-emotion-cache-ropwps h1{
		     color:  black;
    		     font-family: "Merriweather", serif;
    		     font-weight: 700;
    		     background: white;
    		     width: 60%;
       		     border-radius: 10px;
		     border: 2px solid white;
                     text-align: center;
                     position: relative;
                     top: 50px;
                     left: 10%;
		     text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
                     box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
		}

	</style>

    """,unsafe_allow_html=True)
    container = st.container(border=True, height = 300)
    container.write("  ")
    st.markdown(
    """
        <style>
              .st-emotion-cache-c79bx6 {
    			border: 2px solid white;
    			padding: calc(-1px + 1rem);
    			height: 350px;
    			overflow: auto;
    			background-color: grey;
			width: auto;
			}

		.st-emotion-cache-1cvow4s p {
   			color: black;
    			font-size: 1.0em;
			font-weight: 700;
			}

		.st-emotion-cache-7czcpc > img {
   			 border-radius: 0.5rem;
			// border: 4px solid white;
    			 position: relative;
    			 left: 12%;
			}

	</style>

    """,unsafe_allow_html=True)
    container.write(" ")
    col1, col2 = container.columns(2)
    with col1:
        image_url = "https://companiesmarketcap.com/img/company-logos/256/GOOG.webp"
        st.image(image_url, width=250)
        st.write(" ")
    with col2:
        st.write(f"company_name : {info.get("displayName")}")
        st.write(f"rank :    #5")
        st.write(f"Total Market Cap :      {info.get('marketCap')/ 1e9:.2f} B")
        st.write(f"Company Location :      {info.get('country')}")
        st.write(f"Latest Price:           {info.get('currentPrice'):.2f}")
        st.write(f"Change in One Day:      {info.get('regularMarketChangePercent'):.2f}%")
        st.write(f"Change in One Year:     {info.get('52WeekChange'):.2f}%")


def Meta_Platforms():
    st.title("Meta Platforms Stock")
    ticker = "META"
    stock = yf.Ticker(ticker)
    info = stock.info
    st.markdown(
    """
        <style>
	      @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap');
	      @import url('https://fonts.googleapis.com/css2?family=Meow+Script&display=swap');
              .st-emotion-cache-13k62yr {
                    background-color:  #1877F2;
               }
	      .st-emotion-cache-ropwps h1{
		     color:  black;
    		     font-family: "Merriweather", serif;
    		     font-weight: 700;
    		     background: white;
    		     width: 85%;
       		     border-radius: 10px;
		     border: 2px solid black;
                     text-align: center;
                     position: relative;
                     top: 50px;
                     left: 6%;
		     text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
                     box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
		}

	</style>

    """,unsafe_allow_html=True)
    container = st.container(border=True, height = 300)
    container.write("  ")
    st.markdown(
    """
        <style>
              .st-emotion-cache-c79bx6 {
    			border: 2px solid black;
    			padding: calc(-1px + 1rem);
    			height: 350px;
    			overflow: auto;
    			background-color: grey;
			width: auto;
			}

		.st-emotion-cache-1cvow4s p {
   			color: black;
    			font-size: 1.0em;
			font-weight: 700;
			}

		.st-emotion-cache-7czcpc > img {
   			 border-radius: 0.5rem;
			// border: 4px solid white;
    			 position: relative;
    			 left: 14%;
			}

	</style>

    """,unsafe_allow_html=True)
    container.write(" ")
    col1, col2 = container.columns(2)
    with col1:
        image_url = "https://companiesmarketcap.com/img/company-logos/256/META.webp"
        st.image(image_url, width=250)
        st.write(" ")
    with col2:
        st.write(f"company_name : {info.get("displayName")}")
        st.write(f"rank :    #7")
        st.write(f"Total Market Cap :      {info.get('marketCap')/ 1e9:.2f} B")
        st.write(f"Company Location :      {info.get('country')}")
        st.write(f"Latest Price:           {info.get('currentPrice'):.2f}")
        st.write(f"Change in One Day:      {info.get('regularMarketChangePercent'):.2f}%")
        st.write(f"Change in One Year:     {info.get('52WeekChange'):.2f}%")


def Tesla():
    st.title("Tesla Stock")
    ticker = "TSLA"
    stock = yf.Ticker(ticker)
    info = stock.info
    st.markdown(
    """
        <style>
	      @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap');
	      @import url('https://fonts.googleapis.com/css2?family=Meow+Script&display=swap');
              .st-emotion-cache-13k62yr {
                    background-color:  #E82127;
               }
	     
	     .st-emotion-cache-ropwps h1{
		     color:  black;
    		     font-family: "Merriweather", serif;
    		     font-weight: 700;
    		     background: white;
    		     width: 55%;
       		     border-radius: 10px;
		     border: 2px solid black;
                     text-align: center;
                     position: relative;
                     top: 50px;
                     left: 6%;
		     text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
                     box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
		}

	</style>

    """,unsafe_allow_html=True)
    container = st.container(border=True, height = 300)
    container.write("  ")
    st.markdown(
    """
        <style>
              .st-emotion-cache-c79bx6 {
    			border: 2px solid black;
    			padding: calc(-1px + 1rem);
    			height: 350px;
    			overflow: auto;
    			background-color: grey;
			width: auto;
			}

		.st-emotion-cache-1cvow4s p {
   			color: black;
    			font-size: 1.0em;
			font-weight: 700;
			}

		.st-emotion-cache-7czcpc > img {
   			 border-radius: 0.5rem;
			// border: 4px solid white;
    			 position: relative;
    			 left: 14%;
			}
	</style>

    """,unsafe_allow_html=True)
    container.write(" ")
    col1, col2 = container.columns(2)
    with col1:
        image_url = "https://companiesmarketcap.com/img/company-logos/256/TSLA.webp"
        st.write(" ")
        st.image(image_url, width=250)
        st.write(" ")
    with col2:
        st.write(f"company_name : {info.get("displayName")}")
        st.write(f"rank :    #11")
        st.write(f"Total Market Cap :      {info.get('marketCap')/ 1e9:.2f} B")
        st.write(f"Company Location :      {info.get('country')}")
        st.write(f"Latest Price:           {info.get('currentPrice'):.2f}")
        st.write(f"Change in One Day:      {info.get('regularMarketChangePercent'):.2f}%")
        st.write(f"Change in One Year:     {info.get('52WeekChange'):.2f}%")


def Intel():
    st.title("Intel Stock")
    ticker = "INTC"
    stock = yf.Ticker(ticker)
    info = stock.info
    st.markdown(
    """
        <style>
	      @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap');
	      @import url('https://fonts.googleapis.com/css2?family=Meow+Script&display=swap');
              .st-emotion-cache-13k62yr {
                    background-color: #0071C5;
               }
	      .st-emotion-cache-ropwps h1{
		     color:  black;
    		     font-family: "Merriweather", serif;
    		     font-weight: 700;
    		     background: white;
    		     width: 55%;
       		     border-radius: 10px;
		     border: 2px solid white;
                     text-align: center;
                     position: relative;
                     top: 50px;
                     left: 6%;
		     text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
                     box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
		}


	</style>

    """,unsafe_allow_html=True)
    container = st.container(border=True, height = 300)
    container.write("  ")
    st.markdown(
    """
        <style>
              .st-emotion-cache-c79bx6 {
    			border: 2px solid white;
    			padding: calc(-1px + 1rem);
    			height: 350px;
    			overflow: auto;
    			background-color: grey;
			width: auto;
			}

		.st-emotion-cache-1cvow4s p {
   			color: black;
    			font-size: 1.0em;
			font-weight: 700;
			}

		.st-emotion-cache-7czcpc > img {
   			 border-radius: 0.5rem;
			// border: 4px solid white;
    			 position: relative;
    			 left: 14%;
			}

	</style>

    """,unsafe_allow_html=True)
    container.write(" ")
    col1, col2 = container.columns(2)
    with col1:
        image_url = "https://companiesmarketcap.com/img/company-logos/256/INTC.webp"
        st.image(image_url, width=250)
        st.write(" ")
    with col2:
        st.write(f"company_name : {info.get("displayName")}")
        st.write(f"rank :    #170")
        st.write(f"Total Market Cap :      {info.get('marketCap')/ 1e9:.2f} B")
        st.write(f"Company Location :      {info.get('country')}")
        st.write(f"Latest Price:           {info.get('currentPrice'):.2f}")
        st.write(f"Change in One Day:      {info.get('regularMarketChangePercent'):.2f}%")
        st.write(f"Change in One Year:     {info.get('52WeekChange'):.2f}%")


def Oracle():
    st.title("Oracle Stock")
    ticker = "ORCL"
    stock = yf.Ticker(ticker)
    info = stock.info
    st.markdown(
    """
        <style>
	      @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap');
	      @import url('https://fonts.googleapis.com/css2?family=Meow+Script&display=swap');
              .st-emotion-cache-13k62yr {
                    background-color:#F80000;
               }
	      .st-emotion-cache-ropwps h1{
		     color:  black;
    		     font-family: "Merriweather", serif;
    		     font-weight: 700;
    		     background: white;
    		     width: 55%;
       		     border-radius: 10px;
		     border: 2px solid black;
                     text-align: center;
                     position: relative;
                     top: 50px;
                     left: 6%;
		     text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
                     box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
		}

	</style>

    """,unsafe_allow_html=True)
    container = st.container(border=True, height = 300)
    container.write("  ")
    st.markdown(
    """
        <style>
              .st-emotion-cache-c79bx6 {
    			border: 2px solid black;
    			padding: calc(-1px + 1rem);
    			height: 350px;
    			overflow: auto;
    			background-color: grey;
			width: auto;
			}

		.st-emotion-cache-1cvow4s p {
   			color: black;
    			font-size: 1.0em;
			font-weight: 700;
			}

		.st-emotion-cache-7czcpc > img {
   			 border-radius: 0.5rem;
			// border: 4px solid white;
    			 position: relative;
    			 left: 10%;
			}

	</style>

    """,unsafe_allow_html=True)
    container.write(" ")
    col1, col2 = container.columns(2)
    with col1:
        image_url = "https://companiesmarketcap.com/img/company-logos/256/ORCL.webp"
        st.image(image_url, width=250)
        st.write(" ")
    with col2:
        st.write(f"company_name : {info.get("displayName")}")
        st.write(f"rank :    #18")
        st.write(f"Total Market Cap :      {info.get('marketCap')/ 1e9:.2f} B")
        st.write(f"Company Location :      {info.get('country')}")
        st.write(f"Latest Price:           {info.get('currentPrice'):.2f}")
        st.write(f"Change in One Day:      {info.get('regularMarketChangePercent'):.2f}%")
        st.write(f"Change in One Year:     {info.get('52WeekChange'):.2f}%")

def SAP():
    st.title("SAP Stock")
    ticker = "SAP"
    stock = yf.Ticker(ticker)
    info = stock.info
    st.markdown(
    """
        <style>
	      @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap');
	      @import url('https://fonts.googleapis.com/css2?family=Meow+Script&display=swap');
              .st-emotion-cache-13k62yr {
                    background-color:#0A4C8C;
               }
	      .st-emotion-cache-ropwps h1{
		     color:  black;
    		     font-family: "Merriweather", serif;
    		     font-weight: 700;
    		     background: white;
    		     width: 55%;
       		     border-radius: 10px;
		     border: 2px solid white;
                     text-align: center;
                     position: relative;
                     top: 50px;
                     left: 6%;
		     text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
                     box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
		}

	</style>

    """,unsafe_allow_html=True)
    container = st.container(border=True, height = 300)
    container.write("  ")
    st.markdown(
    """
        <style>
              .st-emotion-cache-c79bx6 {
    			border: 2px solid white;
    			padding: calc(-1px + 1rem);
    			height: 350px;
    			overflow: auto;
    			background-color: grey;
			width: auto;
			}

		.st-emotion-cache-1cvow4s p {
   			color: black;
    			font-size: 1.0em;
			font-weight: 700;
			}

		.st-emotion-cache-7czcpc > img {
   			 border-radius: 0.5rem;
			// border: 4px solid white;
    			 position: relative;
    			 left: 14%;
			}
	</style>

    """,unsafe_allow_html=True)
    container.write(" ")
    col1, col2 = container.columns(2)
    with col1:
        image_url = "https://companiesmarketcap.com/img/company-logos/256/SAP.webp"
        st.image(image_url, width=250)
        st.write(" ")
    with col2:
        st.write(f"company_name : {info.get("displayName")}")
        st.write(f"rank :    #30")
        st.write(f"Total Market Cap :      {info.get('marketCap')/ 1e9:.2f} B")
        st.write(f"Company Location :      {info.get('country')}")
        st.write(f"Latest Price:           {info.get('currentPrice'):.2f}")
        st.write(f"Change in One Day:      {info.get('regularMarketChangePercent'):.2f}%")
        st.write(f"Change in One Year:     {info.get('52WeekChange'):.2f}%")


def Netflix():
    st.title("Netflix Stock")
    ticker = "NFLX"
    stock = yf.Ticker(ticker)
    info = stock.info
    st.markdown(
    """
        <style>
	      @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap');
	      @import url('https://fonts.googleapis.com/css2?family=Meow+Script&display=swap');
              .st-emotion-cache-13k62yr {
                    background-color:#E50914;
               }
	      .st-emotion-cache-ropwps h1{
		     color:  black;
    		     font-family: "Merriweather", serif;
    		     font-weight: 700;
    		     background: white;
    		     width: 55%;
       		     border-radius: 10px;
		     border: 2px solid black;
                     text-align: center;
                     position: relative;
                     top: 50px;
                     left: 6%;
		     text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
                     box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
		}

	</style>

    """,unsafe_allow_html=True)
    container = st.container(border=True, height = 300)
    container.write("  ")
    st.markdown(
    """
        <style>
              .st-emotion-cache-c79bx6 {
    			border: 2px solid black;
    			padding: calc(-1px + 1rem);
    			height: 350px;
    			overflow: auto;
    			background-color: grey;
			width: auto;
			}

		.st-emotion-cache-1cvow4s p {
   			color: black;
    			font-size: 1.0em;
			font-weight: 700;
			}

		.st-emotion-cache-7czcpc > img {
   			 border-radius: 0.5rem;
			// border: 4px solid white;
    			 position: relative;
    			 left: 14%;
			}
	</style>

    """,unsafe_allow_html=True)
    container.write(" ")
    col1, col2 = container.columns(2)
    with col1:
        image_url = "https://companiesmarketcap.com/img/company-logos/256/NFLX.webp"
        st.image(image_url, width=250)
        st.write(" ")
    with col2:
        st.write(f"company_name : {info.get("displayName")}")
        st.write(f"rank :    #22")
        st.write(f"Total Market Cap :      {info.get('marketCap')/ 1e9:.2f} B")
        st.write(f"Company Location :      {info.get('country')}")
        st.write(f"Latest Price:           {info.get('currentPrice'):.2f}")
        st.write(f"Change in One Day:      {info.get('regularMarketChangePercent'):.2f}%")
        st.write(f"Change in One Year:     {info.get('52WeekChange'):.2f}%")


def AMD():
    st.title("AMD Stock")
    ticker = "AMD"
    stock = yf.Ticker(ticker)
    info = stock.info
    st.markdown(
    """
        <style>
	      @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap');
	      @import url('https://fonts.googleapis.com/css2?family=Meow+Script&display=swap');
              .st-emotion-cache-13k62yr {
                    background-color: black;
               }
	     .st-emotion-cache-ropwps h1{
		     color:  black;
    		     font-family: "Merriweather", serif;
    		     font-weight: 700;
    		     background: white;
    		     width: 55%;
       		     border-radius: 10px;
		     border: 2px solid white;
                     text-align: center;
                     position: relative;
                     top: 50px;
                     left: 6%;
		     text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
                     box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
		}

	</style>

    """,unsafe_allow_html=True)
    container = st.container(border=True, height = 300)
    container.write("  ")
    st.markdown(
    """
        <style>
              .st-emotion-cache-c79bx6 {
    			border: 2px solid white;
    			padding: calc(-1px + 1rem);
    			height: 350px;
    			overflow: auto;
    			background-color: grey;
			width: auto;
			}

		.st-emotion-cache-1cvow4s p {
   			color: black;
    			font-size: 1.0em;
			font-weight: 700;
			}

		.st-emotion-cache-7czcpc > img {
   			 border-radius: 0.5rem;
			// border: 4px solid white;
    			 position: relative;
    			 left: 9%;
			}
	</style>

    """,unsafe_allow_html=True)
    container.write(" ")
    col1, col2 = container.columns(2)
    with col1:
        image_url = "https://companiesmarketcap.com/img/company-logos/256/AMD.webp"
        st.image(image_url, width=250)
        st.write(" ")
    with col2:
        st.write(f"company_name : {info.get("displayName")}")
        st.write(f"rank :    #86")
        st.write(f"Total Market Cap :      {info.get('marketCap')/ 1e9:.2f} B")
        st.write(f"Company Location :      {info.get('country')}")
        st.write(f"Latest Price:           {info.get('currentPrice'):.2f}")
        st.write(f"Change in One Day:      {info.get('regularMarketChangePercent'):.2f}%")
        st.write(f"Change in One Year:     {info.get('52WeekChange'):.2f}%")


def Salesforce():
    st.title("Salesforce Stock")
    ticker = "CRM"
    stock = yf.Ticker(ticker)
    info = stock.info
    st.markdown(
    """
        <style>
	      @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap');
	      @import url('https://fonts.googleapis.com/css2?family=Meow+Script&display=swap');
              .st-emotion-cache-13k62yr {
                    background-color: #00A1E0;
               }
	      .st-emotion-cache-ropwps h1{
		     color:  black;
    		     font-family: "Merriweather", serif;
    		     font-weight: 700;
    		     background: white;
    		     width: 65%;
       		     border-radius: 10px;
		     border: 2px solid black;
                     text-align: center;
                     position: relative;
                     top: 50px;
                     left: 7%;
		     text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
                     box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
		}

	</style>

    """,unsafe_allow_html=True)
    container = st.container(border=True, height = 300)
    container.write("  ")
    st.markdown(
    """
        <style>
              .st-emotion-cache-c79bx6 {
    			border: 2px solid black;
    			padding: calc(-1px + 1rem);
    			height: 350px;
    			overflow: auto;
    			background-color: grey;
			width: auto;
			}

		.st-emotion-cache-1cvow4s p {
   			color: black;
    			font-size: 1.0em;
			font-weight: 700;
			}

		.st-emotion-cache-7czcpc > img {
   			 border-radius: 0.5rem;
			// border: 4px solid white;
    			 position: relative;
    			 left: 14%;
			}
	</style>

    """,unsafe_allow_html=True)
    container.write(" ")
    col1, col2 = container.columns(2)
    with col1:
        image_url = "https://companiesmarketcap.com/img/company-logos/256/CRM.webp"
        st.image(image_url, width=250)
        st.write(" ")
    with col2:
        st.write(f"company_name : {info.get("displayName")}")
        st.write(f"rank :    #37")
        st.write(f"Total Market Cap :      {info.get('marketCap')/ 1e9:.2f} B")
        st.write(f"Company Location :      {info.get('country')}")
        st.write(f"Latest Price:           {info.get('currentPrice'):.2f}")
        st.write(f"Change in One Day:      {info.get('regularMarketChangePercent'):.2f}%")
        st.write(f"Change in One Year:     {info.get('52WeekChange'):.2f}%")


def Zoom():
    st.title("Zoom Stock")
    ticker = "ZM"
    stock = yf.Ticker(ticker)
    info = stock.info
    st.markdown(
    """
        <style>
	      @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap');
	      @import url('https://fonts.googleapis.com/css2?family=Meow+Script&display=swap');
              .st-emotion-cache-13k62yr {
                    background-color:#0078D4;
               }
	     .st-emotion-cache-ropwps h1{
		     color:  black;
    		     font-family: "Merriweather", serif;
    		     font-weight: 700;
    		     background: white;
    		     width: 55%;
       		     border-radius: 10px;
		     border: 2px solid white;
                     text-align: center;
                     position: relative;
                     top: 50px;
                     left: 6%;
		     text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
                     box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
		}

	</style>

    """,unsafe_allow_html=True)
    container = st.container(border=True, height = 300)
    container.write("  ")
    st.markdown(
    """
        <style>
              .st-emotion-cache-c79bx6 {
    			border: 2px solid white;
    			padding: calc(-1px + 1rem);
    			height: 350px;
    			overflow: auto;
    			background-color: grey;
			width: auto;
			}

		.st-emotion-cache-1cvow4s p {
   			color: black;
    			font-size: 1.0em;
			font-weight: 700;
			}

		.st-emotion-cache-7czcpc > img {
   			 border-radius: 0.5rem;
			// border: 4px solid white;
    			 position: relative;
    			 left: 7%;
			}
	</style>

    """,unsafe_allow_html=True)
    container.write(" ")
    col1, col2 = container.columns(2)
    with col1:
        image_url = "https://companiesmarketcap.com/img/company-logos/256/ZM.webp"
        st.image(image_url, width=250)
        st.write(" ")
    with col2:
        st.write(f"company_name : {info.get("displayName")}")
        st.write(f"rank :    #883")
        st.write(f"Total Market Cap :      {info.get('marketCap')/ 1e9:.2f} B")
        st.write(f"Company Location :      {info.get('country')}")
        st.write(f"Latest Price:           {info.get('currentPrice'):.2f}")
        st.write(f"Change in One Day:      {info.get('regularMarketChangePercent'):.2f}%")
        st.write(f"Change in One Year:     {info.get('52WeekChange'):.2f}%")


def Adobe():
    st.title("Adobe Stock")
    ticker = "ADBE"
    stock = yf.Ticker(ticker)
    info = stock.info
    st.markdown(
    """
        <style>
	      @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap');
	      @import url('https://fonts.googleapis.com/css2?family=Meow+Script&display=swap');
              .st-emotion-cache-13k62yr {
                    background-color: #FF0000;
               }
	      .st-emotion-cache-ropwps h1{
		     color:  black;
    		     font-family: "Merriweather", serif;
    		     font-weight: 700;
    		     background: white;
    		     width: 55%;
       		     border-radius: 10px;
		     border: 2px solid black;
                     text-align: center;
                     position: relative;
                     top: 50px;
                     left: 6%;
		     text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
                     box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
		}

	</style>

    """,unsafe_allow_html=True)
    container = st.container(border=True, height = 300)
    container.write("  ")
    st.markdown(
    """
        <style>
              .st-emotion-cache-c79bx6 {
    			border: 2px solid black;
    			padding: calc(-1px + 1rem);
    			height: 350px;
    			overflow: auto;
    			background-color: grey;
			width: auto;
			}

		.st-emotion-cache-1cvow4s p {
   			color: black;
    			font-size: 1.0em;
			font-weight: 700;
			}

		.st-emotion-cache-7czcpc > img {
   			 border-radius: 0.5rem;
			// border: 4px solid white;
    			 position: relative;
    			 left: 7%;
			}
	</style>

    """,unsafe_allow_html=True)
    container.write(" ")
    col1, col2 = container.columns(2)
    with col1:
        image_url = "https://companiesmarketcap.com/img/company-logos/256/ADBE.webp"
        st.image(image_url, width=250)
        st.write(" ")
    with col2:
        st.write(f"company_name : {info.get("displayName")}")
        st.write(f"rank :    #74")
        st.write(f"Total Market Cap :      {info.get('marketCap')/ 1e9:.2f} B")
        st.write(f"Company Location :      {info.get('country')}")
        st.write(f"Latest Price:           {info.get('currentPrice'):.2f}")
        st.write(f"Change in One Day:      {info.get('regularMarketChangePercent'):.2f}%")
        st.write(f"Change in One Year:     {info.get('52WeekChange'):.2f}%")


if choose == "About":
    About()
elif choose == "Apple":
    Apple()
elif choose == "Nvidia":
    Nvidia()
elif choose == "Microsoft":
    Microsoft()
elif choose == "Amazon":
    Amazon()
elif choose == "Alphabet":
    Alphabet()
elif choose == "Meta Platforms":
    Meta_Platforms()
elif choose == "Tesla":
    Tesla()
elif  choose == "Intel":
    Intel()
elif choose == "Oracle":
    Oracle()
elif choose == "SAP":
    SAP()
elif  choose == "Netflix":
    Netflix()
elif choose =="AMD":
    AMD()
elif choose == "Salesforce":
    Salesforce()
elif choose == "Zoom":
    Zoom()
elif choose == "Adobe":
    Adobe()

