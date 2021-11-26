<template>
  <div>
    <div class="movie-items" v-for="i in 1" :key="i" style="padding: 10px 0;">
      <label class="" 
      style="display: inline-block;					
      font-size: 24px;
      line-height: 30px;
      font-weight: 700;" for="">좋아한 영화들</label>
      <carousel-3d disable3d="true" :space="250" :autoplay="false" :autoplay-timeout="5000" :display="20" :controlsVisible="true" :clickable="false" :width="230" :height="325"> 
        <slide v-for="(slide, i) in movies" :index="i" :key="i">
          <template slot-scope="{ index, isCurrent, leftIndex, rightIndex }">
            <div class="movie-item" style="width: 100%;">								
              <img :data-index="index" :class="{ current: isCurrent, onLeft: (leftIndex >= 0), onRight: (rightIndex >= 0) }" :src="`https://image.tmdb.org/t/p/original${slide.poster_path}`">
              <div class="hvr-inner">
                <a @click.prevent="$router.push({name: 'MovieDetail', params: {id: slide.id}})" href="moviesingle.html"> Read more <i class="ion-android-arrow-dropright"></i> </a>
              </div>
          
              <div class="title-in" style="margin-bottom: 40px;">    
                <h6><a href="#">{{ slide.title }}</a></h6>
                <p><i class="ion-android-star"></i><span>{{ slide.rating_average }}</span> /10</p>
              </div>
            </div>
          </template>
        </slide>
      </carousel-3d>
    </div>
  </div>

</template>

<script>
import axios from 'axios'
import { Carousel3d, Slide } from 'vue-carousel-3d';

export default {
  name: 'CelebMovie',
  props: {
    celeb: Object
  },
  methods: {
    // goToMovie: function () {
    //   this.$router.push({name: 'MovieDetail', params: {id: this.review.movie.id}})
    // },
    // goToReview: function () {
    //   this.$router.push({name: 'ReviewDetail', params: {reviewId: this.review.id}})
    // },
  }
}
</script>

<style>

</style>


