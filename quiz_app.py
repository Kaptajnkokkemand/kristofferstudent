import streamlit as st

# App konfiguration
st.set_page_config(page_title="Kristoffers Studentergave 🎓", page_icon="🎓")

# Farver og stil
st.markdown(
    """
    <style>
    .big-font {
        font-size:28px !important;
        color: #C1121F;
    }
    .emoji {
        font-size: 24px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Titel og intro
st.markdown('<p class="big-font">🎓 Tillykke med huen, Kristoffer! 🎓</p>', unsafe_allow_html=True)
st.image("https://upload.wikimedia.org/wikipedia/commons/1/15/Dansk_student_hue.png", width=150)
st.write("Tillyke med huen Kristoffer")
st.write("Velkommen til din helt egen quiz – en lille del af din studentergave fra Asbjørn, Ulla og Niels. 🎁")
st.write("Vi er glade for, at du har gennemført gymnasiet og har klaret dig godt! 👏")

# Introslider
gladhed = st.slider("På en skala fra 1-10, hvor glad er du for at være færdig med gymnasiet? 🎓", 1, 10)

# Dynamisk respons baseret på valg
if gladhed < 5:
    st.write("😅 Hmm... du kunne vist godt være lidt gladere.")
elif 5 <= gladhed <= 7:
    st.write("😊 Det lyder som en lettelse – godt gået!")
else:
    st.write("🎉 Fantastisk! Det har du også fortjent.")

st.markdown("---")

# Spørgsmål og svar
score = 0

st.subheader("Spørgsmål 1: Berserk")
q1 = st.radio(
    "Hvad hedder hovedpersonen i mangaen Berserk?",
    ["A) Guts", "B) Mogens", "C) Zodd", "D) Baruto"]
)
if q1.startswith("A"):
    score += 1

st.subheader("Spørgsmål 2: One Piece")
q2 = st.radio(
    "Hvad hedder skibet, som Luffy og hans besætning sejler med i starten af One Piece?",
    ["A) Red Force", "B) Thousand Sunny", "C) Going Merry", "D) Merry Go"]
)
if q2.startswith("C"):
    score += 1

st.subheader("Spørgsmål 3: Ado")
q3 = st.radio(
    "Hvilket gennembrudshit gjorde Ado kendt i Japan i 2020?",
    ["A) Cotten eye joe", "B) Usseewa", "C) Barbie Girl", "D) Kaze no Uta"]
)
if q3.startswith("B"):
    score += 1

st.subheader("Spørgsmål 4: Gaveindpakning")
q4 = st.number_input("Hvor mange møtrikker blev brugt i indpakningen?", min_value=0, max_value=100, step=1)
if q4 == 50:
    score += 1

st.subheader("Spørgsmål 5: Berserk – karakter")
q5 = st.radio(
    "Hvilken af disse karakterer i Berserk bliver kendt som “The White Hawk”?",
    ["A) Guts", "B) Skull Knight", "C) Griffith", "D) Serpico"]
)
if q5.startswith("C"):
    score += 1

st.markdown("---")

# Resultat
if st.button("🔐 Vis resultat"):
    st.subheader("🎉 Resultat 🎉")
    st.write(f"Du fik {score} ud af 5 rigtige!")
    
    if score >= 4:
        st.success("Tillykke – du har gennemført quizen! 🎉")

        st.markdown(
            """
Vi er glade for, at du har gennemført gymnasiet og har klaret dig godt – det er virkelig sejt gået.  
Gaven er fra os tre – **Ulla, Niels og Asbjørn** – og vi ønsker dig alt det bedste i det næste kapitel.

Uanset om fremtiden byder på en rejse til Japan eller et kørekort, så håber vi, du får et fantastisk sabbatår og et stærkt afsæt videre. 🌞✈️🚗

**TILLYKKE, Kristoffer!** 🎓🇩🇰❤️

Tak fordi du legede med – og tillykke igen fra os alle tre! 💸🎈
            """
        )
    else:
        st.warning("Hmm, prøv igen og se, om du kan få adgang til gaven... 😉")

