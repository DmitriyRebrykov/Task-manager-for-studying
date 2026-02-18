# Task Manager for Studying

Modern task manager designed specifically for students and self-learners.  
Helps organize study goals, track progress, manage deadlines and maintain motivation during long-term learning.

| Django | Docker | HTML + CSS + JS(HTMX) |
|--------|--------|-----------------------|

## Main Features

- Creation, editing and deletion of tasks and study projects
- Deadline and priority setting
- Simple categorization / subjects / topics
- Responsive design (mobile + desktop)
- Docker-ready deployment (development & production)
- Clean and maintainable project structure

## Technology Stack

**Backend**
- Python 3.13
- Django 5.2

**Frontend**
- HTML5
- CSS3 ( BootstrapV5 / custom styles)
- JavaScript (HTMX)

**Database**
- SQLite (default)

**Infrastructure**
- Docker + Docker Compose
- pre-commit hooks (ruff, djhtml, mirrors-prettier)

## Project Structure

```text
Task-manager-for-studying/
├── apps/                   # Django local applications
│   ├── main/               # main app — tasks, projects
│   └── accounts/           # user management 
├── config/                 # project settings
├── staticfiles/            # static files (css, js, images)
├── .pre-commit-config.yaml
├── Dockerfile
├── docker-compose.yml
├── docker-entrypoint.sh
├── manage.py
├── requirements.txt
└── .gitignore
```
## Quick Start (Docker)

Follow these steps to launch the application using Docker Compose:

1. **Clone the repository**

   ```bash
   git clone https://github.com/DmitriyRebrykov/Task-manager-for-studying.git
   cd Task-manager-for-studying
   ```
   
2. **Prepare the environment file**

    ⚠️ Important: Before launching the containers, you need to configure your OAuth credentials in the .env file.
    👉 Please follow the instructions in the [Setting Up Social Authentication]() section below, then return here.
   
   ```bash
   cp .env.example .env
   ```

3. **Build and start the containers**

   ```bash
   docker compose up -d --build
   ```
## Setting Up Social Authentication (Google & GitHub OAuth)

To enable login/registration via Google and GitHub accounts, you need to register your application with each provider and obtain **Client ID** and **Client Secret**. These values must be stored securely (preferably in the `.env` file).

### 1. Google OAuth 2.0 Credentials

1. Go to the [Google Cloud Console → APIs & Services → Credentials](https://console.cloud.google.com/apis/credentials).
2. Click **Create Credentials** → **OAuth client ID**.
3. Select **Application type**: **Web application**.
4. Enter a meaningful **Name** (e.g., "Task Manager for Studying – Dev").
5. In the **Authorized redirect URIs** section, add the callback URL(s) used by your Django project.  
   Common options (add all that apply):
   - `http://localhost:8000/accounts/google/login/callback/`
6. Click **Create**.
7. Copy the generated **Client ID** and **Client Secret**.
8. Save them in your `.env` file:

   ```env
   OAUTH_GITHUB_CLIENT_ID=your-google-client-id.apps.googleusercontent.com
   OAUTH_GITHUB_SECRET=your-google-client-secret
   ```
   
### 2. GitHub OAuth Application Setup

1. Log in to your GitHub account.
2. In the upper-right corner of any page, click your profile photo, then select **Settings**.
3. In the left sidebar, click **Developer settings**.
4. In the left sidebar, click **OAuth Apps**.
5. Click **New OAuth App**  
   *(If you have not created any OAuth apps previously, the button may be labeled **Register a new application**.)*
6. Complete the registration form with the following values:
   - **Application name**  
     Example: `Task Manager for Studying – Dev`
   - **Homepage URL**  
     `http://localhost:8000/`  
     *(For production environments, replace with your actual domain, e.g., `https://your-domain.com/`)*
   - **Application description** (optional, but recommended)  
     Brief description visible to users, e.g., “Study task manager with progress tracking and deadlines”
   - **Authorization callback URL**  
     `http://localhost:8000/accounts/github/login/callback/`  
     *(This value must match exactly the redirect URI configured in your Django social auth library — most commonly used with `django-allauth`. Adjust the path if your project uses a different callback endpoint, e.g., `/accounts/github/callback/`.)*
7. Click **Register application**.
8. On the following screen:
   - Copy the displayed **Client ID**.
   - Click **Generate a new client secret** (if no secret is shown) and immediately copy the generated **Client Secret**.  
     **Note**: The client secret is shown only once — store it securely.
9. Add these credentials to your `.env` file (do not commit this file to version control):

   ```env
   OAUTH_GITHUB_CLIENT_ID=your-github-client-id
   OAUTH_GITHUB_SECRET=your-github-client-secret
   ```
