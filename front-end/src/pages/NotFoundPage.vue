<template>
  <div>
    <h1>404 NOT FOUND</h1>
    <p>Redirecting...</p>
  </div>
</template>

<script>
import HomePage from './HomePage'
import LoginPage from './LoginPage'

export default {
  name: 'NotFoundPage',
  mounted () {
    const redirectRouteName = this.$store.state.loggedIn ? HomePage.name : LoginPage.name
    setTimeout(() => {
      this.$router.replace({ name: redirectRouteName })
    }, 3000)
  }
}
</script>
