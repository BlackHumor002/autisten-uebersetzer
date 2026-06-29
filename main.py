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
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("❌ API-Key nicht gefunden. Bitte überprüfe die Streamlit Secrets.")
    st.stop()

# 3. Eingabebereich für den Nutzer
user_input = st.text_area(
    "Was hat die Person geschrieben / gesagt?",
    placeholder="Z.B.: 'Klar wir können uns gern treffen, aber heute nicht'",
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
    "### 3. Dein nächster Zug (Logische Handlungsempfehlung)\n\n"
    "Hier ist die Aussage, die du analysieren sollst:\n"
)

# 5. Logik beim Klick auf den Button
if st.button("Subtext knacken 🚀", use_container_width=True):
    if not user_input.strip():
        st.warning("⚠️ Bitte gib zuerst einen Text ein, den ich übersetzen soll.")
    else:
        with st.spinner("Analysiere neurotypische Verhaltensmuster... Bitte warten."):
            try:
                # Wir nutzen das bewährte, absolut stabile "gemini-pro" Modell
                model = genai.GenerativeModel('gemini-pro')

                # Wir kleben deine Anweisung und die Eingabe des Nutzers einfach aneinander!
                full_text_to_analyze = system_prompt + f'"{user_input}"'

                # Anfrage an die KI senden
                response = model.generate_content(full_text_to_analyze)

                # Antwort ausgeben
                st.success("Analyse abgeschlossen!")
                st.markdown("---")
                st.markdown(response.text)

            except Exception as e:
                st.error(f"Fehler bei der API-Abfrage: {e}")
