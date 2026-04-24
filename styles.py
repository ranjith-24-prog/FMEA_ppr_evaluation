import streamlit as st

STYLE_CSS = """
<style>
    /* 1. THE LAYOUT FIX - Detects Wide Mode and Forces Expansion */
    
    /* This targets the container ONLY when Streamlit thinks it should be wide */
    [data-testlayout="wide"] .main .block-container,
    [data-testid="stAppViewBlockContainer"] {
        max-width: 100% !important;
        width: 100% !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }

    /* Target the horizontal wrapper for your 4 columns */
    [data-testid="stHorizontalBlock"] {
        width: 100% !important;
    }

    /* Force the columns to actually grow to fill that 100% space */
    [data-testid="column"] {
        flex: 1 1 0% !important;
        min-width: 0 !important;
    }

    /* 2. THE BACKGROUND */
    .stApp {
        background: radial-gradient(circle at top left, #e0f2fe 0, #f4f3ed 55%, #e5e7eb 100%) !important;
    }

    /* 3. BUTTONS (Keeping your teal pill design) */
    .stButton > button {
        background: linear-gradient(135deg, #0f766e, #22c55e) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 999px !important;
        padding: 0.45rem 1.3rem !important;
        font-weight: 600 !important;
    }

    /* 4. INPUT AREAS */
    .stTextArea textarea, div[data-testid="stTextInput"] input {
        border: 1px solid #d4d4d8 !important;
        border-radius: 14px !important;
        background-color: #f9fafb !important;
    }

    /* 5. TABS */
    [data-testid="stTabs"] {
        width: 100% !important;
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
