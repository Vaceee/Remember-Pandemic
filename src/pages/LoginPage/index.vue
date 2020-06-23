<template>
  <div>
    <login-form/>
    <login-bg/>
  </div>
</template>

<script>
import loginForm from './loginForm'
import loginBg from './loginBg'

export default {
  name: 'LoginPage',
  components: {
    loginForm, loginBg
  }
}
</script>
