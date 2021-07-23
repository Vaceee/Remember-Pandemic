// src/plugins/vuetify.js

import Vue from 'vue'
import Vuetify from 'vuetify/lib'

Vue.use(Vuetify)

const opts = new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#7b7cdd',
        secondary: '#818bc4',
        thirdary: '#676e43', // 949aff
        accent: '#292d52',
        error: '#b71c1c',
        colorful1: '#6567e4',
        colorful2: '#e4dff9'
      }
    }
  }
})

export default opts
