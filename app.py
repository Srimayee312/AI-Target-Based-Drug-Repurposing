import streamlit as st
from repurposing_engine import match_targets, calculate_score

st.title("AI-Based Drug Repurposing Platform")

st.write("This demo identifies FDA-approved drugs targeting selected disease proteins.")

disease_targets = ["EGFR", "BRCA1"]

drug_data = [
    {"name": "DrugA", "target": "EGFR", "target_score": 0.9, "evidence_score": 0.8},
    {"name": "DrugB", "target": "TP53", "target_score": 0.7, "evidence_score": 0.6},
    {"name": "DrugC", "target": "BRCA1", "target_score": 0.85, "evidence_score": 0.75},
]

if st.button("Find Repurposable Drugs"):
    matches = match_targets(disease_targets, drug_data)

    for drug in matches:
        score = calculate_score(drug)
        st.write(f"Drug: {drug['name']}")
        st.write(f"Target: {drug['target']}")
        st.write(f"Repurposing Confidence Score: {score}")
        st.write("---")