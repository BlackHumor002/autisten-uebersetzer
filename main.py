import streamlit as st
from openai import OpenAI

# 1. Konfiguration
st.set_page_config(page_title="Autisten-Übersetzer", page_icon="🧩")

# Sidebar für die Kanal-Werbung
st.sidebar.title("Über den Erfinder")
st.sidebar.write("Ich baue solche Tools, während ich mich auf mein Abi vorbereite.")
st.sidebar.markdown("### Folgt meinem Kanal für mehr:")
st.sidebar.subheader("📺 SchwarzerHumorTV")
st.sidebar.write("Wenn ihr meinen Weg zum Studium und weitere Projekte sehen wollt, abonniert mich!")
st.sidebar.markdown("---")
st.sidebar.info("Viel Erfolg beim Subtext knacken!")

# Hauptbereich
st.title("🧩 Der Autisten-Übersetzer")

# 2. API-Key aus den Secrets laden
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except Exception:
    st.error("❌ OpenAI API-Key nicht gefunden. Bitte prüfe die Secrets!")
    st.stop()

# 3. Eingabe
user_input = st.text_area("Was hat die Person geschrieben / gesagt?", height=150)

# 4. Logik
if st.button("Subtext knacken 🚀"):
    if not user_input.strip():
        st.warning("⚠️ Bitte gib Text ein.")
    else:
        with st.spinner("Analysiere..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Du bist der 'Autismus-Übersetzer'. Analysiere den Subtext (Fassade, Realität, Nächster Zug). Antworte direkt und logisch."},
                        {"role": "user", "content": user_input}
                    ]
                )
                st.success("Analyse abgeschlossen!")
                st.markdown("---")
                st.markdown(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Fehler: {e}")
