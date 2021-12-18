import Vue from 'vue'
import Vuex from 'vuex'
// import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";
Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    token: '',

  },
  mutations: {
    LOGIN_COMPLETED: function (state, res) {
      const token = res.data.access
      console.log(token)
      state.token = token
      // throw new Error(`${state.token}`)
    },
    LOGOUT: function (state) {
      state.token = ''
      // throw new Error(`${state.token}`)
    },   
  },
  actions: {
    loginCompleted: function (context, res) {
      context.commit('LOGIN_COMPLETED', res)
      // console.log(username)
      // console.log(context)
    },
    logout: function (context) {
      context.commit('LOGOUT')
      // console.log(username)
      // console.log(context)
    },    
    // addOneLineComments ({commit}, item) {
    //   axios({
    //     url: api + ''
    //   })
    //   commit('ADD_ONE_LINE_COMMENTS', item)
    // }
  },
  getters: {
    token (state) {
      return state.token
    }
  },
  modules: {
  },
  // update () {
	// 	const token = localStorage.getItem('jwt')

  //   if (token) {
  //     this.isLogin = true
  //     this.$store.state.token = token
  //   }

	// },
})
