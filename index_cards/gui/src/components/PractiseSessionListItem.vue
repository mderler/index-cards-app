<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  props: ["practiseSessionId", "sessionStart"],
});
</script>

<template>
  <div class="card">
    <div id="count">Count</div>
    {{ sessionStart }}
    <button>Continue</button>
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
