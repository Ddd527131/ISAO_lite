// frontend/app.js

const map = L.map('map').setView([48.85, 2.35], 12); // Position centrée sur Paris

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

const alertList = document.getElementById("alert-list");

// Fetch les alertes depuis le backend
async function fetchAlerts() {
    try {
        const res = await fetch("http://127.0.0.1:8000/alerts");
        const data = await res.json();

        alertList.innerHTML = "";

        data.forEach(alert => {
            const marker = L.marker([alert.latitude, alert.longitude])
                .addTo(map)
                .bindPopup(`<b>${alert.type}</b><br>${alert.description}`);

            const li = document.createElement("li");
            li.innerHTML = `<strong>${alert.type}</strong><br>${alert.description}`;
            li.onclick = () => {
                map.setView([alert.latitude, alert.longitude], 15);
                marker.openPopup();
            };

            alertList.appendChild(li);
        });
    } catch (err) {
        console.error("Erreur fetch alerts:", err);
    }
}

// Refresh toutes les 10s
fetchAlerts();
setInterval(fetchAlerts, 10000);