// Login page logic
// Owner: Task 8, Deadline: Sun 15
//
// TODO:
// 1. listen for the form submit, call event.preventDefault()
// 2. check username and password are not empty
// 3. send them to the backend:
//
//    const response = await fetch("/api/login", {
//        method: "POST",
//        headers: { "Content-Type": "application/json" },
//        body: JSON.stringify({ username, password })
//    });
//    const result = await response.json();
//
// 4. if response.ok -> window.location.href = "/dashboard"
//    else -> show result.message in the error box