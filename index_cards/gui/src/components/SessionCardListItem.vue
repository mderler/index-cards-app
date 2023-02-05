<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  props: ["question", "answer", "userAnswer", "correct"],
});
</script>

<template>
  <tr>
    <td>{{ question }}</td>
    <td>{{ answer }}</td>
    <td :class="{ 'ok-message': correct, 'error-message': !correct }">
      {{ userAnswer }}
    </td>
  </tr>
</template>
