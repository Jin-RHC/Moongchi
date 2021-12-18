<template>
  <div>
    <div class="comment-box">
      
      <div class="author-box">
        <a @click.prevent="$router.push({ name: 'UserProfile', params: { username: comment.user.username }})" href=""><h6>{{ comment.user.username }}</h6></a>             
      </div>
      <div class="content-box">
        <p>{{ comment.content }}</p>
      </div>
      <div class="btn-box">
        <div class="date-box">
          <span id="time" class="time">
            {{ comment.created_at.slice(0, 10) + '   ' + comment.created_at.slice(11, 19)}}
          </span>
          <a id="delete-btn" @click.prevent="deleteComment" href="" class="time">X</a>
        </div>
        <div id="like-box">
          <a id="report-btn" @click.prevent="reportComment" href="" v-show="isLogin">
            <h6 class="time">신고</h6>
          </a>
          <a id="comment-like-btn" @click.prevent="likeComment" href="" class="time">
            <font-awesome-icon :icon="['far', 'thumbs-up']" size="1x" style="margin-left: 7px; margin-right: 7px;" />
            <strong>{{ commentLike }}</strong> 
          </a>
          <a id="comment-dlike-btn" @click.prevent="dislikeComment" href="" class="time">
            <font-awesome-icon :icon="['far', 'thumbs-down']" size="1x" style=" margin-right: 7px; margin-left: 7px;" />
            <strong>{{ commentDislike }}</strong> 
          </a>
        </div>
      </div>    
    </div>

      
    <div v-show="comment.nestedcomment_set.length">
      <nested-comment-items
        v-for="nestedComment in comment.nestedcomment_set" 
        :key="nestedComment.id"
        :nestedComment="nestedComment"
        :commentId="comment.id"
        @noti-comment="notiNestedComment" 
        :is-login="isLogin"       
      ></nested-comment-items>
    </div>    
    <a v-show="isLogin" @click.prevent="openCommentForm" href="" style="border: 1px solid #ddd; padding: 0px 7px;">답글</a>
    <form action="#" v-show="isNested">   
      <div class="row">
        <div class="col-md-12">
          <textarea v-model.trim="nestedContent" name="message" id="" placeholder="주제와 무관한 댓글, 악플은 삭제될 수 있습니다."></textarea>
        </div>
      </div>
      <div style="display: flex; justify-content: end;">
        <a @click.prevent="leaveNestedComment" placeholder="submit" href=""><button>등록</button></a>
      </div>
    </form>  
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
import NestedCommentItems from './NestedCommentItems.vue'
const API = process.env.VUE_APP_BACKEND_URL

