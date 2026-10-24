
import streamlit as st
import subprocess
import sys


st.set_page_config(
    page_title="OpenSource Scout",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 OpenSource Scout")
st.subheader("Discover Open-Source Projects with AI")

st.write(
    "Find GitHub repositories related to your interests "
    "and explore AI-generated summaries."
)

topic = st.text_input(
    "What would you like to explore?",
    placeholder="e.g., machine learning"
)

if st.button("Discover Projects"):
    if topic.strip():
        with st.spinner("Searching for repositories..."):
            try:
                result = subprocess.run(
                    [sys.executable, "search_repositories.py"],
                    input=topic + "\n",
                    capture_output=True,
                    text=True,
                    timeout=120
                )

                if result.returncode == 0:
                    st.success("Search completed!")
                    st.markdown("### 🤖 AI Report")
                    st.write(result.stdout)
                else:
                    st.error("Something went wrong.")
                    st.code(result.stderr)

            except subprocess.TimeoutExpired:
                st.error("The search took too long. Please try again.")

    else:
        st.warning("Please enter a topic first.")

st.divider()
st.caption("OpenSource Scout | Python • GitHub API • AI")