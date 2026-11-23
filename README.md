# Student Biodata System

Group 5 project. A student registration and login system.

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python Flask
- **Database:** MySQL (via XAMPP)

## How it works

```
Browser (client/)  --JSON over HTTP-->  Flask API (server/)  --SQL-->  MySQL (database/)
        ^                                        |
        └------------- JSON response ------------┘
```

The backend follows **MVC**:

| Layer | Folder | Job |
|---|---|---|
| Model | `server/models/` | All SQL queries |
| View | `client/` | Pages, styling, browser JavaScript |
| Controller | `server/routes/` | API endpoints that connect the two |

## Folder structure

```
├── client/                   frontend
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   ├── css/style.css
│   └── js/register.js, login.js, dashboard.js
├── server/                   backend
│   ├── app.py                starts the server, serves pages, registers routes
│   ├── config.py             settings read from .env
│   ├── db.py                 database connection
│   ├── requirements.txt
│   ├── .env.example
│   ├── models/               student_model.py, auth_model.py
│   └── routes/               auth_routes.py, student_routes.py
├── database/
│   └── schema.sql            tables, keys, sample data
└── docs/
    └── API.md                endpoint documentation
```

## Setup

**You need:** Python 3.10+, XAMPP, Git.

1. **Get the code**
   ```bash
   git clone https://github.com/VUG-SEN-305-Group-5/group_5_assignment_html_form.git
   cd group_5_assignment_html_form
   git checkout <your-branch>
   git merge main
   ```

2. **Set up the database**
   - Open the XAMPP Control Panel and start **Apache** and **MySQL**
   - Go to `http://localhost/phpmyadmin` and open the **SQL** tab
   - Paste everything from `database/schema.sql` and click **Go**

3. **Set up Python** (inside the `server` folder)
   ```bash
   cd server
   python -m venv venv
   venv\Scripts\activate          # Windows
   source venv/bin/activate       # Mac/Linux
   pip install -r requirements.txt
   ```
   If PowerShell blocks activation, run this once:
   `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`

4. **Create your `.env`**
   ```bash
   copy .env.example .env         # Windows
   cp .env.example .env           # Mac/Linux
   ```
   Change `SECRET_KEY` to any random text. If port 5050 is taken on your machine, change `PORT`.

5. **Run the server**
   ```bash
   python app.py
   ```

6. **Check it works**
   - `http://127.0.0.1:5050/api/health` should show `"status": "ok"`
   - `http://127.0.0.1:5050/` should show the registration form

## Team workflow

1. Before you start: `git checkout <your-branch>`, then `git merge main`
2. **Only edit the files you own.** The owner and deadline are written at the top of each file.
3. Commit often with clear messages, e.g. `add get_all_departments to student_model`
4. Push your branch and open a **Pull Request into `main`**
5. The team lead reviews and merges

Never commit your `.env` file or the `venv/` folder.

## Tasks

| # | Task | Files | Deadline |
|---|---|---|---|
| 1 | Setup | `server/app.py`, `config.py`, `db.py` | Wed 11 ✅ |
| 2 | Database & ER diagram | `database/schema.sql` | Thu 12 |
| 3 | Student model | `server/models/student_model.py` | Fri 13 |
| 4 | Auth model | `server/models/auth_model.py` | Fri 13 |
| 5 | Auth routes | `server/routes/auth_routes.py` | Sat 14 |
| 6 | Student routes | `server/routes/student_routes.py` | Sat 14 |
| 7 | Register page | `client/register.html`, `client/js/register.js` | Sun 15 |
| 8 | Login page | `client/login.html`, `client/js/login.js` | Sun 15 |
| 9 | Dashboard & UI | `client/dashboard.html`, `client/js/dashboard.js`, `client/css/style.css` | Sun 15 |
| 10 | Docs & testing | `README.md`, `docs/API.md` | Mon 16 |

**Final merge and full test: Tue 17**