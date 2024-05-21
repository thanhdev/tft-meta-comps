<script setup>
const props = defineProps(['alt']);
const normalizedName = props.alt.replace(/[^a-zA-Z]/g, '');
const src = `https://rerollcdn.com/items/${normalizedName}.png`
</script>

<template>
  <img class="character-item-icon" :src :alt>
</template>

<style scoped>
.character-item-icon {
    width: 18px;
    height: 18px;
}
</style>