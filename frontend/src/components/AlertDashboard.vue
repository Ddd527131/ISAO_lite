<template>
  <div class="p-4">
    <label class="font-bold mr-2">Filtrer par type :</label>
    <select v-model="selectedType" @change="fetchAlerts" class="border rounded px-2 py-1">
      <option value="">Tous</option>
      <option v-for="type in alertTypes" :key="type" :value="type">{{ type }}</option>
    </select>

    <ul class="mt-4 space-y-2">
      <li v-for="alert in alerts" :key="alert.id" class="bg-gray-100 p-2 rounded shadow">
        <strong>{{ alert.type.toUpperCase() }}</strong> : {{ alert.description }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      alerts: [],
      selectedType: "",
      alertTypes: ["feu", "inondation", "incident chimique"], // statique, sinon auto-générer depuis les données
    };
  },
  methods: {
    async fetchAlerts() {
      const query = this.selectedType ? `?type=${this.selectedType}` : "";
      const res = await fetch(`http://127.0.0.1:8000/alerts${query}`);
      this.alerts = await res.json();
    },
  },
  mounted() {
    this.fetchAlerts();
  },
};
</script>
<script>
export default {
  data() {
    return {
      alerts: [],
      selectedType: "",
      alertTypes: ["feu", "inondation", "incident chimique"],
      socket: null,
    };
  },
  methods: {
    async fetchAlerts() {
      const query = this.selectedType ? `?type=${this.selectedType}` : "";
      const res = await fetch(`http://127.0.0.1:8000/alerts${query}`);
      this.alerts = await res.json();
    },
    setupWebSocket() {
      this.socket = new WebSocket("ws://127.0.0.1:8000/ws/alerts");
      this.socket.onmessage = (event) => {
        const newAlert = JSON.parse(event.data);
        // si filtre actif, ne push que les bons types
        if (!this.selectedType || newAlert.type === this.selectedType) {
          this.alerts.unshift(newAlert);
        }
      };
      this.socket.onclose = () => {
        console.warn("WebSocket fermé, reconnexion...");
        setTimeout(this.setupWebSocket, 2000); // tentative reconnexion
      };
    },
  },
  mounted() {
    this.fetchAlerts();
    this.setupWebSocket();
  },
};
</script>

