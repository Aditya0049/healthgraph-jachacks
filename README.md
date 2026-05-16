# HealthGraph 🩺

**JacHacks Spring - Consumer Healthcare Track**

HealthGraph is a virtual medical triage agent built natively in **Jaclang**, the world's first agentic programming language.

## Overview
HealthGraph uses graph-native data modeling and AI walkers to triage patients. By leveraging Jac's `Node`, `Walker`, and `by llm()` constructs, HealthGraph dynamically maps a patient's symptoms and traverses this graph to suggest potential diagnoses.

## How It Works
1. **Graph Nodes**: The system models `Patient`, `Symptom`, and `Diagnosis` as nodes.
2. **Walkers**:
   - `TriageAgent`: Starts at the root, spawns the patient, and (using LLMs) extracts structured symptoms from natural language, connecting them to the patient node.
   - `DiagnosticWalker`: Traverses the patient's symptom graph and evaluates the network to generate diagnoses.
3. **Frontend**: A simple Streamlit UI built in Python that interfaces with the Jac engine.

## Running Locally
1. Install Jaclang and dependencies:
   ```bash
   pip install jaclang streamlit
   ```
2. Run the Streamlit UI:
   ```bash
   streamlit run ui.py
   ```

## Jaclang Features Used
- **Graph Modeling**: Object-Spatial Programming (OSP) linking `Patient -> Symptom -> Diagnosis`.
- **Walkers**: Autonomous agents navigating the graph (`spawn`, `visit [-->]`).
- **Meaning-Typed Programming**: `by llm()` for parsing user input and generating medical insights.
