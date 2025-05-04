import streamlit as st
import pandas as pd
import numpy as np


# Initialisation de l'état si ce n'est pas déjà fait
if "commencer" not in st.session_state:
    st.session_state.commencer = False

# Titre et intro
st.title("Bienvenue")
st.write("Cette interface a été créée pour t’aider à mieux comprendre certaines habitudes de ton quotidien qui peuvent influencer ton poids et ton bien-être."
" Ces facteurs sont variés : ta fréquentation de la cantine scolaire, ta consommation de substances comme le cannabis ou l’alcool, ou encore ton temps de sommeil moyen"
" chaque nuit. L’objectif est de te permettre de visualiser les facteurs qui pourraient avoir le plus d’impact sur toi. "
"Si tu identifies des comportements susceptibles d’améliorer ton bien-être, n’hésite pas à te renseigner davantage.")
st.write("Prêt ?")
# Bouton pour commencer
if st.button("commencer"):
    st.session_state.commencer = True

# Si "Commencer" a été cliqué
if st.session_state.commencer:
    st.write("Pour cela, je peux te montrer quels facteurs agissent sur toi.")

    option1 = st.selectbox("Si tu souhaites connaître un peu mieux ce qui peut agir sur toi alors continuons.", ["", "CONTINUER", "NE PAS CONTINUER"])

    if option1 == "CONTINUER":
        st.write("Super ! Je vais maintenant te poser quelques questions pour mieux te connaître. Il me sera plus facile de te présenter ce qui peut t’impacter si je comprends mieux qui tu es.")

        option2 = st.selectbox(" Tout d'abord, peux-tu m'indiquer ton sexe ?", ["", "Femme", "Homme"])

        if option2 == "Femme":
            option3F = st.selectbox(
                "Super. Peux-tu m’indiquer le type de métier exercé par tes parents ? Choisis la situation qui, selon toi, caractérise le mieux la situation professionnelle de ta famille. "
                 "Au moins un de mes parents est... ",
                ["", "Cadre, profession intermédiaire, artisan, chef d'entreprise ou agriculteur", 
                 "Employé, ouvrier ou occupe une autre situation"]
            )

            if option3F == "Cadre, profession intermédiaire, artisan, chef d'entreprise ou agriculteur":
                st.write("Super, ce graphique va pouvoir t'indiquer quelques facteurs qui peuvent influencer ton bien-être.")
                data_F_123={ "variables":["CANTINE","SPORT","CIGARETTES", "CANNABIS",
                          "ALCOOL", "SOMMEIL", "TEMPS ECRAN"], 
                            "VARIATION":[1.96 , -3.71, 0.16, -4.11, 1.17, -1.14, 2.42] }
                tab_F_123=pd.DataFrame(data_F_123)
                tab_F_123.set_index("variables", inplace=True)
                st.bar_chart(tab_F_123["VARIATION"], use_container_width=True)
                
                st.write("Les variables dont la barre du graphique est vers le haut représentent les facteurs qui augmentent la probabilité de développer des problèmes "
                "de poids. À l’inverse, les variables dont la barre est située vers le bas diminuent cette probabilité. "
                "Plus la barre est grande, plus le facteur en question joue fortement (et inversement). Tu dois interpréter la grandeur des barres en terme de variation en pourcentage."
                "Les variables sont données à titre indicatif et des renseignements plus complets te sont proposés en fin de page. "
                "Comme tu peux le voir, pratiquer une activité sportive ou manger souvent à la cantine te permettront de garder le contrôle sur ton corps. "
                "Aussi, si tu arrives à avoir un bon rythme de sommeil avec une durée suffisante, tes chances de développer des problèmes de poids vont diminuer."
                " Si tu veux éviter d'augmenter tes chances d'être en surpoids, diminue ta consommation d’écran, car cela te sédentarise. "
                "Ta consommation de substances à risque (alcool, tabac et cannabis) ne joue que très peu sur tes probabilités de développer un problème de poids. "
                "Ces substances peuvent effectivement modifier ton rapport à la nourriture. Cependant, je te rapelle que la consommation de ces produits représente un réel danger pour la santé.")
            
                
                st.write("Maintenant, si tu souhaites consulter des ressources plus complètes sur le sujet, il existe d'autres plateformes."
                " Les liens ci-dessous te permettront de les consulter."
                " https://obesicare.patientys.com/login. Cette plateforme va te permettre d'être mis en lien avec des spécialistes qui ne sont pas dans le jugement. "
                "Si tu préfères simplement te documenter, tu peux consulter cette plateforme : https://cnao.fr. ")
                

            elif option3F == "Employé, ouvrier ou occupe une autre situation":
                st.write("Super, ce graphique va pouvoir t'indiquer quelques facteurs qui peuvent influencer ton bien-être.")
                data_F_456={ "variables":["CANTINE","SPORT","CIGARETTES", "CANNABIS","ALCOOL", "SOMMEIL", "TEMPS ECRAN"],
                "VARIATION":[2.87 , 1.07, -1.42, 3.58, 1.02, 0.68, -0.09] }
                tab_F_456=pd.DataFrame(data_F_456)
                tab_F_456.set_index('variables', inplace=True)
                st.bar_chart(tab_F_456['VARIATION'], use_container_width=True)
                st.write("Les variables dont la barre du graphique est vers le haut représentent les facteurs qui augmentent la probabilité de développer des problèmes de poids."
                " À l’inverse, les variables dont la barre est située vers le bas diminuent cette probabilité. Plus la barre est grande, plus le facteur en question joue fortement "
                "(et inversement). Tu dois interpréter la grandeur des barres en terme de variation en pourcentage. Ces variables te sont données à titre indicatif, des renseignements plus complets te sont proposés en fin de page."
                " Comme tu peux le voir, pratiquer une activité sportive ou manger souvent à la cantine te permettront de garder le contrôle sur ton corps. "
                "Dormir un peu plus peut te permettre de garder un rythme de vie sain."
                " Aussi, tu n’as pas besoin de modifier considérablement ta consommation de temps d’écran moyen."
                " Il est vrai qu’il est indiqué que cela peut diminuer tes chances de développer des problèmes de poids, mais il ne faut pas tirer de conclusions hâtives. Ce facteur n’est pas très impactant. "
                "Ces indicateurs ne te feront probablement pas diminuer cette probabilité, mais ils ne l’augmenteront pas non plus totalement. "
                "Ta consommation de substances à risque (alcool, tabac et cannabis) ne joue que très peu sur tes probabilités de développer un problème de poids. "
                "Ces substances peuvent effectivement modifier ton rapport à la nourriture. Cependant, je te rapelle que la consommation de ces produits représente un réel danger pour la santé.")
                st.write("Maintenant, si tu souhaites consulter des ressources plus complètes sur le sujet, il existe d'autres plateformes."
                " Les liens ci-dessous te permettront de les consulter."
                "https://obesicare.patientys.com/login. Cette plateforme va te permettre d'être mis en lien avec des spécialistes qui ne sont pas dans le jugement."
                "Si tu préfères simplement te documenter, tu peux consulter cette plateforme : https://cnao.fr. ")
                
        elif option2 == "Homme":
            option3H = st.selectbox("Super. Peux-tu m’indiquer le type de métier exercé par tes parents ? Choisis la situation qui, selon toi, caractérise le mieux la situation professionnelle de ta famille. "
                 "Au moins un de mes parents est... ",
                ["", "Cadre, profession intermédiaire, artisan, chef d'entreprise ou agriculteur", 
                 "Employé, ouvrier ou occupe une autre situation"])

            if option3H == "Cadre, profession intermédiaire, artisan, chef d'entreprise ou agriculteur":
                st.write("Super, ce graphique va pouvoir t'indiquer quelques facteurs qui peuvent influencer ton bien-être.")
                data_H_123={ "variables":["CANTINE","SPORT","CIGARETTES", "CANNABIS","ALCOOL", "SOMMEIL", "TEMPS ECRAN"],
                "VARIATION":[1.56 ,-5.32 , -2.98, 2.17, -0.34, -1.33, 1.27] }
                tab_H_123=pd.DataFrame(data_H_123)
                tab_H_123.set_index('variables', inplace=True)
                st.bar_chart(tab_H_123['VARIATION'], use_container_width=True)
                st.write("Les variables dont la barre du graphique est vers le haut représentent les facteurs qui augmentent la probabilité de développer des problèmes de poids."
                " À l’inverse, les variables dont la barre est située vers le bas diminuent cette probabilité. Plus la barre est grande, plus le facteur en question joue fortement "
                "(et inversement). Tu dois interpréter la grandeur des barres en terme de variation en pourcentage. Ces variables te sont données à titre indicatif, des renseignements plus complets te sont proposés en fin de page."
                "Comme tu peux le voir, pratiquer une activité sportive ou manger souvent à la cantine te permettront de garder le contrôle sur ton corps. "
                "Dormir un peu plus peut te permettre de garder un rythme de vie sain. "
                "Aussi, tu n’as pas besoin de modifier considérablement ta consommation de temps d’écran moyen. "
                "Il est vrai qu’il est indiqué que cela peut diminuer tes chances de développer des problèmes de poids, mais il ne faut pas tirer de conclusions hâtives. Ce facteur n’est pas très impactant. "
                "Ces indicateurs ne te feront probablement pas diminuer cette probabilité, mais ils ne l’augmenteront pas non plus totalement. "
                "Ta consommation de substances à risque (alcool, tabac et cannabis) ne joue que très peu sur tes probabilités de développer un problème de poids. "
                "Ces substances peuvent effectivement modifier ton rapport à la nourriture. Cependant, je te rapelle que la consommation de ces produits représente un réel danger pour la santé.")
                
                st.write("Maintenant, si tu souhaites consulter des ressources plus complètes sur le sujet, il existe d'autres plateformes."
                " Les liens ci-dessous te permettront de les consulter."
                "https://obesicare.patientys.com/login. Cette plateforme va te permettre d'être mis en lien avec des spécialistes qui ne sont pas dans le jugement."
                "Si tu préfères simplement te documenter, tu peux consulter cette plateforme : https://cnao.fr. ")
                


            elif option3H == "Employé, ouvrier ou occupe une autre situation":
                st.write("Super, ce graphique va pouvoir t'indiquer quelques facteurs qui peuvent influencer ton bien-être.")
                data_H_456={ "variables":["CANTINE","SPORT","CIGARETTES", "CANNABIS","ALCOOL", "SOMMEIL", "TEMPS ECRAN"],
                "VARIATION":[-0.03 ,-1.55 , -0.50, -21.63, -1.49, -4.73, 1.88] }
                tab_H_456=pd.DataFrame(data_H_456)
                tab_H_456.set_index('variables', inplace=True)
                st.bar_chart(tab_H_456['VARIATION'], use_container_width=True)
                st.write("Les variables dont la barre du graphique est vers le haut représentent les facteurs qui augmentent la probabilité de développer des problèmes de poids. "
                "À l’inverse, les variables dont la barre est située vers le bas diminuent cette probabilité. Plus la barre est grande, plus le facteur en question joue fortement "
                "(et inversement). Tu dois interpréter la grandeur des barres en terme de variation en pourcentage. Ces variables te sont données à titre indicatif, des renseignements plus complets te sont proposés en fin de page. " 
                "Si tu pratiques une activité sportive en dehors de ton établissement scolaire et que tu manges plus souvent à la cantine pour bénéficier d’un meilleur "
                "encadrement, tu as de meilleures chances de garder un contrôle sur ton corps. Il semble que diminuer ton temps de sommeil te permettra de diminuer"
                " la probabilité de développer des problèmes de poids. Fais cependant attention à garder une durée de sommeil assez importante pour pouvoir être en forme."
                " Si tu veux éviter d'augmenter tes risques d'être en surpoids, diminue ta consommation d'écran car cela te sédentarise. Ta consommation de substances"
                " à risque (alcool, tabac et cannabis) ne joue que très peu sur tes probabilités de développer un problème de poids. Ces substances peuvent "
                "effectivement modifier ton rapport à la nourriture. Cependant, je te rapelle que la consommation de ces produits représente un réel danger pour la santé.")
                
                st.write("Maintenant, si tu souhaites consulter des ressources plus complètes sur le sujet, il existe d'autres plateformes."
                " Les liens ci-dessous te permettront de les consulter."
                "https://obesicare.patientys.com/login. Cette plateforme va te permettre d'être mis en lien avec des spécialistes qui ne sont pas dans le jugement."
                "Si tu préfères simplement te documenter, tu peux consulter cette plateforme : https://cnao.fr.")
                
            

        else:
            st.write("Choisis un sexe")

    elif option1 == "NE PAS CONTINUER":
        st.write("Pas de souci, peut-être une autre fois !")

