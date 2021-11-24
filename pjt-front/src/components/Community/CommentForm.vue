<template>
  <div class="comment-form">
    <h4>Leave a comment</h4>
    <form action="#">
      <div class="row">
        <!-- <div class="col-md-4">
          <input v-model.trim="author" type="text" placeholder="Your name">
        </div> -->


        <!-- <div class="col-md-4">
          <input type="text" placeholder="Your email">
        </div> -->
        <!-- <div class="col-md-4">
          <input type="text" placeholder="Website">
        </div> -->
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
export default {
  name: 'CommentForm',
  data () {
    return {
      message: null,
    }
  },
  methods: {
    leaveComment () {
      if (this.message) {
        this.$emit('get-message', {message: this.message})
        this.message = null
      }

    }
  }
}
</script>

<style>

</style>