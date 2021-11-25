<template>
  <div class="movie-item-style-2 userrate">
    <img @click.prevent="goToMovie" :src="`https://image.tmdb.org/t/p/original${review.movie.poster_path}`" alt="">
    <div @click.prevent="goToReview" class="mv-item-infor">
      <h6><a href="#">{{ review.movie.title }} <span> {{ review.movie.release_date.slice(0,4) }} </span></a></h6>
      <!-- <p class="time sm-text">your rate:</p>
      <p class="rate"><i class="ion-android-star"></i><span>9.0</span> /10</p> -->
      <span style="display: inline;" class="time sm-text">Review Title:</span>
      <h6><a href="#">{{ review.title }}</a></h6>
      <p>{{ review.content }}</p>		
      <p class="time sm">{{ review.updated_at.slice(5,7) }}/{{ review.updated_at.slice(8,10) }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserReviews',
  props: {
    review: Object
  },
  methods: {
    goToMovie: function () {
      this.$router.push({name: 'MovieDetail', params: {id: this.review.movie.id}})
    },
    goToReview: function () {
      this.$router.push({name: 'ReviewDetail', params: {reviewId: this.review.id}})
    },
  }
}
</script>

<style>

</style>