// Dashboard page logic
// Owner: Task 9, Deadline: Sun 15
//
// TODO:
// 1. when the page loads, fetch("/api/me")
//    - status 401 -> window.location.href = "/login"
//    - otherwise fill in the profile details
// 2. if the user's role is "admin", fetch("/api/students") and build a table
// 3. logout button -> fetch("/api/logout", { method: "POST" }) then go to /login