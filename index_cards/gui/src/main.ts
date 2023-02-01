import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";
import Home from "./views/Home.vue";
import CreateTopic from "./views/CreateTopic.vue";
import AddCardsVue from "./views/AddCards.vue";
import "./style.css";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", name: "Home", component: Home },
    { path: "/createtopic", name: "Create Topic", component: CreateTopic },
    {
      path: "/addcards",
      name: "Add cards",
      component: AddCardsVue,
      props: true,
    },
  ],
});

function mount() {
  const app = createApp(App);
  app.use(router);
  app.mount("#app");
}

window.onload = mount;
