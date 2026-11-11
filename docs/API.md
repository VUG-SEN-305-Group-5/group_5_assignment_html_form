# API Documentation

Owner: Task 10 · Deadline: Mon 16

Base URL (local): `http://127.0.0.1:5050`

All endpoints send and receive JSON.

| Method | Endpoint | Login needed | Description | Status |
|---|---|---|---|---|
| GET | `/api/health` | No | Check the database connection | ✅ Done |
| POST | `/api/register` | No | Create a student and their login | ⏳ Task 5 |
| POST | `/api/login` | No | Log in, start a session | ⏳ Task 5 |
| POST | `/api/logout` | Yes | End the session | ✅ Done |
| GET | `/api/departments` | No | List departments for the dropdown | ⏳ Task 6 |
| GET | `/api/me` | Yes | Logged-in student's profile | ⏳ Task 6 |
| GET | `/api/students` | Admin | List all students | ⏳ Task 6 |

## TODO
For every endpoint add:
- an example request body
- an example success response
- an example error response
- a screenshot from Thunder Client or Postman (save in `docs/screenshots/`)