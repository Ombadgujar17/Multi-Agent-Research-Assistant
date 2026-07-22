import streamlit as st

from api import research

st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🔍",
)

st.title("🔍 Multi-Agent Research Assistant")

query = st.text_input(
    "Enter your research topic"
)

if st.button("Research"):

    if not query.strip():
        st.warning("Please enter a topic.")
        st.stop()

    with st.spinner("Researching..."):

        result = research(query)

    st.success("Done!")

    st.markdown(result["report"])

    with st.expander("Summary"):
        st.write(result["summary"])

    with st.expander("Sources"):
        for source in result["sources"]:
            st.markdown(
                f"- [{source['title']}]({source['url']})"
            )