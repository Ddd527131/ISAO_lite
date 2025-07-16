import { createRouter, createWebHistory } from 'vue-router';
import DashboardView from '@/views/DashboardView.vue';
import MapView from '@/views/MapView.vue'; // si tu l’as

const routes = [{
        path: '/',
        redirect: '/dashboard',
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: DashboardView,
    },
    {
        path: '/map',
        name: 'Map',
        component: MapView,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;