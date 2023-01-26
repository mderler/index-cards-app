import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";

function mount() {
  const app = createApp(App);
  app.mount("#app");
}

window.onload = mount;
