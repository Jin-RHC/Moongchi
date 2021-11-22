import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import MovieList from '../views/MovieList.vue'
import MovieDetail from '../views/MovieDetail.vue'
import Community from '../views/Community.vue'
import ReviewForm from '@/components/Community/ReviewForm.vue'
import ReviewDetail from '../views/ReviewDetail.vue'
import UserProfile from '../views/UserProfile.vue'
import NotFoundComponent from '../views/NotFoundComponent.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',    
    component: Home
  },
  {
    path: '/movielist',
    name: 'MovieList',
    component: MovieList
  },  
  {
    path: '/movie/:id',
    name: 'MovieDetail',
    component: MovieDetail,
  },
  {
    path: '/community',
    name: 'Community',
    component: Community,
    props: true
  },
  {
    path: '/review-create',
    name: 'ReviewForm',
    component: ReviewForm
  },
  {
    path: '/review/:id',
    name: 'ReviewDetail',
    component: ReviewDetail
  },
  {
    path: '/profile/:username',
    name: 'UserProfile',
    component: UserProfile
  },
  {
    path: "/page-not-found",
    name: "NotFoundComponent",    
    component: NotFoundComponent,
  },
  {
    path: '*',
    redirect: "/page-not-found"
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

