import streamlit as st
import time
import pandas as pd
import numpy as np

def display_image(image_path):
    """
    Displays the image in the center of the app with a reduced size.
    """
    try:
        st.image(image_path, width=400, caption="Sarthana UPSC Preparation Hub")  # Reduce image size to 400px width
    except:
        st.write("Could not find or load image")

def main():
    # Initialize session state for performance tracking
    if 'start_time' not in st.session_state:
        st.session_state.start_time = time.time()
        st.session_state.page_loads = 0
        st.session_state.total_time_on_page = 0
        st.session_state.mock_test_data = pd.DataFrame({
          'Test ID': ['Test 1', 'Test 2', 'Test 3'],
          'Score': [75, 82, 68],
          'Time Taken (minutes)': [120, 110, 130]
        })

    #Display the image first
    image_path = r"sarthana.png"  # Ensure the correct path to the image
    display_image(image_path)

    # Increment page load count
    st.session_state.page_loads += 1

    # Track time spent on the page so far
    elapsed_time = time.time() - st.session_state.start_time
    st.session_state.total_time_on_page += elapsed_time

    # App title and description
    st.title("UPSC Preparation Hub")

    st.write("""
        Welcome to the **UPSC Preparation Hub**! This platform is designed to assist you in preparing for the UPSC exams.
        You can stay updated with **Current Affairs**, summarize important topics, practice **Mock Tests**, save and manage **Notes**, and even work on **Essay Writing** to boost your performance in the UPSC Mains.
    """)

    # Performance Analytics Section
    st.header("Performance Analytics")

    # Display page load count
    st.write(f"**Page Loads:** {st.session_state.page_loads}")

    # Display total time on page
    st.write(f"**Total Time on Page:** {st.session_state.total_time_on_page:.2f} seconds")

    # Display Mock Test Performance
    st.subheader("Mock Test Performance")
    st.write("Here's a summary of your mock test performance:")
    st.dataframe(st.session_state.mock_test_data)

    # Example: Add a random mock test score
    if st.button("Add New Mock Test Result"):
      new_id = "Test " + str(len(st.session_state.mock_test_data)+1)
      new_score = np.random.randint(50,100)
      new_time = np.random.randint(90, 150)
      new_data = pd.DataFrame({'Test ID': [new_id], 'Score':[new_score],'Time Taken (minutes)': [new_time]})
      st.session_state.mock_test_data = pd.concat([st.session_state.mock_test_data, new_data], ignore_index=True)
      st.experimental_rerun()

    # Reset start time after tracking it
    st.session_state.start_time = time.time()


if __name__ == "__main__":
    main()
