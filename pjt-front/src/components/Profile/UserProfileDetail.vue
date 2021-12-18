<template>
  <div class="form-style-1 user-pro" action="#">
    <!-- <form action="#" class="user"> -->
      <div class="card-body">
          <div class="row">
            <div class="col-sm-3">
              <h6 class="mb-0">Full Name</h6>
            </div>
            <div class="col-sm-9 text-secondary">
              김싸피
            </div>
          </div>
          <hr>
          <div class="row">
            <div class="col-sm-3" >
              <h6 class="mb-0"><span @click="openFollowings">Followings</span></h6>
            </div>
            <div class="col-sm-9 text-secondary">
              <a @click.prevent="openFollowings" href="">{{ followingsCount }}</a>
            </div>
          </div>
          <hr>
          <div class="row">
            <div class="col-sm-3">
              <h6 class="mb-0"><span @click.prevent="openFollowers">Followers</span></h6>
            </div>
            <div class="col-sm-9 text-secondary">
              <a @click.prevent="openFollowers" href="">{{ followersCount }}</a>
            </div>
          </div>
          <hr>
          <div class="row">
            <div class="col-sm-3">
              <h6 class="mb-0">Email</h6>
            </div>
            <div class="col-sm-9 text-secondary">
              {{ userName }}@ssafy.edu
            </div>
          </div>
          <hr>
          <div class="row">
            <div class="col-sm-3">
              <h6 class="mb-0">Phone</h6>
            </div>
            <div class="col-sm-9 text-secondary">
              (239) 816-9029
            </div>
          </div>
          <hr>
          <div class="row">
            <div class="col-sm-3">
              <h6 class="mb-0">Nickname</h6>
            </div>
            <div class="col-sm-9 text-secondary">
              {{ userNickname }}
            </div>
          </div>
          <hr>
          <div class="row">
            <div class="col-sm-3">
              <h6 class="mb-0">Address</h6>
            </div>
            <div class="col-sm-9 text-secondary">
              당신의 마음 속, 역삼 멀티캠퍼스.
            </div>
          </div>
          <hr>
  
        </div>
      <!-- <h4 style="font-size: 30px;">Profile details</h4>
      <div class="row">
        <div class="col-md-6 form-it">
          <label>Username : <span style="font-size: 20px;">edwardkennedy</span></label>
          
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
      </div>	 -->
    <!-- </form> -->
    <!-- <form action="#" class="password">
      <h4>02. Change password</h4>
      <div class="row">
        <div class="col-md-6 form-it">
          <label>Old Password</label>
          <input type="text" placeholder="**********">
        </div>
      </div>
      <div class="row">
        <div class="col-md-6 form-it">
          <label>New Password</label>
          <input type="text" placeholder="***************">
        </div>
      </div>
      <div class="row">
        <div class="col-md-6 form-it">
          <label>Confirm New Password</label>
          <input type="text" placeholder="*************** ">
        </div>
      </div>
      <div class="row">
        <div class="col-md-2">
          <input class="submit" type="submit" value="change">
        </div>
      </div>	
    </form> -->
  </div>
</template>

<script>
import UserFollowingList from './UserFollowingList.vue'
import UserFollowerList from './UserFollowerList.vue'

export default {
  name: 'UserProfileDetail',
  props: {
    userData: Object
  },
  methods: {
    openFollowings () {
      this.$modal.show(
        UserFollowingList,  
      { text: 'This text is passed as a property' },
      { name: 'UserFollowingList',
        // adaptive: true,
        scrollable: true,
        width: '400',
        height: 'auto',
        focusTrap: true,  
        },
      )
    },
    openFollowers () {
      this.$modal.show(
        UserFollowerList,  
      { text: 'This text is passed as a property' },
      { name: 'UserFollowingList',
        // adaptive: true,
        scrollable: true,
        width: '400',
        height: 'auto',
        focusTrap: true,  
        },
      )
    },
  },
  computed: {
		followersCount () {
      if (this.userData) {
        return this.userData.followers.length
      } else {
        return 0
      }
		},
		followingsCount () {
      if (this.userData) {
        return this.userData.followings.length        
      } else {
        return 0
      }
		},
    userName () {
      if (this.userData) {
        return this.userData.username
      } else {
        return ''
      }
    },
    userNickname () {
      if (this.userData) {
        return this.userData.nickname
      } else {
        return ''
      }
    }
	}
}
</script>

<style scoped>
body{
    margin-top:20px;
    color: #1a202c;
    text-align: left;
    background-color: #e2e8f0;    
}
.main-body {
    padding: 15px;
}
.card {
    box-shadow: 0 1px 3px 0 rgba(0,0,0,.1), 0 1px 2px 0 rgba(0,0,0,.06);
}

.card {
    position: relative;
    display: flex;
    flex-direction: column;
    min-width: 0;
    word-wrap: break-word;
    background-color: #fff;
    background-clip: border-box;
    border: 0 solid rgba(0,0,0,.125);
    border-radius: .25rem;
}

.card-body {
    flex: 1 1 auto;
    min-height: 1px;
    padding: 1rem;
}

.gutters-sm {
    margin-right: -8px;
    margin-left: -8px;
}

.gutters-sm>.col, .gutters-sm>[class*=col-] {
    padding-right: 8px;
    padding-left: 8px;
}
.mb-3, .my-3 {
    margin-bottom: 1rem!important;
}

.bg-gray-300 {
    background-color: #e2e8f0;
}
.h-100 {
    height: 100%!important;
}
.shadow-none {
    box-shadow: none!important;
}
</style>