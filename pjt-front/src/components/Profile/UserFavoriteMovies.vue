<template>
			<div>
				<div id="container" class="" style="padding: 5px 10px; background-color: #e4eaf0;">
					<p id="content" style="margin-left: 10px;">Found <span style="color: #4280bf;">{{ favoriteMovies.length }} movies</span> in total</p>
					<!-- <label>Sort by:</label>
					<select>
						<option value="range">-- Choose option --</option>
						<option value="saab">-- Choose option 2--</option>
					</select>
					<a href="" class="list" @click.prevent="none"><i class="ion-ios-list-outline "></i></a>
					<a href="" class="grid" @click.prevent="none"><i class="ion-grid active"></i></a> -->
					<!-- <a href="userfavoritelist.html" class="list"><i class="ion-ios-list-outline "></i></a>
					<a  href="userfavoritegrid.html" class="grid"><i class="ion-grid active"></i></a> -->
				</div>
				
					

				<div class="movie-items" v-for="i in 1" :key="i" style="padding: 10px 0;">
					
						<label class="" 
						style="display: inline-block;					
						font-size: 24px;
						line-height: 30px;
						font-weight: 700;" for="">좋아한 영화들</label>
						<carousel-3d v-if="favoriteMovies.length" :disable3d="true" :space="250" :autoplay="false" :autoplay-timeout="5000" :display="20" :controlsVisible="true" :clickable="false" :width="230" :height="325"> 
							<slide v-for="(slide, i) in favoriteMovies" :index="i" :key="i">
								<template slot-scope="{ index, isCurrent, leftIndex, rightIndex }">
									<div class="movie-item" style="width: 100%;">								
										<img :data-index="index" :class="{ current: isCurrent, onLeft: (leftIndex >= 0), onRight: (rightIndex >= 0) }" :src="`https://image.tmdb.org/t/p/original${slide.poster_path}`">
										<div class="hvr-inner">
											<a @click.prevent="$router.push({name: 'MovieDetail', params: {id: slide.id}})" href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
										</div>
								
										<div class="title-in" style="margin-bottom: 40px;">    
											<h6><a href="#">{{ slide.title }}</a></h6>
											<p><i class="ion-android-star"></i><span>{{ Math.round(slide.rating_average * 10) / 10 }}</span> /10</p>
										</div>
									</div>
								</template>
							</slide>
						</carousel-3d>
					
					<div v-else style="margin-top: 50px;">
						<span class="time" style="font-size: 30px; top: 50px;">등록된 영화가 없습니다.</span>
					</div>
					
					<hr> 
					
							<!-- <div class="slide-it">
								<div class="movie-item">
									<div class="mv-img">
										<img src="images/uploads/mv-item1.jpg" alt="" width="185" height="284">
									</div> 
									<div class="hvr-inner">
										<a  href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
									</div>
									<div class="title-in">
										<h6><a href="#">Interstellar</a></h6>
										<p><i class="ion-android-star"></i><span>7.4</span> /10</p>
									</div>
								</div>
							</div> -->
						

						<!-- <div class="movie-item-style-2 movie-item-style-1 style-3">
							<img src="images/uploads/mv1.jpg" alt="">
							<div class="hvr-inner">
								<a  href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
								<div class="mv-item-infor">
									<h6><a href="moviesingle.html">oblivion</a></h6>
									<p class="rate"><i class="ion-android-star"></i><span>8.1</span> /10</p>
								</div>
							</div>
						</div>	 -->


						<!-- <div class="movie-item-style-2 movie-item-style-1 style-3">
							<img src="images/uploads/mv2.jpg" alt="">
							<div class="hvr-inner">
	            				<a  href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
	            			</div>
							<div class="mv-item-infor">
								<h6><a href="moviesingle.html">into the wild</a></h6>
								<p class="rate"><i class="ion-android-star"></i><span>7.8</span> /10</p>
							</div>
						</div>	


						<div class="movie-item-style-2 movie-item-style-1 style-3">
	            			<img src="images/uploads/mv-item3.jpg" alt="">
	            			<div class="hvr-inner">
	            				<a  href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
	            			</div>
	            			<div class="mv-item-infor">
	            				<h6><a href="moviesingle.html">Die hard</a></h6>
	            				<p class="rate"><i class="ion-android-star"></i><span>7.4</span> /10</p>
	            			</div>
	            		</div>
					
					
						<div class="movie-item-style-2 movie-item-style-1 style-3">
	            			<img src="images/uploads/mv-item4.jpg" alt="">
	            			<div class="hvr-inner">
	            				<a  href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
	            			</div>
	            			<div class="mv-item-infor">
	            				<h6><a href="moviesingle.html">The walk</a></h6>
	            				<p class="rate"><i class="ion-android-star"></i><span>7.4</span> /10</p>
	            			</div>
	            		</div>


	            		<div class="movie-item-style-2 movie-item-style-1 style-3">
							<img src="images/uploads/mv3.jpg" alt="">
							<div class="hvr-inner">
	            				<a  href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
	            			</div>
							<div class="mv-item-infor">
								<h6><a href="moviesingle.html">blade runner  </a></h6>
								<p class="rate"><i class="ion-android-star"></i><span>7.3</span> /10</p>
							</div>
						</div>


						<div class="movie-item-style-2 movie-item-style-1 style-3">
							<img src="images/uploads/mv4.jpg" alt="">
							<div class="hvr-inner">
	            				<a  href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
	            			</div>
							<div class="mv-item-infor">
								<h6><a href="moviesingle.html">Mulholland pride</a></h6>
								<p class="rate"><i class="ion-android-star"></i><span>7.2</span> /10</p>
							</div>
						</div>


						<div class="movie-item-style-2 movie-item-style-1 style-3">
							<img src="images/uploads/mv5.jpg" alt="">
							<div class="hvr-inner">
	            				<a  href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
	            			</div>
							<div class="mv-item-infor">
								<h6><a href="moviesingle.html">skyfall: evil of boss</a></h6>
								<p class="rate"><i class="ion-android-star"></i><span>7.0</span> /10</p>
							</div>
						</div>
						<div class="movie-item-style-2 movie-item-style-1 style-3">
	            			<img src="images/uploads/mv-item1.jpg" alt="">
	            			<div class="hvr-inner">
	            				<a  href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
	            			</div>
	            			<div class="mv-item-infor">
	            				<h6><a href="moviesingle.html">Interstellar</a></h6>
	            				<p class="rate"><i class="ion-android-star"></i><span>7.4</span> /10</p>
	            			</div>
	            		</div>
	            		<div class="movie-item-style-2 movie-item-style-1 style-3">
	            			<img src="images/uploads/mv-item2.jpg" alt="">
	            			<div class="hvr-inner">
	            				<a  href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
	            			</div>
	            			<div class="mv-item-infor">
	            				<h6><a href="moviesingle.html">The revenant</a></h6>
	            				<p class="rate"><i class="ion-android-star"></i><span>7.4</span> /10</p>
	            			</div>
	            		</div>
	            		<div class="movie-item-style-2 movie-item-style-1 style-3">
	            			<img src="images/uploads/mv-it10.jpg" alt="">
	            			<div class="hvr-inner">
	            				<a  href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
	            			</div>
	            			<div class="mv-item-infor">
	            				<h6><a href="moviesingle.html">harry potter</a></h6>
	            				<p class="rate"><i class="ion-android-star"></i><span>7.4</span> /10</p>
	            			</div>
	            		</div>
						<div class="movie-item-style-2 movie-item-style-1 style-3">
	            			<img src="images/uploads/mv-it11.jpg" alt="">
	            			<div class="hvr-inner">
	            				<a  href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
	            			</div>
	            			<div class="mv-item-infor">
	            				<h6><a href="moviesingle.html">guardians galaxy</a></h6>
	            				<p class="rate"><i class="ion-android-star"></i><span>7.4</span> /10</p>
	            			</div>
	            		</div>
	            		<div class="movie-item-style-2 movie-item-style-1 style-3">
	            			<img src="images/uploads/mv-it12.jpg" alt="">
	            			<div class="hvr-inner">
	            				<a  href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
	            			</div>
	            			<div class="mv-item-infor">
	            				<h6><a href="moviesingle.html">the godfather</a></h6>
	            				<p class="rate"><i class="ion-android-star"></i><span>7.4</span> /10</p>
	            			</div>
	            		</div>
						<div class="movie-item-style-2 movie-item-style-1 style-3">
	            			<img src="images/uploads/mv-item6.jpg" alt="">
	            			<div class="hvr-inner">
	            				<a  href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
	            			</div>
	            			<div class="mv-item-infor">
	            				<h6><a href="moviesingle.html">blue velvet</a></h6>
	            				<p class="rate"><i class="ion-android-star"></i><span>7.4</span> /10</p>
	            			</div>
	            		</div>
	            		<div class="movie-item-style-2 movie-item-style-1 style-3">
	            			<img src="images/uploads/mv-item7.jpg" alt="">
	            			<div class="hvr-inner">
	            				<a  href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
	            			</div>
	            			<div class="mv-item-infor">
	            				<h6><a href="moviesingle.html">gravity</a></h6>
	            				<p class="rate"><i class="ion-android-star"></i><span>7.4</span> /10</p>
	            			</div>
	            		</div>
	            		<div class="movie-item-style-2 movie-item-style-1 style-3">
	            			<img src="images/uploads/mv-item8.jpg" alt="">
	            			<div class="hvr-inner">
	            				<a  href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
	            			</div>
	            			<div class="mv-item-infor">
	            				<h6><a href="moviesingle.html">southpaw</a></h6>
	            				<p class="rate"><i class="ion-android-star"></i><span>7.4</span> /10</p>
	            			</div>
	            		</div>
	            		<div class="movie-item-style-2 movie-item-style-1 style-3">
	            			<img src="images/uploads/mv-it9.jpg" alt="">
	            			<div class="hvr-inner">
	            				<a  href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
	            			</div>
	            			<div class="mv-item-infor">
	            				<h6><a href="moviesingle.html">jurassic park</a></h6>
	            				<p class="rate"><i class="ion-android-star"></i><span>7.4</span> /10</p>
	            			</div>
	            		</div>
	            		<div class="movie-item-style-2 movie-item-style-1 style-3">
	            			<img src="images/uploads/mv-item9.jpg" alt="">
	            			<div class="hvr-inner">
	            				<a  href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
	            			</div>
	            			<div class="mv-item-infor">
	            				<h6><a href="moviesingle.html">the forest</a></h6>
	            				<p class="rate"><i class="ion-android-star"></i><span>7.4</span> /10</p>
	            			</div>
	            		</div>
	            		<div class="movie-item-style-2 movie-item-style-1 style-3">
	            			<img src="images/uploads/mv-item10.jpg" alt="">
	            			<div class="hvr-inner">
	            				<a  href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
	            			</div>
	            			<div class="mv-item-infor">
	            				<h6><a href="moviesingle.html">spectre</a></h6>
	            				<p class="rate"><i class="ion-android-star"></i><span>7.4</span> /10</p>
	            			</div>
	            		</div>
	            		<div class="movie-item-style-2 movie-item-style-1 style-3">
	            			<img src="images/uploads/mv-item11.jpg" alt="">
	            			<div class="hvr-inner">
	            				<a  href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
	            			</div>
	            			<div class="mv-item-infor">
	            				<h6><a href="moviesingle.html">strager things</a></h6>
	            				<p class="rate"><i class="ion-android-star"></i><span>7.4</span> /10</p>
	            			</div>
	            		</div>
	            		<div class="movie-item-style-2 movie-item-style-1 style-3">
	            			<img src="images/uploads/mv-item12.jpg" alt="">
	            			<div class="hvr-inner">
	            				<a  href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
	            			</div>
	            			<div class="mv-item-infor">
	            				<h6><a href="moviesingle.html">la la land</a></h6>
	            				<p class="rate"><i class="ion-android-star"></i><span>7.4</span> /10</p>
	            			</div>
	            		</div> -->
				</div>		
				<!-- <div class="topbar-filter">
					<label>Movies per page:</label>
					<select>
						<option value="range">20 Movies</option>
						<option value="saab">10 Movies</option>
					</select>					
				</div> -->
			</div>
