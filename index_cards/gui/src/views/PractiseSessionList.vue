<script lang="ts">
import { defineComponent, ref } from "vue";
import { APIInterface, APIError } from "../api";
import { PractiseSession } from "../models";
import PractiseSessionListItem from "../components/PractiseSessionListItem.vue";
import HomeButton from "../components/HomeButton.vue";

export default defineComponent({
  components: {
    PractiseSessionListItem,
    HomeButton,
  },
  data() {
    const practiseSessions = ref<PractiseSession[]>();
    APIInterface.getPractiseSessions().then(
      (data) => (practiseSessions.value = data)
    );

    return {
      practiseSessions,
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
    deletePractiseSession(practiseSessionId: number) {
      APIInterface.deletePractiseSessions(practiseSessionId)
        .then(() => {
          const topic = this.practiseSessions?.find(
            (practiseSession) => practiseSession.id === practiseSessionId
          );
          if (!topic) return;
          const index = this.practiseSessions?.indexOf(topic);
          if (index === undefined) return;
          this.practiseSessions?.splice(index, 1);
        })
        .catch((error) => {
          this._handleError(error);
        });
    },
  },
});
</script>

<template>
  <HomeButton />
  <h1>Practise Sessions</h1>
  <PractiseSessionListItem
    v-for="practiseSession in practiseSessions"
    :practise-session-id="practiseSession.id"
    :session-start="practiseSession.sessionStart"
    @delete-practise-session="deletePractiseSession"
  />
</template>
