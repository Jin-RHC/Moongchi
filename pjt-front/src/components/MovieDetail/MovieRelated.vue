<template>
  <div class="row">
    <!-- <h3>Related Movies To</h3>
    <h2>Skyfall: Quantum of Spectre</h2> -->
    <div v-if="isLogin">

    <div class="topbar-filter">
      <p>Found <span>3 movies</span> in total</p>
      <label>Sort by:</label>
      <select disabled>
        <option value="popularity">Popularity Descending</option>
        <option value="popularity">Popularity Ascending</option>
        <option value="rating">Rating Descending</option>
        <option value="rating">Rating Ascending</option>
        <option value="date">Release date Descending</option>
        <option value="date">Release date Ascending</option>
      </select>
    </div>
    <movie-related-item 
    v-for="movie in recommendedMovies"
    :key="movie.id"
    :movie="movie"
    ></movie-related-item>    


    <!-- <div class="topbar-filter">
      <label>Movies per page:</label>
      <select>
        <option value="range">5 Movies</option>
        <option value="saab">10 Movies</option>
      </select>
      <div class="pagination2">
        <span>Page 1 of 2:</span>
        <a class="active" href="#">1</a>
        <a href="#">2</a>
        <a href="#"><i class="ion-arrow-right-b"></i></a>
      </div>
    </div> -->
    </div>
    <div v-else>
      
      <span class="time" style="font-size: 20px;">로그인이 필요한 페이지입니다.</span>
      
    </div>
</div>
</template>

<script>
import axios from 'axios'
import MovieRelatedItem from './MovieRelatedItem.vue'
const API = process.env.VUE_APP_BACKEND_URL

export default {
  components: { MovieRelatedItem },
  name: 'MovieRelated',
  data () {
    return {
      recommendedMovies: [],
      isLogin: false
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
    getMovies () {
      axios({
      method: 'get',
      url: `${API}/api/v1/movies/movie/${this.$route.params.id}/recommended/`,
      headers: this.setToken()
    })
      .then(res => {
        // console.log(res.data)
        this.recommendedMovies = res.data
      })
  }},
  created () {
    this.getMovies()
    if (this.$store.state.token) {
      this.isLogin = true
    }
  }


}
</script>

<style>

</style>