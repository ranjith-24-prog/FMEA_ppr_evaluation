import streamlit as st

STYLE_CSS = """
<style>
    /* 1. MINIMAL LAYOUT CORRECTION */
    /* Only remove the max-width restriction without forcing fixed widths */
    .block-container {
        max-width: none !important;
        padding-top: 2rem !important;
    }

    /* 2. THE BACKGROUND */
    .stApp {
        background: radial-gradient(circle at top left, #e0f2fe 0, #f4f3ed 55%, #e5e7eb 100%) !important;
    }

    /* 3. BUTTONS (Teal Pill Design) */
    .stButton > button {
        background: linear-gradient(135deg, #0f766e, #22c55e) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 999px !important;
        padding: 0.45rem 1.3rem !important;
        font-weight: 600 !important;
        box-shadow: 0 6px 18px rgba(15, 118, 110, 0.35) !important;
        transition: transform 0.1s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        filter: brightness(1.05);
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
    
    [data-testid="stTabs"] button[role="tab"] p {
        font-weight: 700 !important;
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
