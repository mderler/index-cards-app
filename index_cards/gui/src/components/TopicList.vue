<script lang="ts">
import TopicListItem from "./TopicListItem.vue";
import { defineComponent, ref } from "vue";
import { APIInterface, APIError } from "../api";
import { Topic } from "../models";

export default defineComponent({
  components: {
    TopicListItem,
  },
  data() {
    const loaded = ref(false);
    const topics = ref<Topic[]>();
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
    _handleError(error: Error | APIError) {
      if (error instanceof APIError) {
        let errorJson;
        alert(JSON.stringify(errorJson));
      } else if (error instanceof Error) {
        alert("Connection to server failed: " + error.message);
      }
    },
    deleteTopic(topicId: number) {
      APIInterface.deleteTopic(topicId)
        .then(() => {
          const topic = this.topics?.find((topic) => topic.id === topicId);
          if (!topic) return;
          const index = this.topics?.indexOf(topic);
          if (!index) return;
          this.topics?.splice(index, 1);
        })
        .catch((error) => this._handleError(error));
    },
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
