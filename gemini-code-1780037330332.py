import random
import streamlit as st

# ==========================================
# BASE DE DONNÉES DES 140 QUESTIONS DU QUIZ
# ==========================================
QUIZ_DATA = {
    "Ceinture Blanche-Jaune": [
        {"question": "Que signifie le mot 'Judo' ?", "options": ["Voie de la souplesse", "Voie de la force", "L'art de combattre", "École de la vie"], "answer": "Voie de la souplesse"},
        {"question": "Qui est le fondateur du Judo ?", "options": ["Jigorō Kanō", "Morihei Ueshiba", "Gichin Funakoshi", "Akira Kurosawa"], "answer": "Jigorō Kanō"},
        {"question": "En quelle année le Judo a-t-il été créé ?", "options": ["1882", "1900", "1945", "1750"], "answer": "1882"},
        {"question": "Comment appelle-t-on le lieu où l'on pratique le judo ?", "options": ["Le Dojo", "Le Tatami", "Le Stadium", "Le Ring"], "answer": "Le Dojo"},
        {"question": "Comment appelle-t-on le tapis de judo ?", "options": ["Le Tatami", "Le Judogi", "Le Shiai", "Le Randori"], "answer": "Le Tatami"},
        {"question": "Comment s'appelle la tenue du judoka ?", "options": ["Le Judogi (ou Kimono)", "Le Hakama", "Le Karatégi", "Le Maillot"], "answer": "Le Judogi (ou Kimono)"},
        {"question": "Que signifie le terme 'Rei' ?", "options": ["Le salut", "Le professeur", "La chute", "L'arrêt"], "answer": "Le salut"},
        {"question": "Comment dit-on 'Commencez' en judo ?", "options": ["Hajime", "Matte", "Sore-made", "Osae-komi"], "answer": "Hajime"},
        {"question": "Comment dit-on 'Arrêtez' en judo ?", "options": ["Matte", "Hajime", "Sono-mama", "Yuko"], "answer": "Matte"},
        {"question": "Comment appelle-t-on celui qui fait la technique (l'attaquant) ?", "options": ["Tori", "Uke", "Sensei", "Sempai"], "answer": "Tori"},
        {"question": "Comment appelle-t-on celui qui subit la technique (le partenaire) ?", "options": ["Uke", "Tori", "Judoka", "Arbitre"], "answer": "Uke"},
        {"question": "Que signifie 'Ukemi' ?", "options": ["Les brise-chutes", "Les projections", "Les contrôles au sol", "Les esquives"], "answer": "Les brise-chutes"},
        {"question": "Quelle est la chute vers l'arrière ?", "options": ["Ushiro-ukemi", "Yoko-ukemi", "Mae-ukemi", "Zenpo-kaiten"], "answer": "Ushiro-ukemi"},
        {"question": "Quelle est la première ceinture de couleur après la blanche ?", "options": ["Blanche-Jaune", "Jaune", "Orange", "Verte"], "answer": "Blanche-Jaune"},
        {"question": "Dans quel pays le Judo a-t-il pris naissance ?", "options": ["Le Japon", "La Chine", "La Corée", "La France"], "answer": "Le Japon"},
        {"question": "Comment appelle-t-on le professeur de judo (ceinture noire) ?", "options": ["Sensei", "Tori", "Uke", "Shihan"], "answer": "Sensei"},
        {"question": "Que signifie 'Migite' ?", "options": ["La main droite", "La main gauche", "Le pied droit", "La saisie"], "answer": "La main droite"},
        {"question": "Que signifie 'Hidari' ?", "options": ["Gauche", "Droite", "Avancer", "Reculer"], "answer": "Gauche"},
        {"question": "Comment appelle-t-on la veste du judogi ?", "options": ["Uwagi", "Zubon", "Obi", "Zori"], "answer": "Uwagi"},
        {"question": "Comment appelle-t-on la ceinture du judoka ?", "options": ["Obi", "Uwagi", "Zubon", "紐 (Himo)"], "answer": "Obi"}
    ],
    "Ceinture Jaune": [
        {"question": "Que signifie 'Kumi-kata' ?", "options": ["La saisie / la garde", "Le salut debout", "Le combat officiel", "L'échauffement"], "answer": "La saisie / la garde"},
        {"question": "Quelle est la chute latérale (sur le côté) ?", "options": ["Yoko-ukemi", "Ushiro-ukemi", "Mae-ukemi", "Mae-mawari"], "answer": "Yoko-ukemi"},
        {"question": "Que signifie 'Anza' ?", "options": ["La position assise en tailleur", "La position à genoux", "Le salut traditionnel", "L'arbitrage"], "answer": "La position assise en tailleur"},
        {"question": "Que signifie 'Seiza' ?", "options": ["La position à genoux (formelle)", "La position debout", "Le combat libre", "La garde droite"], "answer": "La position à genoux (formelle)"},
        {"question": "Comment qualifie-t-on les techniques de projection ?", "options": ["Nage-waza", "Katame-waza", "Ne-waza", "Atemi-waza"], "answer": "Nage-waza"},
        {"question": "Comment qualifie-t-on le travail au sol ?", "options": ["Ne-waza", "Nage-waza", "Tachi-waza", "Katas"], "answer": "Ne-waza"},
        {"question": "Que signifie 'O-soto-gari' ?", "options": ["Grand fauchage extérieur", "Grand fauchage intérieur", "Petite section de hanche", "Roue autour de la hanche"], "answer": "Grand fauchage extérieur"},
        {"question": "Que signifie 'Hon-kesa-gatame' ?", "options": ["Contrôle fondamental en écharpe", "Contrôle par le dessus", "Contrôle arrière par quatre coins", "Immobilisation latérale"], "answer": "Contrôle fondamental en écharpe"},
        {"question": "Quel terme annonce le début d'une immobilisation au sol ?", "options": ["Osae-komi", "Toketa", "Ippon", "Waza-ari"], "answer": "Osae-komi"},
        {"question": "Quel terme annonce qu'une immobilisation est rompus/brisée ?", "options": ["Toketa", "Osae-komi", "Matte", "Hime"], "answer": "Toketa"},
        {"question": "Comment appelle-t-on le pantalon du judogi ?", "options": ["Zubon", "Uwagi", "Obi", "Zori"], "answer": "Zubon"},
        {"question": "Quel mot désigne les sandales utilisées hors du tatami ?", "options": ["Zori", "Zubon", "Tatami", "Geta"], "answer": "Zori"},
        {"question": "Qu'est-ce qu'un 'Randori' ?", "options": ["Un combat souple d'entraînement", "Une compétition officielle", "Une démonstration technique", "Un exercice de chutes"], "answer": "Un combat souple d'entraînement"},
        {"question": "Qu'est-ce qu'un 'Shiai' ?", "options": ["Un combat de compétition officielle", "Un échauffement", "Une étude technique statique", "Une chute avant"], "answer": "Un combat de compétition officielle"},
        {"question": "Quelle technique consiste à projeter par la hanche en la plaçant sous le partenaire ?", "options": ["O-goshi", "Ippon-seoi-nage", "De-ashi-barai", "O-soto-gari"], "answer": "O-goshi"},
        {"question": "Quelle partie du corps caractérise les techniques 'Te-waza' ?", "options": ["Les mains / les bras", "Les hanches", "Les jambes", "Le sacrifice"], "answer": "Les mains / les bras"},
        {"question": "Quelle partie du corps caractérise les techniques 'Koshi-waza' ?", "options": ["Les hanches", "Les pieds", "Les épaules", "Les bras"], "answer": "Les hanches"},
        {"question": "Quelle partie du corps caractérise les techniques 'Ashi-waza' ?", "options": ["Les jambes / les pieds", "Le tronc", "La tête", "Les mains"], "answer": "Les jambes / les pieds"},
        {"question": "Comment salue-t-on debout ?", "options": ["Ritsurei", "Zarei", "Hajime", "Chokurei"], "answer": "Ritsurei"},
        {"question": "Comment salue-t-on au sol / à genoux ?", "options": ["Zarei", "Ritsurei", "Anza", "Sensei-ni"], "answer": "Zarei"}
    ],
    "Ceinture Jaune-Orange": [
        {"question": "Que signifie 'Kuzushi' ?", "options": ["Le déséquilibre", "La préparation", "L'exécution", "La chute"], "answer": "Le déséquilibre"},
        {"question": "Que désigne le terme 'Tsukuri' ?", "options": ["La préparation / le placement du corps", "Le brise-chute", "La projection finale", "La fin du combat"], "answer": "La préparation / le placement du corps"},
        {"question": "Que désigne le terme 'Kake' ?", "options": ["L'exécution / la conclusion de la technique", "La garde de manche", "L'arbitre de coin", "Le tapis"], "answer": "L'exécution / la conclusion de la technique"},
        {"question": "Quel est le sens de 'Ko-uchi-gari' ?", "options": ["Petit fauchage intérieur", "Grand fauchage intérieur", "Petit fauchage extérieur", "Balayage des deux pieds"], "answer": "Petit fauchage intérieur"},
        {"question": "Quel est le sens de 'O-uchi-gari' ?", "options": ["Grand fauchage intérieur", "Petit fauchage intérieur", "Grand fauchage extérieur", "Fauchage par la hanche"], "answer": "Grand fauchage intérieur"},
        {"question": "Que signifie 'Shintai' ?", "options": ["Les déplacements", "Les esquives", "Les saluts", "Les saisies"], "answer": "Les déplacements"},
        {"question": "Comment appelle-t-on le déplacement en pas chassés ?", "options": ["Tsugi-ashi", "Ayumi-ashi", "Tai-sabaki", "Suri-ashi"], "answer": "Tsugi-ashi"},
        {"question": "Comment appelle-t-on le déplacement en pas marchés normaux ?", "options": ["Ayumi-ashi", "Tsugi-ashi", "Tai-sabaki", "Mae-geri"], "answer": "Ayumi-ashi"},
        {"question": "Quelle technique se traduit par 'Projection de l'épaule par un bras' ?", "options": ["Ippon-seoi-nage", "Morote-seoi-nage", "Eri-seoi-nage", "Tai-otoshi"], "answer": "Ippon-seoi-nage"},
        {"question": "Comment appelle-t-on l'ensemble des techniques d'immobilisation au sol ?", "options": ["Osaekomi-waza", "Shime-waza", "Kansetsu-waza", "Atemi-waza"], "answer": "Osaekomi-waza"},
        {"question": "Quel score maximal termine immédiatement un combat de judo ?", "options": ["Ippon", "Waza-ari", "Yuko", "Koka"], "answer": "Ippon"},
        {"question": "Combien de 'Waza-ari' faut-il pour obtenir la victoire (Waza-ari-awasete-ippon) ?", "options": ["2", "3", "4", "1 seul suffit"], "answer": "2"},
        {"question": "Que signifie 'Tai-sabaki' ?", "options": ["La rotation ou esquive du corps", "Le contrôle des bras", "L'attaque simultanée", "Le brise-chute avant"], "answer": "La rotation ou esquive du corps"},
        {"question": "Quelle est la signification de 'De-ashi-barai' ?", "options": ["Balayage du pied avancé", "Fauchage arrière", "Soutien du genou", "Accrochage du talon"], "answer": "Balayage du pied avancé"},
        {"question": "Que signifie 'Yoko-shiho-gatame' ?", "options": ["Contrôle latéral par les quatre coins", "Contrôle supérieur par les quatre coins", "Immobilisation en écharpe inverse", "Verrou de la jambe"], "answer": "Contrôle latéral par les quatre coins"},
        {"question": "Comment s'appelle l'école originelle fondée par Jigoro Kano à Tokyo ?", "options": ["Le Kodokan", "Le Budokan", "Le Tokai", "Le Shojin"], "answer": "Le Kodokan"},
        {"question": "Que signifie l'expression 'Shin-Gi-Tai' en Judo ?", "options": ["Esprit, Technique, Corps", "Force, Vitesse, Souplesse", "Salut, Respect, Courage", "Attaque, Défense, Contre"], "answer": "Esprit, Technique, Corps"},
        {"question": "Quel mot signifie 'La main gauche' ?", "options": ["Hidarite", "Migite", "Hidari-ashi", "Migi-ashi"], "answer": "Hidarite"},
        {"question": "Quelle est la chute vers l'avant roulée ?", "options": ["Mae-mawari-ukemi (Zenpo-kaiten)", "Mae-ukemi", "Yoko-ukemi", "Ushiro-ukemi"], "answer": "Mae-mawari-ukemi (Zenpo-kaiten)"},
        {"question": "Comment appelle-t-on la manche du judogi ?", "options": ["Sode", "Eri", "Obi", "Zubon"], "answer": "Sode"}
    ],
    "Ceinture Orange": [
        {"question": "Que signifie le terme 'Eri' ?", "options": ["Le revers de la veste", "La manche", "La ceinture", "Le pantalon"], "answer": "Le revers de la veste"},
        {"question": "Quelle technique signifie 'Renversement par la hanche' ?", "options": ["Koshi-guruma", "O-goshi", "Uki-goshi", "Harai-goshi"], "answer": "Koshi-guruma"},
        {"question": "Quelle technique signifie 'Hanche fauchée' ?", "options": ["Harai-goshi", "Koshi-guruma", "Tsurikomi-goshi", "Hane-goshi"], "answer": "Harai-goshi"},
        {"question": "Que signifie 'Kami-shiho-gatame' ?", "options": ["Contrôle supérieur par les quatre coins", "Contrôle arrière par le bas", "Immobilisation latérale inversée", "Écharpe brisée"], "answer": "Contrôle supérieur par les quatre coins"},
        {"question": "Quelle pénalité légère donne l'arbitre en cas de faute ou non-combativité ?", "options": ["Shido", "Hansoku-make", "Chui", "Keikoku"], "answer": "Shido"},
        {"question": "Quelle pénalité grave équivaut à une disqualification directe ?", "options": ["Hansoku-make", "Shido", "Waza-ari", "Ippon"], "answer": "Hansoku-make"},
        {"question": "Combien de Shidos provoquent la disqualification (Hansoku-make) en compétition moderne ?", "options": ["3", "4", "2", "5"], "answer": "3"},
        {"question": "Que signifie 'Sasae-tsurikomi-ashi' ?", "options": ["Blocage du pied en tirant et levant", "Balayage de la jambe d'appui", "Grand fauchage par le bas", "Accrochage du talon"], "answer": "Blocage du pied en tirant et levant"},
        {"question": "Quel mot désigne 'L'esprit de décision' ou la combativité ?", "options": ["Shin", "Kiai", "Ki", "Shiai-jo"], "answer": "Shin"},
        {"question": "Comment appelle-t-on le cri poussé par le judoka pour libérer l'énergie ?", "options": ["Le Kiai", "Le Rei", "Le Matte", "Le Randori"], "answer": "Le Kiai"},
        {"question": "Que signifie 'Migi-sabaki' ?", "options": ["Esquive ou déplacement vers la droite", "Esquive ou déplacement vers la gauche", "Garde haute", "Contre-attaque de hanche"], "answer": "Esquive ou déplacement vers la droite"},
        {"question": "Que signifie 'Hidari-sabaki' ?", "options": ["Esquive ou déplacement vers la gauche", "Esquive ou déplacement vers la droite", "Saisie de manche arrière", "Chute bloquée"], "answer": "Esquive ou déplacement vers la gauche"},
        {"question": "Quelle technique s'appelle 'Le barrage du corps' ?", "options": ["Tai-otoshi", "Ippon-seoi-nage", "Sukui-nage", "Uchi-mata"], "answer": "Tai-otoshi"},
        {"question": "Que signifie 'Uki-goshi' ?", "options": ["Hanche flottante", "Grande hanche", "Hanche fauchée", "Hanche soulevée"], "answer": "Hanche flottante"},
        {"question": "Comment appelle-t-on la zone de combat (surface de tapis) ?", "options": ["Shiai-jo", "Dojo", "Kami-za", "Shimo-za"], "answer": "Shiai-jo"},
        {"question": "Quel terme signifie 'Le côté d'honneur' ou place d'honneur dans le dojo (face aux élèves) ?", "options": ["Kamiza", "Shimoza", "Joseki", "Shimoseki"], "answer": "Kamiza"},
        {"question": "Quel terme désigne le côté opposé à la place d'honneur (où s'installent les élèves) ?", "options": ["Shimoza", "Kamiza", "Joseki", "Shimoseki"], "answer": "Shimoza"},
        {"question": "Que signifie 'Tsubame-gaeshi' ?", "options": ["Le contre de l'hirondelle", "La roue de la fortune", "Le fauchage du héron", "Le sacrifice de l'ours"], "answer": "Le contre de l'hirondelle"},
        {"question": "À quel rang de couleur correspond l'expression 'Ceinture Orange' ?", "options": ["4ème Kyu", "5ème Kyu", "3ème Kyu", "6ème Kyu"], "answer": "4ème Kyu"},
        {"question": "Que signifie 'Kuzure' devant le nom d'une immobilisation (ex: Kuzure-kami-shiho-gatame) ?", "options": ["Variante / Forme modifiée", "Forme fondamentale", "Forme inversée", "Technique interdite"], "answer": "Variante / Forme modifiée"}
    ],
    "Ceinture Verte": [
        {"question": "Comment appelle-t-on les techniques de strangulation / d'étranglement ?", "options": ["Shime-waza", "Kansetsu-waza", "Osaekomi-waza", "Atemi-waza"], "answer": "Shime-waza"},
        {"question": "Comment appelle-t-on les techniques de luxation / clés de bras ?", "options": ["Kansetsu-waza", "Shime-waza", "Nage-waza", "Ne-waza"], "answer": "Kansetsu-waza"},
        {"question": "Sur quelle articulation les clés de bras (Kansetsu-waza) sont-elles exclusivement autorisées en Judo ?", "options": ["Le coude", "Le poignet", "Le genou", "L'épaule"], "answer": "Le coude"},
        {"question": "Quelle technique signifie 'Fauchage intérieur de la cuisse' ?", "options": ["Uchi-mata", "Harai-goshi", "O-uchi-gari", "O-soto-gari"], "answer": "Uchi-mata"},
        {"question": "Que signifie 'Okuri-ashi-barai' ?", "options": ["Balayage des deux pieds (ou balayage envoyé)", "Petit fauchage de côté", "Roue autour de la jambe", "Accrochage intérieur"], "answer": "Balayage des deux pieds (ou balayage envoyé)"},
        {"question": "Quelle technique se traduit par 'Roue autour de la hanche avec action des bras' ?", "options": ["Koshi-guruma", "Kuba-guruma", "O-goshi", "Tsurikomi-goshi"], "answer": "Koshi-guruma"},
        {"question": "Que signifie 'Tate-shiho-gatame' ?", "options": ["Contrôle longitudinal par les quatre coins (à cheval)", "Contrôle en écharpe par le dessus", "Immobilisation par le côté", "Verrou de bras inversé"], "answer": "Contrôle longitudinal par les quatre coins (à cheval)"},
        {"question": "Comment exprime-t-on l'abandon au sol pour signaler que l'on souffre d'un étranglement ou d'une clé ?", "options": ["En frappant deux ou trois coups légers avec la main ou le pied", "En criant 'Matte'", "En levant les bras", "En fermant les yeux"], "answer": "En frappant deux ou trois coups légers avec la main ou le pied"},
        {"question": "Que signifie 'Kata-juji-jime' ?", "options": ["Étranglement croisé normal", "Étranglement par le côté", "Étranglement à l'envers", "Étranglement nu"], "answer": "Étranglement croisé normal"},
        {"question": "Que signifie 'Ude-hishigi-juji-gatame' ?", "options": ["Clé de bras en croix", "Clé de bras par le dessous", "Clé de bras avec l'aisselle", "Luxation du poignet en tournant"], "answer": "Clé de bras en croix"},
        {"question": "Que signifie 'Ko-soto-gari' ?", "options": ["Petit fauchage extérieur", "Grand fauchage extérieur", "Petit fauchage intérieur", "Balayage de côté"], "answer": "Petit fauchage extérieur"},
        {"question": "Que signifie 'Ko-soto-gake' ?", "options": ["Petit accrochage extérieur", "Petit fauchage extérieur", "Grand accrochage intérieur", "Balayage en cuillère"], "answer": "Petit accrochage extérieur"},
        {"question": "Quelle technique de hanche se traduit par 'Hanche pêchée et levée' ?", "options": ["Tsurikomi-goshi", "O-goshi", "Harai-goshi", "Hane-goshi"], "answer": "Tsurikomi-goshi"},
        {"question": "Que signifie le concept d'arbitrage 'Sono-mama' ?", "options": ["Ne bougez plus (gel de la situation au sol)", "Reprenez le combat", "Sortie de tapis", "Fin du temps réglementaire"], "answer": "Ne bougez plus (gel de la situation au sol)"},
        {"question": "Quel terme dit l'arbitre pour relancer le combat après un 'Sono-mama' ?", "options": ["Yoshi", "Hajime", "Matte", "Sore-made"], "answer": "Yoshi"},
        {"question": "À quel rang de classement (Kyu) correspond la Ceinture Verte ?", "options": ["3ème Kyu", "2ème Kyu", "1er Kyu", "4ème Kyu"], "answer": "3ème Kyu"},
        {"question": "Quelle est la première maxime fondamentale du judo énoncée par Jigoro Kano ?", "options": ["Seiryoku Zenyo (Maximum d'efficacité pour un minimum d'effort)", "Jita Kyoei (Entraide et prospérité mutuelle)", "Shin Gi Tai", "Ju no Ri"], "answer": "Seiryoku Zenyo (Maximum d'efficacité pour un minimum d'effort)"},
        {"question": "Quelle est la deuxième maxime fondamentale du judo axée sur la dimension sociale ?", "options": ["Jita Kyoei (Entraide et prospérité mutuelle)", "Seiryoku Zenyo", "Bushido", "Reishiki"], "answer": "Jita Kyoei (Entraide et prospérité mutuelle)"},
        {"question": "Que signifie 'Sode-tsurikomi-goshi' ?", "options": ["Technique de hanche en chargeant par la manche", "Fauchage de manche", "Projection d'épaule croisée", "Sacrifice par le bras"], "answer": "Technique de hanche en chargeant par la manche"},
        {"question": "Que signifie 'Renraku-waza' ?", "options": ["Enchaînement de techniques", "Contre-attaque", "Esquive latérale", "Travail statique"], "answer": "Enchaînement de techniques"}
    ],
    "Ceinture Bleue": [
        {"question": "Comment appelle-t-on les techniques de sacrifice (où Tori sacrifie son équilibre) ?", "options": ["Sutemi-waza", "Tachi-waza", "Te-waza", "Koshi-waza"], "answer": "Sutemi-waza"},
        {"question": "Dans les Sutemi-waza, comment qualifie-t-on les sacrifices dans l'axe (sur le dos) ?", "options": ["Ma-sutemi-waza", "Yoko-sutemi-waza", "Koshi-waza", "Ashi-waza"], "answer": "Ma-sutemi-waza"},
        {"question": "Dans les Sutemi-waza, comment qualifie-t-on les sacrifices sur le côté ?", "options": ["Yoko-sutemi-waza", "Ma-sutemi-waza", "Te-waza", "Ne-waza"], "answer": "Yoko-sutemi-waza"},
        {"question": "Quelle technique signifie 'Projection en planche de salut' (sacrifice de face, pied à la ceinture) ?", "options": ["Tomoe-nage", "Ura-nage", "Sumi-gaeshi", "Yoko-gake"], "answer": "Tomoe-nage"},
        {"question": "Quelle technique signifie 'Renversement dans le coin' ?", "options": ["Sumi-gaeshi", "Tomoe-nage", "Hik込み-gaeshi", "Tani-otoshi"], "answer": "Sumi-gaeshi"},
        {"question": "Que signifie 'Ushiro-goshi' ?", "options": ["Hanche arrière (contre de hanche)", "Fauchage arrière", "Grande projection par le haut", "Contre d'épaule"], "answer": "Hanche arrière (contre de hanche)"},
        {"question": "Que signifie 'Ude-hishigi-waki-gatame' ?", "options": ["Clé de bras contrôlée par l'aisselle", "Clé de bras en croix", "Clé de bras avec le genou", "Luxation du poignet en tournant"], "answer": "Clé de bras contrôlée par l'aisselle"},
        {"question": "Que signifie 'Hadaka-jime' ?", "options": ["Étranglement nu (par l'avant-bras sans le tissu)", "Étranglement croisé", "Étranglement par la veste", "Étranglement avec les jambes"], "answer": "Étranglement nu (par l'avant-bras sans le tissu)"},
        {"question": "Que signifie 'Okuri-eri-jime' ?", "options": ["Étranglement par les revers coulissants", "Étranglement à mains nues", "Étranglement en croix", "Clé de cou"], "answer": "Étranglement par les revers coulissants"},
        {"question": "Que signifie 'Kaeshi-waza' ?", "options": ["Les contre-attaques / contres", "Les feintes", "Les combinaisons de techniques", "Les projections de jambes"], "answer": "Les contre-attaques / contres"},
        {"question": "Quelle technique se traduit par 'Chute dans la vallée' (sacrifice de côté) ?", "options": ["Tani-otoshi", "Yoko-otoshi", "Soto-makikomi", "Ura-nage"], "answer": "Tani-otoshi"},
        {"question": "Que signifie 'Yoko-guruma' ?", "options": ["Roue latérale", "Roue autour de la hanche", "Balayage de côté", "Grand sacrifice"], "answer": "Roue latérale"},
        {"question": "Que désigne le terme 'Kata' en Judo ?", "options": ["Forme codifiée d'exercices / Enchaînement traditionnel", "Le combat d'entraînement libre", "La tenue officielle de compétition", "Le tableau des scores"], "answer": "Forme codifiée d'exercices / Enchaînement traditionnel"},
        {"question": "Quel est le nom du grand Kata des projections ?", "options": ["Nage-no-kata", "Katame-no-kata", "Ju-no-kata", "Kime-no-kata"], "answer": "Nage-no-kata"},
        {"question": "Combien de groupes de techniques comporte le Nage-no-kata ?", "options": ["5 groupes", "3 groupes", "4 groupes", "6 groupes"], "answer": "5 groupes"},
        {"question": "À quel rang (Kyu) correspond la Ceinture Bleue ?", "options": ["2ème Kyu", "3ème Kyu", "1er Kyu", "5ème Kyu"], "answer": "2ème Kyu"},
        {"question": "Que signifie 'Hane-goshi' ?", "options": ["Hanche bondissante / Hanche percutée", "Hanche balayée", "Hanche soulevée", "Petite hanche intérieure"], "answer": "Hanche bondissante / Hanche percutée"},
        {"question": "Que signifie 'Ushironano-jime' (ou Ushiro-jime) ?", "options": ["Étranglement arrière", "Étranglement de face", "Clé de bras inversée", "Immobilisation sur le ventre"], "answer": "Étranglement arrière"},
        {"question": "Que signifie 'Ude-garami' ?", "options": ["Clé de bras par enroulement (verrou de bras)", "Clé de coude directe en extension", "Étranglement par la manche", "Immobilisation faciale"], "answer": "Clé de bras par enroulement (verrou de bras)"},
        {"question": "Quel mot japonais définit le code moral ou la conduite du combattant ?", "options": ["Bushido", "Reishiki", "Kata", "Sempai"], "answer": "Bushido"}
    ],
    "Ceinture Marron": [
        {"question": "Quelle technique se traduit par 'Projection arrière' (Tori passe sous Uke et le jette sur le dos) ?", "options": ["Ura-nage", "Tomoe-nage", "Tani-otoshi", "Yoko-gake"], "answer": "Ura-nage"},
        {"question": "Que signifie 'O-soto-guruma' ?", "options": ["Grande roue extérieure", "Grand fauchage extérieur", "Grande hanche enroulée", "Contre de jambe"], "answer": "Grande roue extérieure"},
        {"question": "Que signifie 'Uchi-makikomi' ?", "options": ["Enroulement intérieur", "Enroulement extérieur", "Fauchage intérieur de cuisse", "Sacrifice de face"], "answer": "Enroulement intérieur"},
        {"question": "Que signifie 'Soto-makikomi' ?", "options": ["Enroulement extérieur", "Enroulement intérieur", "Projection par la manche", "Barrage du corps"], "answer": "Enroulement extérieur"},
        {"question": "Quel est le nom du Kata des techniques de contrôle au sol ?", "options": ["Katame-no-kata", "Nage-no-kata", "Ju-no-kata", "Itsutsu-no-kata"], "answer": "Katame-no-kata"},
        {"question": "Combien de catégories compose le Katame-no-kata ?", "options": ["3 (Osaekomi, Shime, Kansetsu)", "2 (Nage, Ne-waza)", "5", "4"], "answer": "3 (Osaekomi, Shime, Kansetsu)"},
        {"question": "Que signifie 'Yoko-gake' ?", "options": ["Accrochage latéral", "Fauchage latéral", "Roue de côté", "Chute de côté"], "answer": "Accrochage latéral"},
        {"question": "Que signifie 'Kata-ha-jime' ?", "options": ["Étranglement par contrôle d'une aile (un bras contrôlé en l'air)", "Étranglement croisé à l'envers", "Étranglement par le revers", "Clé de coude croisée"], "answer": "Étranglement par contrôle d'une aile (un bras contrôlé en l'air)"},
        {"question": "Que signifie 'Sankaku-jime' ?", "options": ["Étranglement en triangle (avec les jambes)", "Étranglement nu", "Étranglement par les deux revers", "Clé de bras en extension"], "answer": "Étranglement en triangle (avec les jambes)"},
        {"question": "Que signifie 'Ude-hishigi-hara-gatame' ?", "options": ["Clé de bras contrôlée par le ventre", "Clé de bras contrôlée par l'aisselle", "Clé de bras en croix", "Luxation avec le genou"], "answer": "Clé de bras contrôlée par le ventre"},
        {"question": "Que signifie 'Ude-hishigi-hiza-gatame' ?", "options": ["Clé de bras avec l'aide du genou", "Clé de bras sur le ventre", "Clé de coude directe en extension", "Étranglement par la jambe"], "answer": "Clé de bras avec l'aide du genou"},
        {"question": "À quel rang (Kyu) correspond la Ceinture Marron ?", "options": ["1er Kyu", "2ème Kyu", "3ème Kyu", "1er Dan"], "answer": "1er Kyu"},
        {"question": "Quel grade vient immédiatement après la Ceinture Marron ?", "options": ["Ceinture Noire 1er Dan (Shodan)", "Ceinture Violette", "Ceinture Noire-Blanche", "Ceinture Rouge"], "answer": "Ceinture Noire 1er Dan (Shodan)"},
        {"question": "Quel terme signifie 'Le vainqueur' annoncé par l'arbitre en fin de combat ?", "options": ["Kachi", "Hajime", "Sore-made", "Ippon"], "answer": "Kachi"},
        {"question": "Que signifie 'Sumi-otoshi' ?", "options": ["Chute dans le coin / Renversement dans l'angle", "Grand fauchage", "Balayage d'appui", "Roue de hanche arrière"], "answer": "Chute dans le coin / Renversement dans l'angle"},
        {"question": "Quelle technique signifie 'Ramassage des deux jambes' (aujourd'hui interdite en saisie directe en compétition moderne) ?", "options": ["Morote-gari", "Kuchiki-taoshi", "Kibisu-gaeshi", "Sukui-nage"], "answer": "Morote-gari"},
        {"question": "Que signifie 'Sukui-nage' ?", "options": ["Projection en cuillère", "Projection par l'épaule", "Enroulement de hanche", "Accrochage du talon"], "answer": "Projection en cuillère"},
        {"question": "Qu'est-ce que le 'Gokyo' (ou Gokyo-no-waza) en Judo ?", "options": ["Le programme officiel originel des 40 projections du Judo classées en 5 groupes", "Le code d'arbitrage international", "Le recueil des techniques de clés", "Le règlement intérieur du dojo"], "answer": "Le programme officiel originel des 40 projections du Judo classées en 5 groupes"},
        {"question": "Que signifie 'Te-guruma' ?", "options": ["Roue par les mains (enroulement par les jambes)", "Fauchage d'épaule", "Accrochage intérieur de cuisse", "Contre de hanche flottante"], "answer": "Roue par les mains (enroulement par les jambes)"},
        {"question": "Que signifie 'Tokui-waza' ?", "options": ["La technique favorite / spéciale d'un judoka", "La technique interdite", "La technique fondamentale", "La chute avant parfaite"], "answer": "La technique favorite / spéciale d'un judoka"}
    ]
}

