<template>
	<div class="login-html">
		<input id="tab-1" type="radio" name="tab" class="sign-in" :checked="loginChecked"><label for="tab-1" class="tab">Log In</label>
		<input id="tab-2" type="radio" name="tab" class="sign-up" :checked="signupChecked"><label for="tab-2" class="tab">Sign Up</label>
		<div class="login-form">
			<div class="sign-in-htm">
				<div class="group">
					<label for="user" class="label">Username</label>
					<input v-model.trim="loginCredentials.username" id="user" type="text" class="input" pattern="^[a-zA-Z][a-zA-Z0-9-_\.]{8,20}$" required="required">
				</div>
				<div class="group">
					<label for="pass" class="label">Password</label>
					<input @keyup.enter="login" v-model.trim="loginCredentials.password" id="pass" type="password" class="input" data-type="password" pattern="(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$" required="required">				</div>
				<div class="group">
					<input id="check" type="checkbox" class="check" checked>
					<label for="check"><span class="icon"></span> Keep me Signed in</label>
				</div>
				<div class="group">
					<input @click="login" type="submit" class="button" value="Log In" style="background-color: #dd003f; font-family: 'Dosis', sans-serif; font-weight: bold;">
				</div>
				<div class="hr"></div>
				<div class="foot-lnk">
					<a href="#forgot">Forgot Password?</a>
				</div>
			</div>
			<div class="sign-up-htm">
				<div class="group">
					<label for="user" class="label">Username</label>
					<input v-model.trim="signupCredentials.username" id="user" type="text" class="input" pattern="^[a-zA-Z][a-zA-Z0-9-_\.]{8,20}$" required="required">
				</div>
				<div class="group">
					<label for="pass" class="label">Password</label>
					<input v-model.trim="signupCredentials.password" id="pass" type="password" class="input" data-type="password" pattern="(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$" required="required">
				</div>
				<div class="group">
					<label for="pass" class="label">Repeat Password</label>
					<input v-model.trim="signupCredentials.passwordConfirmation" id="pass" type="password" class="input" data-type="password" pattern="(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$" required="required">
				</div>
				<div class="group">
					<label for="pass" class="label">Nickname</label>
					<input @keyup.enter="signup" v-model.trim="signupCredentials.nickname" id="pass" type="text" class="input">
				</div>
				<div class="group">
					<input @click="signup" type="submit" class="button" value="Sign Up" style="background-color: #dd003f; font-family: 'Dosis', sans-serif; font-weight: bold;">
				</div>
				<div class="hr"></div>
				<div class="foot-lnk">
					<label for="tab-1">Already Member?</label>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios'
const API = process.env.VUE_APP_BACKEND_URL

export default {
  name: 'LoginForm2',
  data () {
    return {
      loginCredentials: {
        username: null,
        password: null,
      },
      signupCredentials: {
        username: null,
        nickname: null,
        password: null,
        passwordConfirmation: null,
      },
      loginChecked: true,
      signupChecked: false,
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: `${API}/api/token/`,
        data: this.loginCredentials,
      })
        .then(res => {
          console.log(res)
          localStorage.setItem('jwt', res.data.access)
					this.$store.dispatch('loginCompleted', res) 
          this.$router.push({name: 'Home'})					
					this.$router.go()
        })
        .catch(err => {
					alert('존재하지 않는 계정이거나 비밀번호가 틀립니다.')
          console.log(err)
        })
    },
    signup: function () {
      axios({
        method: 'post',
        url: `${API}/api/v1/accounts/signup/`,
        data: this.signupCredentials
      })
        .then(() => {
          // console.log(res)
          // this.$router.go()
					this.signupCredentials.username = null
					this.signupCredentials.nickname = null
					this.signupCredentials.password = null
					this.signupCredentials.passwordConfirmation = null
					alert('회원가입이 완료되었습니다. 다시 로그인해 주세요')
					this.$router.go()
        })
        .catch(err => {
          console.log(err)
					alert('정보를 정확히 입력해주세요.')
        })
    }
  },
}
</script>

