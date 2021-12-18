<template>
<div class="col-md-4 col-sm-12 col-xs-12">
  <div id="card" class="blog-item-style-2" style="margin-bottom: 0px;">
    <a @click.prevent="$router.push({ name: 'ReviewDetail', params: {reviewId: review.id }})" href="blogdetail.html">
      <img id="img" :src="`https://image.tmdb.org/t/p/original${review.movie.poster_path}`" alt="" style="height: 65%;"></a>
    <div class="blog-it-infor" style="display: flex; flex-direction: column; justify-content: space-between; height: auto;">
      <div>
        <span id="movie-title"><a id="movie-title-text" style="font-size: 15px;" @click.prevent="$router.push({ name: 'ReviewDetail', params: {reviewId: review.id }})" href="blogdetail.html">{{ review.movie.title }}</a></span>
        <h3 style="margin-top: 1rem; text-overflow: ellipsis; overflow: hidden; white-space: nowrap;"><a @click.prevent="$router.push({ name: 'ReviewDetail', params: {reviewId: review.id }})" href="blogdetail.html"> {{review.title}}</a></h3>
      </div>
      <div style="display: flex; justify-content: start;">
        <span class="time">{{ review.updated_at.slice(0, 10)}} {{review.updated_at.slice(11, 16)}}</span>
      </div>
      <div style="display: flex; justify-content: end; margin-top: 1rem;">
        <a @click.prevent="$router.push({ name: 'UserProfile', params: { username: `${review.user.username}`}})" href=""><span class="" style="font-family: serif; font-weight: light; font-size: 1em;">{{ review.user.nickname }}</span></a>        
      </div>
      <span class="right-it time" style="display: flex; justify-content: end; font-weight: bold; margin-top: 10px;">조회 0 | 추천 {{ review.like_users_count }} | 댓글 {{ commentCount }} </span>      
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
  computed: {    
    commentCount () {
      let cnt = this.review.comment_set.length
      this.review.comment_set.forEach(comment => {
        cnt += comment.nestedcomment_set.length
      })
      return cnt
    }
  }  
}
</script>

<style scoped>
  @media screen and (max-width: 321px) {
    #card {
      height: 65vh;
    }
  }
  @media screen and (min-width: 321px) and (max-width: 375px) {
    #card {
      height: 75vh;
    }
    
  }
  @media screen and (min-width: 375px) and (max-width: 992px) {
    #card {
      height: 60vh;
    }
    #img {
      height: 100%;
    }
  }
  @media screen and (min-width: 992px) and (max-width: 1200px) {
    #card {
      height: 58vh;
    }
  }
  @media screen and (min-width: 1200px) {
    #card {
      height: 60vh;
    }
  }
  #movie-title {
    background-color: #1692bb;
    padding: 3px 5px;
    border-radius: 3px;
    border: 0;
    font-family: inherit;
    font-size: 100%;
    font-style: inherit;
    font-weight: inherit;
    margin: 0;
    outline: 0;
    vertical-align: baseline;
    margin-bottom: 5rem;
  }
  #movie-title-text {
    font-family: 'Dosis', sans-serif;
    font-size: 12px;
    color: #ffffff;
    font-weight: 700;
    text-transform: uppercase;    
  }
</style>