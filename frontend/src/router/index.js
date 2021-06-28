import Vue from 'vue'
import Router from 'vue-router'
import Inicio from '@/components/Inicio.vue'
import Entradas from '@/components/Entradas.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Inicio',
      component: Inicio,
    },
    {
      path: '/leer_entrada',
      name: 'Entradas',
      component: Entradas,
    },
  ],
});
