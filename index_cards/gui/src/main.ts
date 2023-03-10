import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";
import Home from "./views/Home.vue";
import CreateTopic from "./views/CreateTopic.vue";
import EditTopicVue from "./views/EditTopic.vue";
import PractiseSessionListVue from "./views/PractiseSessionList.vue";
import Practise from "./views/Practise.vue";
import PractiseSessionReviewVue from "./views/PractiseSessionReview.vue";
import "./style.css";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", name: "Home", component: Home },
    { path: "/createtopic", name: "Create Topic", component: CreateTopic },
    {
      path: "/practisesessions",
      name: "Practise Sessions",
      component: PractiseSessionListVue,
    },
    {
      path: "/practise/:practiseSessionId",
      name: "Practise",
      component: Practise,
      props: true,
    },
    {
      path: "/practisereview/:practiseSessionId",
      name: "Practise Review",
      component: PractiseSessionReviewVue,
      props: true,
    },
    {
      path: "/edittopic/:topicId",
      name: "Edit Topic",
      component: EditTopicVue,
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
