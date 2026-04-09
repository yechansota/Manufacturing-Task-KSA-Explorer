# Manufacturing Task & KSA Explorer

<p align="center">
<strong>An interactive workforce analysis tool for task-level KSA profiling, cross-training similarity, and safety-integrated workforce planning in Energy Belt manufacturing</strong><br>
<em>(Region: AL · GA · NC · SC · TN)</em>
</p>

**[Try the live tool here](https://yechansota.github.io/Manufacturing-Task-KSA-Explorer/)**

---

## Why This Project Exists
In many manufacturing plants, vital decisions about staff training, job rotations, and succession planning rely on the personal intuition of senior managers. A supervisor "knows" that a machinist could probably learn welding, but cannot quantify why, or compare that option against five alternatives. When the supervisor retires, that intuition leaves with them. This is not just an American problem. Korea's most competitive companies — Hyundai, Samsung, LG — are all built on manufacturing foundations, and the demographic shift is hitting both countries at the same time.

This tool is not a production-ready enterprise system. It is a proof of concept — a demonstration of what becomes possible when workforce decisions are grounded in structured data rather than gut feeling. The framework, the methodology, and the analytical approach are what matter here. The idea that cross-training feasibility, hiring criteria, and succession planning can all be derived from the same underlying KSA data, measured consistently across 191 tasks and 6 industries — that is the contribution.

The aging manufacturing workforce in the U.S. "Energy Belt" faces a critical challenge: the annual 6.6% loss of senior talent erases decades of institutional knowledge. Starting from a macro-level risk model in Project 1, which utilized 15 years of federal data (2006–2024) to demonstrate that demographic exits are now a mathematical certainty rather than a traditional HR concern, this series progressed to building objective measurement tools. In Project 2, an 87-dimensional cognitive distance model grounded in Cattell-Horn-Carroll (CHC) Theory mathematically proves the feasibility of cross-training between roles like Machinists and Welders. But strategy is not execution — an HR manager on the plant floor does not transfer "a Machinist." They reassign a person to specific tasks.

To bridge this gap, Project 3 decomposes 150 occupation codes into 191 specific, measurable tasks (e.g., CNC programming, dimensional inspection), mapping them against a comprehensive data ecosystem including O\*NET 30.0, ESCO v1.2, OSHA safety logs, and DOL RAPIDS. By integrating NLP-driven insights from 1.3M LinkedIn job postings, this tool enables HR professionals to perform side-by-side task comparisons and instant cross-training feasibility analysis, providing a precise roadmap for the specific skills, safety certifications, and interview competencies required to maintain workforce resilience.

The three projects work together as a pipeline:
- **Project 1 (The Warning):** Identified the crisis — the talent supply chain is collapsing.
- **Project 2 (The Strategy):** Mapped which occupations are close enough for cross-training, using cognitive science.
- **Project 3 (The Action):** Made that strategy usable — a tool where you can search tasks, build a shortlist, and get analysis on what it takes to train someone.

Demographic shift does not wait for intuition to catch up. Manufacturing needs tools that turn data into decisions.

---

## What Each Task Contains

Every task in the tool is mapped to:

- **O\*NET SOC code** — the U.S. federal standard for classifying jobs (links back to Project 2)
- **ESCO code** — the European equivalent, for international comparison
- **36 KSA scores** — 12 Knowledge, 12 Skills, 12 Abilities, each rated 1–5
- **Industry standards** — applicable certifications (IATF 16949, AS9100, IEC 62660, etc.)
- **Safety data** — TRIR, DART injury rates, and Hazard Level (LOW to CRITICAL)

---

## How the KSA Scores Were Built

The KSA (Knowledge, Skills, Abilities) scores are the core of this tool. They were not simply copied from a database — they went through a three-step process:

**Step 1 — Federal data as the foundation.** O\*NET 30.0, maintained by the U.S. Department of Labor, provides importance ratings (1–5) for thousands of occupations. This is the most rigorously validated source of occupational skill data available.

**Step 2 — Adjusted for each industry.** A single occupation code like "Machinists" covers very different work depending on the industry. An automotive CNC machinist (T012) works under IATF 16949 standards, while an aerospace variant (T095) works under AS9100 with tighter tolerances. The base O\*NET scores were adjusted to reflect these real differences.

**Step 3 — Validated against real job postings.** I analyzed 1.3 million LinkedIn job postings using NLP, extracting 78,000 clean manufacturing posts. Where the job market showed a significant gap — for example, employers asking for more Programming skills than O\*NET suggested — the scores were calibrated upward.

---

## Why 36 Dimensions Instead of 87

Project 2 used 87 dimensions because it needed to calculate the precise *cost* of moving between occupations.

Project 3 has a different purpose: helping people *explore and compare* tasks. The 36 dimensions (12 Knowledge + 12 Skills + 12 Abilities) were chosen because each one clearly separates different types of manufacturing work:

- **Production knowledge** separates floor operators from office staff.
- **Troubleshooting skill** separates maintenance technicians from assemblers.
- **Manual Dexterity** separates hands-on trades from engineering roles.

Another key difference: Project 3 includes Knowledge because it answers "what should the training program cover?", whereas Project 2 focused on "how hard is this transition?".

---

## How Cross-Training Similarity Works

When you add tasks to the Cart, the tool calculates similarity using **cosine similarity** — a measure of whether two profiles have the same shape.

- **Project 2 measured distance** — how *hard* it is to move between occupations.
- **Project 3 measures similarity** — how much two tasks *overlap* in what they demand.

| Similarity | Color | What it means |
|---|---|---|
| 90% or higher | Green | Very similar profiles — a single training program can cover both tasks |
| 75% to 89% | Yellow | Moderate overlap — a structured cross-training program over several months |
| Below 75% | Red | Different profiles — treat as separate hiring or training needs |

Even when two tasks show 90%+ similarity, the tool displays the top 3 KSA dimensions where they differ most — so you know exactly what to focus cross-training on.

---

## What the Tool Does

The tool has three sections on a single page:

**1. JD Matcher** — Describe a task or paste keywords from a job description at the top. The tool extracts technical terms (CNC, PLC, SCADA, FMEA), scores all 191 tasks by relevance, and shows the top 25 matches with keywords highlighted.

**2. Task Inventory** — Browse all 191 tasks using filters for industry (6 options) and department (6 options). Click "▶ Details" to expand the full KSA profile.

**3. Cart → Analysis** — Add tasks to save them (up to 10). When tasks are added, an Analysis panel appears:

| Section | What it shows | How to use it |
|---|---|---|
| **Common KSA Profile** | Average top 5 K, S, and A across selected tasks | Design interview questions around these specific competencies |
| **KSA Distance Matrix** | Cosine similarity matrix + top 3 KSA gaps per pair | Find which transitions are easy vs. expensive |
| **Training Gap Analysis** | Training hours, tech complexity, and standards matrix | Estimate onboarding investment and certification needs |

---

## Ways HR Professionals Use This

**Hiring for new lines:** Transform vague JDs into specific KSA benchmarks (e.g., "Operations Monitoring: 4.5").

**Cross-training planning:** Instantly visualize realistic transitions and identify critical skill gaps to focus training.

**Retirement prep:** Add a retiring veteran's tasks to the Cart to see exactly what competencies are at risk and find the closest internal candidates to fill the "Mentorship Vacuum."

---

## Industries and Departments

### Industries (6)

| Industry | Tasks | Key Standards |
|---|---|---|
| Automotive | 43 | IATF 16949, VDA 6.3, CQI-15 |
| EV Battery | 31 | IEC 62660, UN 38.3, ISO 6469 |
| Solar | 18 | IEC 61215, IEC 61730, UL 1741 |
| Aerospace | 32 | AS9100, NADCAP, AWS D17.1 |
| Nuclear | 14 | 10 CFR 50, ASME NQA-1, ISO 19443 |
| General Mfg | 53 | ISO 9001, CQI-9/11/12, IPC-A-610 |

### Departments (6)

| Department | Who works here |
|---|---|
| Production Floor | Operators, assemblers, welders, maintenance |
| Engineering | Design, process, quality, and test engineers |
| Quality & Safety | Inspectors, auditors, EHS, NDT technicians |
| Logistics | Planners, coordinators, warehouse, shipping |
| Office & Admin | Plant managers, HR, program managers |
| IT & Automation | PLC/SCADA, MES, ERP, data science |

---

## Data Sources

| Source | What was extracted | How it is used |
|---|---|---|
| **O\*NET 30.0** | Importance ratings (1-5) | Foundation for each task's 36-dimension KSA profile |
| **ESCO v1.2** | European occupation codes | Mapped for international comparability |
| **OSHA IIF** | TRIR and DART injury rates | Industry-level safety baseline |
| **DOL RAPIDS** | Training hour standards | Classifies training pathways (OJT, Apprenticeship) |
| **LinkedIn NLP** | 78K manufacturing job posts | Validates KSA scores against real employer demand |

---

## KSA Dimensions (36 total)

**Knowledge (12):** Production, Mechanical, Engineering, Mathematics, Computers, English, Administration, Customer Service, Safety, Chemistry, Design, Physics

**Skills (12):** Operations Monitoring, Quality Control, Maintenance, Troubleshooting, Critical Thinking, Problem Solving, Active Listening, Reading, Writing, Math, Programming, Systems Analysis

**Abilities (12):** Manual Dexterity, Arm-Hand Steadiness, Near Vision, Perceptual Speed, Deductive Reasoning, Information Ordering, Oral Expression, Written Comprehension, Math Reasoning, Visualization, Reaction Time, Control Precision

---

## tasks.json Schema

| Field | Type | Description |
|---|---|---|
| `id` | string | Task identifier (T001–T191) |
| `dept` | string | Department (FLOOR, ENGINEERING, etc.) |
| `soc` | string | O\*NET SOC code |
| `task` | string | Full task description |
| `hazard` | string | Risk level: LOW, MEDIUM, HIGH, CRITICAL |
| `k`, `s`, `a` | object | KSA scores (12 dimensions each, 1-5) |
| `trainHours` | int | DOL-based estimated training hours |

---

## Setup

```bash
git clone https://github.com/yechansota/TaskInventory_KSA_Analyzer.git
cd TaskInventory_KSA_Analyzer
python build.py
```

- `python build.py` : Build the HTML file.
- `python build.py stats` : Print task statistics.
- `python build.py validate` : Check data integrity.

---

## Limitations

### 1. Safety Rates Are Reported at the Industry Level

OSHA publishes TRIR/DART rates by industry, not task. To address this, each task carries a **Hazard Level** (LOW to CRITICAL) based on the specific process.

### 2. Standard Badges Are Indicative

The ISO/IATF badges show what *typically* applies. Actual certification requirements depend on specific employers and regulations.
