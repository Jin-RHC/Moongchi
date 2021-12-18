<template>
  <div class="form-style-1 user-pro" action="#">
    <form action="#" class="user">
      <h4>01. Profile details</h4>
      <div class="row">
        <div class="col-md-6 form-it">
          <label>Username</label>
          <input type="text" placeholder="edwardkennedy">
        </div>
        <div class="col-md-6 form-it">
          <label>Email Address</label>
          <input type="text" placeholder="edward@kennedy.com">
        </div>
      </div>
      <div class="row">
        <div class="col-md-6 form-it">
          <label>First Name</label>
          <input type="text" placeholder="Edward ">
        </div>
        <div class="col-md-6 form-it">
          <label>Last Name</label>
          <input type="text" placeholder="Kennedy">
        </div>
      </div>
      <div class="row">
        <div class="col-md-6 form-it">
          <label>Country</label>
          <select>
            <option value="united">United States</option>
            <option value="saab">Others</option>
          </select>
        </div>
        <div class="col-md-6 form-it">
          <label>State</label>
          <select>
            <option value="united">New York</option>
            <option value="saab">Others</option>
          </select>
        </div>
      </div>
      <div class="row">
        <div class="col-md-2">
          <input class="submit" type="submit" value="save">
        </div>
      </div>	
    </form>
    <form action="#" class="password">
      <h4>비밀번호 변경</h4>
      <div class="row">
        <div class="col-md-6 form-it">
          <label>기존 비밀번호</label>
          <input v-model="oldPassword" type="password" placeholder="**********">
        </div>
      </div>
      <div class="row">
        <div class="col-md-6 form-it">
          <label>새 비밀번호</label>
          <input v-model="newPassword" type="password" placeholder="***************">
        </div>
      </div>
      <div class="row">
        <div class="col-md-6 form-it">
          <label>비밀번호 확인</label>
          <input v-model="newPasswordConfirmation" type="password" placeholder="*************** ">
        </div>
      </div>
      <div class="row">
        <div class="col-md-2">
          <input @click.prevent="changePassword" class="submit" type="submit" value="change">
        </div>
      </div>	
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'
const API = process.env.VUE_APP_BACKEND_URL

export default {
  name: 'UserChangeForm',
  data () {
    return {
      username: null,
      oldPassword: null,
      newPassword: null,
      newPasswordConfirmation: null,
      // passwordChangeCredentials: {
      //   username: null,
      //   oldPassword: null,
      //   newPassword: null,
      //   newPasswordConfirmation: null,
        
      // },
      // signupCredentials: {
      //   username: null,
      //   nickname: null,
      //   password: null,
      //   passwordConfirmation: null,
      // },
      // loginChecked: true,
      // signupChecked: false,
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
    changePassword: function () {
      if (this.newPassword != this.newPasswordConfirmation) {
        alert('비밀번호와 비밀번호 확인에 같은 비밀번호를 입력하셨는지 확인해 주세요.')
      } else if (!this.newPassword) {
        alert('값을 입력했는지 확인해 주세요.')
      } else {
      axios({
        method: 'post',
        url: `${API}/api/token/`,
        data: {username: jwt_decode(localStorage.getItem('jwt')).username,
          password: this.oldPassword}
      })
        .then(res => {
          localStorage.setItem('jwt', res.data.access)
					this.$store.dispatch('loginCompleted', res) 
					// this.$router.go()
        })
        .then(() => {
          axios({
            method: 'post',
            url: `${API}/api/v1/accounts/changepassword/`,
            headers: this.setToken(),
            data: {newPassword: this.newPassword,
              newPasswordConfirmation: this.newPasswordConfirmation}
          })
            .then(() => {
              alert('비밀번호가 성공적으로 변경되었습니다.')
            })
            .catch(() =>{
              alert('비밀번호는 최소 8자 이상입니다. 잘 작성하셨는지 확인해 주세요.')
            })
        })
        .catch(err => {
					alert(err)
        })
        
        }
    },
  },
}
</script>

<style>

</style>