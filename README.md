▌Écrire une fonction qui génère une paire de clé asymétrique RSA de 2048 bits (clé publique 
Pub1 + clé privée Priv1)

 ▌Écrire une fonction qui prend un message en entrée et qui produit une signature de ce 
message

 ▌Écrire un petit programme qui enchaîne les fonctions suivantes
 
 ▪ Etape 1
 • Concaténation de « Bonjour le monde ! » et de la clé publique Pub1 → Message1
 • Calcul du haché de Message1 → Haché1.1
 • Signature de Haché1.1 → Signature 1
 • Calcul du haché de Signature 1 → Haché1.2
 
 ▪ Etape 2
 • Concaténation du Haché1.2 et de la clé publique Pub1 → Message2
 • Calcul du haché de Message2 → Haché2.1
 • Signature de Haché2.1 → Signature2
 • Calcul du haché de Signature2 → Haché2.2
 
 ▪ Etape 3
 • Concaténation du Haché2.2 et de la clé publique Pub1 → Message3
 • Calcul du haché de Message3 → Haché3.1
 • Signature de Haché3.1 → Signature3
 • Calcul du haché de Signature3 → Haché3.3
 ▪ Afficher Haché3.3
