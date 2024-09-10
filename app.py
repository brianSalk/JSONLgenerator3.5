import streamlit as st
import create_jsonl as cj

if __name__ == "__main__":
    if "messages" not in st.session_state:
        messages = []
        st.session_state["messages"] = messages
    if "next_message" not in st.session_state:
        st.session_state["next_message"] = []
    st.title("Create JSONL for GPT3.5 and newer")
    # role radio must be above form because it resets value each time if its in the form
    role = st.radio("role", ["system", "user", "assistant"], horizontal=True, index=0)
    with st.form("main_form", clear_on_submit=True):
        next_line = st.text_input(
            "content", placeholder="Enter content here", key="content"
        )
        submitted = st.form_submit_button("Append line to messages", disabled=not role)
        if submitted:
            st.session_state["next_message"].append([role, next_line])
        st.write("current messages array:")
        st.code(st.session_state["next_message"])
    if st.button(
        "Append Messages to JSONL file", disabled=not st.session_state["next_message"]
    ):
        st.session_state["messages"].append(st.session_state["next_message"])
        st.session_state["next_message"] = []

    st.subheader(
        ":point_down: :point_down: Your JSONL file is here :point_down: :point_down: "
    )
    st.code(cj.create_json_from_lines(st.session_state["messages"]))
