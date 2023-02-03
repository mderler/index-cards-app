<script lang="ts">
import { ref, defineComponent } from "vue";
import { APIInterface, APIError } from "../api";

export default defineComponent({
  setup() {
    const inputRef = ref<HTMLInputElement | null>();
    const submitButtonRef = ref<HTMLButtonElement | null>();
    const errorMessage = ref("");
    const okMessage = ref("");

    let topicName = "";
    let topicId: null | number = null;

    return {
      inputRef,
      submitButtonRef,
      topicName,
      topicId,
      errorMessage,
      okMessage,
    };
  },
  mounted() {
    this.inputRef?.focus();
  },
  methods: {
    async createTopic() {
      APIInterface.postTopic(this.topicName)
        .then((topic) => {
          this.okMessage = "Topic created";
          console.log(topic);
          this.$router.push({
            name: "Edit Topic",
            params: {
              topicId: topic.id,
            },
          });
        })
        .catch(async (error: Error | APIError) => {
          if (error instanceof APIError) {
            let errorJson;
            switch (error.response.status) {
              case 400:
                errorJson = await error.response.json();
                if (!errorJson.topicName) {
                  break;
                }
                if (errorJson.topicName[0].includes("unique")) {
                  this.errorMessage = "Topic with name already exists";
                }
                break;

              default:
                errorJson = await error.response.json();
                alert(
                  "Unknown internal server error: " + JSON.stringify(errorJson)
                );
            }
          } else if (error instanceof Error) {
            alert("Connection to server failed: " + error.message);
          }
        });
    },
    async submit() {
      if (!this.inputRef || !this.submitButtonRef) {
        return;
      }

      this.inputRef.disabled = true;
      this.submitButtonRef.disabled = true;

      this.errorMessage = "";
      this.topicName = this.topicName.trim();

      if (this.topicName === "") {
        this.errorMessage = "The topic name cannot be empty";
        return;
      }

      if (!/^[\x00-\x7F]*$/.test(this.topicName)) {
        this.errorMessage = "The topic name cannot include special characters.";
        return;
      }

      this.inputRef.value = "";

      await this.createTopic();

      this.topicName = "";

      this.inputRef.disabled = false;
      this.submitButtonRef.disabled = false;
    },
  },
});
</script>

<template>
  <label for="input">Topic Name:</label>
  <input
    id="input"
    @keyup.enter="submit"
    v-model="topicName"
    type="text"
    ref="inputRef"
  />
  <button @click="submit" ref="submitButtonRef">Submit</button>
  <p class="error-message" v-if="errorMessage">{{ errorMessage }}</p>
  <p class="ok-message" v-if="okMessage">{{ okMessage }}</p>
</template>
