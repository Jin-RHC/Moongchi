<template>
  <div>
    
  <div style="display: flex; margin-top: 50px; justify-content: end;">
    
    <div style="margin-right: 50px;">
      <h6><a @click.prevent="" href="">{{ nestedComment.user }}</a></h6>
    </div>
    
    <p style="white-space: pre-line; width: 600px;">{{ nestedComment.content }}</p>
    <div style="margin-right: ">
      <span style="" class="time">{{ nestedComment.created_at.slice(0,10) }} {{nestedComment.created_at.slice(11, 19) }}</span>
      <div style="margin-top: 20px; margin-right: 50px;">
          <a @click.prevent="likeNestedComment" href="" class="time" style="border: solid; border-width: thin; border-radius: 2px; margin-right: 5px;"><font-awesome-icon :icon="['far', 'thumbs-up']" size="1x" style="margin-left: 7px; margin-right: 7px;" />
            <strong style="margin-right: 7px; font-family: tahoma; color: #777;">{{ nestedComment.like_users.length }}</strong> 
          </a>
          <a @click.prevent="dislikeNestedComment" href="" class="time" style="font-weight: bolder; border: solid; border-width: thin; border-radius: 2px;"><font-awesome-icon :icon="['far', 'thumbs-down']" size="1x" style=" margin-right: 7px; margin-left: 7px;" />
            <strong style="margin-right: 7px; font-family: tahoma; color: #777;">{{ nestedComment.dlike_users.length }}</strong> 
          </a>          
        </div>
      </div>            
    </div>
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
          this.$emit('noti-nested-comment-like')
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
          this.$emit('noti-nested-comment-dislike')
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style>

</style>