import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";
import Home from "./views/Home.vue";
import CreateTopic from "./views/CreateTopic.vue";
import "./style.css";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", name: "Home", component: Home },
    { path: "/createtopic", name: "Create Topic", component: CreateTopic },
  ],
});

function mount() {
  const app = createApp(App);
  app.use(router);
  app.mount("#app");
}

window.onload = mount;
