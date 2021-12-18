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
						<a @click.prevent="none" href="#"><img src="images/uploads/user-img.png" alt=""><br></a>
						<div v-if="!myProfile">
							<a v-show="!isFollowing" @click.prevent="follow" href="#" class="redbtn" style="">팔로우</a>
							<a v-show="isFollowing" @click.prevent="follow" href="#" class="redbtn" style="background:grey;">팔로우한 사람입니다.</a>
						</div>
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
							<li v-if="this.$route.params.username === myName" :class="{ active: currentTab === 3}"><a @click.prevent="currentTab = 3" href="#">Change information</a></li>
							<li v-if="this.$route.params.username === myName"><a href="#">Sign out</a></li>
						</ul>
					</div>
				</div>
			</div>
			<div class="col-md-9 col-sm-12 col-xs-12">
        <user-profile-detail v-if="currentTab == 0" :userData="userData"></user-profile-detail>
        <user-favorite-movies :favorite-movies="favoriteMovies" v-if="currentTab == 1"></user-favorite-movies>
        <user-rated-movies v-if="currentTab == 2" :userData="userData"></user-rated-movies>
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
import jwt_decode from "jwt-decode"
const API = process.env.VUE_APP_BACKEND_URL

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
      accountsDetail: ['Profile', 'Favorite Movies', 'Reviewed Movies'],
			userData: null,
			favoriteMovies: null,
			myName: null,
			isFollowing: false,
			profileName: null,
    }
  },
	methods: {
		setToken: function () {
      const token = localStorage.getItem('jwt')
			this.myName = jwt_decode(token).username
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
		getProfile () {
			axios({
				method: 'get',
				url: `${API}/api/v1/accounts/${this.$route.params.username}/`,
				headers: this.setToken()
			})
				.then(res => {
					console.log(res.data)
					this.userData = res.data
					this.favoriteMovies = res.data.like_movies
					this.profileName = res.data.username
					for (const curr of res.data.followers) {
						if (this.myName === curr.username) {
							this.isFollowing = true
						}
					}
					console.log(this.profileName)
				})
				.catch(err => {
					console.log(err)
					this.$router.push({ name: 'Home'})
					// alert('존재하지 않는 유저입니다.')
				})
		},
		follow () {
			axios({
				method: 'POST',
				url: `${API}/api/v1/accounts/${this.$route.params.username}/follow/`,
				headers: this.setToken()
			})
				.then(() => {
					if (this.isFollowing === false) {
						this.isFollowing = true
						// this.userData.followers_count = this.userData.followers_count + 1
					} else {
						this.isFollowing = false
						// this.userData.followers_count = this.userData.followers_count - 1
					}
					this.getProfile()
				})
				.catch(err => {
					console.log(err)
					alert('로그인하셔야 볼 수 있습니다.')
				})
		},

		none: function () {
			
		},
	},

	created () {
		this.getProfile()
		console.log('태어났다!!!')		
		console.log(this.currentTab)
	},
	computed: {
		myProfile () {
			if (this.profileName === this.myName) {
				return true
			} else {
				return false
			}
		}
	}	
}
</script>

<style>

</style>