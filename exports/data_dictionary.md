
### Dictionnaire de données

| Colonne | Description | Type de données |
|---|---|---|
| order_id | Identifiant unique de la commande | object (string) |
| customer_id | Identifiant unique du client | object (string) |
| product_category | Catégorie du produit acheté | object (string) |
| product_name | Nom du produit | object (string) |
| quantity | Nombre d'unités du produit achetées | int64 |
| unit_price | Prix unitaire du produit | float64 |
| order_date | Date à laquelle la commande a été passée | datetime64[ns] |
| customer_age | Âge du client au moment de la commande | int64 |
| customer_region | Région géographique du client | object (string) |
| shipping_cost | Coût de la livraison pour la commande | float64 |
| discount_applied | Pourcentage de remise appliqué | int64 |
| total_amount | Montant total avant remise et livraison (quantity * unit_price) | float64 |
| discounted_amount | Montant après application de la remise | float64 |
| final_amount | Montant final payé par le client (discounted_amount + shipping_cost) | float64 |
| order_month | Mois de la commande (1-12) | int64 |
| order_quarter | Trimestre de la commande (1-4) | int64 |
| age_group | Groupe d'âge du client | category |
| discount_amount | Montant de la remise en devise | float64 |
