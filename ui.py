import streamlit as st
import subprocess
import os

st.set_page_config(page_title="HealthGraph", page_icon="🩺")

st.title("🩺 HealthGraph: AI Medical Triage Agent")
st.markdown("Built with **Jaclang** for JacHacks Spring. Uses graph-native data modeling and AI agents.")

st.sidebar.header("Patient Profile")
name = st.sidebar.text_input("Name", "John Doe")
age = st.sidebar.number_input("Age", 30)

st.subheader("Describe Symptoms")
patient_input = st.text_area("Tell the agent how you are feeling:", 
                             "I have had a severe headache for 3 days and a mild fever.")

if st.button("Run Diagnostic Agent"):
    st.info("Agent is traversing the knowledge graph...")
    
    # Run the jac main.jac file via subprocess, passing input as env var
    env = os.environ.copy()
    env["PATIENT_INPUT"] = patient_input
    
    result = subprocess.run(
        ["jac", "run", "main.jac"], 
        capture_output=True, 
        text=True, 
        env=env
    )
    
    if result.returncode == 0:
        st.success("Analysis Complete!")
        
        output_lines = result.stdout.strip().split('\n')
        
        # Parse output for display
        st.markdown("### 🔍 Agent Traversal Log")
        log_text = ""
        diagnoses = []
        
        for line in output_lines:
            if "Added Diagnosis:" in line:
                diagnoses.append(line.replace("Added Diagnosis: ", ""))
            else:
                log_text += f"{line}\n"
                
        with st.expander("View Internal Agent Traversal Log"):
            st.code(log_text)
            
        st.markdown("### 📋 Final Diagnostic Report")
        if diagnoses:
            for d in diagnoses:
                st.success(d)
        else:
            st.warning("No clear diagnosis could be determined.")
            
    else:
        st.error("Error executing agent:")
        st.code(result.stderr)
