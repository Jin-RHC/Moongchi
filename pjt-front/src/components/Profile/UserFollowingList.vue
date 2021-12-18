<template>
  <div class="container">
    <h3>Followings</h3>
    <hr>
    <ul>
      <div class="user"
        v-for="(following, index) in followings"
        :key="index"
      >
        <h5><a @click.prevent="goUser(following.username)" href="">{{ following.username }}</a></h5>
        <a v-show="isMyProfile" @click.prevent="follow(following.username)" class="flbtn redbtn" href="">팔로우 취소</a>
      </div>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from "jwt-decode"
const API = process.env.VUE_APP_BACKEND_URL

export default {
  name: 'UserFollowingList',
  data () {
    return {
      followings: null,
      isMyProfile: false,
      isFollowing: true,
    }
  },
  methods: {
    show () {
        this.$modal.show('my-first-modal');
    },
    hide () {
        this.$modal.hide('my-first-modal');
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
			this.myname = jwt_decode(token).username
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getProfile () {
			axios({
				method: 'get',
				url: `${API}/api/v1/accounts/${this.$route.params.username}/`,
				headers: this.setToken()
			})
				.then(res => {
					console.log(res.data)
					this.followings = res.data.followings					
					
				})
				.catch(err => {
					console.log(err)
					alert('로그인하셔야 볼 수 있습니다.')
				})
		},
    goUser (username) {
      this.$modal.hide('UserFollowingList')
      this.$router.push({ name: 'UserProfile', params: { username: username }})
    },
    follow (username) {
			axios({
				method: 'POST',
				url: `${API}/api/v1/accounts/${username}/follow/`,
				headers: this.setToken()
			})
				.then(() => {
					if (this.isFollowing === false) {
						this.isFollowing = true            
					} else {
						this.isFollowing = false
					}
          this.getProfile()
				})
				.catch(err => {
					console.log(err)
					alert('로그인하셔야 볼 수 있습니다.')
				})
		},
    
  },
  created () {
    this.getProfile()
    const token = this.$store.state.token
    const decoded = jwt_decode(token)
    if (decoded.username === this.$route.params.username ) {
      this.isMyProfile = true 
    }
  },
  mount () {
      this.show()
  }
}
</script>

<style scoped>
h3 {
  text-align: center;
  margin: 20px 10px;
}
h5 {
  padding: 10px;
}
.container {
  height: auto;
  width: 400px;
  
}
.user {
  margin: 2em 1.5em;
  display: flex;
  justify-content: space-between;
}
.flbtn {
  background:grey;
}
@media screen and (max-width: 320px) {
  .container {
    width: 100vw;
  }
  .user {
    position: relative;
    left: 2em;
  }
  h3 {
    position: relative;
    left: 1.5em;
  }
}
</style>