export default {
  components: { NestedCommentItems },
  name: 'CommentItem',
  props: {
    comment: Object,
    isLogin: Boolean
  },
  data () {
    return {
      isNested: false,
      nestedContent: '',
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
    likeComment () {
      axios({
        method: 'post',
        url: `${API}/api/v1/community/${this.$route.params.reviewId}/comment/${this.comment.id}/like/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.$emit('noti-comment')
        })
        .catch(err => {
          console.log(err)
          alert('로그인이 필요합니다.')
        })
    },
    dislikeComment () {
      axios({
        method: 'post',
        url: `${API}/api/v1/community/${this.$route.params.reviewId}/comment/${this.comment.id}/dlike/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.$emit('noti-comment')
        })
        .catch(err => {
          console.log(err)
          alert('로그인이 필요합니다.')
        })

    },
    deleteComment () {
      axios({
        method: 'delete',
        url: `${API}/api/v1/community/${this.$route.params.reviewId}/comment/${this.comment.id}/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.$emit('noti-comment')
        })
        .catch(err => {
          alert('댓글을 삭제할 권한이 없습니다.')
          console.log(err)
        })
    },
    notiNestedComment () {
      this.$emit('noti-comment')

    },
    openCommentForm () {
      this.isNested = !this.isNested
    },
    leaveNestedComment () {
      
      if (this.nestedContent.length) {
        const nestedContent = {
          content: this.nestedContent
        }
        axios({
        method: 'post',
        url: `${API}/api/v1/community/${this.comment.id}/nestedcomment/`,
        data: nestedContent,
        headers: this.setToken() // Authorization: JWT tokensdjiadnoiqwnd
      })
        .then(res => {
          console.log(res)
          this.nestedContent = ''
          this.$emit('noti-comment') 
        })
        .catch(err => {
          console.log(err)
          alert('답글을 그렇게 길게 작성할 수 없습니다.')
        })
      }
    },
    reportComment () {
      axios({
        method: 'post',
        url: `${API}/api/v1/reports/comment/${this.comment.id}/`,        
        headers: this.setToken() // Authorization: JWT tokensdjiadnoiqwnd
      })
        .then(res => {
          console.log(res)
          alert('신고가 접수되었습니다.')
        })
        .catch(err => {
          console.log(err)
          alert('이미 신고된 댓글입니다.')
        })
    },
    
    
  
  },
  computed: {
    commentLike () {
      return this.comment.like_users.length
    },
    commentDislike () {
      return this.comment.dlike_users.length
    },

  },   
}

</script>

<style scoped>
.comment-box {
  display: flex; 
  justify-content: space-between; 
  margin-top: 30px;
  width: 100%;
}
.author-box {
  width: 15%;
}
.author-box > h6 {
  padding: 0px 10px;
}
.content-box {   
    width: 65%;
}

.content-box > p {
  white-space: pre-line; 
  word-break:break-all;
  width: 100%;    
}
.btn-box {  
  width: 20%;
  margin-left: 1em;
  position: relative;
  left: 4em;
}
.date-box {
  display: flex;
  /* justify-content: end; */
  width: 100%;  
}
.date-box > span {
  width: 70%;
}
.date-box > a {
  
}
#delete-btn {
  border: thin solid; 
  background-color: #F1F3F5;  
  width: 10%;  
  text-align: center;
  margin-left: 1em;
}
#time {
  width: auto;
}
#report-btn > h6{
  margin-top: 5px; 
  margin-right: 5px;
  display: inline;
}

#comment-like-btn {
  border: solid; 
  border-width: thin; 
  border-radius: 2px; 
  margin-right: 5px;
}
#comment-like-btn > strong {
  font-family: tahoma; 
  color: #777;
  padding: 0 0.5em;
}
#comment-dlike-btn > strong {
  font-family: tahoma; 
  color: #777;
  padding: 0 0.5em;
}
#comment-dlike-btn {
  font-weight: bolder; 
  border: solid; 
  border-width: thin; 
  border-radius: 2px;
}
#like-box {
  display: flex;
  /* justify-content: end; */
  margin-top: 1em;
  
}

@media screen and (min-width: 690px) {
  .author-box {
    width: 15%;
  }
  .content-box {   
    width: 60%;
  }  
  .btn-box {  
    width: 25%;
  }
}
@media screen and (min-width: 657px) and (max-width: 690px) {
  .author-box {
    width: 20%;
  }
  .content-box {   
    width: 50%;
  }  
  .btn-box {  
    width: 30%;
  }
}
@media screen and (min-width: 470px) and (max-width: 657px) {
  .author-box {
    width: 20%;
  }
  .content-box {   
    width: 60%;
  }  
  .btn-box {  
    width: 20%;
  }
  .date-box {
    display: flex;
    
  }
  #delete-btn {
    height: 50%;
    width: 20%;
  }
  #time {
    font-size: 0.7em;
  }
  #comment-like-btn {
    text-align: center;
  }
  #comment-dlike-btn {
    text-align: center;
  }
}
@media screen and (min-width: 425px) and (max-width: 470px) {
  .author-box {
    width: 20%;
  }
  .content-box {   
    width: 60%;
  }
  #delete-btn {
    width: 30%;
    height: 60%;
    margin: 0px 0px;
  }
  .btn-box {  
    width: 20%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  #time {
    font-size: 0.6em;
  }

  #like-box {
    display: inline;
  }
  #comment-like-btn {
    display: block;
    width: 70%;
    margin-top: 1rem;
  }
  #comment-dlike-btn {
    display: block;
    width: 70%;
    margin: 1rem 0em;
  }
}
@media screen and (min-width: 375px) and (max-width: 425px) {
  .author-box {
    width: 30%;
  }

  #time {
    font-size: 0.5em;    
    position: relative;
    right: 10px;
  }
  .btn-box {
    display: inline;
  }
  #delete-btn {
    margin: 0px 0px;
    width: 30%;
    height: 50%;
  }
  #comment-like-btn {
   text-align: center; 
  }
  #comment-dlike-btn {
    text-align: center;
  }
}
@media screen and (max-width: 375px) {
  .author-box {
    width: 20%;
  }
  .content-box {
    width: 50%;
  }
  .btn-box {
    width: 30%;
  }
  .date-box {
    width: auto;
  }
  #time {
    font-size: 5px;    
    position: relative;
    right: 1em;
    width: 58px;
  }
  .btn-box {
    display: inline;
    /* margin-left: 1.5em; */
  }
  #delete-btn {  
    position: relative;  
    left: 1em;
    margin: 0px 0px;
    width: 20%;
    height: 50%;
  }
  /* #like-box {
    display: flex;
    flex-direction: column;
    
    width: auto;
  } */
  #comment-like-btn {
   text-align: center; 
  }
  #comment-dlike-btn {
    text-align: center;
  }
  .author-box > a > h6 {
    font-size: 0.9em;
  }
  .content-box > p {
    font-size: 0.8em;
  }
}



</style>