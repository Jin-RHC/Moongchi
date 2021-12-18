<template>
<header class="ht-header">
	<div class="container">
		<nav class="navbar navbar-default navbar-custom">
      <!-- Brand and toggle get grouped for better mobile display -->
				<div class="navbar-header logo">
          <div class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
            <span class="sr-only">Toggle navigation</span>
            <div id="nav-icon1">
            <span></span>
            <span></span>
            <span></span>
          </div>
          </div>
					<a @click.prevent="$router.push({name: 'Home'}).catch(err => {})" href="index_light.html"><img class="logo" src="../assets/뭉치.png" alt="" style="border-radius : 30%" width="119" height="58"></a>
          <!-- <a @click.prevent="$router.push({name: 'Home'})" href="index_light.html"><img class="logo" src="images/logo1.png" alt="" width="119" height="58"></a> -->
        </div>
				<!-- Collect the nav links, forms, and other content for toggling -->
				<div class="collapse navbar-collapse flex-parent" id="bs-example-navbar-collapse-1">
					<ul class="nav navbar-nav flex-child-menu menu-left">
						<li class="hidden">
							<a href="#page-top"></a>
						</li>
						<li class="dropdown first">
							<a @click.prevent="$router.push({name: 'Home'}).catch(err => {})" class="btn btn-default dropdown-toggle lv1" data-toggle="dropdown">
							Home</a>
							
						</li>
						<li class="dropdown first">
							<a @click.prevent="$router.push({name: 'MovieList'}).catch(err => {})" class="btn btn-default dropdown-toggle lv1" data-toggle="dropdown" data-hover="dropdown">
							movies</a>
							
						</li>
						<li class="dropdown first">
							<a @click.prevent="$router.push({name: 'Celebs'}).catch(err => {})" class="btn btn-default dropdown-toggle lv1" data-toggle="dropdown" data-hover="dropdown">
							celebrities</a>
							
						</li>
						<li class="dropdown first">
							<a @click.prevent="$router.push({name: 'Community'}).catch(err => {})" class="btn btn-default dropdown-toggle lv1" data-toggle="dropdown" data-hover="dropdown">
							Community</a>
							
						</li>
						<li @click.prevent="" class="dropdown first">
							<a @click.prevent="$router.push({name: 'UserProfile', params: {username: username}}).catch(err => {})" class="btn btn-default dropdown-toggle lv1" data-toggle="dropdown" data-hover="dropdown">
							User Profile</a>
	
						</li>
					</ul>
					<ul class="nav navbar-nav flex-child-menu menu-right">
					
						<li @click.prevent="showModal" v-if="!isLogin" class=""><a href="#">Log in</a></li>
						<li @click.prevent="showModal" v-if="!isLogin" class="btn signupLink"><a href="#">sign up</a></li>
					
						<li v-if="isLogin"><a @click.prevent="$router.push({name: 'UserProfile', params: {username: username}}).catch(err => {})" href="#">My Page</a></li>
						<li v-if="isLogin"><a @click.prevent="logout" href="#">Logout</a></li>

					
					</ul>
				</div>
			<!-- /.navbar-collapse -->
    </nav>
    <top-search-form></top-search-form>
    
	</div>
</header>
<!-- END | Header -->
</template>

<script>
import jwt_decode from "jwt-decode";
import LoginForm2 from './Account/LoginForm2.vue'
import TopSearchForm from './Header/TopSearchForm.vue'
export default {
  components: { TopSearchForm },
  name: 'Header',
	data () {
		return {
			isLogin: false,
		}
	},
	methods: {
		logout () {
			this.isLogin = false
      localStorage.removeItem('jwt')
			localStorage.removeItem('vuex')
			this.$store.dispatch('logout')
			this.$router.push({name: 'Home'})
      this.$router.go()
		},
		showModal () {
      this.$modal.show(
      LoginForm2,  
      { text: 'This text is passed as a property' },
      { name: 'loginModal',
				draggable: true,
        adaptive: true,
        resizable: true,
        width: '400',
        height: '620',
        },
      )
    },
	},
	computed:{
    token : function () {
      return this.$store.state.token
    },
    username : function(){
			// throw new Error(`${this.token}`)
			// console.log(this.token)
      return jwt_decode(this.token).username
    }
  },
	created () {
		const token = localStorage.getItem('jwt')

    if (token) {
      this.isLogin = true
    }

	}
}
</script>

<style>

</style>