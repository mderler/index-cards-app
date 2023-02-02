<script lang="ts">
import TopicListItem from "./TopicListItem.vue";
import { defineComponent, ref } from "vue";
import { APIInterface } from "../api";
import { Topic } from "../models";

export default defineComponent({
  components: {
    TopicListItem,
  },
  data() {
    let loaded = ref(false);
    let topics = ref<Topic[]>();
    APIInterface.getTopics()
      .then((data) => {
        loaded.value = true;
        topics.value = data;
      })
      .catch((error) => alert(error));

    return {
      loaded,
      topics,
    };
  },
  methods: {
    deleteTopic(topicId: number) {
      const topic = this.topics?.find((topic) => topic.id === topicId);
      if (!topic) return;
      const index = this.topics?.indexOf(topic);
      if (!index) return;
      this.topics?.splice(index, 1);

      APIInterface.deleteTopic(topicId);
    },
    editTopic(topicId: number) {},
  },
});
</script>

<template>
  <div class="topic-search">
    <input type="text" />
    <router-link to="/createtopic" custom v-slot="{ navigate }">
      <button @click="navigate" role="link">Create Topic</button>
    </router-link>
  </div>
  <div v-if="loaded">
    <TopicListItem
      v-for="topic in topics"
      @delete-topic="deleteTopic"
      @edit-topic="editTopic"
      :topic-id="topic.id"
      :topic-name="topic.topicName"
    />
  </div>
</template>

<style scoped>
.topic-search {
  display: flex;
}
</style>
