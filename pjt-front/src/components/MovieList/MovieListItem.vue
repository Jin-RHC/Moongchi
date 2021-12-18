<template>
  <div class="movie-item-style-2 movie-item-style-1">
    <img :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" alt="">
    <div class="hvr-inner" style="margin-left: 3rem;">
      <!-- <router-link :to="{ 
          name: 'MovieDetail',
          params: { 
            movieId: `${movie.id}`,
          }
        }"
      >Read more<i class="ion-android-arrow-dropright"></i></router-link> -->
      <router-link :to="{ 
          name: 'MovieDetail',
          params: { 
            id: `${movie.id}`,
            data: movie,
          }
        }"
        
      >Read more<i class="ion-android-arrow-dropright"></i></router-link>
      <!-- <a :href="`http://localhost:8080/detail_${movie.id}`"> Read more <i class="ion-android-arrow-dropright"></i> </a> -->
    </div>
    <div class="mv-item-infor">
      <h6><a href="#">{{ movie.title }}</a></h6>
      <p class="rate"><i class="ion-android-star"></i><span>{{ Math.round(movie.rating_average * 10) / 10 }}</span> /10</p>
    </div>
  </div>	
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: Object
  },
  methods: {
    detail () {
      this.$router.push(`detail_${this.movie.id}`)
    }
  },
  computed: {
    detailURL () {
      return `http://localhost:8080/detail_${this.movie.id}`
    }
  }
}
</script>

<style>

</style>