import streamlit as st
import google.generativeai as genai

# Layout setup
c1, c2 = st.columns([30, 50])
c2.title("MedGuard: Medicine Info & Alternatives ")
c1.image("logo-removebg-preview.png")

# Configure Gemini API
genai.configure(api_key="AIzaSyDcpeye8nmcA_9BnbVvzbz1bv9-ooc2pLM")  # 🔐 Replace with your actual key

# Create model
def create_gen_model():
    return genai.GenerativeModel('models/gemini-1.5-pro')

# Translate text to Marathi using Gemini
def translate_to_marathi(text, model):
    prompt = f"Translate the following medical content to Marathi:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text if response and response.text else "Translation unavailable."

# Main app
def main():
    medicine_name = st.chat_input("Enter the Medicine Name:")
    
    if medicine_name:
        model = create_gen_model()

        # 🩺 Step 1: Get medicine information in English
        prompt_info = (
            f"Can you provide detailed information about the medicine called {medicine_name}? "
            f"Include the uses, side effects, and any important information related to the medicine."
        )
        response_info = model.generate_content(prompt_info)
        english_info = response_info.text

        st.header("Medicine Information :")
        st.write(english_info)

        # 🌐 Translate to Marathi
        marathi_info = translate_to_marathi(english_info, model)
        st.subheader("औषधाची माहिती :")
        st.write(marathi_info)

        # 🔁 Step 2: Get alternative suggestions
        prompt_alt = (
            f"Please provide a list of alternative medicines that share the same active ingredients as {medicine_name}. "
            f"Ensure that the alternatives have the similar medicinal content. Suggest antibiotics first and then Ayurvedic alternatives if available."
        )
        response_alt = model.generate_content(prompt_alt)
        english_alt = response_alt.text

        st.header("Alternative Medicines :")
        st.write(english_alt)

        # 🌐 Translate to Marathi
        marathi_alt = translate_to_marathi(english_alt, model)
        st.subheader("पर्यायी औषधे :")
        st.write(marathi_alt)

# Run the app
if __name__ == "__main__":
    main()
