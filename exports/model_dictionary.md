
### Documentation du modèle prédictif

**Objectif :** Prédire le montant final ('final_amount') d'une commande.

**Variable Cible :** `final_amount`

**Variables Prédictives :** ['product_category', 'quantity', 'unit_price', 'customer_age', 'customer_region', 'shipping_cost', 'discount_applied']

**Modèle de Base :** Régression Linéaire

**Métriques de Performance de Base :**
- RMSE : 72.86
- R-squared : 0.89

**Critères de succès (Exemples) :**
- Atteindre un R-squared > 0.85 avec un modèle plus avancé (ex: Gradient Boosting).
- Le RMSE doit être inférieur à 10% de la valeur moyenne des commandes.
- Les variables les plus importantes identifiées par le modèle doivent être logiques d'un point de vue commercial.

**Prochaines étapes :**
- Tester des modèles plus complexes (Random Forest, Gradient Boosting).
- Optimiser les hyperparamètres des modèles.
- Analyser l'importance des variables pour comprendre les moteurs du montant des commandes.
