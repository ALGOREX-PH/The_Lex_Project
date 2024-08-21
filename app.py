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
        ["Home", "About Us", "Model", "Model(Filipino)", "Chat"],
        icons = ['book', 'globe', 'tools', "tools", "tools", "tools"],
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
     st.write("## Pinoy AI Engineer and Competitive Programmer")
     st.text("Connect with me via Linkedin : https://www.linkedin.com/in/algorexph/")
     st.text("Kaggle Account : https://www.kaggle.com/daniellebagaforomeer")
     st.write("# Kristine Shyra Carpio")
     st.image('images/Shyra.jpeg')
     st.write("## Operations Manager at Homely Spaces")
     st.text("Connect with me via Linkedin : https://www.linkedin.com/in/kristine-shyra-carpio-618a18214/")
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
             message = """
             Make the Feedback detailed and elaborate on things that should be improved on the Law Firm's Website. Additionally Please assess the Law firm website's chatbox if it is available, contact forms and the website's overall attractiveness to potential clients.

             Here is a List that you need to fill up information on based on your findings on the website :
             1. User Interface & Design
             - Visual Appeal: Does the website have a professional, modern, and aesthetically pleasing design? Are the colors, fonts, and imagery aligned with the firm’s brand?
             - Ease of Navigation: Is the site easy to navigate? Are menus and links clear and intuitive? Can users find key information with minimal clicks?
             - Responsiveness: Does the site work well on all devices, including desktops, tablets, and mobile phones? Is the layout adaptive to different screen sizes?
             - Loading Speed: Are the pages loading quickly? Is there any noticeable lag that could frustrate users?
             - Accessibility: Is the site accessible to people with disabilities? Does it follow best practices for web accessibility (e.g., alt text for images, keyboard navigation)?

             2. Chatbox Functionality (If Available)
             - Availability and Visibility: Is the chatbox easy to locate on the website? Does it stand out without being intrusive?
             - Response Time: How quickly does the chatbox respond to user inquiries? Are the responses timely and relevant?
             - User Experience: Is the chatbox user-friendly? Does it guide users effectively through the conversation? Can users easily connect with a human representative if needed?
             - Content Quality: Are the responses from the chatbox accurate, informative, and helpful? Does it handle a wide range of queries effectively?
             - Integration: Does the chatbox integrate well with the overall design of the website? Does it enhance the user experience?

             3. Contact Forms
             - Ease of Use: Are the contact forms straightforward and simple to fill out? Are there clear instructions and labels for each field?
             - Field Relevance: Are the fields relevant and necessary? Are users asked only for essential information?
             - Validation and Feedback: Does the form validate inputs and provide clear error messages if something is filled out incorrectly? Is there immediate feedback or confirmation upon submission?
             - Accessibility: Is the form accessible to all users, including those with disabilities? Does it follow best practices for web forms?
             - Follow-up Process: Is there a clear indication of what will happen after the form is submitted? Do users receive a confirmation email or message, and is there a defined timeframe for a response?
             4. Overall Attractiveness to Potential Clients
             - First Impressions: Does the website create a strong first impression? Is it clear what services the law firm offers from the homepage?
             - Content Relevance: Is the content on the website relevant and engaging? Does it effectively communicate the law firm’s expertise and value proposition?
             - Trustworthiness: Are there elements on the site that build trust, such as client testimonials, case studies, or professional accolades?
             - Calls to Action: Are there clear and compelling calls to action (CTAs) that guide users toward contacting the firm or scheduling a consultation?
             - SEO Friendliness: Is the website optimized for search engines? Are there appropriate meta tags, keyword-rich content, and a clear structure that aids in discoverability?
             """
             response = chat_session.send_message(message)
    
             st.success("Insight generated successfully!")
             st.subheader(law_firm_website_address)
             st.write(response.text)

