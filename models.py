import streamlit as st
import streamlit.components.v1 as components
from sgmker_bert import query_bert
import time
from sgmker_gemma import query_gemma


def getSentiments(userText, type):
    if type == 'EMOLINGUA-BERT':
        return query_bert({"inputs": userText})

    elif type == 'EMOLINGUA-GEMMA':
        return query_gemma(userText= userText)

def renderPage():
    st.title("Emolingua AI Model Playground")
    # components.html("""<hr style="height:3px;border:none;color:#333;background-color:#333;" /> """)
    # st.markdown("### User Input Text Analysis")
    st.text("")
    type = st.selectbox(
     "$$\large\\text{Select a model}$$",
     ('EMOLINGUA-BERT', 'EMOLINGUA-GEMMA'))
    # userText = st.text_input('User Input', placeholder='Input text HERE')
    # st.text("")
    # if st.button('Predict'):
    #     if(userText!=""):
    #         st.text("")
            

    st.text("")
    with st.container():
        userText = st.text_input("$$\large\\text{Model Input}$$", placeholder='Enter a statement')
        st.text("")
        var = st.button('Predict')

    if type == 'EMOLINGUA-BERT':
        
        with st.container():
            st.title(body = "Results")
            st.text("")
            my_bar = st.progress(0, text="$\large\\text{Positive}$")
            my_bar2 = st.progress(0, text="$\large\\text{Neutral}$")
            my_bar3 = st.progress(0, text="$\large\\text{Negative}$")

            if var:
                result = getSentiments(userText, type)
                pos, neu, neg = round(result['Positive'], 4), round(result['Neutral'], 4), round(result['Negative'], 4)
                print(pos, neg, neu)
                for percent_complete in range(0, int(pos*100)+1):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1, text="$\large\\text{Positive}$"+ " : " + str(pos))

                for percent_complete in range(0, int(neu*100)+1):
                    time.sleep(0.01)
                    my_bar2.progress(percent_complete + 1, text="$\large\\text{Neutral}$"+ " : "  + str(neu))

                for percent_complete in range(0, int(neg*100)+1):
                    time.sleep(0.01)
                    my_bar3.progress(percent_complete + 1, text="$\large\\text{Negative}$"+ " : "  + str(neg))
            

    elif type == 'EMOLINGUA-GEMMA':
        
        with st.container(border= True):

            if var:
                gemma_response = getSentiments(userText, type)
                st.header(body = "Model Response:")
                st.components.v1.html(f"""
                                    <h3 style="color: #ffffff; font-family: Source Sans Pro, sans-serif; font-size: 28px;">{gemma_response}</h3>
        
                                    """, height = 300)
            