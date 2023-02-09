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
    const topics = ref<Topic[]>();
    const displayedTopics = ref<Topic[]>();
    const search = ref("");
    APIInterface.getTopics()
      .then((data) => {
        topics.value = data;
        displayedTopics.value = topics.value;
      })
      .catch((error) => alert(error));

    return {
      topics,
      displayedTopics,
      search,
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
          this.displayedTopics = this.topics;
        })
        .catch((error) => this._handleError(error));
    },
    searchTopics() {
      this.displayedTopics = this.topics?.filter((topic) => {
        return topic.topicName
          .toLowerCase()
          .includes(this.search.trim().toLowerCase());
      });
    },
  },
});
</script>

<template>
  <div class="topic-search">
    <label for="search">Search:</label>
    <input id="search" type="text" @input="searchTopics" v-model="search" />
    <router-link to="/createtopic" custom v-slot="{ navigate }">
      <button @click="navigate" role="link">Create Topic</button>
    </router-link>
  </div>
  <TopicListItem
    v-for="topic in displayedTopics"
    @delete-topic="deleteTopic"
    :topic-id="topic.id"
    :topic-name="topic.topicName"
  />
</template>

<style scoped>
.topic-search label {
  font-size: 1.5em;
  margin-right: 1em;
}
</style>
