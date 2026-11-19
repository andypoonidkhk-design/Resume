# app.py
# Run with: streamlit run app.py

import streamlit as st

# ---------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------
st.set_page_config(
    page_title="Poon Cheuk Man, Andy",
    page_icon="📄",
    layout="centered",
)

# ---------------------------------------------------------------
# Plain styling: white background, black text, no effects
# ---------------------------------------------------------------
st.markdown(
    """
    <style>
        /* White background */
        .stApp {
            background-color: #FFFFFF;
        }

        /* Black text everywhere */
        html, body, [class*="css"] {
            color: #000000;
        }
        h1, h2, h3, h4, h5, h6, p, li, span, div, strong, em, a,
        label, .stMarkdown, .stMarkdown * {
            color: #000000 !important;
        }

        /* Simple black horizontal rule */
        hr {
            border: none;
            border-top: 1px solid #000000;
            margin: 0.6rem 0 1rem 0;
        }

        /* Reduce excessive spacing */
        .block-container {
            padding-top: 2.5rem;
            padding-bottom: 3rem;
            max-width: 900px;
        }

        /* Links: black and underlined */
        a {
            color: #000000 !important;
            text-decoration: underline;
        }

        /* Right-aligned meta text */
        .meta {
            text-align: right;
            font-size: 0.92rem;
            line-height: 1.4;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------
def section(title: str) -> None:
    """Print a section heading with a black divider."""
    st.markdown(f"## {title}")
    st.markdown("<hr>", unsafe_allow_html=True)


def entry(title: str, subtitle: str = "", location: str = "", date: str = "") -> None:
    """Two-column entry: title/subtitle on the left, location/date on the right."""
    left, right = st.columns([3, 1])
    with left:
        st.markdown(f"**{title}**")
        if subtitle:
            # unsafe_allow_html=True so <br> in subtitle creates a new line
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
st.markdown("# Poon Cheuk Man, Andy")
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