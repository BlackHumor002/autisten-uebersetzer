import streamlit as st
from openai import OpenAI

# 1. Konfiguration der Webseite
st.set_page_config(page_title="Autisten-Übersetzer", page_icon="🧩", layout="centered")

st.title("🧩 Der Autisten-Übersetzer")
st.write(
    "Schluss mit verwirrenden Signalen. Kopiere hier Nachrichten, Floskeln oder Dating-Chats "
    "von neurotypischen Menschen rein, um den echten, ungeschönten Subtext zu erfahren."
)

# 2. Sidebar für den API-Key (Sicherheit & Flexibilität)
st.sidebar.header("⚙️ Einstellungen")
api_key = st.sidebar.text_input("OpenAI API Key eingeben:", type="password",
                                help="Deinen API-Key findest du im OpenAI Dashboard.")
st.sidebar.markdown("---")
st.sidebar.write("💡 *Hinweis: Dein Key wird nirgendwo gespeichert, sondern nur für diese Sitzung verwendet.*")

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
    if not api_key:
        st.error("❌ Bitte gib zuerst deinen OpenAI API Key in der linken Sidebar ein!")
    elif not user_input.strip():
        st.warning("⚠️ Bitte gib zuerst einen Text ein, den ich übersetzen soll.")
    else:
        with st.spinner("Analysiere neurotypische Verhaltensmuster... Bitte warten."):
            try:
                # API-Client initialisieren
                client = OpenAI(api_key=api_key)

                # Anfrage an die KI senden (Nutzt gpt-4o für präzise psychologische Analysen)
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_input}
                    ],
                    temperature=0.7
                )

                # Antwort ausgeben
                translation = response.choices[0].message.content
                st.success("Analyse abgeschlossen!")
                st.markdown("---")
                st.markdown(translation)

            except Exception as e:
                st.error(f"Fehler bei der API-Abfrage: {e}")