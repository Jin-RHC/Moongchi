import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import MovieList from '../views/MovieList.vue'
import MovieDetail from '../views/MovieDetail.vue'
import Community from '../views/Community.vue'
import CommunitySearch from '../views/CommunitySearch.vue'
import ReviewForm from '@/components/Community/ReviewForm.vue'
import ReviewDetail from '../views/ReviewDetail.vue'
import CommingSoon from '../views/CommingSoon.vue'
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
    props: true, 
  },
  {
    path: '/community',
    name: 'Community',
    component: Community,
    props: true
  },
  {
    path: '/comunitysearch',
    name: 'CommunitySearch',
    component: CommunitySearch
  },
  {
    path: '/review-create',
    name: 'ReviewForm',
    component: ReviewForm
  },
  {
    path: '/review/:reviewId',
    name: 'ReviewDetail',
    component: ReviewDetail
  },
  {
    path: '/celebrities',
    name: 'CommingSoon',
    component: CommingSoon,
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
  routes,
  scrollBehavior () {
    return { x: 0, y: 0 }
  }
})

export default router


