const token = localStorage.getItem("access");

fetch("/api/student/profile/", {
  headers: { Authorization: `Bearer ${token}` }
})
.then(res => res.json())
.then(data => {
  document.getElementById("first_name").value = data.first_name || "";
  document.getElementById("last_name").value = data.last_name || "";
});


function updateProfile() {
  fetch("/api/student/profile/", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`
    },
    body: JSON.stringify({
      first_name: first_name.value,
      last_name: last_name.value
    })
  });
}

`
const token = localStorage.getItem("access");

if (!token) {
  window.location.href = "/login/";
}

async function loadProfile() {
  const res = await fetch("/api/profile/", {
    headers: {
      "Authorization": `Bearer ${token}`
    }
  });

  const data = await res.json();

  document.getElementById("username").textContent = data.username;
  document.getElementById("email").textContent = data.email;

  document.getElementById("bio").value = data.bio || "";
  document.getElementById("phone").value = data.phone || "";
  document.getElementById("level").value = data.level || "";
}

document.getElementById("profileForm").addEventListener("submit", async e => {
  e.preventDefault();

  await fetch("/api/profile/", {
    method: "PATCH",
    headers: {
      "Authorization": `Bearer ${token}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      bio: bio.value,
      phone: phone.value,
      level: level.value
    })
  });

  alert("Profile updated");
});

loadProfile();
`

