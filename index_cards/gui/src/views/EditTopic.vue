<script lang="ts">
import { defineComponent, ref } from "vue";
import { APIInterface, APIError } from "../api";

export default defineComponent({
  props: ["topicId"],
  created() {
    console.log(this.$props);
  },
  data() {
    const topicName = ref("");
    let oldTopicName = "";

    APIInterface.getTopic(this.topicId)
      .then((topic) => {
        topicName.value = topic.topicName;
        oldTopicName = topic.topicName;
      })
      .catch((error) => alert(error));

    return {
      topicName,
      oldTopicName,
    };
  },
  methods: {
    submitTopicName() {
      if (this.oldTopicName === this.topicName) {
        return;
      }

      APIInterface.putTopic(this.topicId, this.topicName).catch(
        async (error: Error | APIError) => {
          if (error instanceof APIError) {
            let errorJson;
            alert(JSON.stringify(errorJson));
          } else if (error instanceof Error) {
            alert("Connection to server failed: " + error.message);
          }
        }
      );
      this.oldTopicName = this.topicName;
    },
  },
});
</script>

<template>
  <h1>Edit Topic</h1>
  <label for="topic-name">Topic Name:</label>
  <input
    id="topic-name"
    type="text"
    v-model="topicName"
    v-on:focusout="submitTopicName"
    @keyup.enter="submitTopicName"
  />
  <div class="card">
    <label for="question-text-area">Question:</label>
    <textarea id="question-text-area" rows="4" cols="50"></textarea>
    <label for="answer-text-area">Answer:</label>
    <textarea id="answer-text-area" rows="4" cols="50"></textarea>
  </div>
  <button>Submit</button>
  <button>Save</button>
</template>

<style scoped>
textarea {
  height: 120px;
  width: 400px;
  overflow-y: scroll;
  margin: 1em;
  resize: none;
}
.card {
  display: flex;
}
</style>
