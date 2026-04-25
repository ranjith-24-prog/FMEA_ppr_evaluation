import streamlit as st

STYLE_CSS = """
<style>
    /* 1. ROOT LEVEL WIDE MODE FORCE */
    /* Target the specific div that Streamlit uses for content blocks */
    [data-testid="stAppViewBlockContainer"] {
        max-width: 100% !important;
        width: 100% !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        padding-top: 1.5rem !important;
    }

    /* 2. TAB CONTENT EXPANSION */
    /* st.tabs content is often centered; this forces it to use the full width */
    [data-testid="stTabs"] {
        width: 100% !important;
    }

    /* 3. COLUMN FIX */
    /* Ensures st.columns actually span the full width allowed by the container */
    [data-testid="stHorizontalBlock"] {
        width: 100% !important;
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
    
    .stButton > button:hover {
        transform: translateY(-1px);
        filter: brightness(1.05);
    }

    /* 6. INPUT AREAS (Textarea & TextInput) */
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
