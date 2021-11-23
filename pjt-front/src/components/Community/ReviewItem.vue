<template>
<div class="col-md-4 col-sm-12 col-xs-12">
  <div class="blog-item-style-2" style="margin-bottom: auto;">
    <a href="blogdetail.html">
      <img :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" alt=""></a>
    <div class="blog-it-infor">
      <h3><a href="blogdetail.html"> 영화 제목: King Of The Monsters Adds O’Shea Jackson Jr</a></h3>
      <div style="display: flex; justify-content: space-between;">
        <span class="time">27 Mar 2017</span>
        <span class="" style="font-family: serif; font-weight: light; font-size: 1em;">user</span>
      </div>
        <span class="right-it time" style="display: flex; justify-content: end; font-weight: bold; margin-top: 20px;">조회 0 | 추천 0 | 댓글 0 </span>        
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