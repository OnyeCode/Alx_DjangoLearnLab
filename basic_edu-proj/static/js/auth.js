const API = "/api/";

document.getElementById("loginForm")?.addEventListener("submit", async e => {
  e.preventDefault();

  const res = await fetch(API + "login/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      username: username.value,
      password: password.value
    })
  });

  const data = await res.json();
  if (data.access) {
    localStorage.setItem("access", data.access);
    localStorage.setItem("refresh", data.refresh);
    window.location.href = "/profile/";
  }
});

