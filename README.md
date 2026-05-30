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

A team can have different defensive profiles:

## Team A

High DHSS  
High FCCI  
High SBCM  

✔ Complete set-piece control


## Team B

High FCCI  
Low SBCM  

✔ Wins initial contact  
❌ Allows second-phase pressure


## Team C

Low DHSS  
High SBCM  

❌ Allows dangerous deliveries  
✔ Recovers well afterwards

---

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

---

# Author

**Stephen Yaw Ayamah**

Football Data Analyst  
Python | Sports Analytics | Data Storytelling

Data Source: StatsBomb Open Data

