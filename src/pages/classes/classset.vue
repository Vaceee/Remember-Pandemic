<template>
  <v-content id="class-list">
    <v-card elevation="10" height="100%" class="ma-8 pa-4">
      <v-form
        ref="form"
        v-model="valid"
        lazy-validation
        class="px-6 pb-6"
      >
        <v-card-title class="d-flex headline px-0 pt-2" color="primary"><!--justify-center-->
          <span>课程设置</span>
         </v-card-title>
         <div class="textinput">
            <v-text-field
              v-model="classname"
              label="课程名称"
              required
            ></v-text-field>
            <v-text-field
              v-model="classno"
              label="课号"
              counter="8"
              required
            ></v-text-field>
          </div>
          <v-row>
            <v-col>
        <v-date-picker
          v-model="date"
          color="thirdary"
          :first-day-of-week="1"
          locale="zh-cn"
          :landscape="($vuetify.breakpoint.smAndUp)"
        >
          <v-spacer></v-spacer>
          <v-btn text class="subtitle-1" color="thirdary" >取消</v-btn>
          <v-btn text class="subtitle-1" color="thirdary">确定</v-btn>
        </v-date-picker></v-col>
    <v-col cols="12" sm="6">
      <v-text-field v-model="date" label="Date range" prepend-icon="mdi-calender" readonly
      ></v-text-field>

    </v-col></v-row>
            <div class="buttons pt-8 pl-4">
              <v-btn
                color="accent"
                class="mr-4"
              >
                提交
              </v-btn>

              <v-btn
                color="primary"
                class="mr-4"
              >
                清除
              </v-btn>
              </div>
            </v-form>
    </v-card>
  </v-content>
</template>

<script>
export default {
  name: 'classset',
  components: {
  },
  props: ['secId'],
  data () {
    return {
      date: new Date().toISOString().substr(0, 10)
    }
  }
}
</script>

<style>
.textinput{
  width: 50%;
  padding-bottom: 1em;
}
.a{
  color:#676e43;
}
</style>
