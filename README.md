<<<<<<< HEAD
# ProCLI

Application de gestion médicale et administrative développée avec Django, Django REST Framework et Celery.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-6.0.1-success)
![DRF](https://img.shields.io/badge/Django_REST_Framework-API-red)
![Celery](https://img.shields.io/badge/Celery-Asynchrone-green)
![SQLite](https://img.shields.io/badge/SQLite-Development-lightgrey)

---

## Présentation

ProCLI est une plateforme modulaire de gestion hospitalière permettant d'assurer le suivi administratif et médical des patients. Elle centralise la gestion des rendez-vous, consultations, prescriptions, facturations et dossiers médicaux au sein d'une seule application.

Le projet est conçu selon une architecture Django modulaire afin de faciliter l'évolution, la maintenance et les tests.

---

## Fonctionnalités principales

### Gestion des comptes

* Authentification des patients par OTP
* Création de compte patient
* Authentification JWT
* Gestion des groupes et permissions

### Gestion des patients

* Enregistrement des patients
* Consultation de l'historique médical
* Accès sécurisé aux informations personnelles

### Gestion des rendez-vous

* Création et suivi des rendez-vous
* Recherche AJAX
* Filtrage avancé
* Notifications automatiques

### Gestion des consultations

* Enregistrement des consultations médicales
* Historique des consultations
* Accès restreint selon les rôles

### Gestion des prescriptions

* Création des prescriptions médicales
* Gestion des lignes de prescription
* Consultation détaillée des traitements prescrits

### Gestion de la facturation

* Génération automatique des factures
* Calcul du montant total
* Consultation des détails de facturation

### Dossier médical

* Centralisation des données médicales du patient
* Historique des consultations associées

### Notifications

* Rappels automatiques des rendez-vous via Celery

---

## Modules du projet

```text
ProCLI
│
├── comptes
├── patient
├── medecin
├── departement
├── rendez_vous
├── consultations
├── dossier_medical
├── prescriptions
├── facturations
├── paiements
├── apis
│
└── pro_cli
    ├── settings.py
    ├── urls.py
    ├── celery.py
    ├── wsgi.py
    └── asgi.py
```

---

## Description des applications

| Application     | Description                                            |
| --------------- | ------------------------------------------------------ |
| comptes         | Authentification, OTP, tableau de bord, administration |
| patient         | Gestion des patients et de leur historique             |
| medecin         | Gestion des médecins                                   |
| departement     | Gestion des services médicaux                          |
| rendez_vous     | Gestion des rendez-vous                                |
| consultations   | Gestion des consultations                              |
| dossier_medical | Gestion des dossiers médicaux                          |
| prescriptions   | Gestion des prescriptions                              |
| facturations    | Gestion des factures                                   |
| paiements       | Module en cours de développement                       |
| apis            | Permissions et services REST complémentaires           |

---

## Architecture fonctionnelle

```text
Patient
    ↓
RendezVous
    ↓
Consultation
    ↓
Prescription
    ↓
LignePrescription

Consultation
    ↓
Facture
    ↓
DetailFacture

Patient
    ↓
DossierMedical
```

---

## Rôles utilisateurs

| Rôle           | Permissions                           |
| -------------- | ------------------------------------- |
| Administrateur | Gestion complète du système           |
| Réceptionniste | Gestion des rendez-vous               |
| Médecin        | Consultations et prescriptions        |
| Comptable      | Facturation                           |
| Patient        | Consultation de ses données médicales |

---

## Technologies utilisées

* Python 3.x
* Django 6.0.1
* Django REST Framework
* djangorestframework-simplejwt
* django-filters
* Celery
* django-celery-beat
* Jazzmin
* SQLite (développement)
* PostgreSQL recommandé pour la production
* RabbitMQ
* django-cors-headers

---

## Sécurité

Le projet intègre plusieurs mécanismes de sécurité :

* Authentification JWT via `rest_framework_simplejwt`
* Permissions DRF globales : `IsAuthenticated`
* Endpoints OTP accessibles avec `AllowAny`
* OTP avec expiration et indicateur `is_used`
* Validation des mots de passe Django
* Protection CSRF
* Middleware de sécurité Django
* Protection contre le clickjacking
* Backend personnalisé :

  * `comptes.backends.EmailBackend`
  * Backend Django standard
* Permissions métier :

  * `IsMedecin`
  * `IsReceptionniste`
  * `IsComptable`

> **Important :**
>
> En environnement de production, désactiver `DEBUG`, utiliser une clé secrète sécurisée et configurer correctement `ALLOWED_HOSTS`.

---

## Optimisation des performances

Le projet utilise plusieurs techniques d'optimisation :

* `select_related('patient', 'medecin')`
* `prefetch_related('lignes')`
* `prefetch_related('details_facture')`
* Filtres Django (`django_filters`)
* Index SQL sur les champs fréquemment utilisés
* Restriction des données selon l'utilisateur connecté

---

## API REST

### Authentification OTP

#### POST `/api/envoyer/otp/`

Payload :

```json
{
    "telephone": "...",
    "numero_patient": "..."
}
```

Réponse :

```json
{
    "otp_id": 1,
    "message": "OTP envoyé.",
    "otp": "123456"
}
```

---

#### POST `/api/verify-otp/`

Payload :

```json
{
    "otp_id": 1,
    "otp": "123456",
    "password": "motdepasse",
    "password_confirm": "motdepasse"
}
```

Réponse :

```json
{
    "access": "...",
    "refresh": "...",
    "message": "Compte créé avec succès."
}
```

---

#### POST `/api/token/refresh/`

Payload :

```json
{
    "refresh": "<refresh_token>"
}
```

Réponse :

```json
{
    "access": "<new_access_token>"
}
```

---

### Consultations

#### GET `/api/consultations/`

Filtres disponibles :

* date
* date_from
* date_to

Retour :

Liste des consultations du patient connecté.

---

#### GET `/api/consultations/<pk>/`

Retour :

Détail d'une consultation.

---

### Rendez-vous

#### GET `/api/rendez-vous/`

Filtres disponibles :

* date
* date_from
* date_to
* departement

Retour :

Liste des rendez-vous réservés.

---

#### GET `/api/rendez-vous/<pk>/`

Retour :

Détail d'un rendez-vous.

---

### Facturations

#### GET `/api/facturations/`

Filtres disponibles :

* medecin
* date_du
* date_au
* date

Retour :

Factures avec :

* médecin
* détails de facture
* montant total

---

#### GET `/api/facturations/<pk>/`

Retour :

Détail d'une facture.

---

### Prescriptions

#### GET `/api/prescriptions/`

Filtres disponibles :

* medecin
* date_du
* date_au
* date
* departement

Retour :

Prescriptions avec :

* médecin
* consultation
* lignes de prescription

---

#### GET `/api/prescriptions/<pk>/`

Retour :

Détail d'une prescription.

---

### Dossier médical

Les consultations liées au dossier médical du patient connecté sont accessibles via les endpoints dédiés aux consultations selon les permissions applicables.

---

## Routes API enregistrées

Le routeur principal est défini dans `pro_cli/urls.py` :

```python
path('api/', include('comptes.api.urls'))
path('api/', include('facturations.api.urls'))
path('api/', include('prescriptions.api.urls'))
path('api/', include('consultations.api.urls'))
path('api/', include('rendez_vous.api.urls'))
```

---

## Installation rapide

### 1. Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/procli.git

cd procli
```

### 2. Créer un environnement virtuel

#### Linux / macOS

```bash
python -m venv env

source env/bin/activate
```

#### Windows

```bash
python -m venv env

env\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Appliquer les migrations

```bash
python manage.py migrate
```

### 5. Créer un superutilisateur

```bash
python manage.py createsuperuser
```

### 6. Démarrer le serveur

```bash
python manage.py runserver
```

---

## Celery et RabbitMQ

Démarrer le worker :

```bash
celery -A pro_cli worker --loglevel=info
```

Démarrer Celery Beat :

```bash
celery -A pro_cli beat --loglevel=info
```

---

## Variables d'environnement recommandées

Créer un fichier `.env` :

```env
SECRET_KEY=your-secret-key

DEBUG=False

ALLOWED_HOSTS=localhost,127.0.0.1

RABBITMQ_URL=amqp://guest:guest@localhost:5672//

EMAIL_HOST=

EMAIL_PORT=
```

---



## Évolutions prévues

* Finalisation du module de paiements
* Passage à PostgreSQL en production
* Ajout de tests automatisés
* Documentation Swagger/OpenAPI
* Déploiement Docker
* Journalisation avancée
* Tableau de bord analytique

---

## Notes utiles

* `EMAIL_BACKEND` utilise actuellement le backend console pour le développement.
* `JWTAuthentication` est configurée globalement.
* Les API OTP sont volontairement ouvertes avec `AllowAny`.
* Les modèles principaux utilisent des index pour améliorer les performances.


=======
# ProCLI

Application de gestion médicale et administrative développée avec Django, Django REST Framework et Celery.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-6.0.1-success)
![DRF](https://img.shields.io/badge/Django_REST_Framework-API-red)
![Celery](https://img.shields.io/badge/Celery-Asynchrone-green)
![SQLite](https://img.shields.io/badge/SQLite-Development-lightgrey)

---

## Présentation

ProCLI est une plateforme modulaire de gestion hospitalière permettant d'assurer le suivi administratif et médical des patients. Elle centralise la gestion des rendez-vous, consultations, prescriptions, facturations et dossiers médicaux au sein d'une seule application.

Le projet est conçu selon une architecture Django modulaire afin de faciliter l'évolution, la maintenance et les tests.

---

## Fonctionnalités principales

### Gestion des comptes

* Authentification des patients par OTP
* Création de compte patient
* Authentification JWT
* Gestion des groupes et permissions

### Gestion des patients

* Enregistrement des patients
* Consultation de l'historique médical
* Accès sécurisé aux informations personnelles

### Gestion des rendez-vous

* Création et suivi des rendez-vous
* Recherche AJAX
* Filtrage avancé
* Notifications automatiques

### Gestion des consultations

* Enregistrement des consultations médicales
* Historique des consultations
* Accès restreint selon les rôles

### Gestion des prescriptions

* Création des prescriptions médicales
* Gestion des lignes de prescription
* Consultation détaillée des traitements prescrits

### Gestion de la facturation

* Génération automatique des factures
* Calcul du montant total
* Consultation des détails de facturation

### Dossier médical

* Centralisation des données médicales du patient
* Historique des consultations associées

### Notifications

* Rappels automatiques des rendez-vous via Celery

---

## Modules du projet

```text
ProCLI
│
├── comptes
├── patient
├── medecin
├── departement
├── rendez_vous
├── consultations
├── dossier_medical
├── prescriptions
├── facturations
├── paiements
├── apis
│
└── pro_cli
    ├── settings.py
    ├── urls.py
    ├── celery.py
    ├── wsgi.py
    └── asgi.py
```

---

## Description des applications

| Application     | Description                                            |
| --------------- | ------------------------------------------------------ |
| comptes         | Authentification, OTP, tableau de bord, administration |
| patient         | Gestion des patients et de leur historique             |
| medecin         | Gestion des médecins                                   |
| departement     | Gestion des services médicaux                          |
| rendez_vous     | Gestion des rendez-vous                                |
| consultations   | Gestion des consultations                              |
| dossier_medical | Gestion des dossiers médicaux                          |
| prescriptions   | Gestion des prescriptions                              |
| facturations    | Gestion des factures                                   |
| paiements       | Module en cours de développement                       |
| apis            | Permissions et services REST complémentaires           |

---

## Architecture fonctionnelle

```text
Patient
    ↓
RendezVous
    ↓
Consultation
    ↓
Prescription
    ↓
LignePrescription

Consultation
    ↓
Facture
    ↓
DetailFacture

Patient
    ↓
DossierMedical
```

---

## Rôles utilisateurs

| Rôle           | Permissions                           |
| -------------- | ------------------------------------- |
| Administrateur | Gestion complète du système           |
| Réceptionniste | Gestion des rendez-vous               |
| Médecin        | Consultations et prescriptions        |
| Comptable      | Facturation                           |
| Patient        | Consultation de ses données médicales |

---

## Technologies utilisées

* Python 3.x
* Django 6.0.1
* Django REST Framework
* djangorestframework-simplejwt
* django-filters
* Celery
* django-celery-beat
* Jazzmin
* SQLite (développement)
* PostgreSQL recommandé pour la production
* RabbitMQ
* django-cors-headers

---

## Sécurité

Le projet intègre plusieurs mécanismes de sécurité :

* Authentification JWT via `rest_framework_simplejwt`
* Permissions DRF globales : `IsAuthenticated`
* Endpoints OTP accessibles avec `AllowAny`
* OTP avec expiration et indicateur `is_used`
* Validation des mots de passe Django
* Protection CSRF
* Middleware de sécurité Django
* Protection contre le clickjacking
* Backend personnalisé :

  * `comptes.backends.EmailBackend`
  * Backend Django standard
* Permissions métier :

  * `IsMedecin`
  * `IsReceptionniste`
  * `IsComptable`

> **Important :**
>
> En environnement de production, désactiver `DEBUG`, utiliser une clé secrète sécurisée et configurer correctement `ALLOWED_HOSTS`.

---

## Optimisation des performances

Le projet utilise plusieurs techniques d'optimisation :

* `select_related('patient', 'medecin')`
* `prefetch_related('lignes')`
* `prefetch_related('details_facture')`
* Filtres Django (`django_filters`)
* Index SQL sur les champs fréquemment utilisés
* Restriction des données selon l'utilisateur connecté

---

## API REST

### Authentification OTP

#### POST `/api/envoyer/otp/`

Payload :

```json
{
    "telephone": "...",
    "numero_patient": "..."
}
```

Réponse :

```json
{
    "otp_id": 1,
    "message": "OTP envoyé.",
    "otp": "123456"
}
```

---

#### POST `/api/verify-otp/`

Payload :

```json
{
    "otp_id": 1,
    "otp": "123456",
    "password": "motdepasse",
    "password_confirm": "motdepasse"
}
```

Réponse :

```json
{
    "access": "...",
    "refresh": "...",
    "message": "Compte créé avec succès."
}
```

---

#### POST `/api/token/refresh/`

Payload :

```json
{
    "refresh": "<refresh_token>"
}
```

Réponse :

```json
{
    "access": "<new_access_token>"
}
```

---

### Consultations

#### GET `/api/consultations/`

Filtres disponibles :

* date
* date_from
* date_to

Retour :

Liste des consultations du patient connecté.

---

#### GET `/api/consultations/<pk>/`

Retour :

Détail d'une consultation.

---

### Rendez-vous

#### GET `/api/rendez-vous/`

Filtres disponibles :

* date
* date_from
* date_to
* departement

Retour :

Liste des rendez-vous réservés.

---

#### GET `/api/rendez-vous/<pk>/`

Retour :

Détail d'un rendez-vous.

---

### Facturations

#### GET `/api/facturations/`

Filtres disponibles :

* medecin
* date_du
* date_au
* date

Retour :

Factures avec :

* médecin
* détails de facture
* montant total

---

#### GET `/api/facturations/<pk>/`

Retour :

Détail d'une facture.

---

### Prescriptions

#### GET `/api/prescriptions/`

Filtres disponibles :

* medecin
* date_du
* date_au
* date
* departement

Retour :

Prescriptions avec :

* médecin
* consultation
* lignes de prescription

---

#### GET `/api/prescriptions/<pk>/`

Retour :

Détail d'une prescription.

---

### Dossier médical

Les consultations liées au dossier médical du patient connecté sont accessibles via les endpoints dédiés aux consultations selon les permissions applicables.

---

## Routes API enregistrées

Le routeur principal est défini dans `pro_cli/urls.py` :

```python
path('api/', include('comptes.api.urls'))
path('api/', include('facturations.api.urls'))
path('api/', include('prescriptions.api.urls'))
path('api/', include('consultations.api.urls'))
path('api/', include('rendez_vous.api.urls'))
```

---

## Installation rapide

### 1. Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/procli.git

cd procli
```

### 2. Créer un environnement virtuel

#### Linux / macOS

```bash
python -m venv env

source env/bin/activate
```

#### Windows

```bash
python -m venv env

env\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Appliquer les migrations

```bash
python manage.py migrate
```

### 5. Créer un superutilisateur

```bash
python manage.py createsuperuser
```

### 6. Démarrer le serveur

```bash
python manage.py runserver
```

---

## Celery et RabbitMQ

Démarrer le worker :

```bash
celery -A pro_cli worker --loglevel=info
```

Démarrer Celery Beat :

```bash
celery -A pro_cli beat --loglevel=info
```

---

## Variables d'environnement recommandées

Créer un fichier `.env` :

```env
SECRET_KEY=your-secret-key

DEBUG=False

ALLOWED_HOSTS=localhost,127.0.0.1

RABBITMQ_URL=amqp://guest:guest@localhost:5672//

EMAIL_HOST=

EMAIL_PORT=
```



## Évolutions prévues

* Finalisation du module de paiements
* Passage à PostgreSQL en production
* Ajout de tests automatisés
* Documentation Swagger/OpenAPI
* Déploiement Docker
* Journalisation avancée
* Tableau de bord analytique

---

## Notes utiles

* `EMAIL_BACKEND` utilise actuellement le backend console pour le développement.
* `JWTAuthentication` est configurée globalement.
* Les API OTP sont volontairement ouvertes avec `AllowAny`.
* Les modèles principaux utilisent des index pour améliorer les performances.

---

## Licence

Ce projet est actuellement distribué à des fins académiques et de démonstration.

Tous droits réservés.

---

Développé avec Django et Django REST Framework pour la gestion médicale et administrative des établissements de santé.
>>>>>>> e8eb8c86b1b273f922430cc1d42ee6d50500b85b
