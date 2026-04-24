import streamlit as st

STYLE_CSS = """
<style>
    /* 1. LAYOUT & WIDTH OVERRIDES (The "Nuke" fix) */
    /* Target the main container to remove the 1200px limit */
    [data-testid="stAppViewBlockContainer"], .main .block-container {
        max-width: 100% !important;
        width: 100% !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        padding-top: 1.5rem !important;
        padding-bottom: 3rem !important;
    }

    /* Target the horizontal wrapper for columns to use full width */
    [data-testid="stHorizontalBlock"] {
        width: 100% !important;
        gap: 1rem !important;
    }

    /* Force columns to distribute 100% of available space equally */
    [data-testid="stColumn"] {
        width: 100% !important;
        flex: 1 1 0% !important;
        min-width: 0px !important;
    }

    /* 2. GLOBAL BACKGROUND */
    .stApp {
        background: radial-gradient(circle at top left, #e0f2fe 0, #f4f3ed 55%, #e5e7eb 100%) !important;
    }

    /* 3. TYPOGRAPHY */
    body, h1, h2, h3, h4, h5, h6, p {
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        color: #111827;
    }
    h1 {
        font-size: 2rem;
        font-weight: 700;
        letter-spacing: -0.03em;
        margin-bottom: 0.5rem;
    }
    h2 {
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }

    /* 4. BUTTONS (Pill-shaped & Gradient) */
    .stButton > button {
        background: linear-gradient(135deg, #0f766e, #22c55e);
        color: #ffffff;
        border: none;
        border-radius: 999px !important; 
        padding: 0.45rem 1.3rem;
        font-weight: 600;
        font-size: 0.92rem;
        box-shadow: 0 6px 18px rgba(15, 118, 110, 0.35);
        cursor: pointer;
        transition: background-color 0.15s ease, transform 0.15s ease, box-shadow 0.15s ease;
    }
    .stButton > button:hover {
        filter: brightness(1.06);
        transform: translateY(-1px);
        box-shadow: 0 10px 24px rgba(15, 118, 110, 0.45);
    }
    .stButton > button[kind="secondary"],
    .stButton > button[data-testid="baseButton-secondary"] {
        background: #e5f2ff;
        color: #0f172a;
        border-radius: 999px;
        border: 1px solid #cbd5f5;
        box-shadow: none;
    }

    /* 5. TABS */
    [data-testid="stTabs"] {
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
    }
    [data-testid="stTabs"] button[role="tab"] {
        font-weight: 700;
        padding-top: 0.6rem;
        padding-bottom: 0.6rem;
    }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-weight: 700 !important;
    }

    /* 6. INPUTS & TEXTAREAS */
    .stTextArea textarea, div[data-testid="stTextInput"] input {
        border: 1px solid #d4d4d8 !important;
        border-radius: 14px !important;
        background-color: #f9fafb !important;
        padding: 0.9rem 1rem !important;
        box-shadow: 0 2px 6px rgba(15, 23, 42, 0.06);
        font-size: 0.95rem;
    }
    .stTextArea textarea:focus-visible, div[data-testid="stTextInput"] input:focus-visible {
        outline: none !important;
        border: 1px solid #0f766e !important;
        background-color: #ffffff !important;
    }

    /* LLM Selectbox styling */
    .stSelectbox > div[data-baseweb="select"] {
        border-radius: 999px !important;
        border: 1px solid #0f766e !important;
        background: linear-gradient(135deg, #eef2ff, #f9fafb) !important;
        padding: 0 !important;
    }
    .stSelectbox > div[data-baseweb="select"] div[role="combobox"] {
        background-color: transparent !important;
        border-radius: 999px !important;
    }

    /* 7. DATAFRAMES & TABLES */
    div[data-testid="stDataFrame"] > div {
        border-radius: 14px;
        overflow: hidden;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.06);
        border: 1px solid #e5e7eb;
    }
</style>
"""

AGGRID_CUSTOM_CSS = {
    ".ag-root-wrapper": {
        "border-radius": "14px",
        "border": "1px solid #e5e7eb",
        "box-shadow": "0 4px 14px rgba(15, 23, 42, 0.06)",
        "overflow": "hidden",
        "background-color": "#f9fafb",
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
