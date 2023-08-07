import { createRouter, createWebHistory } from 'vue-router'
import CreateView from '../views/Create.vue'
import RoomView from '../views/Play.vue'

const routes = [
  {
    path: '/',
    name: 'Create',
    component: CreateView
  },
  {
    path: '/:room_slug/',
    name: 'Play',
    component: RoomView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
