### 📊 Analyse de Simulation des Données Génomiques et de Survie  

## 👨‍💻 Contributeurs
- ACHENAN Ali
- BOUKTIBA Souhaib
- EL ONSORY Fatimazahraa

## 📝 Aperçu  

Ce notebook Jupyter documente un processus de simulation et d'analyse des données génétiques et de survie en utilisant **Hail** et le modèle de **risques proportionnels de Cox**. Le flux de travail inclut la génération de données VCF simulées, leur importation et filtrage avec Hail, la simulation de données de survie, ainsi que la fusion des deux ensembles pour l'analyse.  

## 🔄 Étapes du Workflow  

1. **🧬 Simulation des Données VCF**  
   - Des données VCF simulées avec des génotypes pour 10 échantillons sont générées.  
   - Le fichier VCF est créé et enregistré sous le nom `simulated.vcf`.  

2. **📥 Importation et Filtrage des Données VCF avec Hail**  
   - Les données VCF sont importées avec Hail.  
   - Les lignes sont filtrées pour ne conserver que celles correspondant à l'identifiant `rs12345`.  
   - Les entrées sont annotées avec des comptes de risque allélique.  

3. **⏳ Simulation des Données de Survie**  
   - Des données de survie sont simulées pour 10 échantillons, incluant le temps et les indicateurs d'événement.  

4. **🔗 Fusion des Données de Survie et Génétiques**  
   - Les ensembles de données de survie et de risque sont fusionnés dans un seul **DataFrame**.  

5. **📈 Analyse avec le Modèle de Cox**  
   - Le modèle de **risques proportionnels de Cox** est ajusté aux données combinées.  
   - Un résumé du modèle est affiché pour interprétation.  

## 🔑 Variables Clés  

- **sample_names** 🏷️ : Liste des noms d'échantillons.  
- **genotypes** 🧬 : Liste des génotypes simulés.  
- **vcf_header** et **vcf_body** 📄 : Contenu du fichier VCF.  
- **vcf_filename** 📁 : Nom du fichier VCF.  
- **df_risk** ⚠️ : DataFrame contenant les comptes de risque allélique par échantillon.  
- **survival_data** ⏳ : DataFrame contenant les données de survie simulées.  
- **combined_df** 🔗 : DataFrame fusionnant les données de survie et de risque génétique.  

## 📌 Prérequis  

- **Python 3.x** 🐍  
- Bibliothèques requises : `numpy`, `pandas`, `lifelines`, `hail` ,`DeepVarient` 📦  
- Environment `Docker`

## 🚀 Utilisation  

1. Assurez-vous que toutes les bibliothèques requises sont installées.  
2. Exécutez le notebook Jupyter pour exécuter le workflow.  
3. Interprétez le résumé du modèle de Cox.  

