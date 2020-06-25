<template>
  <v-container>
    <v-card elevation="4" class="mx-6 py-2 px-6" tile>
      <v-form>
        <v-textarea
          label=""
          auto-grow
          placeholder="欢迎来到记疫。您可以在这里写下有关疫情的一切。"
          v-model="content"
          class="texta"
        ></v-textarea>
        <v-btn
          color="accent"
          class="mr-4"
          @click="reply"
          dark
        >
        回复
      </v-btn>
      </v-form>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'writebox',
  data: () => ({
    content: ''
  }),
  modules: {
  },
  props: {},
  methods: {
    reply () {
      if (!this.content.length) {
        alert('内容不能为空')
      } else {
        this.$axios.post('/replies/new', {
          post_id: this.$route.params.postId,
          content: this.content,
          rep_to: -1 // TODO,暂时只给帖子回复
        }).then(res => {
          if (res.status === 200) {
            const data = res.data
            if (data.status === 'REPLY_SUCCESS') {
              alert('回复成功！')
              this.$router.go(0)
            } else if (data.status === 'REPLY_UNKNOWN') {
              alert('出错了！')
            } else {
              alert('Unknown error occured')
            }
          } else {
            alert('Connection failed.\nPlease check your network condition.')
          }
        }).catch(e => {
          alert(e)
        })
      }
    }
  }
}
</script>

<style scoped>
.texta{
  width: 80%;
  align-self: center;
}
</style>
