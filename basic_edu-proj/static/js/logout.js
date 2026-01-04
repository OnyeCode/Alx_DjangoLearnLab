function logout() {
  localStorage.clear();
  window.location.href = "/login/";
}

`
document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("logoutBtn");

  if (btn) {
    btn.addEventListener("click", () => {
      localStorage.removeItem("access");
      localStorage.removeItem("refresh");
      window.location.href = "/login/";
    });
  }
});
`
