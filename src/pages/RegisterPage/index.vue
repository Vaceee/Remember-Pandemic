<template>
  <div>
    <register-form/>
    <register-bg/>
  </div>
</template>

<script>
import registerForm from './registerForm'
import registerBg from './registerBg'

export default {
  name: 'RegisterPage',
  components: {
    registerForm, registerBg
  }
}
</script>
