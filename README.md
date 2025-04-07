# Todo App

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

## Overview

A simple **Fullstack Todo App** to manage tasks using:
- 🌐 **FastAPI** (Python) for the backend
- 🎨 **Vue.js** for the frontend
- 🗄️ **SQLite + SQLAlchemy** for data storage

This project provides a minimalistic and easy-to-understand way to interact with a backend API and use Vue.js as the frontend for a seamless user experience.

## Features

- **Create tasks**: Add a new task to your list.
- **Update tasks**: Mark tasks as complete or update their information.
- **Delete tasks**: Remove completed tasks from the list.

## Demo

*Add screenshots or GIFs here to showcase your application in action.*

## Tech Stack

- **Frontend**: Vue.js, Composition API
- **Backend**: FastAPI, SQLite, SQLAlchemy
- **Deployment**: (optional, add your deployment tech here)

## Installation

### Backend (FastAPI)

1. Clone the repository:

```bash
git clone https://github.com/yourusername/todo-app.git
cd todo-app
Install backend dependencies:

bash

cd backend
python -m venv env
source env/bin/activate  # On Mac/Linux
# env\Scripts\activate   # On Windows

pip install -r requirements.txt
Run the backend server:

bash

uvicorn api:app --reload
The FastAPI backend will run on http://127.0.0.1:8000

Frontend (Vue.js)
Install frontend dependencies:

bash

cd frontend
npm install
Run the Vue.js development server:

bash

npm run dev
The frontend will run on http://localhost:5173

Usage
Development
Run the backend:

bash

uvicorn api:app --reload
Run the frontend:

bash

npm run dev
Visit the frontend in your browser and interact with the app.

Build for production
Build the Vue.js app:

bash

npm run build
Start the production build:

npm start
API Reference
Endpoints
Method	Endpoint	Description	Parameters
GET	/tasks	Get all tasks	page: Page number
POST	/tasks	Create a new task	name: Task name
GET	/tasks/{id}	Get a single task	None
PUT	/tasks/{id}	Update a task	name: Task name
DELETE	/tasks/{id}	Delete a task	None
Project Structure
bash
Kopioi
Muokkaa
todo-app/
├── backend/
│   ├── api.py         # FastAPI backend code
│   ├── models.py      # SQLAlchemy models
├── frontend/
│   ├── App.vue        # Main Vue.js component
│   ├── components/    # Vue components
│   ├── main.js        # Vue.js entry point
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt   # Python dependencies
Configuration
Environment Variable	Description	Default
PORT	Port number for the backend	8000
DATABASE_URL	SQLite database URL	N/A
Testing
Run tests for both backend and frontend.

Backend Testing
bash
Kopioi
Muokkaa
pytest
Frontend Testing
bash
Kopioi
Muokkaa
npm run test
Deployment
To deploy the app:

Build the Vue.js frontend: npm run build

Set up environment variables on your server.

Start the FastAPI backend and the production Vue.js build.

Contributing
Fork the repository.

Create your feature branch: git checkout -b feature/my-feature.

Commit your changes: git commit -am 'Add new feature'.

Push to the branch: git push origin feature/my-feature.

Submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
FastAPI Documentation

Vue.js Documentation

SQLAlchemy Documentation
