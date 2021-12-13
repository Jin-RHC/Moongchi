<template>
<div>

  <div style="display: flex; justify-content: space-between; margin-top: 30px;">
    
    <div style="width: 100px;">
      <a @click.prevent="$router.push({ name: 'UserProfile', params: { username: comment.user.username }})" href=""><h6>{{ comment.user.username }}</h6></a>             
    </div>
    <div style="margin: 0px 5px;">
      <p style="white-space: pre-line; word-break:break-all; width: 600px; padding: 0px">{{ comment.content }}</p>
    </div>
    <div style="">
      <span style="height: 21px;" class="time">
        {{ comment.created_at.slice(0, 10) + '   ' + comment.created_at.slice(11, 19)}}
      </span>
      <a @click.prevent="deleteComment" href="" class="time" style="border: thin solid;">X</a>
      <div style="display: flex; justify-content: end; margin: 5px 0px;">
        <a @click.prevent="reportComment" href=""><h6 class="time" style="margin-top: 5px; margin-right: 5px;">신고</h6></a>
        <a @click.prevent="likeComment" href="" class="time" style="border: solid; border-width: thin; border-radius: 2px; margin-right: 5px;"><font-awesome-icon :icon="['far', 'thumbs-up']" size="1x" style="margin-left: 7px; margin-right: 7px;" />
          <strong style="margin-right: 7px; font-family: tahoma; color: #777;">{{ commentLike }}</strong> 
        </a>
        <a @click.prevent="dislikeComment" href="" class="time" style="font-weight: bolder; border: solid; border-width: thin; border-radius: 2px;"><font-awesome-icon :icon="['far', 'thumbs-down']" size="1x" style=" margin-right: 7px; margin-left: 7px;" />
          <strong style="margin-right: 7px; font-family: tahoma; color: #777;">{{ commentDislike }}</strong> 
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

const api = 'http://127.0.0.1:8000/api/v1/community/'
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
        url: api + `${this.$route.params.reviewId}/comment/${this.comment.id}/like/`,
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
        url: api + `${this.$route.params.reviewId}/comment/${this.comment.id}/dlike/`,
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
        url: api + `${this.$route.params.reviewId}/comment/${this.comment.id}/`,
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
        url: api + `${this.comment.id}/nestedcomment/`,
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
        url: 'http://127.0.0.1:8000/api/v1/reports/comment/' + `${this.comment.id}/`,        
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

<style>

</style>