BELT_ORDER = [
    "Ceinture Blanche-Jaune", 
    "Ceinture Jaune", 
    "Ceinture Jaune-Orange", 
    "Ceinture Orange", 
    "Ceinture Verte", 
    "Ceinture Bleue", 
    "Ceinture Marron"
]

# --- INITIALISATION DE L'APPLICATION STREAMLIT ---
st.set_page_config(page_title="Quiz Judo Ceintures", page_icon="🥋", layout="centered")
st.primaryColor = "#FF4B4B" # Optionnel
st.showButton = False

if "theme" not in st.session_state:
    st.session_state.theme = "dark"

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

theme_label = "☀️ Mode clair" if st.session_state.theme == "dark" else "🌙 Mode sombre"
col1, col2 = st.columns([9, 1])
with col1:
    st.title("🥋 Quiz Interactif de Progression des Ceintures")
with col2:
    st.button(theme_label, key="theme_button", on_click=toggle_theme)

if st.session_state.theme == "dark":
    page_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .viewerBadge_container__1QSob {display: none !important;}
    body, .main, .block-container, .stApp {
        background-color: #0d1117 !important;
        color: #e5e7eb !important;
    }
    section[data-testid="stSidebar"] {
        background-color: #111827 !important;
        color: #e5e7eb !important;
    }
    div.stButton>button, button[kind="primary"] {
        background-color: #1f2937 !important;
        color: #f9fafb !important;
        border-color: #374151 !important;
    }
    </style>
    """
else:
    page_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .viewerBadge_container__1QSob {display: none !important;}
    body, .main, .block-container, .stApp {
        background-color: #f8fafc !important;
        color: #111827 !important;
    }
    section[data-testid="stSidebar"] {
        background-color: #ffffff !important;
        color: #111827 !important;
    }
    div.stButton>button, button[kind="primary"] {
        background-color: #e2e8f0 !important;
        color: #111827 !important;
        border-color: #cbd5e1 !important;
    }
    </style>
    """

