<template>
  <div class="buster-light">
<div class="hero common-hero">
	<div class="container">
		<div class="row">
			<div class="col-md-12">
				<div class="hero-ct">
					<h1>Movie Listing</h1>
					<ul class="breadcumb">
						<li @click.prevent="$router.push({name: 'Home'})" class="active"><a href="#">Home</a></li>
						<li> <span class="ion-ios-arrow-right"></span> movie listing</li>
					</ul>
				</div>
			</div>
		</div>
	</div>
</div>
<div class="page-single">
	<div class="container">
		<div class="row">
			<div class="col-md-12 col-sm-12 col-xs-12">
				<div class="topbar-filter fw">
					<p>Found <span>{{ movies.length }} movies</span> in total</p>
					<label>Sort by:</label>
					<select disabled>
						<option value="popularity">Popularity Descending</option>
						<option value="popularity">Popularity Ascending</option>
						<option value="rating">Rating Descending</option>
						<option value="rating">Rating Ascending</option>
						<option value="date">Release date Descending</option>
						<option value="date">Release date Ascending</option>
					</select>
					<a href="#" class="list"><i class="ion-ios-list-outline "></i></a>
					<a href="#" class="grid"><i class="ion-grid active"></i></a>
				</div>
				<div class="flex-wrap-movielist mv-grid-fw">
            <movie-list-item v-for="movie in movies" :key="movie.id" :movie="movie"></movie-list-item>									
				</div>
        

				<div class="topbar-filter">
          
					<label>Movies per page:</label>
					<select>
						<option value="range">20 Movies</option>
						<option value="saab">10 Movies</option>
					</select>
					  

					<!-- <div class="pagination2">
						<span>Page 1 of 2:</span>
						<a class="active" href="#">1</a>
						<a href="#">2</a>
						<a href="#">3</a>
						<a href="#">...</a>
						<a href="#">78</a>
						<a href="#">79</a>
						<a href="#"><i class="ion-arrow-right-b"></i></a>
					</div> -->
				</div>

				
			</div>
		</div>
	</div>
</div>
		  <!-- <infinite-loading @infinite="getMovies"></infinite-loading> -->
		</div>

</template>

<script>
// import InfiniteLoading from 'vue-infinite-loading';

import axios from 'axios'
import MovieListItem from '../components/MovieList/MovieListItem.vue'
const API = process.env.VUE_APP_BACKEND_URL

export default {
  components: { 
		MovieListItem, 
		// InfiniteLoading,
	},
  name: 'MovieListSearch',
  data () {
    return {
			// page: 1,
      movies: [],
    }
  },
  methods: {
    getMoviesSearch () {      
      axios({
				method: 'get',
				url: `${API}/api/v1/movies/moviesearch/` + `${this.$route.query.query}/`
			})
				
				.then((res) => {    
          console.log(res.data.length)      
          if (res.data.length === 0) {
            // alert('검색 결과가 없습니다.')
            // this.$router.push({ name: 'MovieList'})            
          } else {
            this.movies = res.data
          }
      })
    }
  },
  created () {    
    this.getMoviesSearch()
  }
}
</script>

<style>

</style>