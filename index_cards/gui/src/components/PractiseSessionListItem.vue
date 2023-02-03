<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  props: ["practiseSessionId", "sessionStart"],
  methods: {
    practise() {
      this.$router.push({
        name: "Practise",
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
    <div id="count">Count</div>
    {{ sessionStart }}
    <button @click="practise">Continue</button>
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
#count {
  display: inline;
}
</style>