st.markdown(page_style, unsafe_allow_html=True)

st.write("Évaluez vos connaissances théoriques du judo. Chaque niveau inclut ses questions ainsi que celles des ceintures précédentes !")

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
    st.session_state.current_questions = []
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.user_answers = []

# --- ÉCRAN DE CONFIGURATION (AVANT DE COMMENCER) ---
if not st.session_state.quiz_started:
    st.subheader("Configuration de votre test")
    
    target_belt = st.selectbox("Sélectionnez la ceinture que vous préparez :", BELT_ORDER)
    num_q = st.slider("Nombre de questions pour le quiz :", min_value=5, max_value=20, value=10, step=5)
    
    if st.button("🥋 Hajime !", type="primary"):
        pool_questions = []
        for belt in BELT_ORDER:
            pool_questions.extend(QUIZ_DATA[belt])
            if belt == target_belt:
                break
        
        num_q = min(num_q, len(pool_questions))
        selected_questions = random.sample(pool_questions, num_q)
        
        game_questions = []
        for q in selected_questions:
            shuffled_opts = list(q["options"])
            random.shuffle(shuffled_opts)
            game_questions.append({
                "txt_question": q["question"],
                "shuffled_options": shuffled_opts,
                "txt_answer": q["answer"]
            })
            
        st.session_state.current_questions = game_questions
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.user_answers = [] 
        st.session_state.quiz_started = True
        st.rerun()

