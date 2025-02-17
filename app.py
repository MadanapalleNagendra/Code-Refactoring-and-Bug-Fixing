import streamlit as st

# Store notes in session state so they persist across interactions
if "notes" not in st.session_state:
    st.session_state.notes = []

# Streamlit App UI
st.title("Note Taking Application")

# Form to add a note
with st.form("note_form"):
    note = st.text_input("Add a Note:")
    submitted = st.form_submit_button("Add Note")

    if submitted and note:
        st.session_state.notes.append(note)  # Add note to session state
        st.success("Note added successfully!")

# Display all notes
st.subheader("Your Notes:")
if st.session_state.notes:
    for idx, note in enumerate(st.session_state.notes, 1):
        st.write(f"{idx}. {note}")
else:
    st.write("No notes added yet.")
