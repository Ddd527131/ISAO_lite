<template>
  <div class="p-4">
    <h1 class="text-3xl font-bold mb-4">ISAO Lite</h1>
    <nav class="mb-4 space-x-4">
      <router-link to="/dashboard" class="text-blue-500 hover:underline">Dashboard</router-link>
      <router-link to="/map" class="text-blue-500 hover:underline">Carte</router-link>
    </nav>

    <router-view />
  </div>
</template>

<script>
export default {};
</script>
