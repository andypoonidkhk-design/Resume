import streamlit as st

# ---------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------
st.set_page_config(
    page_title="Poon Cheuk Man, Andy",
    page_icon="📄",
    layout="centered",
)
# Bright mode is the default.
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

button_label = "🌙 Switch to dark mode" if not st.session_state.dark_mode else "☀️ Switch to bright mode"

if st.button(button_label, key="theme_toggle"):
    st.session_state.dark_mode = not st.session_state.dark_mode
    st.rerun()

dark_mode = st.session_state.dark_mode
dark_mode = st.session_state.get("dark_mode", True)

bg_color = "#111827" if dark_mode else "#FFFFFF"
text_color = "#F3F4F6" if dark_mode else "#000000"
rule_color = "#9CA3AF" if dark_mode else "#000000"
# ---------------------------------------------------------------
# Theme selection
# ---------------------------------------------------------------
dark_mode = st.session_state.get("dark_mode", False)

bg_color = "#111827" if dark_mode else "#FFFFFF"
text_color = "#F3F4F6" if dark_mode else "#000000"
rule_color = "#9CA3AF" if dark_mode else "#000000"

# ---------------------------------------------------------------
# Styling
# ---------------------------------------------------------------
st.markdown(
    f"""
    <style>
        /* Page and text colors */
        .stApp,
        [data-testid="stAppViewContainer"] {{
            background-color: {bg_color};
            color: {text_color};
        }}

        html, body, [class*="css"],
        h1, h2, h3, h4, h5, h6, p, li, span, div, strong, em,
        label, .stMarkdown, .stMarkdown * {{
            color: {text_color} !important;
        }}

        /* Links */
        a {{
            color: {text_color} !important;
            text-decoration: underline;
        }}

        /* Section dividers */
        hr {{
            border: none;
            border-top: 1px solid {rule_color};
            margin: 0.35rem 0 0.6rem 0;
        }}

        /* Compact page layout */
        .block-container {{
            padding-top: 1.5rem;
            padding-bottom: 2rem;
            max-width: 900px;
        }}

        [data-testid="stVerticalBlock"] {{
            gap: 0.5rem;
        }}

        .stMarkdown p,
        .stMarkdown ul {{
            margin-top: 0.1rem;
            margin-bottom: 0.3rem;
        }}

        /* Smaller section headings */
        .stMarkdown h2 {{
            font-size: 1.25rem;
            line-height: 1.35;
            margin-top: 0.55rem;
            margin-bottom: 0.15rem;
        }}

        /* Right-aligned metadata */
        .meta {{
            text-align: right;
            font-size: 0.88rem;
            line-height: 1.35;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------
def section(title: str) -> None:
    """Print a compact section heading with a divider."""
    st.markdown(f"## {title}")
    st.markdown("<hr>", unsafe_allow_html=True)


def entry(
    title: str,
    subtitle: str = "",
    location: str = "",
    date: str = "",
) -> None:
    """Two-column entry: title/subtitle on the left, location/date on the right."""
    left, right = st.columns([3, 1])

    with left:
        st.markdown(f"**{title}**")
        if subtitle:
            st.markdown(subtitle, unsafe_allow_html=True)

    with right:
        meta = "<br>".join(x for x in (location, date) if x)
        st.markdown(f'<div class="meta">{meta}</div>', unsafe_allow_html=True)


def bullets(items) -> None:
    """Print a plain bullet list."""
    st.markdown("\n".join(f"- {item}" for item in items))

# ---------------------------------------------------------------
# Header / contact
# ---------------------------------------------------------------
name_col, toggle_col = st.columns([5, 1])

with name_col:
    st.markdown("# Poon Cheuk Man, Andy")

with toggle_col:
    dark_mode = st.toggle(
        "Dark mode",
        key="dark_mode",
        value=False,
    )

st.markdown(
    "Telephone: (852) 54094972 &nbsp;|&nbsp; "
    "Email: [andypoon.idk.hk@gmail.com](mailto:andypoon.idk.hk@gmail.com)"
)
st.markdown("<hr>", unsafe_allow_html=True)
# ---------------------------------------------------------------
# Education
# ---------------------------------------------------------------
section("Education")

entry(
    title="Hong Kong University of Science and Technology (HKUST)",
    subtitle="Bachelor of Business Administration in Finance — CGPA: 3.07/4.3<br>"
             "Additional major in Operation Management (HKUST STEM Program)",
    location="Hong Kong",
    date="Sep 2024 – Jun 2028",
)
st.markdown(
    "**Relevant Coursework:** Intermediate Investments, Derivative Securities, "
    "Corporate Finance, Fixed Income Securities, Data Mining for Business Analytics"
)
st.write("")

entry(
    title="Wong Tai Shan Memorial College",
    subtitle="HKDSE: 5* in Mathematics, 5 in Module 1 (Calculus and Statistics) and Economics",
    location="",
    date="2018 – 2024",
)

# ---------------------------------------------------------------
# Internship
# ---------------------------------------------------------------
section("Internship")

entry(
    title="Sammy Lau CPA Limited",
    subtitle="Audit Junior — Part Time",
    location="Hong Kong",
    date="Aug – Nov 2026",
)
bullets([
    "Performed basic analytical procedures on financial statement line items to identify "
    "unusual movements and support the audit process.",
    "Prepared and rolled forward audit working papers and supporting schedules in Excel, "
    "ensuring accuracy, consistency and clear documentation for manager and partner review.",
    "Conducted substantive testing through tests of details and sampling, tracing selected "
    "items to ledgers and supporting records to obtain audit evidence.",
    "Supported liquidation engagements by extracting and reconciling financial information "
    "from company ledgers and records, and updating the Official Receiver's Office platform.",
    "Applied Excel extensively for data cleaning, schedule preparation, analytical reviews "
    "and organising working paper files.",
])
st.write("")

entry(
    title="Spacious",
    subtitle="Data Analyst Intern",
    location="Hong Kong",
    date="Jun – Jul 2026",
)
bullets([
    "Supported end-to-end data operations for business intelligence dashboards, cleaning "
    "and structuring over 10,000 property transaction records to enable market trend analysis.",
    "Assisted in developing in-house dataset development, including data researching and "
    "processing; proactively identified data inconsistencies and proposed quality control measures.",
])

# ---------------------------------------------------------------
# Enrichment Activities
# ---------------------------------------------------------------
section("Enrichment Activities")

entry(
    title="HSBC Case Competition 2024",
    subtitle="Participant",
    location="Hong Kong",
    date="2024",
)
bullets([
    "Developed a customized investment portfolio aligned with a client's retirement "
    "objectives, applying principles from Financial Management.",
    "Conducted equity research and statistical market analysis using Business Statistics "
    "methodologies to inform asset allocation and hedging strategies.",
])
st.write("")

entry(
    title="Chartwell Capital Investment Challenge",
    subtitle="Participant",
    location="Hong Kong",
    date="",
)
bullets([
    "Hands-on experience in constructing investment strategy, including valuation models "
    "and a written report on the company's business model and market position.",
    "Produced a comprehensive written report covering business model, competitive "
    "positioning and investment thesis; received positive feedback from judges on report "
    "structure and analytical depth.",
])

# ---------------------------------------------------------------
# Language and Skills
# ---------------------------------------------------------------
section("Language and Skills")

bullets([
    "**Languages:** Native Cantonese; proficient working Mandarin and English.",
    "**Computer:** Proficient in MS Office (Word, Excel, PowerPoint), Bloomberg.",
    "**Programming:** Python (Business Application Development in Python, Coding for "
    "Business), VBA (intermediate).",
])

# ---------------------------------------------------------------
# Footer
# ---------------------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("© 2026 Poon Cheuk Man, Andy")