</template>

<script>
// import axios from 'axios'
import jwt_decode from "jwt-decode"
import { Carousel3d, Slide } from 'vue-carousel-3d';
// const API = process.env.VUE_APP_BACKEND_URL

export default {
  name: 'UserFavoriteMovies',
	components: {
		Carousel3d,
    Slide
  },
	data () {
		return {
			movies: 20,
		}
	},
	props: {
		favoriteMovies: Array
	},
	methods: {
		none: function () {
			const favoriteMovies = this.props.favoriteMovies
			this.movies = favoriteMovies.length
		},
		setToken: function () {
      const token = localStorage.getItem('jwt')
			this.myName = jwt_decode(token).username
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
	},
	created () {
    // const API_KEY = 'e856b3ac18eec7abd7cf6099f977bbff'
		// const ROOT_URL = `${API}`
    // axios({
    //   method: 'get',
    //   url: `${ROOT_URL}/api/v1/accounts/${this.$router.params}/`,
		// 	headers: this.setToken()
    // })
    //   .then(res => {
		// 		console.log(res)
    //     this.movies = res.data.results
    //   })
  },
	// updated () {
  //   // const API_KEY = 'e856b3ac18eec7abd7cf6099f977bbff'
	// 	const ROOT_URL = 'http://127.0.0.1:8000/'
  //   axios({
  //     method: 'get',
  //     url: `${ROOT_URL}/api/v1/accounts/${username}/`
  //   })
  //     .then(res => {
	// 			console.log(res)
  //       this.movies = res.data.results
  //       // console.log(this.movieItems)
  //     })
  // },
}
</script>

<style scoped>
</style>