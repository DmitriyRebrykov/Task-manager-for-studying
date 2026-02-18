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

   ```bash
   cp .env.example .env
   ```

3. **Build and start the containers**

   ```bash
   docker compose up -d --build
   ```
   
