<template>
  <!--signup form popup-->
<div class="login-wrapper"  id="signup-content">
    <div class="login-content">
        <a href="#" class="close">x</a>
        <h3>sign up</h3>
        <form method="post" action="#">
            <div class="row">
                 <label for="username-2">
                    Username:
                    <input v-model="credentials.username" type="text" name="username" id="username-2" placeholder="" pattern="^[a-zA-Z][a-zA-Z0-9-_\.]{8,20}$" required="required" />
                </label>
            </div>
           
            <div class="row">
                <label for="email-2">
                    your Nickname:
                    <input v-model="credentials.nickname" type="text" name="nickname" id="nickname-2" placeholder="" pattern="(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$" required="required" />
                </label>
            </div>
             <div class="row">
                <label for="password-2">
                    Password:
                    <input v-model="credentials.password" type="password" name="password" id="password-2" placeholder="" pattern="(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$" required="required" />
                </label>
            </div>
             <div class="row">
                <label for="repassword-2">
                    re-type Password:
                    <input @keyup.enter="signup" v-model="credentials.passwordConfirmation" type="password" name="password" id="repassword-2" placeholder="" pattern="(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$" required="required" />
                </label>
            </div>
           <div class="row">
             <button @click="signup" type="submit">sign up</button>
           </div>
        </form>
    </div>
</div>
<!--end of signup form popup-->
</template>

<script>
import axios from 'axios'
export default {
  name: 'SignupForm',
  data () {
    return {
      credentials: {
        username: null,
        nickname: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/api/v1/accounts/signup/',
        data: this.credentials
      })
        .then(() => {
          // console.log(res)
          this.$router.go()
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