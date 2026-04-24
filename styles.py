import streamlit as st

STYLE_CSS = """
<style>
    /* 1. TARGET THE ABSOLUTE OUTER WRAPPERS */
    /* This targets the dynamic flex containers that Streamlit uses to center your app */
    .stAppViewMainContainer > div:nth-child(1),
    .stAppViewBlockContainer,
    .main .block-container,
    .stMainBlockContainer,
    [data-testid="stAppViewBlockContainer"] {
        max-width: 100% !important;
        width: 100% !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        padding-top: 1rem !important;
        padding-bottom: 3rem !important;
    }

    /* 2. TAB & COLUMN EXPANSION */
    /* Force the tabs and the horizontal rows to stretch */
    [data-testid="stTabs"], 
    [data-testid="stHorizontalBlock"],
    [data-testid="stVerticalBlock"] {
        width: 100% !important;
        max-width: 100% !important;
    }

    /* Force columns to be equal and take up 100% of the parent width */
    [data-testid="column"], [data-testid="stColumn"] {
        flex: 1 1 0% !important;
        width: 100% !important;
        min-width: 0 !important;
    }

    /* 3. YOUR AESTHETIC THEMING */
    .stApp {
        background: radial-gradient(circle at top left, #e0f2fe 0, #f4f3ed 55%, #e5e7eb 100%) !important;
    }

    /* Typography */
    body, h1, h2, h3, h4, h5, h6, p, label {
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
        color: #111827 !important;
    }

    /* Primary Pill Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #0f766e, #22c55e) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 999px !important;
        padding: 0.45rem 1.3rem !important;
        font-weight: 600 !important;
        box-shadow: 0 6px 18px rgba(15, 118, 110, 0.35) !important;
    }

    /* Selectboxes and Inputs */
    .stSelectbox > div[data-baseweb="select"], 
    .stTextArea textarea, 
    div[data-testid="stTextInput"] input {
        border: 1px solid #d4d4d8 !important;
        border-radius: 14px !important;
        background-color: #f9fafb !important;
    }

    /* Selectbox Pill Shape */
    .stSelectbox > div[data-baseweb="select"] {
        border-radius: 999px !important;
    }
</style>
"""

AGGRID_CUSTOM_CSS = {
    ".ag-root-wrapper": {
        "border-radius": "14px",
        "border": "1px solid #e5e7eb",
        "box-shadow": "0 4px 14px rgba(15, 23, 42, 0.06)",
        "overflow": "hidden",
    },
    ".ag-header": {
        "background-color": "#0f172a !important",
        "color": "#f9fafb !important",
    },
    ".ag-row-hover": {
        "background-color": "#e0f2fe !important",
    },
}

def apply_global_styles() -> None:
    """Inject the global CSS into the Streamlit app."""
    st.markdown(STYLE_CSS, unsafe_allow_html=True)
