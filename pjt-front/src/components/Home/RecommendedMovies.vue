<template>
<div class="col-md-12">
	<div class="title-hd">
		<h2>추천작</h2>
		<a @click.prevent="$router.push({name: 'MovieList'})" href="#" class="viewall">View all <i class="ion-ios-arrow-right"></i></a>
	</div>
	<div class="row">
		<carousel-3d :disable3d="true" :space="395" :autoplay="true" :autoplay-timeout="5000" :display="20" :controlsVisible="true" :height="510" :clickable="false">
			<slide v-for="(slide, i) in slides" :index="i" :key="i">
				<template slot-scope="{ index, isCurrent, leftIndex, rightIndex }">												
          <div class="movie-item" style="width: 100%;">
            <img :data-index="index" :class="{ current: isCurrent, onLeft: (leftIndex >= 0), onRight: (rightIndex >= 0) }" :src="`https://image.tmdb.org/t/p/original${slide.poster_path}`">
            <div class="hvr-inner">
              <a @click.prevent="$router.push({ name: 'MovieDetail', params: { id: `${slide.id}` }})" href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
            </div>
          
            <div class="title-in" style="margin-bottom: 40px;">    
              <h6><a href="#" style="font-size: 20px;">{{ slide.title }}</a></h6>
              <p><i class="ion-android-star"></i><span>{{ Math.round(slide.rating_average * 10) / 10 }}</span> /10</p>
            </div>
          </div>
				</template>
			</slide>
		</carousel-3d>
	</div>
	<hr>
	<br>
</div>
</template>

<script>
import axios from 'axios'
import { Carousel3d, Slide } from 'vue-carousel-3d';
const API = process.env.VUE_APP_BACKEND_URL

export default {
  components: {
		Carousel3d,
    Slide
  },
  name: 'RecommendedMovies',
  data () {
    return {
      slides: 20,
			
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
    getRecommended () {
      axios({
          method: 'get',
          url: `${API}/api/v1/movies/recommended/`,          
          headers: this.setToken()
        })
        .then(res => {
          // console.log(res.data)
          this.slides = res.data
        })
        .catch(() => {
          // console.log(err)
        })
    }
  },
  created () { 
    this.getRecommended()
  },
}
</script>

<style>

</style>