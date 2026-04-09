# Data Sources

**You do not need to download these files to use the tool** — all processed data is already in `tasks.json`. This documentation exists for academic reproducibility.

---

## Source Files (8 sources)

### 1. O*NET 30.0
- **Download:** https://www.onetcenter.org/database.html#individual-files
- **Format:** CSV/Excel — **License:** CC-BY 4.0
- **Extracted:** Importance ratings (1–5) for 12 Knowledge, 12 Skills, 12 Abilities per SOC code
- **Processing:** Filtered to manufacturing SOC codes, mapped to 191 tasks

### 2. BLS OES May 2024
- **Download:** https://www.bls.gov/oes/special-requests/oesm24all.zip
- **Format:** ZIP (Excel) — **License:** Public Domain
- **Extracted:** Employment counts and median annual wages by SOC code

### 3. ESCO v1.2
- **Download:** https://esco.ec.europa.eu/en/use-esco/download
- **Format:** CSV — **License:** EU Open Data
- **Extracted:** ESCO occupation codes and titles
- **Processing:** Cross-referenced to O\*NET SOC codes for international comparability

### 4. OSHA IIF
- **Download:** https://www.bls.gov/iif/home.htm → Table R8
- **Format:** Excel — **License:** Public Domain
- **Extracted:** TRIR and DART rates by NAICS industry code

### 5. OSHA 300 Log
- **Download:** https://www.osha.gov/Establishment-Specific-Injury-and-Illness-Data
- **Format:** CSV — **License:** Public Domain
- **Extracted:** Establishment-level injury data for cross-validation

### 6. DOL RAPIDS
- **Download:** https://www.apprenticeship.gov/data-and-statistics
- **Format:** CSV/Excel — **License:** Public Domain
- **Extracted:** Training hour standards and program types by occupation

### 7. Industry Standards
- IATF/VDA/CQI/AIAG (Automotive), AS9100/NADCAP (Aerospace), IEC 62660/UN 38.3 (Battery), 10 CFR/NQA-1 (Nuclear)
- **License:** Proprietary (referenced, not reproduced)

### 8. LinkedIn 1.3M Job Postings
- **Download:** https://www.kaggle.com/datasets/asaniczka/1-3m-linkedin-jobs-and-skills-2024
- **Format:** CSV (~5GB) — **License:** Kaggle Terms (cannot redistribute)
- **Extracted:** 78K clean manufacturing posts via NLP pipeline (21 CSVs)
- **Processing:** Used to validate and calibrate O\*NET KSA scores against real-world demand

---

## Why raw files are not included

| Reason | Details |
|---|---|
| Size | LinkedIn dataset is ~5GB |
| License | LinkedIn/Kaggle data cannot be redistributed |
| Not needed | All processed data is in `tasks.json` (272KB) |
