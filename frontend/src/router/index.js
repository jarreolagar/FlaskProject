import {createRouter, createWebHistory} from 'vue-router'
import Vue from 'vue'
import Router from 'vue-router'
import Inicio from '@/components/Inicio.vue'
import Entradas from '@/components/Entradas.vue'
import DetalleEntrada from '@/components/DetalleEntrada.vue'


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
    {
      path: '/leer_entrada/:id/',
      name: 'DetalleEntrada',
      component: DetalleEntrada,
      props:true
    }
  ],
});