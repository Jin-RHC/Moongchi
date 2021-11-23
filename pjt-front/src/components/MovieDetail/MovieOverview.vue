<template>
  <div class="row">
      <div class="col-md-8 col-sm-12 col-xs-12">
        <p>{{ movie.overview }}</p>
  <div class="title-hd-sm" style="margin-top: 100px;">
    <h3>영화 기대지수</h3>
    <!-- <a href="#" class="time">All 5 Videos & 245 Photos <i class="ion-ios-arrow-right"></i></a> -->
  </div>  
  
  <div class="mvsingle-item ov-item" style="margin-top: 40px;" >


    


    <!-- <a class="img-lightbox"  data-fancybox-group="gallery" href="images/uploads/image11.jpg" ><img src="images/uploads/image1.jpg" alt=""></a>
    <a class="img-lightbox"  data-fancybox-group="gallery" href="images/uploads/image21.jpg" ><img src="images/uploads/image2.jpg" alt=""></a>
    <a class="img-lightbox"  data-fancybox-group="gallery" href="images/uploads/image31.jpg" ><img src="images/uploads/image3.jpg" alt=""></a>
    <div class="vd-it">
      <img class="vd-img" src="images/uploads/image4.jpg" alt="">
      <a class="fancybox-media hvr-grow" href="https://www.youtube.com/embed/o-0hcF97wy0"><img src="images/uploads/play-vd.png" alt=""></a>
    </div> -->
  </div>

  <div class="charts">
    <div style="display: flex; justify-content: space-between;">
      <a @click.prevent="addLike" style="" href="" title="좋아요"><font-awesome-icon :icon="['far', 'thumbs-up']" size="2x" color="#DB4455" /><span style="font-size: 2em;">{{like}}</span></a>
      <a @click.prevent="addDislike" style="" href="" title="글쎄요"><font-awesome-icon :icon="['far', 'thumbs-down']" size="2x" color="#0679C0"  /><span style="font-size: 2em;">{{dislike}}</span></a>
    </div>
    <div class="charts__chart chart--p100 chart--blue chart--sm" style="position: relative;">
      <div :class="`charts__chart chart--p${percentage} chart--red`">      
    <div v-if="!(like || dislike)" class="charts__chart chart--p100 chart--gray chart--sm" style="position: absolute; top: -5px"></div>
      </div>
    </div>
  
 </div>
  
  
  <div class="title-hd-sm" style="margin-top: 100px;">
    <h3 style="font-family: sans-serif;">한줄평 </h3>
    <a href="#" class="time">총 <span>120</span> 건 <i class="ion-ios-arrow-right"></i></a>
  </div>
  <!-- movie user review -->
      <div class="mv-user-review-item" >
        <span v-if="oneLineComments.length === 0">
          작성된 한줄평이 없습니다.
        </span>
        <span v-else>
          <ul>
            <one-line-comment v-for="(oneLineComment, index) in oneLineComments" :key="index" :oneLineComment="oneLineComment"></one-line-comment>
          </ul>
        </span>
      </div>
     <one-line-form @pass-one-line="getOneLine"></one-line-form>
  </div>




      <div class="col-md-4 col-xs-12 col-sm-12">
        <div class="ads">
        <div class="sb-it">
          <h6>Now in Netflix</h6>
          <img src="../../assets/Netflix-new-icon.png" alt="" style="width: 50%;">
        </div>
        </div>
        <div class="sb-it">
          <h6>Director: </h6>
          <p><a href="#">Joss Whedon</a></p>
        </div>
        <div class="sb-it">
          <h6>Writer: </h6>
          <p><a href="#">Joss Whedon,</a> <a href="#">Stan Lee</a></p>
        </div>
        <div class="sb-it">
          <h6>Stars: </h6>
          <p><a href="#">Robert Downey Jr,</a> <a href="#">Chris Evans,</a> <a href="#">Mark Ruffalo,</a><a href="#"> Scarlett Johansson</a></p>
        </div>
        <div class="sb-it">
          <h6>Genres:</h6>
          <p><a href="#">Action, </a> <a href="#"> Sci-Fi,</a> <a href="#">Adventure</a></p>
        </div>
        <div class="sb-it">
          <h6>Release Date:</h6>
          <p>{{ movie.release_date }}</p>
          <!-- <p>May 1, 2015 (U.S.A)</p> -->
        </div>
        <div class="sb-it">
          <h6>Run Time:</h6>
          <p>{{ movie.runtime }} min</p>
        </div>
        <div class="sb-it">
          <h6>MMPA Rating:</h6>
          <p>PG-13</p>
        </div>
        <!-- <div class="sb-it">
          <h6>Plot Keywords:</h6>
          <p class="tags">
            <span class="time"><a href="#">superhero</a></span>
      <span class="time"><a href="#">marvel universe</a></span>
      <span class="time"><a href="#">comic</a></span>
      <span class="time"><a href="#">blockbuster</a></span>
      <span class="time"><a href="#">final battle</a></span>
          </p>
        </div> -->
      
      </div>
    </div>
				
</template>

<script>
import OneLineComment from './OneLineComment.vue'
import OneLineForm from './OneLineForm.vue'

export default {
  name: 'MovieOverview',
  components: {
    OneLineComment,
    OneLineForm

  },
  props: {
    movie: Object
  },
  data () {
    return {      
      like: 0,
      dislike: 0,
      oneLineComments: [],
    }
  },
  methods: {
    addLike () {
      this.like += 1
    },
    addDislike () {
      this.dislike += 1
    },
    getOneLine (data) {
      this.oneLineComments.push(data)
    }
  },
  computed: {
    percentage () {
      return Math.round((this.like / (this.like + this.dislike)) * 100)
    }
  },  
}
</script>

<style scoped>

</style>