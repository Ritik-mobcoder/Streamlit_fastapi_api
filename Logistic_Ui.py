import streamlit as st
import requests


def get_prediction(pclass, sex, age, sibsp, parch, fare):
    url = "http://127.0.0.1:8000/titanic"
    payload = {
        "pclass": pclass,
        "sex": sex,
        "age": age,
        "sibsp": sibsp,
        "parch": parch,
        "fare": fare,
    }
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error in API request: {e}")
        return None


def main():
    st.title("Titanic Survival Prediction App")

    pclass = st.slider("Passenger Class", min_value=1, max_value=3, step=1, value=1)
    sex = st.selectbox("Sex", options=["male", "female"], index=0)
    age = st.slider("Age", min_value=0, max_value=100, step=1, value=30)
    sibsp = st.slider(
        "Number of Siblings/Spouses aboard", min_value=0, max_value=10, step=1, value=0
    )
    parch = st.slider(
        "Number of Parents/Children aboard", min_value=0, max_value=10, step=1, value=0
    )
    fare = st.slider("Fare", min_value=0.0, max_value=500.0, step=1.0, value=50.0)

    if st.button("Submit"):
        sex = 1 if sex == "male" else 0
        st.write(
            f"Predicting result for passenger details: {pclass}, {sex}, {age} years old, {sibsp} siblings/spouses, {parch} parents/children, fare of {fare}"
        )

        response = get_prediction(pclass, sex, age, sibsp, parch, fare)

        result = response["result"]

        if result:
            st.write(f"Prediction Result: {result}")

        else:
            st.error("Failed to retrieve prediction.")


if __name__ == "__main__":
    main()
