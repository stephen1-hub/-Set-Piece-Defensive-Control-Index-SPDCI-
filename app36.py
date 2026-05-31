# ============================================================
# ⚽ SET-PIECE DEFENSIVE CONTROL INDEX (SPDCI)
# Streamlit Dashboard
# ============================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------

st.set_page_config(
    page_title="SPDCI | Football Analytics",
    layout="wide"
)


# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------

@st.cache_data
def load_data():

    df = pd.read_csv(
        "spdci_summary.csv"
    )

    return df


df = load_data()


# ------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------

st.sidebar.title(
    "⚙️ Dashboard Controls"
)


team = st.sidebar.selectbox(
    "Select Team",
    sorted(df["defending_team"].unique())
)


min_corners = st.sidebar.slider(
    "Minimum Corners Faced",
    1,
    int(df["Corners_Faced"].max()),
    1
)


filtered = df[
    df["Corners_Faced"] >= min_corners
]


# ------------------------------------------------------------
# HEADER
# ------------------------------------------------------------

st.title(
    "⚽ Set-Piece Defensive Control Index (SPDCI)"
)


st.markdown(
"""
### A multi-phase framework for evaluating corner defensive performance la liga 2020/2021 Season

SPDCI evaluates **where teams gain or lose control** during set-piece defending.

Corner Defense Pipeline:

Corner Delivery ➜ First Contact ➜ Second Ball Control
"""
)


# ------------------------------------------------------------
# KPI SECTION
# ------------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Teams Analysed",
    filtered["defending_team"].nunique()
)


col2.metric(
    "Corners Analysed",
    int(filtered["Corners_Faced"].sum())
)


col3.metric(
    "Average SPDCI",
    round(filtered["SPDCI"].mean(),2)
)


best_team = (
    filtered
    .sort_values(
        "SPDCI",
        ascending=False
    )
    ["defending_team"]
    .iloc[0]
)


col4.metric(
    "Best Rated Team",
    best_team
)


# ------------------------------------------------------------
# SPDCI RANKING
# ------------------------------------------------------------

st.subheader(
    "🏆 SPDCI League Ranking"
)


ranking = filtered.sort_values(
    "SPDCI",
    ascending=False
)


fig = px.bar(

    ranking,

    x="SPDCI",

    y="defending_team",

    orientation="h",

    text="SPDCI",

    hover_data=[
        "DHSS",
        "FCCI",
        "SBCM"
    ]

)


fig.update_layout(

    yaxis_title="Team",

    xaxis_title="SPDCI Score"

)


st.plotly_chart(
    fig,
    use_container_width=True
)


st.dataframe(
    ranking,
    use_container_width=True
)



# ------------------------------------------------------------
# TEAM ANALYSIS
# ------------------------------------------------------------

st.subheader(
    f"📋 {team} Defensive Profile"
)


team_data = df[
    df["defending_team"] == team
].iloc[0]


a,b,c,d = st.columns(4)


a.metric(
    "SPDCI",
    round(team_data["SPDCI"],2)
)


b.metric(
    "DHSS",
    round(team_data["DHSS"],2)
)


c.metric(
    "FCCI",
    round(team_data["FCCI"],2)
)


d.metric(
    "SBCM",
    round(team_data["SBCM"],2)
)


# ------------------------------------------------------------
# RADAR CHART
# ------------------------------------------------------------

st.subheader(
    "🧠 Defensive DNA"
)


radar_df = pd.DataFrame({

    "Metric":[
        "Delivery Suppression",
        "First Contact",
        "Second Ball"
    ],

    "Score":[

        team_data["DHSS"],

        team_data["FCCI"],

        team_data["SBCM"]

    ]

})


fig = go.Figure()


fig.add_trace(

    go.Scatterpolar(

        r=radar_df["Score"],

        theta=radar_df["Metric"],

        fill="toself"

    )

)


fig.update_layout(

    polar=dict(

        radialaxis=dict(

            visible=True,

            range=[0,100]

        )

    ),

    showlegend=False

)


st.plotly_chart(
    fig,
    use_container_width=True
)


# ------------------------------------------------------------
# MODEL BREAKDOWN
# ------------------------------------------------------------

st.subheader(
    "🔬 Model Explanation"
)


st.markdown(
"""

### 1️⃣ DHSS — Delivery Hotspot Suppression System

Measures:

**Did the team prevent dangerous corner deliveries?**

---

### 2️⃣ FCCI — First Contact Control Index

Measures:

**Did the team win the first action after delivery?**

---

### 3️⃣ SBCM — Second Ball Control Model

Measures:

**After the first contest, did the team regain control?**

---

### Final Formula

SPDCI =

**40% DHSS + 35% FCCI + 25% SBCM**

"""
)


# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------

st.caption(
    "Built by Stephen Yaw Ayamah | Football Analytics | Python | StatsBomb Event Data"
)
