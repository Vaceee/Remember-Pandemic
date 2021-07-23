<template>
  <v-container>
    <v-card elevation="4" class="mx-6 py-2 px-6" tile>
      <v-form>
        <v-textarea
          label=""
          auto-grow
          value="欢迎来到SJBBS，您可以在此畅所欲言！"
          class="texta"
        ></v-textarea>
        <v-btn
          color="accent"
          class="mr-4"
          @click="submit"
          dark
        >
        提交
      </v-btn>
      </v-form>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'writebox',
  data: () => ({
  }),
  modules: {
  },
  props: {}
}
</script>

<style scoped>
.texta{
  width: 80%;
  align-self: center;
}
</style>
