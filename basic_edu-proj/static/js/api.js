const token = localStorage.getItem("access");

async function fetchProfile() {
  const res = await fetch("/api/profile/", {
    headers: {
      "Authorization": `Bearer ${token}`
    }
  });

  const data = await res.json();
  document.getElementById("profile").innerHTML =
    `<p>${data.username}</p><p>${data.email}</p>`;
}

if (document.getElementById("profile")) {
  fetchProfile();
}

