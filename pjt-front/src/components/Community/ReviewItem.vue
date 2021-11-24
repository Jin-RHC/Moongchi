<template>
<div class="col-md-4 col-sm-12 col-xs-12">
  <div class="blog-item-style-2" style="margin-bottom: auto;">
    <a @click.prevent="$router.push({ name: 'ReviewDetail', params: {reviewId: review.id }})" href="blogdetail.html">
      <img :src="`https://image.tmdb.org/t/p/original${review.movie.poster_path}`" alt=""></a>
    <div class="blog-it-infor">
      <h3><a @click.prevent="$router.push({ name: 'ReviewDetail', params: {reviewId: review.id }})" href="blogdetail.html"> {{ review.movie.title }}: {{review.title}}</a></h3>
      <div style="display: flex; justify-content: space-between;">
        <span class="time">{{ review.updated_at.slice(0, 10)}} {{review.updated_at.slice(11, 16)}}</span>
        <span class="" style="font-family: serif; font-weight: light; font-size: 1em;">{{ review.user.nickname }}</span>
      </div>
        <span class="right-it time" style="display: flex; justify-content: end; font-weight: bold; margin-top: 20px;">조회 0 | 추천 {{ review.like_users_count }} | 댓글 {{ review.comment_set.length }} </span>        
      <!-- <p>Looks like Kong: Skull Island started a tradition with its casting of Straight ...</p> -->
    </div>
  </div>
  <hr style="margin-bottom: 30px;">
</div>
</template>

<script>
// import axios from 'axios'
export default {
  name: 'ReviewItem',
  props: {
    review: Object
  },
  data () {
    return {
      movie: null,
    }
  },
  // created () {
  //   const API_KEY = 'e856b3ac18eec7abd7cf6099f977bbff'
  //   console.log(this.review)    
  //   axios({
  //     method: 'get',
  //     url: `https://api.themoviedb.org/3/movie/${this.review.movieId}?api_key=${API_KEY}&language=ko-KR`
  //   })
  //     .then(res => {        
  //       this.movie = res.data
  //     })
  // },
}
</script>

<style>

</style>