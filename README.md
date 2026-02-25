# Django Backend — Nicolas Garlinski Blog

This is the Django REST API backend for the blog. It handles blog posts and contact form submissions.

---

## Project Structure

```
django-backend/
├── core/                  # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── blog/                  # Blog posts app
│   ├── models.py          # Post and PostContent models
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── contact/               # Contact form app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── react-updates/         # Drop these into your React src/ folder
│   ├── Navbar.jsx
│   ├── Home.jsx
│   ├── BlogPost.jsx
│   ├── Contact.jsx
│   └── .env.example
├── seed.py                # Populates DB with your original posts
├── manage.py
└── requirements.txt
```

---

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/posts/` | List all posts |
| GET | `/api/posts/<slug>/` | Get a single post with content |
| POST | `/api/contact/` | Submit a contact message |

---

## Local Setup

### 1. Create and activate a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create a .env file
```bash
copy .env.example .env   # Windows
cp .env.example .env     # Mac/Linux
```
Then open `.env` and set a SECRET_KEY (any long random string).

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Seed the database with your blog posts
```bash
python seed.py
```

### 6. Create an admin user
```bash
python manage.py createsuperuser
```

### 7. Run the dev server
```bash
python manage.py runserver
```

Visit http://localhost:8000/api/posts/ to confirm it works.
Visit http://localhost:8000/admin/ to manage posts via the admin panel.

---

## Connecting React to Django

1. Copy all files from `react-updates/` into the matching locations in your React project:
   - `Navbar.jsx` → `src/components/Navbar.jsx`
   - `Home.jsx` → `src/pages/Home.jsx`
   - `BlogPost.jsx` → `src/pages/BlogPost.jsx`
   - `Contact.jsx` → `src/pages/Contact.jsx`

2. Copy `.env.example` to `.env` in your React project root:
```
VITE_API_URL=http://localhost:8000
```

3. Run both servers at the same time:
   - Django: `python manage.py runserver` (port 8000)
   - React: `npm run dev` (port 5173)

---

## Deploying to Render

### 1. Push this folder to a GitHub repo
Create a new repo (e.g. `blog-backend`) and push this folder to it.

### 2. Create a new Web Service on Render
- Go to render.com and sign up
- Click **New → Web Service**
- Connect your GitHub repo
- Set these values:
  - **Build Command:** `pip install -r requirements.txt`
  - **Start Command:** `gunicorn core.wsgi:application`
  - **Environment:** Python 3

### 3. Add environment variables in Render dashboard
- `SECRET_KEY` → any long random string
- `DEBUG` → False
- `DATABASE_URL` → Render provides this automatically if you add a PostgreSQL database

### 4. Add a PostgreSQL database
- In Render, click **New → PostgreSQL**
- Copy the **Internal Database URL** and paste it as the `DATABASE_URL` environment variable in your web service

### 5. Run migrations on Render
In your Render web service, go to the **Shell** tab and run:
```bash
python manage.py migrate
python seed.py
python manage.py createsuperuser
```

### 6. Update your React .env for production
Once Render gives you a URL (e.g. `https://blog-backend.onrender.com`), update your React project:
```
VITE_API_URL=https://blog-backend.onrender.com
```
Then redeploy React:
```bash
npm run deploy
```
