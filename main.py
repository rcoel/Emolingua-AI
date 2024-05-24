import streamlit as st
import sidebar
import models

page = sidebar.show()

if page == 'models':
    models.renderPage()