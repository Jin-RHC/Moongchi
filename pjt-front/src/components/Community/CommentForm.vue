<template>
  <div class="comment-form">
    <h4>Leave a comment</h4>
    <form action="#">
      <div class="row"> 
      </div>
      <div class="row">
        <div class="col-md-12">
          <textarea v-model.trim="message" name="message" id="" placeholder="주제와 무관한 댓글, 악플은 삭제될 수 있습니다."></textarea>
        </div>
      </div>
      <div style="display: flex; justify-content: end;">
        <input @click.prevent="leaveComment" class="submit" type="submit" placeholder="submit" value="등록">
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const api = 'http://127.0.0.1:8000/api/v1/community/'
export default {
  name: 'CommentForm',
  data () {
    return {
      message: null,
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
    leaveComment () {
      if (this.message) {
        const comment = {
          content: this.message
        }
        axios({
          method: 'post',
          url: api + `${this.$route.params.reviewId}/comment/`,
          data: comment,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            this.$emit('noti-comment')
            this.message = null
          })
          .catch(err => {
            console.log(err)
            alert('댓글을 그렇게 길게 작성할 수 없습니다.')
          })
      }

    }
  }
}
</script>

<style>

</style>