# --- ÉCRAN DE JEU (SÉQUENTIEL & SÉCURISÉ CÔTÉ STRING) ---
else:
    idx = st.session_state.current_index
    questions = st.session_state.current_questions
    
    if idx < len(questions):
        current_q = questions[idx]
        
        st.progress(idx / len(questions), text=f"Question {idx + 1} sur {len(questions)}")
        st.markdown(f"### 🤔 {current_q['txt_question']}")
        st.write("Cliquez directement sur votre réponse ci-dessous :")
        
        chosen_option = None
        for option in current_q['shuffled_options']:
            if st.button(option, key=f"btn_q{idx}_{hash(option)}", use_container_width=True):
                chosen_option = option

        if chosen_option is not None:
            correct_answer = current_q["txt_answer"]
            
            # 🛠️ CORRECTION DU SIÈCLE : Nettoyage absolu des chaînes de caractères
            # Supprime les espaces normaux, les espaces insécables (\xa0) et passe en minuscules
            clean_choice = chosen_option.replace(" ", "").replace("\xa0", "").lower()
            clean_answer = correct_answer.replace(" ", "").replace("\xa0", "").lower()
            is_correct = (clean_choice == clean_answer)
            
            st.session_state.user_answers.append({
                "q_text": str(current_q["txt_question"]),
                "u_choice": str(chosen_option),
                "c_answer": str(correct_answer),
                "is_ok": bool(is_correct)
            })
            
            if is_correct:
                st.session_state.score += 1
                
            st.session_state.current_index += 1
            st.rerun()
                
    # --- ÉCRAN DE RÉSULTATS (FIN DU QUIZ) ---
    else:
        st.balloons()
        st.subheader("🏁 Quiz Terminé ! Sore-Made !")
        
        score = st.session_state.score
        total = len(questions)
        percentage = (score / total) * 100
        
        st.metric(label="Votre Score Final", value=f"{score} / {total}", delta=f"{percentage:.1f}% d'exactitude")
        
        if percentage == 100:
            st.success("🏆 Magnifique ! IPPON ! Vous maîtrisez parfaitement votre sujet historique et technique.")
        elif percentage >= 75:
            st.info("👍 WAZA-ARI ! Très bonne performance, vous êtes prêt pour l'examen de grade.")
        elif percentage >= 50:
            st.warning("🥋 YUKO. C'est un passage, mais il reste quelques déséquilibres (Kuzushi) dans vos révisions.")
        else:
            st.error("❌ SHIDO ! Pénalité pour manque de révisions. Retournez travailler vos bases sur le tatami !")
            
        st.markdown("### 📋 Analyse de vos combats (réponses)")
        
        for i, record in enumerate(st.session_state.user_answers):
            with st.expander(f"Question {i+1} : {record['q_text']}"):
                if record['is_ok']:
                    st.success(f"✅ **Correct !** Votre réponse : {record['u_choice']}")
                else:
                    st.error(f"❌ **Incorrect.** Vous avez répondu : *{record['u_choice']}*")
                    st.info(f"💡 La bonne réponse était : **{record['c_answer']}**")
        
        if st.button("🔄 Recommencer un nouveau Quiz", type="primary"):
            st.session_state.quiz_started = False
            st.session_state.user_answers = [] 
            st.rerun()
