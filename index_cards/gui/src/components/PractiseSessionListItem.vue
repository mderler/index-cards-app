<script lang="ts">
import { defineComponent, ref } from "vue";
import { APIInterface } from "../api";

export default defineComponent({
  props: ["practiseSessionId", "sessionStart"],
  data() {
    const count = ref(0);
    const answeredCount = ref(0);
    const topicName = ref("");

    APIInterface.getSessionCardsPractiseSession(this.practiseSessionId).then(
      (sessionCards) => {
        count.value = sessionCards.length;
        answeredCount.value = sessionCards.filter(
          (sessionCard) => sessionCard.correct !== null
        ).length;
      }
    );

    APIInterface.getPractiseSession(this.practiseSessionId).then(
      (practiseSession) =>
        APIInterface.getTopic(practiseSession.topicId).then(
          (topic) => (topicName.value = topic.topicName)
        )
    );

    return {
      count,
      answeredCount,
      topicName,
    };
  },
  methods: {
    practise() {
      this.$router.push({
        name: "Practise",
        params: {
          practiseSessionId: this.practiseSessionId,
        },
      });
    },
    review() {
      this.$router.push({
        name: "Practise Review",
        params: {
          practiseSessionId: this.practiseSessionId,
        },
      });
    },
  },
});
</script>

<template>
  <div class="card">
    <div class="info">{{ topicName }}</div>
    <div class="info">{{ answeredCount }}/{{ count }}</div>
    {{ sessionStart }}
    <button @click="practise">Continue</button>
    <button @click="review">Review</button>
    <button @click="$emit('deletePractiseSession', practiseSessionId)">
      Delete
    </button>
  </div>
</template>

<style scoped>
.card {
  border: 2px;
  border-color: aliceblue;
}

.info {
  display: inline;
  margin-right: 1em;
}
</style>
