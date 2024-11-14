import streamlit as st
import requests

def get_prediction(experience):
    url = "http://127.0.0.1:8000/predict"  
    payload = {"experience": experience}
    try:
        response = requests.post(url, json=payload)
        return response.json() 
    except requests.exceptions.RequestException as e:
        st.error(f"Error in API request: {e}")
        return None

def main():
    st.title("Experience Prediction App")

    experience = st.number_input("Enter your experience (in years)", min_value=0, max_value=50, step=1)

    if st.button("Submit"):
        if experience >= 0:
            st.write(f"Predicting result for {experience} years of experience...")
            result = get_prediction(experience)

            if result:
                st.write("Prediction Result:")
                st.text(result) 
        else:
            st.error("Please enter a valid experience.")

if __name__ == "__main__":
    main()
