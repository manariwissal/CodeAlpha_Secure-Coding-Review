Rapport — Secure Coding Review (TASK 3)

Date : 26/09/2025
Auditeur : Wissal

1. Contexte & portée

Langage : Python 3.13.3

Application audité : app.py (vulnérable) et app_fixed.py (corrigé)

Objectif : Identifier et corriger les vulnérabilités de sécurité, valider les corrections et documenter les preuves.

2. Étapes réalisées

Sélection du langage et application : Python et fichier app.py.

Audit du code :

Inspection manuelle : lignes de code vulnérables à l’injection SQL (concaténation de chaînes).

Analyse statique avec Bandit (avant et après correction).

Tests unitaires avec pytest pour valider le fonctionnement et la sécurité.

Correction du code :

Requêtes paramétrées pour éviter SQL Injection.

Hash des mots de passe avec bcrypt.

Documentation et recommandations : résumé des findings et bonnes pratiques.

3. Preuve — audit Bandit
3.1 Avant correction (app.py)
>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
   Severity: Medium   Confidence: Low
   CWE: CWE-89
   Location: .\app.py:7:12


Interprétation : SQL Injection possible via concaténation des inputs utilisateur dans la requête.

3.2 Après correction (app_fixed.py)
No issues identified.


Interprétation : Le code corrigé n’a plus de vulnérabilités détectées par Bandit.

4. Preuve — tests unitaires (pytest)
...                                                                      [100%]
3 passed in 1.23s


Les tests couvrent :

Authentification avec mot de passe correct (succès)

Authentification avec mot de passe incorrect (échec)

Tentative d’injection SQL (échec)

5. Changements appliqués pour sécuriser le code

Utilisation de requêtes paramétrées pour toutes les requêtes SQL.

Stockage sécurisé des mots de passe avec bcrypt.

Fermeture sécurisée des connexions SQLite.

Ajout de tests unitaires pour valider les corrections.

6. Recommandations & bonnes pratiques

Ne jamais construire de requêtes SQL par concaténation.

Hasher les mots de passe avec bcrypt ou Argon2.

Ajouter un rate limiting pour prévenir les attaques par force brute.

Activer des logs d’audit pour les connexions réussies et échouées.

Protéger les fichiers de base de données (permissions strictes).

Migrer vers un SGBD serveur pour la production multi-utilisateur.

Exécuter Bandit + pytest dans un pipeline CI/CD pour analyse continue.

Maintenir les dépendances à jour (pip-audit, safety, bcrypt).

7. Conclusion

La vulnérabilité SQL Injection dans app.py a été identifiée et corrigée.

Après correction (app_fixed.py), Bandit n’a trouvé aucune issue et tous les tests unitaires sont passés.

Le code est désormais sécurisé et suit les bonnes pratiques de codage sécurisé.

8. Livrables

app.py (vulnérable)

app_fixed.py (corrigé)

app_secure.py (exemple sécurisé)

create_db.py (création DB)

users.db (SQLite de test)

test_auth.py (tests pytest)

bandit_before.txt, bandit_after.txt, pytest_output.txt (preuves)

report.md (ce fichier)