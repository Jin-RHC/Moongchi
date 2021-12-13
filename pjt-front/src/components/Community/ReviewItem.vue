<template>
<div class="col-md-4 col-sm-12 col-xs-12">
  <div id="card" class="blog-item-style-2" style="margin-bottom: 0px;">
    <a @click.prevent="$router.push({ name: 'ReviewDetail', params: {reviewId: review.id }})" href="blogdetail.html">
      <img :src="`https://image.tmdb.org/t/p/original${review.movie.poster_path}`" alt=""></a>
    <div class="blog-it-infor">
      <h3><a @click.prevent="$router.push({ name: 'ReviewDetail', params: {reviewId: review.id }})" href="blogdetail.html"> [{{ review.movie.title }}]</a></h3>
      <h3><a @click.prevent="$router.push({ name: 'ReviewDetail', params: {reviewId: review.id }})" href="blogdetail.html"> {{review.title}}</a></h3>
      <div style="display: flex; justify-content: start;">
        <span class="time">{{ review.updated_at.slice(0, 10)}} {{review.updated_at.slice(11, 16)}}</span>
      </div>
      <div style="display: flex; justify-content: end; margin-top: 15px;">
        <a @click.prevent="$router.push({ name: 'UserProfile', params: { username: `${review.user.username}`}})" href=""><span class="" style="font-family: serif; font-weight: light; font-size: 1em;">{{ review.user.nickname }}</span></a>        
      </div>
    <span class="right-it time" style="display: flex; justify-content: end; font-weight: bold; margin-top: 10px;">조회 0 | 추천 {{ review.like_users_count }} | 댓글 {{ review.comment_set.length }} </span>      
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

<style scoped>
  @media screen and (max-width: 992px) {
    #card {
      height: 700px;
    }
  }
  @media screen and (min-width: 992px) {
    #card {
      height: 55vh;
    }
  }
</style>