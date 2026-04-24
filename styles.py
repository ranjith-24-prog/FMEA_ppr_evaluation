import streamlit as st

STYLE_CSS = """
<style>
    /* 1. THE ULTIMATE FULL-WIDTH OVERRIDE */
    
    /* Target the very first div that Streamlit uses to wrap your content */
    .stAppViewMainContainer > div:nth-child(1) {
        width: 100% !important;
        max-width: none !important;
    }

    /* Target the main block container specifically */
    [data-testid="stAppViewBlockContainer"] {
        max-width: 100% !important;
        width: 100% !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        padding-top: 1rem !important;
    }

    /* Kill the 'max-width' on all potential parent containers */
    .main .block-container, .stMainBlockContainer {
        max-width: none !important;
        width: 100% !important;
    }

    /* 2. FORCE COLUMNS TO SPREAD */
    [data-testid="stHorizontalBlock"] {
        width: 100% !important;
    }
    
    [data-testid="column"], [data-testid="stColumn"] {
        width: 100% !important;
        flex: 1 1 0% !important;
    }

    /* 3. YOUR AESTHETIC STYLING */
    .stApp {
        background: radial-gradient(circle at top left, #e0f2fe 0, #f4f3ed 55%, #e5e7eb 100%) !important;
    }

    /* Typography & UI Elements */
    body, h1, h2, h3, h4, h5, h6, p {
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        color: #111827;
    }
    
    /* Pill Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #0f766e, #22c55e);
        color: #ffffff;
        border: none;
        border-radius: 999px !important; 
        padding: 0.45rem 1.3rem;
        font-weight: 600;
        box-shadow: 0 6px 18px rgba(15, 118, 110, 0.35);
    }

    /* Inputs & Selectboxes */
    .stTextArea textarea, div[data-testid="stTextInput"] input {
        border: 1px solid #d4d4d8 !important;
        border-radius: 14px !important;
        background-color: #f9fafb !important;
    }

    .stSelectbox > div[data-baseweb="select"] {
        border-radius: 999px !important;
        border: 1px solid #0f766e !important;
    }
</style>
"""

def apply_global_styles() -> None:
    """Inject the global CSS into the Streamlit app."""
    st.markdown(STYLE_CSS, unsafe_allow_html=True)
