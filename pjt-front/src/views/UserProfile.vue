<template>
		<div class="buster-light">

  <div class="hero user-hero">
	<div class="container">
		<div class="row">
			<div class="col-md-12">
				<div class="hero-ct">
					<h1>{{ $route.params.username }}님의 프로필</h1>
					<ul class="breadcumb">
						<li class="active"><a href="#">Home</a></li>
						<li> <span class="ion-ios-arrow-right"></span>프로필</li>
					</ul>
				</div>
			</div>
		</div>
	</div>
</div>
<div class="page-single">
	<div class="container">
		<div class="row ipad-width">
			<div class="col-md-3 col-sm-12 col-xs-12">
				<div class="user-information">
					<div class="user-img">
						<a href="#"><img src="images/uploads/user-img.png" alt=""><br></a>
						<a href="#" class="redbtn">프로필 바꾸기</a>
					</div>
					<div class="user-fav">
						<p>Account Details</p>
						<ul>
              <li v-for="(tab, index) in accountsDetail" :key="index" :class="{ active: currentTab === index }">
                <a @click.prevent="currentTab = index " href="#">{{ tab }}</a>
              </li>
							<!-- <li  class="active"><a href="userprofile.html">Profile</a></li>
							<li><a href="userfavoritelist.html">Favorite movies</a></li>
							<li><a href="userrate.html">Rated movies</a></li> -->
						</ul>
					</div>
					<div class="user-fav">
						<p>Others</p>
						<ul>
							<li :class="{ active: currentTab === 3}"><a @click.prevent="currentTab = 3" href="#">Change information</a></li>
							<li><a href="#">Log out</a></li>
						</ul>
					</div>
				</div>
			</div>
			<div class="col-md-9 col-sm-12 col-xs-12">
        <user-profile-detail v-if="currentTab == 0" :userData="userData"></user-profile-detail>
        <user-favorite-movies v-if="currentTab == 1"></user-favorite-movies>
        <user-rated-movies v-if="currentTab == 2"></user-rated-movies>
				<user-change-form v-if="currentTab == 3"></user-change-form>
			</div>
		</div>
	</div>
</div>
		</div>
</template>

<script>
import axios from 'axios'
import UserChangeForm from '../components/Profile/UserChangeForm.vue'
import UserFavoriteMovies from '../components/Profile/UserFavoriteMovies.vue'
import UserProfileDetail from '../components/Profile/UserProfileDetail.vue'
import UserRatedMovies from '../components/Profile/UserRatedMovies.vue'
const api = 'http://127.0.0.1:8000/api/v1/accounts/'
export default {
  name: 'UserProfile',
  components: {
    UserChangeForm,
    UserFavoriteMovies,
    UserRatedMovies,
    UserProfileDetail
  },
  data () {
    return {
      currentTab: 0,      
      accountsDetail: ['Profile', 'Favorite Movies', 'Rated Movies'],
			userData: null
    }
  },
	methods: {
		setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
		getProfile () {
			axios({
				method: 'get',
				url: api + `${this.$route.params.username}/`,
				headers: this.setToken()
			})
				.then(res => {
					console.log(res.data)
					this.userData = res.data
				})
				.catch(err => {
					console.log(err)
				})
		}
	},
	created () {
		this.getProfile()
	}
}
</script>

<style>

</style>