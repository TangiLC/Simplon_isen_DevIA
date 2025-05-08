import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

données['CA'] = données['prix'] * données['qte']
qte_par_produit = données.groupby('produit', as_index=False)['qte'].sum()
ca_par_produit = données.groupby('produit', as_index=False)['CA'].sum()

quantity_by_region = px.pie(données, values='qte', names='region', title='quantité vendue par région')

quantity_by_product=px.bar(qte_par_produit, x='produit',  y='qte', title='quantités totales vendues par produit', color='produit')

ca_by_product = px.bar(ca_par_produit, x='produit', y='CA', title ='CA par produit', color='produit')


quantity_by_region.write_html('ventes-par-region.html')
print('ventes-par-région généré avec succès !')

ca_by_product.write_html('ca-par-produit.html')
print('ca-par-produit généré avec succès !')

quantity_by_product.write_html('ventes-par-produit.html')
print('ventes-par-produit généré avec succès !')
