import streamlit as st
import create_jsonl as cj

if __name__ == "__main__":
    with st.sidebar:
        st.header('How To Use')
        st.write('**1)** Select the roll you want and write your content for that roll')
        st.write('**2)** Enter your content for that roll')
        st.write("**3) When you are done, click 'append line to messages'")
        st.write('**4)** repeate steps 1-3 as many times as necessary')
        st.write("**5)** finally, click 'append messages to JSON file' and repeate all steps until your file is complete")
        st.write()
        st.write('Check out my github [here](https://github.com/brianSalk/JSONLgenerator3.5)')
        
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
