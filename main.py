import streamlit as st
import pandas

print('console')

st.title('minha primeira pagina :wolf:')

st.write('''aosnfoiansiofnas  
asibiabjfa  
asknsoidvnoksdv
sdbnvosmdvs
ndsdkvnds usd vubdv ysbdnvusbndv us vujsdnvui snvsidunv sdiuvn sdnv sduv sdiuv dv  
sd un sduhsd8ijhs divsd8j sidjv sdijv dsivjsdiojv sidjv iosj divj sdv
''')
df = pandas.read_csv('https://raw.githubusercontent.com/hermeson883/data_science_workshop/main/linguagens.csv')

st.dataframe(df)