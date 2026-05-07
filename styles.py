import streamlit as st

STYLE_CSS = """
<style>
    /* 1. TARGET THE ROOT FLEX CONTAINER */
    /* This overrides the JavaScript-calculated width on the main viewport */
    .stAppViewMainContainer > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) {
        max-width: 100% !important;
        width: 100% !important;
    }

    /* 2. OVERRIDE ALL BLOCK CONTAINERS */
    /* Targets both the standard class and the specific test ID */
    [data-testid="stAppViewBlockContainer"], .main .block-container {
        max-width: 100% !important;
        width: 100% !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        padding-top: 2rem !important;
    }

    /* 3. FIX FOR TABS & COLUMNS */
    /* st.tabs content is often trapped in a centered div; this breaks it out */
    [data-testid="stTabs"], [data-testid="stHorizontalBlock"] {
        width: 100% !important;
    }

    /* Force columns to use the expanded width */
    [data-testid="column"] {
        flex: 1 1 0% !important;
        min-width: 0 !important;
    }

    /* 4. THE BACKGROUND (Radial Gradient) */
    .stApp {
        background: radial-gradient(circle at top left, #e0f2fe 0, #f4f3ed 55%, #e5e7eb 100%) !important;
    }

    /* 5. BUTTONS (Teal Pill Design) */
    .stButton > button {
        background: linear-gradient(135deg, #0f766e, #22c55e) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 999px !important;
        padding: 0.45rem 1.3rem !important;
        font-weight: 600 !important;
        box-shadow: 0 6px 18px rgba(15, 118, 110, 0.35) !important;
    }

    /* 6. INPUT AREAS */
    .stTextArea textarea, div[data-testid="stTextInput"] input {
        border: 1px solid #d4d4d8 !important;
        border-radius: 14px !important;
        background-color: #f9fafb !important;
        padding: 0.9rem 1rem !important;
    }
</style>
"""

AGGRID_CUSTOM_CSS = {
    ".ag-root-wrapper": {
        "border-radius": "14px",
        "border": "1px solid #e5e7eb",
        "overflow": "hidden",
    },
    ".ag-header": {
        "background-color": "#0f172a !important",
        "color": "#f9fafb !important",
    }
}

def apply_global_styles() -> None:
    st.markdown(STYLE_CSS, unsafe_allow_html=True)
