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
      <a @click.prevent="addLike" style="" href="" title="좋아요"><font-awesome-icon :icon="['far', 'thumbs-up']" size="2x" color="#DB4455" /><span style="font-size: 2em;">{{like.length}}</span></a>
      <a @click.prevent="addDislike" style="" href="" title="글쎄요"><font-awesome-icon :icon="['far', 'thumbs-down']" size="2x" color="#0679C0"  /><span style="font-size: 2em;">{{dislike.length}}</span></a>
    </div>
    <div class="charts__chart chart--p100 chart--blue chart--sm" style="position: relative;">
      <div :class="`charts__chart chart--p${percentage} chart--red`">      
    <div v-if="!(like || dislike)" class="charts__chart chart--p100 chart--gray chart--sm" style="position: absolute; top: -5px"></div>
      </div>
    </div>
  
 </div>
  
  
  <div class="title-hd-sm" style="margin-top: 100px;">
    <h3 style="font-family: sans-serif;">한줄평 </h3>
    <span href="#" class="time">총 <span>{{ commentsData.length }}</span> 건 <i class="ion-ios-arrow-right"></i></span>
  </div>
  <!-- movie user review -->
      <div class="mv-user-review-item" >
        <span v-if="oneLineComments.length === 0">
          작성된 한줄평이 없습니다.
        </span>
        <span v-else>
          <ul>
            <one-line-comment 
              v-for="(oneLineComment, index) in oneLineComments" 
              :key="index" 
              :oneLineComment="oneLineComment" 
              :movie="movie"
              @get-one-line-comment-like="getData"
              @get-one-line-comment-dislike="getData"
              @get-one-line-comment-delete="getData"
              :is-login="isLogin"
            ></one-line-comment>
          </ul>
        </span>
        <a id="moreBtn" v-show="moreItems" @click.prevent="getMoreComments" href=""><button>더보기</button></a>
      </div>
     <one-line-form @noti-one-line-comment="getData" v-show="(isLogin) && (!writer)"></one-line-form>
  </div>




      <div class="col-md-4 col-xs-12 col-sm-12">
        <div class="ads">
        <div class="sb-it" v-show="movie.is_netflix">
          <h6>Now in Netflix</h6>
          <img src="../../assets/Netflix-new-icon.png" alt="" style="width: 50%;">
        </div>
        </div>
        <!-- <div class="sb-it">
          <h6>Director: </h6>
          <p><a href="#">Joss Whedon</a></p>
        </div>
        <div class="sb-it">
          <h6>Writer: </h6>
          <p><a href="#">Joss Whedon,</a> <a href="#">Stan Lee</a></p>
        </div> -->
        <div class="sb-it">
          <h6>Stars: </h6>
          <p>
            <a @click.prevent="" href="" v-for="actor in movieActors" :key="actor.id">{{ actor.name }}, </a> 
          </p>
        </div>
        <div class="sb-it">
          <h6>Genres:</h6>
          <p> 
            <a @click.prevent="" href="" v-for="genre in movieGenres" :key="genre.id">{{ genre.name }} | </a>
          </p>
        </div>
        <div class="sb-it">
          <h6>Release Date:</h6>
          <p>{{ movie.release_date }}</p>
          <!-- <p>May 1, 2015 (U.S.A)</p> -->
        </div>
        <div class="sb-it">
          <h6> Country:</h6>
          <p>{{ movie.country}}</p>
        </div>
        <div class="sb-it">
          <!-- <h6>Run Time:</h6> -->
          <!-- <p>{{ movie.runtime }} min</p> -->
        </div>
        <div class="sb-it">
          <h6>Popularity:</h6>
          <p>{{ movie.popularity }}</p>
        </div>

      
      </div>
    </div>
				
</template>

<script>
import axios from 'axios'
import jwt_decode from "jwt-decode"
import OneLineComment from './OneLineComment.vue'
import OneLineForm from './OneLineForm.vue'
const API = process.env.VUE_APP_BACKEND_URL

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
      isLogin: false,
      writer: false,
      like: this.movie.like_users,
      dislike: this.movie.dlike_users,
      oneLineComments: [],
      movieGenres: this.movie.genres,
      movieActors: this.movie.actors,
      commentsData: this.movie.rating_set.reverse(),
      page: 1,
      moreItems: false
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

    addLike () {
      axios({
        method: 'post',
        url: `${API}/api/v1/community/${this.$route.params.id}/like/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res, '데이터 전송 성공')
          this.getData()
        })
        .catch(err => {
          alert('로그인이 필요합니다.')
          console.log(err)
        })
    },
    addDislike () {
      axios({
        method: 'post',
        url: `${API}/api/v1/community/${this.$route.params.id}/dlike/`,
        headers: this.setToken()
      })
        .then(res => {          
          console.log(res, '데이터 전송 성공')
          this.getData()
        })
        .catch(err => {
          alert('로그인이 필요합니다.')
          console.log(err)
        })
    },    
    getData () {
      // this.$emit('noti-one-line-comment')
			axios({
			method: 'get',
			url: `${API}/api/v1/movies/movie/${this.$route.params.id}/`
		})
			.then(res => {
				this.like = res.data.like_users
        this.dislike = res.data.dlike_users
        this.oneLineComments = res.data.rating_set.reverse().slice(0, 3 * this.page)
				console.log(this.oneLineComments, '데이터 갱신 완료!')
        this.checkWriter()
			})
		},
    getMoreComments () {
      this.page += 1
      this.getData()
      console.log(this.oneLineComments)

    },
    checkWriter () {
      const token = this.$store.state.token
      const decoded = jwt_decode(token)
      const name = this.oneLineComments.find(comment => decoded.username === comment.user.username)
      console.log(name)
      if (name) {
        this.writer = true
      } else {
        this.writer = false
      }
      if (this.oneLineComments.length < this.commentsData.length) {
        this.moreItems = true
      } else {
        this.moreItems = false
      }
    }    
  },
  computed: {

    percentage () {
      return Math.round((this.like.length / (this.like.length + this.dislike.length)) * 100)
    },

    genresList () {
      const data = []
      const genreData = {
        12: '모험',
        14: '판타지',
        16: '애니메이션',
        18: '드라마',
        27: '공포',
        28: '액션',
        35: '코미디',
        36: '역사',
        37: '서부',
        53: '스릴러',
        80: '범죄',
        99: '다큐멘터리',
        878: 'SF',
        9648: '미스터리',
        10402: '음악',
        10749: '로맨스',
        10751: '가족',
        10752: '전쟁',
        10770: 'TV 영화'
      }
      this.movieGenres.forEach(movieGenre => {
        data.push(genreData[movieGenre])
      })
      return data
    },

  },
  created () {
    this.oneLineComments = this.commentsData.slice(0, 3)
    this.checkWriter()
    if (this.$store.state.token) {
      this.isLogin = true
    }
  },
}
</script>

<style scoped>
  #moreBtn {
    display: flex; 
    justify-content: center;
    position: relative;
    bottom: 50px;
  }
</style>