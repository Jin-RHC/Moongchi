<template>
    <!-- <h3>Best Marvel movie in my opinion</h3> -->
    <li id="comment-box" style="">  

      <div style="display: flex; justify-content: space-between;">        
        <p class="time">          
          <a @click.prevent="$router.push({ name: 'UserProfile', params: {username: oneLineComment.user.username }})" href="#" style="margin: 0 5px"> 
            {{ oneLineComment.user.nickname }} 
          </a> 
          | 
          <span style="margin: 0 5px;"> 
            {{ createdAt }} 
          </span> 
          | 
          <a id="delete-btn" @click.prevent="deleteOneLineComment" href="" class="time">X</a>
          |
          <a @click.prevent="report" href="#" style="margin: 0 5px;" v-if="isLogin">
            신고
          </a>
        </p>

      </div>
        <star-rating :max-rating=10	:rating="oneLineComment.rating" :star-size="15" :read-only="true"></star-rating>

      <div style="width: 100%">
        
        <p style="white-space: pre-line;">{{ oneLineComment.content }}</p>
        <div style="display: flex; justify-content: end;">
        <div>

          <a @click.prevent="likeOneLineComment" href="" class="time" style="border: solid; border-width: thin; border-radius: 2px; margin-right: 5px;"><font-awesome-icon :icon="['far', 'thumbs-up']" size="1x" style="margin-left: 7px; margin-right: 7px;" />
            <strong style="margin-right: 7px; font-family: tahoma; color: #777;">{{ oneLineComment.like_users.length }}</strong> 
          </a>
          <a @click.prevent="dislikeOneLineComment" href="" class="time" style="font-weight: bolder; border: solid; border-width: thin; border-radius: 2px;"><font-awesome-icon :icon="['far', 'thumbs-down']" size="1x" style=" margin-right: 7px; margin-left: 7px;" />
            <strong style="margin-right: 7px; font-family: tahoma; color: #777;">{{ oneLineComment.dlike_users.length }}</strong> 
          </a>
        </div>
        </div>
      <hr>
      <br>
      </div>
    </li>    
</template>

<script>
import axios from 'axios'
import StarRating from 'vue-star-rating';
const API = process.env.VUE_APP_BACKEND_URL

export default {
  name: 'OneLineComment',
  components: {
    StarRating

  },
  props: {
    oneLineComment: Object,
    movie: Object,
    isLogin: Boolean
  },
  data () {
    return {
      oneLineCommentLike: this.oneLineComment.like_users,
      oneLineCommentDislike: this.oneLineComment.dlike_users,
      
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
    likeOneLineComment () {
      axios({
          method: 'post',
          url: `${API}/api/v1/community/${this.$route.params.id}/rating/${this.oneLineComment.id}/like/`,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            this.$emit('get-one-line-comment-like')
          })
          .catch(err => {
            console.log(err)
            alert('로그인이 필요합니다.')
          })
    },
    dislikeOneLineComment () {
      axios({
          method: 'post',
          url: `${API}/api/v1/community/${this.$route.params.id}/rating/${this.oneLineComment.id}/dlike/`,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            this.$emit('get-one-line-comment-dislike')
          })
          .catch(err => {
            console.log(err)
            alert('로그인이 필요합니다.')
          })
    },
    report () {
      axios({
          method: 'post',
          url: `${API}/api/v1/reports/rating/${this.oneLineComment.id}/`,
          headers: this.setToken()
        })
          .then(() => {
            alert('신고가 접수되었습니다.')
          })
          .catch(() => {
            alert('이미 접수한 신고입니다.')
          })
    },
    deleteOneLineComment () {
      axios({
        method: 'delete',
        url: `${API}/api/v1/community/${this.movie.id}/rating/${this.oneLineComment.id}/`,
        headers: this.setToken()
      })
        .then(res => {          
          console.log(res, '데이터 전송 성공')
          this.$emit('get-one-line-comment-delete')
        })
        .catch(err => {
          alert('삭제할 권한이 없습니다.')
          console.log(err)
        })
    },   
  },
  
  
  computed: {
    createdAt () {
      return this.oneLineComment.created_at.slice(0, 10) + '   ' + this.oneLineComment.created_at.slice(11, 19)
    },
  },
}
</script>

<style scoped>
  #delete-btn {
    border: 0px solid; 
    padding: 0.1em;
    /* background-color: lightgrey;       */
    text-align: center;    
  }
</style>