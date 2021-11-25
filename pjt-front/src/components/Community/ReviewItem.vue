<template>
<div class="col-md-4 col-sm-12 col-xs-12">
  <div class="blog-item-style-2" style="margin-bottom: auto; ">
    <a @click.prevent="$router.push({ name: 'ReviewDetail', params: {reviewId: review.id }})" href="blogdetail.html">
      <img :src="`https://image.tmdb.org/t/p/original${review.movie.poster_path}`" alt=""></a>
    <div class="blog-it-infor">
      <h3><a @click.prevent="$router.push({ name: 'ReviewDetail', params: {reviewId: review.id }})" href="blogdetail.html"> [{{ review.movie.title }}] {{review.title}}</a></h3>
      <div style="display: flex; justify-content: space-between;">
        <span class="time">{{ review.updated_at.slice(0, 10)}} {{review.updated_at.slice(11, 16)}}</span>
        <a @click.prevent="$router.push({ name: 'UserProfile', params: { username: `${review.user.username}`}})" href=""><span class="" style="font-family: serif; font-weight: light; font-size: 1em;">{{ review.user.nickname }}</span></a>        
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
}
</script>

<style>

</style>