import { createRouter, createWebHistory } from 'vue-router'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import HomeView from '../views/HomeView.vue'
import SignOut from '../views/SignOut.vue'
import ProductList from '../views/ProductList.vue'



const routes = [
  { path: '/sign-up', name: 'SignUp', component: SignUp },
  { path: '/log-in', name: 'LogIn', component: LogIn },
  { path: '/', name: 'HomeView', component: HomeView },
  { path: '/sign-out', name: 'SignOut', component: SignOut, },
  { path: '/product-list', name: 'ProductList', component: ProductList},
]
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})
export default router
