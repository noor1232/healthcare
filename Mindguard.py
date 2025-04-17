import streamlit as st

# Define bilingual questions and choices
questions = {
    "Q1": {
        "question": "How often do you feel sad or hopeless? | आपण किती वेळा दु:खी किंवा निराश वाटता?",
        "choices": [
            "Never | कधीच नाही",
            "Rarely | क्वचितच",
            "Sometimes | कधी कधी",
            "Often | वारंवार",
            "Always | नेहमीच"
        ]
    },
    "Q2": {
        "question": "Do you have trouble sleeping? | आपल्याला झोपण्यास अडचण येते का?",
        "choices": [
            "Never | कधीच नाही",
            "Rarely | क्वचितच",
            "Sometimes | कधी कधी",
            "Often | वारंवार",
            "Always | नेहमीच"
        ]
    },
    "Q3": {
        "question": "Do you experience excessive worry or anxiety? | आपल्याला खूप काळजी किंवा चिंतेचा अनुभव येतो का?",
        "choices": [
            "Never | कधीच नाही",
            "Rarely | क्वचितच",
            "Sometimes | कधी कधी",
            "Often | वारंवार",
            "Always | नेहमीच"
        ]
    },
    "Q4": {
        "question": "Do you feel tired or fatigued most of the time? | आपल्याला बहुतेक वेळा थकवा किंवा दमल्यासारखे वाटते का?",
        "choices": [
            "Never | कधीच नाही",
            "Rarely | क्वचितच",
            "Sometimes | कधी कधी",
            "Often | वारंवार",
            "Always | नेहमीच"
        ]
    },
    "Q5": {
        "question": "Do you have trouble concentrating or making decisions? | लक्ष केंद्रित करण्यात किंवा निर्णय घेण्यात अडचण येते का?",
        "choices": [
            "Never | कधीच नाही",
            "Rarely | क्वचितच",
            "Sometimes | कधी कधी",
            "Often | वारंवार",
            "Always | नेहमीच"
        ]
    },
    "Q6": {
        "question": "How often do you experience irritability or anger? | आपल्याला चिडचिड किंवा राग किती वेळा येतो?",
        "choices": [
            "Never | कधीच नाही",
            "Rarely | क्वचितच",
            "Sometimes | कधी कधी",
            "Often | वारंवार",
            "Always | नेहमीच"
        ]
    },
    "Q7": {
        "question": "Do you isolate yourself from others frequently? | आपण स्वतःला इतरांपासून वारंवार वेगळे ठेवता का?",
        "choices": [
            "Never | कधीच नाही",
            "Rarely | क्वचितच",
            "Sometimes | कधी कधी",
            "Often | वारंवार",
            "Always | नेहमीच"
        ]
    },
    "Q8": {
        "question": "Do you engage in self-destructive behaviors? | आपण स्वत:ला हानी पोहोचवणाऱ्या वागणुकीत सामील होता का?",
        "choices": [
            "Never | कधीच नाही",
            "Rarely | क्वचितच",
            "Sometimes | कधी कधी",
            "Often | वारंवार",
            "Always | नेहमीच"
        ]
    },
    "Q9": {
        "question": "Do you feel hopeless about the future? | आपल्याला भविष्यासाठी निराशा वाटते का?",
        "choices": [
            "Never | कधीच नाही",
            "Rarely | क्वचितच",
            "Sometimes | कधी कधी",
            "Often | वारंवार",
            "Always | नेहमीच"
        ]
    },
    "Q10": {
        "question": "Have you lost interest in activities you once enjoyed? | आपल्याला पूर्वी आवडलेल्या गोष्टींमध्ये आता रस वाटत नाही का?",
        "choices": [
            "Never | कधीच नाही",
            "Rarely | क्वचितच",
            "Sometimes | कधी कधी",
            "Often | वारंवार",
            "Always | नेहमीच"
        ]
    }
}


def analyze_responses(responses):
    score = 0
    for response in responses.values():
        if "Often" in response or "Always" in response or "वारंवार" in response or "नेहमीच" in response:
            score += 1

    if score >= 4:
        return (
            "⚠️ You may be experiencing significant mental health issues. It is advisable to seek professional help.\n\n"
            "⚠️ आपण गंभीर मानसिक आरोग्य समस्यांचा सामना करत आहात. कृपया व्यावसायिक सल्ला घ्या.",
            "💡 Seek professional help like counseling or therapy. Engage in relaxation techniques, get proper sleep and social support.\n\n"
            "💡 समुपदेशन (counseling) किंवा मानसोपचारतज्ज्ञांचा सल्ला घ्या. ध्यान, व्यायाम आणि झोपेची काळजी घ्या."
        )
    elif score == 2 or score == 3:
        return (
            "😐 You may be experiencing mild mental health issues. Consider taking care of yourself and seek support if needed.\n\n"
            "😐 आपण सौम्य मानसिक आरोग्य समस्यांचा सामना करत आहात. स्वतःची काळजी घ्या आणि आवश्यक असल्यास मदत घ्या.",
            "💡 Practice self-care like exercise, meditation, hobbies, and spending time with loved ones.\n\n"
            "💡 व्यायाम, ध्यान, छंद जोपासा आणि प्रियजनांसोबत वेळ घालवा."
        )
    else:
        return (
            "✅ Your mental health seems to be stable. Keep practicing self-care.\n\n"
            "✅ आपले मानसिक आरोग्य स्थिर वाटते. स्वत:ची काळजी घेत राहा.",
            "💡 Continue good habits, eat well, sleep well, and maintain social connections.\n\n"
            "💡 चांगल्या सवयी जपा, सकस आहार घ्या, पुरेशी झोप घ्या आणि सामाजिक नाती जपा."
        )


# Streamlit UI
st.set_page_config(page_title="MindGuard", layout="centered")

st.markdown("""
    <style>
        .background {
            background-image: url("https://media.tenor.com/VW7r4lcGlvMAAAAM/happy-hogging-thumbs-up.gif");
            background-size: cover;
            height: 100%;
            width: 100%;
            position: absolute;
        }
    </style>
    """, unsafe_allow_html=True)
st.markdown('<div class="background">', unsafe_allow_html=True)

c1, c2 = st.columns([30, 50])
c2.title("🧠 MindGuard: Psychological Condition Assessment Test | मानसिक आरोग्य मूल्यांकन चाचणी")
c1.image("logo-removebg-preview.png")

responses = {}
for qid, data in questions.items():
    st.markdown(f"**{qid}: {data['question']}**")
    responses[qid] = st.radio("Choose your answer | तुमचे उत्तर निवडा", data["choices"], key=qid)

if st.button("✅ Submit | सबमिट करा"):
    status, solution = analyze_responses(responses)
    st.markdown("### 🧾 Mental Health Status | मानसिक आरोग्य स्थिती")
    st.info(status)
    st.markdown("### 💡 Suggested Solution | सुचवलेले उपाय")
    st.success(solution)
