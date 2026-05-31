# ⚽ Set-Piece Defensive Control Index (SPDCI)

## A Multi-Phase Football Analytics Framework for Evaluating Corner Defense

This project introduces the **Set-Piece Defensive Control Index (SPDCI)** — a data-driven framework that evaluates how effectively football teams control every phase of defending corner situations.

Instead of only asking:

❌ "Did the team concede?"

This framework asks:

✔ "Where exactly did the defensive sequence succeed or fail?"

The model analyzes corner defense through three connected phases:

Corner Delivery → First Contact → Second Ball Control

---

# 🎯 Project Objective

Traditional set-piece analysis often focuses on final outcomes:

- Goals conceded
- Shots allowed
- xG conceded

However, defensive performance is a process.

A team may concede danger because:

- The delivery entered a dangerous zone
- They lost the first contact
- They failed to recover the second ball

SPDCI breaks this process into measurable components.

---

# 🧠 Framework Architecture

# 🧮 SPDCI Calculation

The final Set-Piece Defensive Control Index combines all three defensive phases:

SPDCI = (0.40 × DHSS) + (0.35 × FCCI) + (0.25 × SBCM)


### Weighting Logic

| Component | Weight | Reason |
|---|---:|---|
| DHSS | 40% | Preventing dangerous deliveries reduces threat before contact occurs |
| FCCI | 35% | Winning the first action prevents immediate danger |
| SBCM | 25% | Controlling second phases prevents sustained pressure |

The final score ranges from 0–100.

Higher SPDCI indicates stronger overall corner defensive control.
Weights are based on the chronological importance of each defensive phase and can be adjusted depending on tactical philosophy."


## 1️⃣ Delivery Hotspot Suppression System (DHSS)

### Question:
How well does a team prevent dangerous deliveries?

### Method:

All corner deliveries are mapped using event coordinates.

Each delivery is classified into spatial danger zones:

| Zone | Risk |
|---|---|
| 6-Yard Box | Very High |
| Penalty Spot | High |
| Edge Zone | Medium |
| Wide Delivery | Low |

A weighted danger score is assigned to every delivery.

### Outputs:

- Corners Faced
- Average Delivery Danger
- Delivery Suppression Score (DHSS)

---

# 2️⃣ First Contact Control Index (FCCI)

### Question:
Who controls the first action after delivery?

Tracks first-contact events:

- Clearances
- Duels
- Blocks
- Defensive actions
- Attacking contacts

### Outputs:

- First Contact Situations
- First Contacts Won
- FCCI %

---

# 3️⃣ Second Ball Control Model (SBCM)

### Question:
After the first action, who controls the next phase?

The model identifies:

First Phase:

- Clearance
- Duel
- Block
- Interception

Second Phase:

- Ball Recovery
- Pass
- Carry
- Controlled possession

### Outputs:

- Second Ball Situations
- Second Balls Controlled
- SBCM %

---

# 📊 Defensive Funnel

Example:
Corners Faced
↓
Delivery Zone Quality
↓
First Contact Battle
↓
Second Ball Control
↓
Threat Neutralized

This allows analysts to identify where defensive breakdowns occur.

---

# 📈 Example Insights

# 📈 Case Study: La Liga Sample Analysis

The model was tested on StatsBomb event data from La Liga matches.

### SPDCI Rankings (Sample)

| Team | DHSS | FCCI | SBCM | SPDCI |
|---|---:|---:|---:|---:|
| Getafe | 25.0 | 100.0 | 100.0 | 70.0 |
| Real Betis | 35.7 | 83.3 | 83.3 | 64.3 |
| Deportivo Alavés | 51.3 | 83.3 | 41.7 | 60.1 |
| Barcelona | 32.9 | 76.7 | 31.8 | 47.9 |
| Real Madrid | 19.2 | 50.0 | 40.0 | 35.2 |


## Tactical Findings

### Barcelona Profile

Strong:
✔ First-contact dominance (76.7 FCCI)

Weakness:
⚠ Lower second-phase control (31.8 SBCM)

Interpretation:

Barcelona frequently won the initial action but opponents were able to continue some second-phase attacks.


### Real Betis Profile

Strong:
✔ First-contact control  
✔ Second-ball recovery

Interpretation:

Real Betis showed strong ability to neutralize chaos after deliveries.
# 🖥 Streamlit Dashboard

The interactive dashboard includes:

## Overview

- Team rankings
- SPDCI leaderboard
- Defensive comparison


## DHSS Dashboard

- Delivery danger analysis
- Zone risk scoring
- Spatial evaluation


## FCCI Dashboard

- First-contact dominance
- Contact success rates


## SBCM Dashboard

- Second phase control
- Recovery analysis

  # 📸 Dashboard Preview

Dashboard features:

- SPDCI league rankings
- Team defensive profiles
- DHSS/FCCI/SBCM breakdown
- Interactive team comparison
- Tactical interpretation reports

(Screenshots to be added)

---

# 🛠 Technology Stack

- Python
- Pandas
- NumPy
- Streamlit
- Plotly
- Matplotlib
- StatsBomb Event Data

---

# 📂 Project Structure
SPDCI/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── notebooks/
│ ├── 01_DHSS_Model.ipynb
│ ├── 02_FCCI_Model.ipynb
│ ├── 03_SBCM_Model.ipynb
│ └── 04_SPDCI_Framework.ipynb
│
├── src/
│ ├── data_loader.py
│ ├── dhss.py
│ ├── fcci.py
│ ├── sbcm.py
│ └── spdci.py
│
├── dashboard/
│ └── app.py
│
├── README.md
└── requirements.txt

---

# 🔮 Future Improvements

Planned development:

- Full-season analysis
- xG weighting of delivery zones
- Opponent strength adjustment
- Player-level set-piece evaluation
- Automated scouting reports

---

# 📚 Key Learnings

This project demonstrates:

- Event-data processing
- Spatial analytics
- Feature engineering
- Custom metric development
- Football tactical modelling
- Interactive dashboard creation

# ⚠️ Limitations

Current model limitations:

- Analysis uses available StatsBomb open-data matches, not every league fixture
- Small samples can inflate percentage-based metrics
- Current model does not adjust for opponent delivery quality
- Player-level responsibility is not included yet

Future versions will address these areas.

---

# Author

**Stephen Yaw Ayamah**

Football Data Analyst  
Python | Sports Analytics | Data Storytelling

Data Source: StatsBomb Open Data

