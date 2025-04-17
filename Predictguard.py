import streamlit as st
import google.generativeai as genai

# UI layout
c1, c2 = st.columns([30, 50])
c2.title("PredictGuard: Predicting the disease based on symptoms")
c1.image("logo-removebg-preview.png")

# API key setup
genai.configure(api_key="AIzaSyDcpeye8nmcA_9BnbVvzbz1bv9-ooc2pLM")

# Create Gemini model
def create_gen_model():
    return genai.GenerativeModel('models/gemini-1.5-pro')

# Main logic
def main():
    query = st.chat_input("Enter the Symptoms:")
    if query:
        model = create_gen_model()

        # Single prompt asking for disease, causes, precautions, meds in both English and Marathi
        full_prompt = f"""
        I have the following symptoms: {query}.

        1. Predict the most likely disease. Just mention the name of the disease.
        2. Suggest possible causes.
        3. Suggest precautions to take.
        4. Suggest general medications (if available).

        After providing all this information in **English**, also provide the same details in **Marathi** below it.

        Format:

        Disease:\n
        Causes:\n
        Precautions:\n
        Medications:\n

        रोग:\n
        कारणे:\n
        खबरदारी:\n
        औषधे:\n
        """

        # Safe response generation with error handling
        try:
            response = model.generate_content(full_prompt)
            if response:
                st.subheader("Predictions")
                st.markdown(response.text)
        except Exception as e:
            st.error("⚠️ API error: You may have hit your rate limit or quota. Please wait and try again.")
            st.code(str(e), language='bash')

# Run the app
if __name__ == "__main__":
    main()
