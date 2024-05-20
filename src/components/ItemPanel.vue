<script setup>
import {reactive, ref} from "vue";
import Item from "@/components/Item.vue";

const props = defineProps(['items']);
defineEmits(['selectItem', 'removeItem', 'clearItems']);

const items = ref([
  "B.F. Sword",
  "Chain Vest",
  "Giant's Belt",
  "Needlessly Large Rod",
  "Negatron Cloak",
  "Recurve Bow",
  "Sparring Gloves",
  "Spatula",
  "Tear of the Goddess",
  // "Dryad Emblem",
  // "Fated Emblem",
  // "Ghostly Emblem",
  // "Heavenly Emblem",
  // "Mythic Emblem",
  // "Porcelain Emblem",
  // "Storyweaver Emblem",
  // "Umbral Emblem",
  // "Adaptive Helm",
  // "Archangel's Staff",
  // "Bloodthirster",
  // "Blue Buff",
  // "Bramble Vest",
  // "Crownguard",
  // "Deathblade",
  // "Dragon's Claw",
  // "Edge of Night",
  // "Evenshroud",
  // "Gargoyle Stoneplate",
  // "Giant Slayer",
  // "Guardbreaker",
  // "Guinsoo's Rageblade",
  // "Hand of Justice",
  // "Hextech Gunblade",
  // "Infinity Edge",
  // "Ionic Spark",
  // "Jeweled Gauntlet",
  // "Last Whisper",
  // "Morellonomicon",
  // "Nashor's Tooth",
  // "Protector's Vow",
  // "Quicksilver",
  // "Rabadon's Deathcap",
  // "Red Buff",
  // "Redemption",
  // "Runaan's Hurricane",
  // "Spear of Shojin",
  // "Statikk Shiv",
  // "Steadfast Heart",
  // "Sterak's Gage",
  // "Sunfire Cape",
  // "Tactician's Crown",
  // "Thief's Gloves",
  // "Titan's Resolve",
  // "Warmog's Armor"
]);
const selectedItems = reactive(props.items);

</script>

<template>
  <div class="items-panel">
    <Item v-for="item in items" :alt="item" :key="item" @click="$emit('selectItem', item)"/>
  </div>
  <div class="items-panel" v-show="selectedItems.length">
    <Item v-for="item in selectedItems" :alt="item" :key="item" @click="$emit('removeItem', item)"/>
    <button v-show="selectedItems.length"
            class="float-right team-playstyle"
            @click="$emit('clearItems')">
      Clear
    </button>
  </div>
</template>

<style scoped>
button.team-playstyle {
  border: none;
  float: right;
}
</style>