elif options == "Model(Filipino)" :
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
             message = """
             Make the Feedback in Filipino, it has to detailed and elaborate on things that should be improved on the Law Firm's Website. Additionally Please assess the Law firm website's chatbox if it is available, contact forms and the website's overall attractiveness to potential clients.

             Here is a List that you need to fill up information on based on your findings on the website :
             1. User Interface & Design
             - Visual Appeal: Does the website have a professional, modern, and aesthetically pleasing design? Are the colors, fonts, and imagery aligned with the firm’s brand?
             - Ease of Navigation: Is the site easy to navigate? Are menus and links clear and intuitive? Can users find key information with minimal clicks?
             - Responsiveness: Does the site work well on all devices, including desktops, tablets, and mobile phones? Is the layout adaptive to different screen sizes?
             - Loading Speed: Are the pages loading quickly? Is there any noticeable lag that could frustrate users?
             - Accessibility: Is the site accessible to people with disabilities? Does it follow best practices for web accessibility (e.g., alt text for images, keyboard navigation)?

             2. Chatbox Functionality (If Available)
             - Availability and Visibility: Is the chatbox easy to locate on the website? Does it stand out without being intrusive?
             - Response Time: How quickly does the chatbox respond to user inquiries? Are the responses timely and relevant?
             - User Experience: Is the chatbox user-friendly? Does it guide users effectively through the conversation? Can users easily connect with a human representative if needed?
             - Content Quality: Are the responses from the chatbox accurate, informative, and helpful? Does it handle a wide range of queries effectively?
             - Integration: Does the chatbox integrate well with the overall design of the website? Does it enhance the user experience?

             3. Contact Forms
             - Ease of Use: Are the contact forms straightforward and simple to fill out? Are there clear instructions and labels for each field?
             - Field Relevance: Are the fields relevant and necessary? Are users asked only for essential information?
             - Validation and Feedback: Does the form validate inputs and provide clear error messages if something is filled out incorrectly? Is there immediate feedback or confirmation upon submission?
             - Accessibility: Is the form accessible to all users, including those with disabilities? Does it follow best practices for web forms?
             - Follow-up Process: Is there a clear indication of what will happen after the form is submitted? Do users receive a confirmation email or message, and is there a defined timeframe for a response?
             4. Overall Attractiveness to Potential Clients
             - First Impressions: Does the website create a strong first impression? Is it clear what services the law firm offers from the homepage?
             - Content Relevance: Is the content on the website relevant and engaging? Does it effectively communicate the law firm’s expertise and value proposition?
             - Trustworthiness: Are there elements on the site that build trust, such as client testimonials, case studies, or professional accolades?
             - Calls to Action: Are there clear and compelling calls to action (CTAs) that guide users toward contacting the firm or scheduling a consultation?
             - SEO Friendliness: Is the website optimized for search engines? Are there appropriate meta tags, keyword-rich content, and a clear structure that aids in discoverability?
             """
             response = chat_session.send_message(message)
    
             st.success("Insight generated successfully!")
             st.subheader(law_firm_website_address)
             st.write(response.text)


