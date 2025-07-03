# Django + React + Vite Full Stack App

This project is a full-stack web application built using:

- **Django** for the backend (API and database)
- **React** for the frontend (UI)
- **Vite** as the build tool and development server for React

It allows users to submit and view a list of people with their name, age, and email.

---

## 🚀 Features

- RESTful API built with Django and Django REST Framework
- React frontend powered by Vite for fast development
- Communication between frontend and backend using Vite's proxy server
- Full CRUD-ready architecture for extending functionality

---

## 🧱 Project Structure

django_react_website/
├── website/ # Django project root
│ ├── core/ # Django app (models, views, serializers)
│ ├── website/ # Django settings and root URLs
│ └── manage.py
│
├── frontend/ # Vite + React frontend
│ ├── index.html
│ ├── vite.config.js
│ ├── package.json
│ └── src/
│ ├── App.jsx # React component for form + list
│ └── main.jsx
│
└── venv/ or .venv/ # Python virtual environment


---

## ⚙️ How It Works

### 🐍 Django Backend

- Django uses Django REST Framework to expose a RESTful API endpoint at `/home/` (or `/api/people/` if renamed).
- `ReactView` in `views.py` handles `GET` (retrieve people) and `POST` (add person).
- Data is serialized with `ReactSerializer`.

### ⚛️ React Frontend (with Vite)

- `App.jsx` is a class-based React component.
- It displays a form to collect user input (name, age, email).
- On submit, it POSTs the data to Django.
- It also fetches and renders the list of all people using a GET request.
- Vite serves the frontend and proxies API requests to Django.

### 🔁 Vite as a Bridge

- `vite.config.js` uses the `proxy` field to forward `/home/` requests to Django at `http://127.0.0.1:8000`
- This allows frontend requests like `axios.get("/home/")` to talk to Django **without CORS errors**

---

## 💻 Running the Project

### Backend (Django)

```bash
cd website
source ../venv/bin/activate        # or your virtualenv activate command
python manage.py runserver

### Frontend (React + Vite )

cd frontend
npm install        # Only needed once
npm run dev


