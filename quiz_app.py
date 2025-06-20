import streamlit as st

st.title("🎉 Gæt & Vind!")

name = st.text_input("Hvad er dit navn?")
q1 = st.radio("Hvilken farve har himlen normalt?", ["Grøn", "Blå", "Rød"])
q2 = st.radio("Hvor mange ben har en edderkop?", ["6", "8", "10"])

if st.button("Tjek dine svar"):
    if q1 == "Blå" and q2 == "8":
        st.success(f"Tillykke {name}! Du har vundet en overraskelse 🥳")
    else:
        st.error("Ups! Det var ikke helt rigtigt. Prøv igen.")