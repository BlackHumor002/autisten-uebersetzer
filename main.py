import streamlit as st
import google.generativeai as genai

# 1. Konfiguration der Webseite
st.set_page_config(page_title="Autisten-Übersetzer", page_icon="🧩", layout="centered")

st.title("🧩 Der Autisten-Übersetzer")
st.write(
    "Schluss mit verwirrenden Signalen. Kopiere hier Nachrichten, Floskeln oder Dating-Chats "
    "von neurotypischen Menschen rein, um den echten, ungeschönten Subtext zu erfahren."
)

# 2. API-Key sicher und unsichtbar laden
# Da der Key sicher in den Streamlit-Secrets liegt, brauchen die Nutzer ihn nicht mehr einzugeben.
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("❌ API-Key nicht gefunden. Bitte überprüfe die Streamlit Secrets.")
    st.stop()

# 3. Eingabebereich für den Nutzer
user_input = st.text_area(
    "Was hat die Person geschrieben / gesagt?",
    placeholder="Z.B.: 'Wir müssen uns voll gerne mal wieder treffen!' oder 'Mir geht's gut...'",
    height=150
)

# 4. Der System-Prompt (Das Regelwerk für die KI)
system_prompt = (
    "Du bist der 'Autismus-Übersetzer'. Deine Aufgabe ist es, Chatverläufe und Aussagen von "
    "neurotypischen Menschen zu analysieren. Lege den Fokus auf versteckten Subtext, indirekte Botschaften, "
    "höfliche Lügen, verdeckte Absichten, Manipulation oder Dating-Spielchen. "
    "Erkläre dem Nutzer absolut direkt, logisch, ohne soziale Schnörkel und mit einer Prise trockenem/schwarzem Humor, "
    "was die Person wirklich meint und wie er sich verhalten sollte.\n\n"
    "Strukturiere deine Antwort IMMER in diesen drei Abschnitten:\n"
    "### 1. Die Fassade (Was gesagt wurde)\n"
    "### 2. Die Realität (Was wirklich gemeint ist - der Subtext)\n"
    "### 3. Dein nächster Zug (Logische Handlungsempfehlung)"
)

# 5. Logik beim Klick auf den Button
if st.button("Subtext knacken 🚀", use_container_width=True):
    if not user_input.strip():
        st.warning("⚠️ Bitte gib zuerst einen Text ein, den ich übersetzen soll.")
    else:
        with st.spinner("Analysiere neurotypische Verhaltensmuster... Bitte warten."):
            try:
                # Hier nutzen wir jetzt den zukunftssicheren Alias "gemini-flash"!
                model = genai.GenerativeModel(
                    model_name='gemini-flash',
                    system_instruction=system_prompt
                )

                # Anfrage an die KI senden
                response = model.generate_content(user_input)

                # Antwort ausgeben
                st.success("Analyse abgeschlossen!")
                st.markdown("---")
                st.markdown(response.text)

            except Exception as e:
                st.error(f"Fehler bei der API-Abfrage: {e}")
