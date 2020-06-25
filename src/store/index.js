import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    loggedIn: false,
    userData: {}
  },
  mutations: {
    login (state, payload) {
      state.loggedIn = true
      state.userData = payload.userData
    },
    logout (state) {
      state.loggedIn = false
      state.userData = {}
    }
  },
  getters: {
    username: state => state.userData.username
  }
})
