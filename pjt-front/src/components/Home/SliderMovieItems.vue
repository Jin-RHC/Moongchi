<template>
<div class="slider movie-items" style="">
	<div class="container">
		<div class="row">
			<div class="social-link">
				<p>Follow us: </p>
				<a href="https://ko-kr.facebook.com/zuck"><i class="ion-social-facebook"></i></a>
				<a href="https://twitter.com/jack"><i class="ion-social-twitter"></i></a>
				<a href="https://www.youtube.com/c/%EC%8A%B9%EC%9A%B0%EC%95%84%EB%B9%A0"><i class="ion-social-youtube"></i></a>
			</div>
	    	<!-- <div  class="slick-multiItemSlider"> -->
					<!-- <slider-movie-item 
						:movieItem="movieItem"
					></slider-movie-item> -->
					<carousel-3d :autoplay="true" :autoplay-timeout="5000" :display="20" :controlsVisible="true" :height="490" :style="{width: width + 'px'}">
						<slide v-for="(slide, i) in slides" :index="i" :key="i">      
							<template slot-scope="{ index, isCurrent, leftIndex, rightIndex }">
								<div class="movie-item" style="width: 100%;">
									<img :data-index="index" :class="{ current: isCurrent, onLeft: (leftIndex >= 0), onRight: (rightIndex >= 0) }" :src="`https://image.tmdb.org/t/p/original${slide.poster_path}`" style="">
									<div class="hvr-inner">
										<a @click.prevent="$router.push({ name: 'MovieDetail', params: { id: `${slide.id}`}})" href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
									</div>
								
									<div class="title-in">
										<div class="cate">
											<!-- <span class="blue"><a href="#">Sci-fi</a></span> -->
										</div>
										<h6><a @click.prevent="$router.push({ name: 'MovieDetail', params: { id: `${slide.id}`}})" href="#" style="font-size: 25px;">{{ slide.title }}</a></h6>
										<p><i class="ion-android-star"></i><span>{{ Math.round(slide.rating_average * 10) / 10 }}</span> /10</p>
									</div>            
								</div>
							</template>
						</slide>
					</carousel-3d>
	    		
	    	<!-- </div> -->
	    </div>
	</div>
</div>
</template>

<script>
import axios from 'axios'
import { Carousel3d, Slide } from 'vue-carousel-3d';
const API = process.env.VUE_APP_BACKEND_URL

// import SliderMovieItem from './SliderMovieItem.vue'
export default {
  components: { 
		// SliderMovieItem 
		Carousel3d,
		Slide
		},
  name: 'SliderMovieItems',
	data () {
    return {
			slides: 20,			
			width: null
			
    }
  },
	methods: {
		handler () {
			if (425 < window.innerWidth) {
				this.width = null
				console.log('425 < window.innerwidth')
			}	else if (window.innerWidth <= 375 ) {
				console.log('window.innerwidth <= 375')
				this.width = 300
			} else {
				this.width = 350
				console.log('375 < window.innerwidth <= 425')
			}
		}
	},
  created () {
		axios({
			method: 'get',
        url: `${API}/api/v1/movies/mainmovies/` 
      })
        .then(res => {          
					this.slides = res.data['now-playing']
        })
		this.handler()
  },
	mounted () {
		window.addEventListener('resize', this.handler())
	}		
}
</script>

<style>

</style>