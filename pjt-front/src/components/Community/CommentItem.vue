<template>
  <div style="display: flex;">
    <div style="margin-right: 50px; width: 0px;">
      <h6><a @click.prevent="" href="">{{ comment.user }} </a></h6>
    </div>
    <p style="white-space: pre-line; width: 650px;">{{ comment.content }}</p>
    <div style="margin-right: ">
      <span style="" class="time">{{ comment.created_at.slice(0, 10) + '   ' + comment.created_at.slice(11, 19)}}</span>
      <div style=";">
        <a @click.prevent="likeComment" href="" class="time" style="border: solid; border-width: thin; border-radius: 2px; margin-right: 5px;"><font-awesome-icon :icon="['far', 'thumbs-up']" size="1x" style="margin-left: 7px; margin-right: 7px;" />
          <strong style="margin-right: 7px; font-family: tahoma; color: #777;">{{ comment.like_users.length }}</strong> 
        </a>
        <a @click.prevent="dislikeComment" href="" class="time" style="font-weight: bolder; border: solid; border-width: thin; border-radius: 2px;"><font-awesome-icon :icon="['far', 'thumbs-down']" size="1x" style=" margin-right: 7px; margin-left: 7px;" />
          <strong style="margin-right: 7px; font-family: tahoma; color: #777;">{{ comment.dlike_users.length }}</strong> 
        </a>
      </div>
    </div>
  </div>  
</template>

<script>
import axios from 'axios'

const api = 'http://127.0.0.1:8000/api/v1/community/'
export default {
  name: 'CommentItem',
  props: {
    comment: Object
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
          this.$emit('noti-like-comment')
        })
        .catch(err => {
          console.log(err)
        })
    },
    dislikeComment () {
      axios({
        method: 'post',
        url: api + `${this.$route.params.reviewId}/comment/${this.comment.id}/dislike/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.$emit('noti-dislike-comment')
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