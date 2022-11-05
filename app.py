# Import der Bibliothek streamlit zur Darstellung der Webapp
# Dokumentation zu Streamlit hier vorhanden: https://docs.streamlit.io/
import streamlit as st

# main Function, die aufgerufen wird und die Webapp startet
def main():
    # Seitentitel, Favicon und Layout der Seite auswählen
    st.set_page_config(page_title="Programmieren für Data Science", page_icon="👨‍💻", layout="centered")
    # Überschrift festlegen
    st.header("⚖️ Konverter Gewichtseinheiten")
    # Unterüberschrift definieren
    st.subheader("👨‍💻 Programmieren für Data Science")
    # mittels CSS wird Standard Layout von Streamlit geändert
    hide_streamlit_style = """ 
            <style>
           div.block-container{padding-top:6rem;}
              div[data-testid="stToolbar"] {
               visibility: hidden;
               height: 0%;
               position: fixed;
               }
          </style>
          """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    # Markdown Schrift fett darstellen
    st.markdown("**Die folgende Anwendung dient zum Umrechnen von verschiedenen Gewichtseinheiten.**")
    # Starten des try Blocks
    try:
        # Eingabe Widget für numerische positive Werte. Speichern der Eingabe in Variable value_in
        value_in = st.number_input("Bitte integer oder float für value_in eingeben:",min_value=0.00, format="%f",step=1.00,value=1.00)
        # Dropdown-Liste für Gewichtseinheiten. Speichern der Auswahl in Variable unit_in
        unit_in = st.selectbox("Bitte Gewichtseinheit für unit_in auswählen:",
                              ("mug","mg","g","dag","kg","t","oz","troz","lb","tnsh","tnl"),index=2)
        # Dropdown-Liste für Gewichtseinheiten. Speichern der Auswahl in Variable unit_out
        unit_out = st.selectbox("Bitte Gewichtseinheit für unit_out auswählen:",
                               ("mug", "mg", "g", "dag", "kg", "t", "oz", "troz", "lb", "tnsh", "tnl"),index=2)
        # Dictionary, welches die einzelnen Gewichtseinheiten ins Verhältnis zu 1000 mug setzt
        weights = {"mug":1_000, "mg":1_000_000, "g":1_000_000_000,"dag":10_000_000_000,
                   "kg":1_000_000_000_000,"t":1_000_000_000_000_000,"oz":28_349_523_125,"troz":31_103_476_800,
                   "lb":453_592_370_000,"tnsh":907_184_740_000_000,"tnl":1_016_046_908_800_000}
        # horizontale Trennlinie mittels Markdown anzeigen
        st.markdown("""----""")
        # Durchführen der Konvertierung des Gewichts und Ausgabe des Ergebnisses
        st.success(str(value_in)+" "+str(unit_in)+ " entspricht "+str(value_in * weights[unit_in] / weights[unit_out])+" "+str(unit_out))
    # Falls Fehler auftritt
    except:
        st.warning("Es ist ein Fehler aufgetreten,bitte Seite neu laden.")

# aufrufen der main Function
if __name__ == '__main__':
    main()
