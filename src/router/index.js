import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'
import axios from '../axios'

import NotFoundRoute from './NotFoundRoute'
import LoginRoute from './LoginRoute'
import HomeRoute from './HomeRoute'
import PostsRoute from './PostsRoute'
import PostRoute from './PostRoute'
import WriteRoute from './WriteRoute'
import RegisterRoute from './RegisterRoute'

Vue.use(VueRouter)

const routes = [
  NotFoundRoute,
  LoginRoute,
  RegisterRoute,
  HomeRoute,
  PostsRoute,
  PostRoute,
  WriteRoute
]

const router = new VueRouter({
  routes,
  mode: 'history'
})

router.beforeEach((to, from, next) => {
  axios.get('/login').then(res => {
    let loggedIn = false
    let userData = {}
    if (res.status === 200) {
      const data = res.data
      if (data.status === 'GET_SUCCESS') {
        loggedIn = true
        userData = {
          username: data.usr_name,
          gender: data.usr_gender,
          level: data.userlevel,
          no: data.usr_no
        }
      }
    }
    if (loggedIn && !store.state.loggedIn) {
      store.commit({
        type: 'login',
        userData
      })
    } else if (!loggedIn && store.state.loggedIn) {
      store.commit('logout')
    }

    if (to.name === 'LoginPage' && loggedIn) {
      if (from.name === 'LoginPage' || from.name === null) {
        next({ name: 'HomePage' })
      } else {
        next(false)
      }
    } else if (to.name !== 'LoginPage' && !loggedIn) {
      if (to.name === 'RegisterPage') {
        next()
      } else if (from.name !== 'LoginPage') {
        next({ name: 'LoginPage' })
      } else {
        next(false)
      }
    } else {
      next()
    }
  })
})

export default router