<style scoped>
body{
	margin:0;
	color:#6a6f8c;
	background:#c8c8c8;
	font:600 16px/18px 'Open Sans',sans-serif;
}
*,:after,:before{box-sizing:border-box}
.clearfix:after,.clearfix:before{content:'';display:table}
.clearfix:after{clear:both;display:block}
a{color:inherit;text-decoration:none}

.login-wrap{
	width:100%;
	margin:auto;
	max-width:525px;
	min-height:670px;
	position:relative;
	background:url(https://raw.githubusercontent.com/khadkamhn/day-01-login-form/master/img/bg.jpg) no-repeat center;
	box-shadow:0 12px 15px 0 rgba(0,0,0,.24),0 17px 50px 0 rgba(0,0,0,.19);
}
.login-html{
	width:100%;
	height:100%;
	position:absolute;
	padding:90px 70px 50px 70px;
	background:rgba(40,57,101,.9);
}
.login-html .sign-in-htm,
.login-html .sign-up-htm{
	top:0;
	left:0;
	right:0;
	bottom:0;
	position:absolute;
	transform:rotateY(180deg);
	backface-visibility:hidden;
	transition:all .4s linear;
}
.login-html .sign-in,
.login-html .sign-up,
.login-form .group .check{
	display:none;
}
.login-html .tab,
.login-form .group .label,
.login-form .group .button{
	text-transform:uppercase;
}
.login-html .tab{
	font-size:22px;
	margin-right:15px;
	padding-bottom:5px;
	margin:0 15px 10px 0;
	display:inline-block;
	border-bottom:2px solid transparent;
}
.login-html .sign-in:checked + .tab,
.login-html .sign-up:checked + .tab{
	color:#fff;
	border-color:#1161ee;
}
.login-form{
	min-height:345px;
	position:relative;
	perspective:1000px;
	transform-style:preserve-3d;
}
.login-form .group{
	margin-bottom:15px;
}
.login-form .group .label,
.login-form .group .input,
.login-form .group .button{
	width:100%;
	color:#fff;
	display:block;
}
.login-form .group .input,
.login-form .group .button{
	border:none;
	padding:15px 20px;
	border-radius:25px;
	background:rgba(255,255,255,.1);
}
.login-form .group input[data-type="password"]{
	text-security:circle;
	-webkit-text-security:circle;
}
.login-form .group .label{
	color:#aaa;
	font-size:12px;
}
.login-form .group .button{
	background:#1161ee;
}
.login-form .group label .icon{
	width:15px;
	height:15px;
	border-radius:2px;
	position:relative;
	display:inline-block;
	background:rgba(255,255,255,.1);
}
.login-form .group label .icon:before,
.login-form .group label .icon:after{
	content:'';
	width:10px;
	height:2px;
	background:#fff;
	position:absolute;
	transition:all .2s ease-in-out 0s;
}
.login-form .group label .icon:before{
	left:3px;
	width:5px;
	bottom:6px;
	transform:scale(0) rotate(0);
}
.login-form .group label .icon:after{
	top:6px;
	right:0;
	transform:scale(0) rotate(0);
}
.login-form .group .check:checked + label{
	color:#fff;
}
.login-form .group .check:checked + label .icon{
	background:#1161ee;
}
.login-form .group .check:checked + label .icon:before{
	transform:scale(1) rotate(45deg);
}
.login-form .group .check:checked + label .icon:after{
	transform:scale(1) rotate(-45deg);
}
.login-html .sign-in:checked + .tab + .sign-up + .tab + .login-form .sign-in-htm{
	transform:rotate(0);
}
.login-html .sign-up:checked + .tab + .login-form .sign-up-htm{
	transform:rotate(0);
}

.hr{
	height:2px;
	margin:60px 0 50px 0;
	background:rgba(255,255,255,.2);
}
.foot-lnk{
	text-align:center;
}

</style>