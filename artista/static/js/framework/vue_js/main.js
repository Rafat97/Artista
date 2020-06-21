import Vue from 'vue';
const axios = require('axios').default;
import App from './components/App'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app-vue')

