import streamlit as st

st.set_page_config(
    page_title="KI im Alltag",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "seite" not in st.session_state:
    st.session_state.seite = "Startseite"

if "modus" not in st.session_state:
    st.session_state.modus = "Hell"

if "schrift" not in st.session_state:
    st.session_state.schrift = "Groß"

if "kontrast" not in st.session_state:
    st.session_state.kontrast = False

if "ergebnis" not in st.session_state:
    st.session_state.ergebnis = ""

if "ergebnis_titel" not in st.session_state:
    st.session_state.ergebnis_titel = ""

farben = {
    "Hell": ["#F7F6F2", "#FFFFFF", "#E8EFE9",
             "#23372D", "#315C49", "#FFFFFF", "#B4C5B8"],
    "Dunkel": ["#171C19", "#29332D", "#35463B",
               "#FFFFFF", "#315C49", "#FFFFFF", "#AFC2B4"],
    "Neutral": ["#F3F3F1", "#FFFFFF", "#E7E8E6",
                "#252525", "#424A44", "#FFFFFF", "#B8B8B8"]
}

bg, karte, weich, text, akzent, buttontext, rahmen = farben[
    st.session_state.modus
]

groesse = {
    "Normal": 19,
    "Groß": 23,
    "Sehr groß": 28
}[st.session_state.schrift]

if st.session_state.kontrast:
    if st.session_state.modus == "Dunkel":
        bg = "#000000"
        karte = "#111111"
        weich = "#171717"
        text = "#FFFFFF"
        akzent = "#FFFFFF"
        buttontext = "#000000"
        rahmen = "#FFFFFF"
    else:
        bg = "#FFFFFF"
        karte = "#FFFFFF"
        weich = "#F2F2F2"
        text = "#000000"
        akzent = "#000000"
        buttontext = "#FFFFFF"
        rahmen = "#000000"

st.markdown(f"""
<style>
html, body, .stApp,
[data-testid="stAppViewContainer"],
[data-testid="stHeader"] {{
    background-color: {bg} !important;
    color: {text} !important;
}}

.block-container {{
    max-width: 1050px !important;
    width: 100% !important;
    padding: 2rem 1.5rem 4rem !important;
    margin: auto !important;
    box-sizing: border-box;
}}

[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li,
[data-testid="stWidgetLabel"] p {{
    font-size: {groesse}px !important;
    line-height: 1.65 !important;
    color: {text} !important;
}}

h1, h2, h3 {{
    color: {text} !important;
    line-height: 1.25 !important;
}}

h1 {{
    font-size: clamp(36px, 4.5vw, 54px) !important;
}}

h2 {{
    font-size: {groesse + 11}px !important;
}}

h3 {{
    font-size: {groesse + 5}px !important;
}}

.stButton button {{
    min-height: 58px !important;
    border-radius: 10px !important;
    padding: 12px 18px !important;
    border: 2px solid {rahmen} !important;
    background-color: {karte} !important;
    color: {text} !important;
}}

.stButton button p {{
    font-size: {groesse - 1}px !important;
    line-height: 1.5 !important;
    color: {text} !important;
}}

.stButton button[kind="primary"] {{
    background-color: {akzent} !important;
    border-color: {akzent} !important;
}}

.stButton button[kind="primary"] p {{
    color: {buttontext} !important;
}}

.stButton button:hover {{
    background-color: {weich} !important;
    border-color: {akzent} !important;
}}

.stButton button[kind="primary"]:hover p {{
    color: {text} !important;
}}

button:focus-visible,
input:focus-visible,
textarea:focus-visible {{
    outline: 3px solid #BB872A !important;
    outline-offset: 3px !important;
}}

.st-key-begruessung {{
    background-color: {weich};
    border: 2px solid {rahmen};
    border-radius: 20px;
    padding: clamp(22px, 4vw, 45px);
}}

.st-key-karte1 button,
.st-key-karte2 button,
.st-key-karte3 button,
.st-key-karte4 button {{
    width: 100% !important;
    min-height: 165px !important;
    padding: 23px !important;
    background-color: {karte} !important;
    border: 2px solid {rahmen} !important;
    border-radius: 15px !important;
    text-align: left !important;
    justify-content: flex-start !important;
    white-space: normal !important;
}}

.st-key-karte1 button p,
.st-key-karte2 button p,
.st-key-karte3 button p,
.st-key-karte4 button p {{
    font-size: {groesse}px !important;
    color: {text} !important;
    line-height: 1.6 !important;
}}

.st-key-karte1 button:hover,
.st-key-karte2 button:hover,
.st-key-karte3 button:hover,
.st-key-karte4 button:hover {{
    background-color: {weich} !important;
    border-color: {akzent} !important;
}}

[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea {{
    background-color: {karte} !important;
    color: {text} !important;
    border: 1px solid {rahmen} !important;
    font-size: {groesse}px !important;
    line-height: 1.6 !important;
}}

[data-testid="stTextInput"] input::placeholder,
[data-testid="stTextArea"] textarea::placeholder {{
    color: {text} !important;
    opacity: 0.7 !important;
}}

[data-baseweb="select"] > div,
[data-baseweb="popover"],
[data-baseweb="menu"],
[role="listbox"],
[role="option"] {{
    background-color: {karte} !important;
    color: {text} !important;
}}

[data-baseweb="select"] span,
[data-baseweb="select"] input,
[data-baseweb="menu"] *,
[role="option"] *,
[data-testid="stPopoverBody"] *,
[data-testid="stWidgetLabel"] * {{
    color: {text} !important;
}}

[data-baseweb="select"] span,
[role="option"] {{
    font-size: {groesse}px !important;
}}

[data-testid="stPopoverBody"] {{
    background-color: {karte} !important;
    color: {text} !important;
}}

[data-testid="stPopoverBody"] button {{
    color: {text} !important;
}}

[data-testid="stCaptionContainer"] p {{
    color: {text} !important;
    font-size: {max(17, groesse - 4)}px !important;
}}

[data-testid="stMarkdownContainer"] a {{
    color: {text} !important;
    text-decoration: underline;
}}

@media (max-width: 650px) {{
    .block-container {{
        padding: 1.5rem 1rem 3rem !important;
    }}

    .st-key-karte1 button,
    .st-key-karte2 button,
    .st-key-karte3 button,
    .st-key-karte4 button {{
        min-height: 115px !important;
    }}
}}
</style>
""", unsafe_allow_html=True)


def wechseln(seite):
    st.session_state.seite = seite
    st.session_state.ergebnis = ""
    st.rerun()


kopf1, kopf2 = st.columns([2, 1], vertical_alignment="center")

with kopf1:
    st.markdown("**KI IM ALLTAG**")

with kopf2:
    with st.popover("Anzeige anpassen", use_container_width=True):
        st.radio(
            "Farbdarstellung",
            ["Hell", "Dunkel", "Neutral"],
            key="modus"
        )

        st.select_slider(
            "Schriftgröße",
            options=["Normal", "Groß", "Sehr groß"],
            key="schrift"
        )

        st.toggle(
            "Hoher Kontrast",
            key="kontrast"
        )

st.divider()

if st.session_state.seite != "Startseite":
    if st.button("← Zur Startseite"):
        wechseln("Startseite")


if st.session_state.seite == "Startseite":

    with st.container(key="begruessung"):
        st.caption("VERSTÄNDLICH. PRAKTISCH. IN IHREM TEMPO.")

        st.title("Künstliche Intelligenz im Alltag entdecken")

        st.write("""
        Künstliche Intelligenz kann bei vielen alltäglichen
        Aufgaben eine hilfreiche Unterstützung sein.

        Auf dieser Webseite erfahren Sie, wie Sie KI
        einfach verstehen und selbst nutzen können.

        Entdecken Sie die Möglichkeiten in Ihrem eigenen Tempo.
        """)

        if st.button("Starten", type="primary"):
            wechseln("Verstehen")

    st.write("")

    st.header("Was möchten Sie kennenlernen?")

    st.write(
        "Wählen Sie einen Bereich aus, der Sie interessiert."
    )

    links, rechts = st.columns(2, gap="medium")

    with links:
        if st.button(
            "**KI verstehen**\n\n"
            "Was ist künstliche Intelligenz?",
            key="karte1",
            use_container_width=True
        ):
            wechseln("Verstehen")

    with rechts:
        if st.button(
            "**KI im Alltag**\n\n"
            "Praktische Hilfe bei alltäglichen Aufgaben",
            key="karte2",
            use_container_width=True
        ):
            wechseln("Alltag")

    links, rechts = st.columns(2, gap="medium")

    with links:
        if st.button(
            "**Sicherer Umgang**\n\n"
            "Datenschutz und verlässliche Informationen",
            key="karte3",
            use_container_width=True
        ):
            wechseln("Sicherheit")

    with rechts:
        if st.button(
            "**Schritt für Schritt**\n\n"
            "Anleitungen zur Nutzung von KI",
            key="karte4",
            use_container_width=True
        ):
            wechseln("Anleitungen")

    st.divider()

    st.header("Sie möchten mit einem Menschen sprechen?")

    st.write("""
    Künstliche Intelligenz kann unterstützen.
    Ein persönliches Gespräch kann sie jedoch nicht ersetzen.

    Hier finden Sie wichtige Anlaufstellen und
    Telefonnummern in Deutschland.
    """)

    if st.button(
        "Beratungsstellen und Telefonnummern ansehen",
        use_container_width=True
    ):
        wechseln("Hilfe")


elif st.session_state.seite == "Verstehen":

    st.title("Künstliche Intelligenz einfach verstehen")

    st.write("""
    Künstliche Intelligenz, kurz KI, bezeichnet
    Computersysteme, die beispielsweise Sprache
    verarbeiten, Muster erkennen oder Texte erstellen können.
    """)

    st.subheader("Wo begegnet uns KI?")

    st.write("""
    KI kommt heute in verschiedenen Anwendungen vor.

    Dazu gehören Sprachassistenten, Übersetzungsprogramme
    und Programme, mit denen man Fragen stellen kann.
    """)

    st.subheader("Wie funktioniert ein KI-Chatbot?")

    st.write("""
    Sie geben eine Frage ein und das Programm
    erstellt daraufhin eine Antwort.

    Diese Antworten können hilfreich sein,
    sind aber nicht immer richtig.
    """)

    if st.button("Weiter: KI im Alltag", type="primary"):
        wechseln("Alltag")


elif st.session_state.seite == "Alltag":

    st.title("KI im Alltag nutzen")

    st.write("""
    Künstliche Intelligenz kann bei unterschiedlichen
    Aufgaben im Alltag unterstützen.
    """)

    st.subheader("Kommunikation")

    st.write(
        "KI kann beim Formulieren von Nachrichten, "
        "Briefen und E-Mails helfen."
    )

    st.subheader("Haushalt und Kochen")

    st.write(
        "Sie können beispielsweise nach Rezeptideen "
        "oder Einkaufslisten fragen."
    )

    st.subheader("Freizeit")

    st.write(
        "KI kann Ideen für Aktivitäten, Hobbys "
        "oder Ausflüge vorschlagen."
    )

    st.subheader("Wissen und Unterhaltung")

    st.write(
        "Lassen Sie sich unbekannte Begriffe erklären "
        "oder lernen Sie, wie ein Gespräch mit KI funktioniert."
    )

    st.write("")

    if st.button("Alltagshelfer öffnen", type="primary"):
        wechseln("Helfer")


elif st.session_state.seite == "Sicherheit":

    st.title("Sicher mit KI umgehen")

    st.subheader("Persönliche Daten schützen")

    st.write(
        "Geben Sie keine Passwörter, Bankdaten "
        "oder andere vertrauliche Informationen ein."
    )

    st.subheader("Antworten überprüfen")

    st.write(
        "KI kann auch falsche Informationen liefern. "
        "Überprüfen Sie wichtige Aussagen."
    )

    st.subheader("Hilfe von Fachpersonen")

    st.write(
        "Bei medizinischen, rechtlichen oder finanziellen "
        "Fragen sollten Sie sich zusätzlich an "
        "geeignete Fachpersonen wenden."
    )


elif st.session_state.seite == "Anleitungen":

    st.title("Schritt für Schritt zur ersten KI-Anfrage")

    st.write(
        "Wir zeigen Ihnen, wie Sie einen KI-Chatbot "
        "für eine einfache Aufgabe verwenden können."
    )

    st.subheader("Schritt 1")

    st.write(
        "Öffnen Sie einen KI-Chatbot, "
        "beispielsweise ChatGPT."
    )

    st.subheader("Schritt 2")

    st.write(
        "Suchen Sie das Eingabefeld für Nachrichten."
    )

    st.subheader("Schritt 3")

    st.write(
        "Schreiben Sie Ihre Frage in das Eingabefeld."
    )

    st.subheader("Schritt 4")

    st.write(
        "Senden Sie die Nachricht und lesen Sie die Antwort."
    )

    st.subheader("Schritt 5")

    st.write(
        "Falls Sie etwas nicht verstehen, "
        "können Sie eine Rückfrage stellen."
    )

    if st.button("Eine eigene Anfrage vorbereiten", type="primary"):
        wechseln("Helfer")


elif st.session_state.seite == "Helfer":

    st.title("Ihr KI-Alltagshelfer")

    st.write(
        "Wählen Sie aus, wobei Sie Unterstützung benötigen."
    )

    auswahl = st.selectbox(
        "Was möchten Sie machen?",
        [
            "Nachricht schreiben",
            "Rezeptidee vorbereiten",
            "Freizeit planen",
            "Gespräch beginnen",
            "Etwas erklären lassen"
        ]
    )

    if auswahl == "Nachricht schreiben":

        empfaenger = st.text_input(
            "An wen möchten Sie schreiben?",
            placeholder="Zum Beispiel: Magda"
        )

        wunsch = st.text_area(
            "Worum soll es in der Nachricht gehen?",
            placeholder="Zum Beispiel: Magda soll bitte Fisch einkaufen.",
            height=140
        )

        if st.button("KI-Anfrage erstellen", type="primary"):

            if empfaenger.strip() and wunsch.strip():

                st.session_state.ergebnis = (
                    f"Schreibe mir eine freundliche Nachricht an "
                    f"{empfaenger.strip()}. "
                    f"Folgender Inhalt soll vermittelt werden: "
                    f"{wunsch.strip()}. "
                    f"Achte auf eine korrekte Rechtschreibung, "
                    f"eine verständliche Formulierung und "
                    f"einen passenden Ton."
                )

                st.session_state.ergebnis_titel = (
                    "Ihre vorbereitete KI-Anfrage"
                )

            else:
                st.warning(
                    "Bitte geben Sie einen Namen und ein Anliegen ein."
                )

    else:

        beschreibung = st.text_area(
            "Beschreiben Sie Ihren Wunsch",
            placeholder="Schreiben Sie hier einige Stichwörter.",
            height=140
        )

        if st.button("Anfrage vorbereiten", type="primary"):

            if not beschreibung.strip():

                st.warning(
                    "Bitte beschreiben Sie zuerst Ihren Wunsch."
                )

            else:

                if auswahl == "Rezeptidee vorbereiten":
                    text_anfrage = (
                        "Schlage mir ein einfaches Rezept vor. "
                        f"Meine Wünsche oder Zutaten: {beschreibung}. "
                        "Erkläre die Zubereitung Schritt für Schritt."
                    )

                elif auswahl == "Freizeit planen":
                    text_anfrage = (
                        "Schlage mir drei passende Freizeitaktivitäten vor. "
                        f"Meine Interessen: {beschreibung}."
                    )

                elif auswahl == "Gespräch beginnen":
                    text_anfrage = (
                        "Ich möchte mich über Folgendes unterhalten: "
                        f"{beschreibung}. "
                        "Stelle mir jeweils eine Frage und warte auf meine Antwort."
                    )

                else:
                    text_anfrage = (
                        "Erkläre mir dieses Thema in einfachen Worten: "
                        f"{beschreibung}. Verwende ein anschauliches Beispiel."
                    )

                st.session_state.ergebnis = text_anfrage
                st.session_state.ergebnis_titel = (
                    "Ihre vorbereitete KI-Anfrage"
                )

    if st.session_state.ergebnis:

        st.subheader(st.session_state.ergebnis_titel)

        st.text_area(
            "Text zum Kopieren",
            value=st.session_state.ergebnis,
            height=220
        )

        st.write(
            "Sie können den Text markieren und kopieren."
        )

    st.info(
        "Diese Webseite bereitet Ihre Anfrage für eine KI-Anwendung vor. "
        "Kopieren Sie den erstellten Text und fügen Sie ihn "
        "beispielsweise in ChatGPT ein. "
        "Die eigentliche Antwort wird dort erstellt."
    )


elif st.session_state.seite == "Hilfe":

    st.title("Hilfe und persönliche Kontakte")

    st.write(
        "Hier finden Sie wichtige Telefonnummern "
        "und Beratungsangebote in Deutschland."
    )

    st.subheader("Notfälle")

    st.markdown("### Polizei: 110")
    st.write("Bei akuter Gefahr. Rund um die Uhr.")

    st.markdown("### Rettungsdienst und Feuerwehr: 112")
    st.write("Bei lebensbedrohlichen Notfällen. Rund um die Uhr.")

    st.divider()

    st.subheader("Gespräche und Beratung")

    st.markdown("### Silbernetz")
    st.markdown("**0800 4 70 80 90**")
    st.write("Bei Einsamkeit im Alter.")
    st.write("Täglich von 8 bis 22 Uhr.")
    st.markdown("[Zur Webseite](https://silbernetz.org/)")

    st.divider()

    st.markdown("### TelefonSeelsorge")
    st.markdown("**116 123**")
    st.write("Bei Sorgen, Krisen und Einsamkeit.")
    st.write("Rund um die Uhr.")
    st.markdown("[Zur Webseite](https://www.telefonseelsorge.de/)")

    st.divider()

    st.markdown("### Info-Telefon Depression")
    st.markdown("**0800 33 44 533**")
    st.write("Informationen über Depression und Hilfsangebote.")
    st.write("Montag, Dienstag, Donnerstag: 13–17 Uhr.")
    st.write("Mittwoch, Freitag: 8:30–12:30 Uhr.")
    st.markdown(
        "[Zur Webseite](https://www.deutsche-depressionshilfe.de/hilfe/info-telefon)"
    )

    st.divider()

    st.markdown("### Alzheimer-Telefon")
    st.markdown("**030 259 37 95 14**")
    st.write("Beratung bei Fragen zu Demenz.")
    st.write("Montag bis Donnerstag: 9–18 Uhr.")
    st.write("Freitag: 9–15 Uhr.")
    st.markdown(
        "[Zur Webseite](https://www.deutsche-alzheimer.de/alzheimer-telefon)"
    )

    st.divider()

    st.markdown("### Ärztlicher Bereitschaftsdienst")
    st.markdown("**116 117**")
    st.write(
        "Für dringende gesundheitliche Beschwerden, "
        "die nicht lebensbedrohlich sind."
    )
    st.write("Rund um die Uhr.")
    st.markdown("[Zur Webseite](https://www.116117.de/)")