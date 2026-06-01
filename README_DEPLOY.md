Déploiement Docker + Caddy (open-source) — options gratuites

Ce guide explique plusieurs méthodes gratuites pour déployer l'app Streamlit sans le badge Streamlit Cloud. La méthode recommandée ici utilise Caddy (open-source) comme reverse-proxy HTTPS automatique.

1) Option simple (Render - gratuit) — recommandé si tu veux zéro administration
--------------------------------------------------------------------------
- Crée un compte gratuit sur https://render.com
- Connecte ton dépôt GitHub `CercleJudo/cerle-quiz`
- Crée un "Web Service"
  - Branch: `main`
  - Build command: `docker build -t cerle-quiz .`
  - Start command: `streamlit run gemini-code-1780037330332.py --server.port $PORT --server.address=0.0.0.0`
Render fournit automatiquement une URL HTTPS. Pas de badge Streamlit Cloud.

2) VPS gratuit (Oracle Cloud Always Free) + Docker + Caddy (auto TLS)
------------------------------------------------------------------
Pré-requis:
- Un VPS (ex: Oracle Cloud Free Tier) et un nom de domaine pointant vers l'IP publique.

Sur le VPS (ex: Ubuntu 22.04) :

```bash
# Installer Docker & docker-compose
sudo apt update
sudo apt install -y docker.io docker-compose git
sudo systemctl enable --now docker

# Cloner ton dépôt
git clone https://github.com/CercleJudo/cerle-quiz.git
cd cerle-quiz

# Modifier ./caddy/Caddyfile: remplacer YOUR_DOMAIN_HERE et ton e-mail
# Puis construire et démarrer
sudo docker compose up -d --build

# Caddy obtiendra automatiquement les certificats Let's Encrypt
# (assure-toi que les ports 80 et 443 sont ouverts sur ton VPS)
```

3) Tunnel HTTPS gratuit (Cloudflare Tunnel)
-------------------------------------------
Si tu n'as pas de domaine ou VPS, Cloudflare Tunnel te permet d'exposer ton service localement via HTTPS gratuit.
- Crée un compte Cloudflare et ajoute un site (ou utilise un sous-domaine Cloudflare).
- Installe `cloudflared` sur le serveur local ou VPS et crée un tunnel vers `http://localhost:8501`.

Exemple rapide (sur ta machine locale):

```bash
# Installer cloudflared (suivre docs officiel)
cloudflared tunnel --url http://localhost:8501
# Suis les instructions pour créer un tunnel et obtenir une URL *.trycloudflare.com
```

Fichiers ajoutés dans le dépôt:
- `Dockerfile`
- `docker-compose.yml`
- `caddy/Caddyfile`
- `README_DEPLOY.md`

Choisis l'option que tu préfères et je te fournis les commandes exactes et j'adapterai les fichiers (`caddy/Caddyfile` et `docker-compose.yml`) avec ton domaine ou la configuration Cloudflare si tu me fournis l'IP du VPS ou le domaine.
