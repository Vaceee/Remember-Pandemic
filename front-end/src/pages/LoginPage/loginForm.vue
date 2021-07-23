<template>
  <div>
    <v-card elevation="10" height="100%" width="33%" class="containcard" tile>
      <v-container>
        <v-row no-gutters>
          <v-col>
            <v-img src="../../assets/logo.png" class="mx-6 mb-3" height="100" width="100">
            </v-img>
            <v-form
              ref="form"
              lazy-validation
              class="px-6 pb-6"
            >
              <v-card-title class="d-flex headline px-0 pt-2" color="primary"><!--justify-center-->
                <span>用户登录</span>
              </v-card-title>
              <v-text-field
                v-model="usrNo"
                :counter="7"
                label="账号"
                required
                clearable
                autocomplete="false"
              ></v-text-field>
              <v-text-field
                v-model="usrPassword"
                label="密码"
                required
                type="password"
                clearable
                autocomplete="false"
                @keyup.enter="try_login"
              ></v-text-field>

              <div class="buttons">
                <v-btn
                  color="accent"
                  class="mr-4"
                  @click="try_login"
                >登陆</v-btn>
                <router-link class="link" to="/register">
                <v-btn
                  color="primary"
                  class="mr-4"
                >注册</v-btn>
                </router-link>
              </div>
            </v-form>
          </v-col>
        </v-row>
      </v-container>
    </v-card>
  </div>
</template>

<script>
import hash from 'sha.js'
export default {
  name: 'LoginForm',
  data () {
    return {
      usrNo: '',
      usrPassword: '',
      registerAlert: false
    }
  },
  computed: {
    passwdHash () {
      return hash('sha256').update(this.usrPassword).digest('hex')
    }
  },
  methods: {
    try_login () {
      if (!this.usrNo.length || !this.usrPassword.length) {
        this.login_alert('用户名或密码不能为空')
      } else {
        this.$axios.post('/login', {
          usr_no: this.usrNo,
          usr_password: this.passwdHash
        }).then(res => {
          if (res.status === 200) {
            const data = res.data
            if (data.status === 'GET_SUCCESS') {
              const userData = {
                username: data.usr_name,
                gender: data.usr_gender,
                level: data.userlevel,
                no: data.usr_no
              }
              this.$store.commit({
                type: 'login',
                userData
              })
              this.$router.push('home')
            } else if (data.status === 'NAME_PASSWORD_WRONG') {
              this.login_alert('用户名或密码错误！')
            } else if (data.status === 'LOGINOUT_UNKNOWN') {
              this.login_alert('出错了！')
            } else {
              this.login_alert('Unknown error occured')
            }
          } else {
            this.login_alert('Connection failed.\nPlease check your network condition.')
          }
        }).catch(e => {
          this.login_alert(e)
        })
      }
    },
    login_alert (msg) {
      alert(msg)
    }
  }
}
</script>

<style scoped>
  .buttons {
    justify-content: center;
    margin-top: 15px;
  }
  .containcard {
    position: fixed;
    top:0;
    right:5%;
    transform: translate(20%,0);
    z-index: 10;
  }
  .alert-container {
    padding-right: 1em;
  }
</style>
