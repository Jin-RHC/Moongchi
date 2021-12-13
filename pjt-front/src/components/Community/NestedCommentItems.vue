<template>
  
  <div style="">

    <div style="display: flex; justify-content: space-between; margin-top: 10px;">    
      <span style="">└</span>
      <div style="width: 100px;">
        <a @click.prevent="$router.push({name: 'UserProfile', params: { username: nestedComment.user.username }})" href=""><h6>{{ nestedComment.user.username }}</h6></a>
      </div>      
      <div style="margin: 0px 5px; word-break:break-all;">
        <p style="white-space: pre-line; width: 550px;">{{ nestedComment.content }}</p>
      </div>

      <div style="">
        <span style="" class="time">{{ nestedComment.created_at.slice(0,10) }} {{nestedComment.created_at.slice(11, 19) }}</span>
        <a @click.prevent="deleteNestedComment" href="" class="time" style="border: thin solid; margin-left: 2px;">X</a>
        <div style="display: flex; justify-content: end; margin: 5px 0px;">
          <a @click.prevent="reportNestedComment" href=""><h6 class="time" style="margin-top: 5px; margin-right: 5px;">신고</h6></a>

          <a @click.prevent="likeNestedComment" href="" class="time" style="border: solid; border-width: thin; border-radius: 2px; margin-right: 5px;"><font-awesome-icon :icon="['far', 'thumbs-up']" size="1x" style="margin-left: 7px; margin-right: 7px;" />
            <strong style="margin-right: 7px; font-family: tahoma; color: #777;">{{ nestedComment.like_users.length }}</strong> 
          </a>
          <a @click.prevent="dislikeNestedComment" href="" class="time" style="font-weight: bolder; border: solid; border-width: thin; border-radius: 2px;"><font-awesome-icon :icon="['far', 'thumbs-down']" size="1x" style=" margin-right: 7px; margin-left: 7px;" />
            <strong style="margin-right: 7px; font-family: tahoma; color: #777;">{{ nestedComment.dlike_users.length }}</strong> 
          </a>          
        </div>
      </div>          
    </div>
    <!-- <div style="margin: 0px 5px;">
      <p style="white-space: pre-line; width: 550px;">{{ nestedComment.content }}</p>
    </div> -->
  </div>
  
  
</template>

<script>
import axios from 'axios'
const api = 'http://127.0.0.1:8000/api/v1/community/'

export default {
  name: 'NestedCommentItems',
  props: {
    nestedComment: Object,
    commentId: Number
  },
  data () {
    return {

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

    likeNestedComment () {
      axios({
        method: 'post',
        url: api + `${this.commentId}/nestedcomment/${this.nestedComment.id}/like/`,
        headers: this.setToken() // Authorization: JWT tokensdjiadnoiqwnd
      })
        .then(res => {
          console.log(res)          
          this.$emit('noti-comment')
        })
        .catch(err => {
          console.log(err)
        })
    },
    dislikeNestedComment () {
      axios({
        method: 'post',
        url: api + `${this.commentId}/nestedcomment/${this.nestedComment.id}/dlike/`,
        headers: this.setToken() // Authorization: JWT tokensdjiadnoiqwnd
      })
        .then(res => {
          console.log(res)
          this.$emit('noti-comment')
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteNestedComment () {
      axios({
        method: 'delete',
        url: api + `${this.commentId}/nestedcomment/${this.nestedComment.id}/`,
        headers: this.setToken() // Authorization: JWT tokensdjiadnoiqwnd
      })
        .then(res => {
          console.log(res)
          this.$emit('noti-comment')
        })
        .catch(err => {
          console.log(err)
          alert('댓글을 삭제할 권한이 없습니다.')
        })
    },
    reportNestedComment () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/api/v1/reports/nestedcomment/' + `${this.nestedComment.id}/`,        
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
    }
  }
}
</script>

<style>

</style>