if options == "Chat" :
   # Step 1: Title and Instructions
   st.title("Website Chat Initialization")
   st.write("Please enter a website link to initialize the chat.")

   # Step 2: Input field for website link
   website_link = st.text_input("Website URL", "")

   # Step 3: Button to initialize chat
   if website_link:
      if st.button("Initialize Chat"):
         # Assuming there's a function to validate the link
         if "http" in website_link:
             # Proceed to chat after validating the link
             st.success("Link validated. Initializing chat...")
             # Add your chat initialization code here
             response = requests.get(website_link)
             soup = BeautifulSoup(response.content, 'html.parser')
             system_prompt = "What do you think that we can improve on this website, here is the html structure : " + str(soup) + "/n" + "Make the Feedback detailed and elaborate on things that should be improved on the Law Firm's Website. Additionally Please assess the Law firm website's chatbox if it is available, contact forms and the website's overall attractiveness to potential clients."
             def initialize_conversation(prompt):
                 if 'messages' not in st.session_state:
                    st.session_state.messages = []
                    st.session_state.messages.append({"role": "user", "content": prompt})
                    chat_session = model.start_chat(history = st.session_state.messages)
                    message = """
             Make the Feedback in Filipino, it has to detailed and elaborate on things that should be improved on the Law Firm's Website. Additionally Please assess the Law firm website's chatbox if it is available, contact forms and the website's overall attractiveness to potential clients.

             Here is a List that you need to fill up information on based on your findings on the website :
             1. User Interface & Design
             - Visual Appeal: Does the website have a professional, modern, and aesthetically pleasing design? Are the colors, fonts, and imagery aligned with the firm’s brand?
             - Ease of Navigation: Is the site easy to navigate? Are menus and links clear and intuitive? Can users find key information with minimal clicks?
             - Responsiveness: Does the site work well on all devices, including desktops, tablets, and mobile phones? Is the layout adaptive to different screen sizes?
             - Loading Speed: Are the pages loading quickly? Is there any noticeable lag that could frustrate users?
             - Accessibility: Is the site accessible to people with disabilities? Does it follow best practices for web accessibility (e.g., alt text for images, keyboard navigation)?

             2. Chatbox Functionality (If Available)
             - Availability and Visibility: Is the chatbox easy to locate on the website? Does it stand out without being intrusive?
             - Response Time: How quickly does the chatbox respond to user inquiries? Are the responses timely and relevant?
             - User Experience: Is the chatbox user-friendly? Does it guide users effectively through the conversation? Can users easily connect with a human representative if needed?
             - Content Quality: Are the responses from the chatbox accurate, informative, and helpful? Does it handle a wide range of queries effectively?
             - Integration: Does the chatbox integrate well with the overall design of the website? Does it enhance the user experience?

             3. Contact Forms
             - Ease of Use: Are the contact forms straightforward and simple to fill out? Are there clear instructions and labels for each field?
             - Field Relevance: Are the fields relevant and necessary? Are users asked only for essential information?
             - Validation and Feedback: Does the form validate inputs and provide clear error messages if something is filled out incorrectly? Is there immediate feedback or confirmation upon submission?
             - Accessibility: Is the form accessible to all users, including those with disabilities? Does it follow best practices for web forms?
             - Follow-up Process: Is there a clear indication of what will happen after the form is submitted? Do users receive a confirmation email or message, and is there a defined timeframe for a response?
             4. Overall Attractiveness to Potential Clients
             - First Impressions: Does the website create a strong first impression? Is it clear what services the law firm offers from the homepage?
             - Content Relevance: Is the content on the website relevant and engaging? Does it effectively communicate the law firm’s expertise and value proposition?
             - Trustworthiness: Are there elements on the site that build trust, such as client testimonials, case studies, or professional accolades?
             - Calls to Action: Are there clear and compelling calls to action (CTAs) that guide users toward contacting the firm or scheduling a consultation?
             - SEO Friendliness: Is the website optimized for search engines? Are there appropriate meta tags, keyword-rich content, and a clear structure that aids in discoverability?
             """
                    response = chat_session.send_message(message)
                    st.session_state.messages.append({"role" : "user", "content" : message})
                    st.session_state.messages.append({"role": "assistant", "content": response.text})

             initialize_conversation(system_prompt)

             for messages in st.session_state.messages :
                 if messages['role'] == 'system' : continue 
                 else :
                    with st.chat_message(messages["role"]):
                         st.markdown(messages["content"])

             if user_message := st.chat_input("Say something"):
                with st.chat_message("user"):
                     st.markdown(user_message)
                st.session_state.messages.append({"role": "user", "content": user_message})
                response = chat_session.send_message(user_message)
                with st.chat_message("assistant"):
                     st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})