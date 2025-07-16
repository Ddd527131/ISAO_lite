<template>
  <div>
    <h1 class="text-2xl font-bold mb-4">Tableau de bord des alertes</h1>
    <AlertDashboard />
  </div>
</template>

<script>
import AlertDashboard from "@/components/AlertDashboard.vue";

export default {
  components: {
    AlertDashboard,
  },
};
</script>
