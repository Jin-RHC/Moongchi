<template>


    	<div class="buster-light">
<div class="hero mv-single-hero">
	<div class="container">
		<div class="row">
			<div class="col-md-12">
				<!-- <h1> movie listing - list</h1>
				<ul class="breadcumb">
					<li class="active"><a href="#">Home</a></li>
					<li> <span class="ion-ios-arrow-right"></span> movie listing</li>
				</ul> -->
			</div>
		</div>
	</div>
</div>
<div class="page-single movie-single movie_single" v-if="movie">
	<div class="container">
		<div class="row ipad-width2">
			<div class="col-md-4 col-sm-12 col-xs-12">
				<div class="movie-img sticky-sb">
					<img :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" alt="">
					<div class="movie-btn">	
						<div class="btn-transform transform-vertical red">
							<div><a href="#" class="item item-1 redbtn"> <i class="ion-play"></i> Watch Trailer</a></div>
							<div><a :href="`https://www.youtube.com/embed/${movie.video_path}`" class="item item-2 redbtn fancybox-media hvr-grow"><i class="ion-play"></i></a></div>
						</div>
						<!-- <div class="btn-transform transform-vertical">
							<div><a href="#" class="item item-1 yellowbtn"> <i class="ion-card"></i> Buy ticket</a></div>
							<div><a href="#" class="item item-2 yellowbtn"><i class="ion-card"></i></a></div>
						</div> -->
					</div>
				</div>
			</div>
			<div class="col-md-8 col-sm-12 col-xs-12">
				<div class="movie-single-ct main-content">
					<h1 class="bd-hd">{{ movie.title }}<span>{{ movie.release_date.slice(0, 4) }}</span> </h1>
					
					<div class="social-btn" style="overflow: hidden;">
					
						<a @click.prevent="addLike" href="" class="parent-btn"><i class="ion-heart"></i> Add to Playlist</a>
						<div class="hover-bnt">
							<a @click.prevent="" href="" class="parent-btn"><i class="ion-android-share-alt"></i>share</a>																					

							<div class="hvr-item">
								<a href="https://ko-kr.facebook.com/zuck" class="hvr-grow"><i class="ion-social-facebook"></i></a>
								<a href="https://twitter.com/jack" class="hvr-grow"><i class="ion-social-twitter"></i></a>
								<!-- <a href="#" class="hvr-grow"><i class="ion-social-googleplus"></i></a> -->
								<a href="https://www.youtube.com/c/%EC%8A%B9%EC%9A%B0%EC%95%84%EB%B9%A0" class="hvr-grow"><i class="ion-social-youtube"></i></a>
							</div>
						</div>		
					</div>
					<div class="movie-rate">
						<div class="rate">
							<i class="ion-android-star"></i>
							<p><span>{{ Math.round(movie.rate.rate * 10) / 10 }}</span> /10<br>
								<span class="rv">{{ movie.rating_set.length }} Comments</span>
							</p>
						</div>
						<div class="rate-star">
							<p>Rate This Movie:  </p>
							<i v-for="(star1, index) in Math.round(movie.rate.rate)" :key="index + 'b'" class="ion-ios-star"></i>	
							<i v-for="(star2, index) in 10 - Math.round(movie.rate.rate)" :key="index + 'c'" class="ion-ios-star-outline"></i>
						</div>
					</div>


					<div class="movie-tabs">
						<div class="tabs">
							<ul class="tab-links tabs-mv">
								<li v-for="(tab, idx) in tabs" :key="idx" :class="{ active: currentTab === idx }">
									<a @click.prevent="currentTab = idx " href="#">{{ tab }}</a>
								</li>
								<!-- <li class="active"><a @click.prevent="" href="#overview">Overview</a></li>
								<li><a @click.prevent="" href="#reviews"> Reviews</a></li>
								<li><a @click.prevent="" href="#cast">  Cast & Crew </a></li>
								<li><a @click.prevent="" href="#media"> Media</a></li> 
								<li><a @click.prevent="" href="#moviesrelated"> Related Movies</a></li>                         -->
							</ul>
						    <div class="tab-content">

									<!-- 줄거리 -->
									<div v-show="currentTab == 0" id="overview" class="">							
										<movie-overview :movie="movie"></movie-overview>
									</div>


									<!-- 리뷰 -->
						        <div v-show="currentTab == 1" id="reviews" class="">
						           <movie-review :movie="movie"></movie-review>
						        </div>

									<!-- 배우 -->
										<div v-show="currentTab == 2" id="cast" class="">
							        <movie-cast :movie="movie"></movie-cast>
					       	 	</div>

									<!-- 미디어 -->
					       	 	<div v-show="currentTab == 3" id="media" class="">
						        	<movie-media></movie-media>
					       	 	</div>

									<!-- 관련 영화 -->
									<div v-show="currentTab == 4" id="moviesrelated" class="">
										<movie-related></movie-related>
									</div>

							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
		</div>

</template>

<script>
import axios from 'axios'
import MovieOverview from '../components/MovieDetail/MovieOverview.vue'
import MovieReview from '../components/MovieDetail/MovieReview.vue'
import MovieCast from '../components/MovieDetail/MovieCast.vue'
import MovieMedia from '../components/MovieDetail/MovieMedia.vue'
import MovieRelated from '../components/MovieDetail/MovieRelated.vue'
// import jwt_decode from "jwt-decode";

const api = 'http://127.0.0.1:8000/api/v1/movies/movie/'

export default {
  components: { MovieOverview, MovieReview, MovieCast, MovieMedia, MovieRelated },
  name: 'Detail',
  data () {
    return {
      movie: null,
			currentTab: 0,
			tabs: ['overview', 'review', 'cast & crew', 'media', 'related movies'],
    }
  },
	methods: {
		getMovie () {
			axios({
			method: 'get',
			url: api + `${this.$route.params.id}/`
		})
			.then(res => {
				this.movie = res.data
				// console.log(this.movie)
			})
			.catch(err => {
				console.log(err)
				this.$router.push({ name: 'Home'})
				alert('존재하지 않는 영화입니다.')
			})
		},
		setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
		addLike () {
			if (!this.$store.state.token) {
				alert('로그인이 필요합니다.')
				this.$router.go()
			}	else {
				// const token = this.$store.state.token
				// const decoded = jwt_decode(token)
				axios({
							method: 'post',
							url: 'http://127.0.0.1:8000/api/v1/community/' + `${this.$route.params.id}/like/`,
							headers: this.setToken()
						})
							.then(res => {
								console.log(res, '데이터 전송 성공')
								if (res.data.is_like) {
									alert('영화 뭉치에 추가했습니다.')
								} else {
									alert('영화 뭉치에서 제거했습니다.')
								}
								this.getMovie()
								// this.$router.go()
								// console.log(decoded)
								// this.$router.push({name: 'UserProfile', params: {username: decoded.username}})
							})
							.catch(err => {
								console.log(err)
								alert('로그인이 필요합니다.')
							})											
			}
		}
	},
		
  created () {
		this.getMovie()
	},	
}
</script>

<style>

</style>