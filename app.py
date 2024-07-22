import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key
from bs4 import BeautifulSoup
import requests
import warnings
from streamlit_option_menu import option_menu
from streamlit_extras.mention import mention
warnings.filterwarnings("ignore")

genai.configure(api_key=google_gemini_api_key)
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 32768,
    "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

st.set_page_config(page_title="Lex Project by Algorex Technologies", page_icon="", layout="wide")

with st.sidebar :
    st.image('images/Logo.png')
    with st.container() :
        l, m, r = st.columns((1, 3, 1))
        with l : st.empty()
        with m : st.empty()
        with r : st.empty()

    options = option_menu(
        "Dashboard", 
        ["Home", "About Us", "Model"],
        icons = ['book', 'globe', 'tools'],
        menu_icon = "book", 
        default_index = 0,
        styles = {
            "icon" : {"color" : "#dec960", "font-size" : "20px"},
            "nav-link" : {"font-size" : "17px", "text-align" : "left", "margin" : "5px", "--hover-color" : "#262730"},
            "nav-link-selected" : {"background-color" : "#262730"}          
        })



# Options : Home
if options == "Home" :

   st.title('The Lex Project by Algorex Technologies')
   st.subheader("Overview")
   st.write("The Lex Project is an innovative AI application designed to revolutionize the digital landscape of law firm websites. Our mission is to help legal practices enhance their online presence by delivering in-depth UX and UI reviews, coupled with actionable recommendations for improvement.")
   st.write("## Key Features")
   st.write("### 1. Automated UX/UI Analysis :")
   st.write("The Lex Project utilizes advanced machine learning algorithms to automatically evaluate the user experience and interface of law firm websites. This includes assessing navigation, layout, visual appeal, and overall usability.")
   st.write("### 2. Actionable Insights :")
   st.write("Our AI-driven analysis provides clear, actionable insights that law firms can implement to improve their website's performance. This includes suggestions for design enhancements, content restructuring, and navigation improvements.")
   st.write("### 3. Performance Metrics :")
   st.write("The Lex Project offers detailed performance metrics, including page load times, mobile responsiveness, and user engagement statistics. These metrics help law firms understand their website's strengths and areas for improvement.")
   st.write("### 4. Customizable Reports :")
   st.write("Users can generate customizable reports that highlight key findings and recommendations. These reports are designed to be easily understood by both technical and non-technical stakeholders, ensuring that all team members can contribute to the improvement process.")
   st.write("### 5. Benchmarking :")
   st.write("The Lex Project includes benchmarking features that allow law firms to compare their website's performance against industry standards and competitors. This provides valuable context and helps set realistic improvement goals.")
   st.write("## Benefits")
   st.write("Enhanced Client Experience: By optimizing their website's UX and UI, law firms can provide a more engaging and user-friendly experience for their clients, leading to higher satisfaction and retention rates.")
   st.write("Increased Conversion Rates: A well-designed website can lead to increased conversion rates, as potential clients are more likely to contact a law firm if they have a positive online experience.")
   st.write("Competitive Advantage: Law firms that leverage the Lex Project can gain a competitive edge by staying ahead of industry trends and ensuring their website meets the highest standards of usability and design.")
   st.write("Data-Driven Decisions: With access to detailed analytics and insights, law firms can make data-driven decisions to continually improve their online presence and client engagement.")
   st.write("## How It Works")
   st.write("1. Website Analysis: The user inputs the URL of the law firm website into the Lex Project platform.")
   st.write("2. AI Evaluation: Our AI models analyze the website, evaluating various aspects of UX and UI.")
   st.write("3. Report Generation: The Lex Project generates a comprehensive report detailing the findings and providing actionable recommendations.")
   st.write("4. Implementation: Law firms can use the insights and recommendations to make targeted improvements to their website.")
   st.write("5. Continuous Improvement: By regularly using the Lex Project, law firms can continuously monitor and enhance their website's performance.")
   st.write("The Lex Project is your partner in creating a compelling and effective online presence for your law firm. With our AI-driven insights and recommendations, you can ensure your website not only looks great but also delivers an exceptional user experience.")

elif options == "About Us" :
     st.title('The Lex Project by Algorex Technologies')
     st.subheader("About Us")
     st.write("# Algorex PH")
     st.image('images/Meer.jpg')
     st.write("Pinoy AI Engineer and Competitive Programmer")
     st.text("Connect with me via Linkedin : https://www.linkedin.com/in/algorexph/")
     st.text("Kaggle Account : https://www.kaggle.com/daniellebagaforomeer")
     st.write("\n")


elif options == "Model" :
     st.title('The Lex Project by Algorex Technologies')
     st.subheader("Specify the Law Firm Website you want to review")
     col1, col2, col3 = st.columns([1, 2, 1])

     with col2:
          law_firm_website_address = st.text_input("Law Firm Website Address", placeholder="www.lawfirm.com")
          submit_button = st.button("Generate Insights")

     if submit_button:
        with st.spinner("Generating Insights"):
             response = requests.get(law_firm_website_address)
             soup = BeautifulSoup(response.content, 'html.parser')
             prompt = "What do you think that we can improve on this website, here is the html structure : " + str(soup) + "/n" + "Make the Feedback detailed and elaborate on things that should be improved on the Law Firm's Website. Additionally Please assess the Law firm website's chatbox if it is available, contact forms and the website's overall attractiveness to potential clients."
             chat_session = model.start_chat(history=[{"role": "user", "parts": [prompt]}])
             response = chat_session.send_message("Make the Feedback detailed and elaborate on things that should be improved on the Law Firm's Website. Additionally Please assess the Law firm website's chatbox if it is available, contact forms and the website's overall attractiveness to potential clients.")
    
        st.success("Insight generated successfully!")
        st.subheader(law_firm_website_address)
        st.write(response.text)