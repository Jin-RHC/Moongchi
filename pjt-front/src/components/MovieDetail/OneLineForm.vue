<template>       
  <div class="comment-box ml-2">
    <hr>
    <h4 style="margin-bottom: 10px;">Add a comment</h4>
    <star-rating :star-size="15" v-model.trim="rating"></star-rating>
    <div class="comment-area"> <textarea @keyup.enter="addOneLineComment" class="form-control" placeholder="한줄평을 작성하세요" rows="4" v-model.trim="oneLineComment"></textarea> </div>
          
    
    <a @click.prevent="addOneLineComment" class="redbtn" style="float: right;" href="">Send</a> 

          
          
  </div>
        


</template>

<script>
import StarRating from 'vue-star-rating';

export default {
  name: 'OneLineForm',
  components: {
    StarRating
  },
  data () {
    return {
      rating: null,
      oneLineComment: null,
    }
  },
  methods: {
    addOneLineComment () {
      if (this.rating && this.oneLineComment) {
        const oneLineCommentData = {
          rating: this.rating,
          content: this.oneLineComment,
          author: 'user' 
        }
        this.$emit('pass-one-line', oneLineCommentData)
        this.rating = null
        this.oneLineComment = null
      }
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@200&display=swap');

html,
body {
    height: 100%
}

body {
    display: grid;
    place-items: center;
    font-family: 'Manrope', sans-serif;
    background: red
}

.card {
    position: relative;
    display: flex;
    flex-direction: column;
    min-width: 0;
    padding: 20px;
    width: 450px;
    word-wrap: break-word;
    background-color: #fff;
    background-clip: border-box;
    border-radius: 6px;
    -moz-box-shadow: 0px 0px 5px 0px rgba(212, 182, 212, 1)
}

.comment-box {
    padding: 5px
}

.comment-area textarea {
    resize: none;
    border: 1px solid #ad9f9f
}

.form-control:focus {
    color: #495057;
    background-color: #fff;
    border-color: #ffffff;
    outline: 0;
    box-shadow: 0 0 0 1px rgb(255, 0, 0) !important
}

.send {
    color: #fff;
    background-color: #ff0000;
    border-color: #ff0000
}

.send:hover {
    color: #fff;
    background-color: #f50202;
    border-color: #f50202
}

.rating {
    display: flex;
    margin-top: -10px;
    flex-direction: row-reverse;
    margin-left: -4px;
    float: left
}

.rating>input {
    display: none
}

.rating>label {
    position: relative;
    width: 19px;
    font-size: 25px;
    color: #ff0000;
    cursor: pointer
}

.rating>label::before {
    content: "\2605";
    position: absolute;
    opacity: 0
}

.rating>label:hover:before,
.rating>label:hover~label:before {
    opacity: 1 !important
}

.rating>input:checked~label:before {
    opacity: 1
}

.rating:hover>input:checked~label:before {
    opacity: 0.4
}

</style>