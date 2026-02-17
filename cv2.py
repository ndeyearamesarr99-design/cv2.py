import streamlit as st

st.title("CURRICULUM VITAE")

with st.sidebar:

    st.image("IMG_8997.jpg",width=500)
    nom=st.subheader("NDEYE ARAME SARR")
    email=st.write("ndeyearamesarr99@gmail.com")
    tel=st.write("📞783876524")

    st.info("📃Education")
    st.write("BAC")
    st.write("licence en géographie")
    st.write("BTS en géomatique")

    st.info("Langues")
    st.write("francais")
    st.write("anglais")

st.subheader("🚺Profil")
st.write("""Titulaire d'une licence3 en géographie et actuellemlent geomaticienne de formation,j'ai un interet particulier en SIG et base de donnée.
je suis en mesure de gérer des taches comme etablir une base de donnée,faire le géoréférencement et gérer des questions liés a la géographie.""")

st.header("🎓Experience")
st.write("collecte des données de Masaliqul Djinane avec le prof de cartograhie")
st.write("representation de la région de kaolack sur QGIS et numerisation de toutes les routes et villages qui s'y trouvent.")

st.header("📝Projets académiques")
st.write("projet de numérisation sur QGIS")
st.write("projet de géoréférencement sur QGIS et ARCGIS")

st.header("🛠️Compétences")
st.write("bonne maitrise des outils SIG(QGIS,ARCGIS)")
st.write("analyse des données spatiales,géoréférencement et numérisation")
st.write("maitrise des suites bureautique comme word, excel,power point")

st.header("👩‍💻projet personnel")
st.write("ouvrir une boutique de vetements pudiques pour femmes") 
          
    
        
    


