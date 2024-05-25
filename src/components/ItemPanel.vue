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
    <Item v-for="item in items"
          :alt="item"
          :key="item"
          @click="$emit('selectItem', item)"
    />
  </div>
  <div class="items-panel position-relative" v-show="selectedItems.length">
    <Item v-for="item in selectedItems"
          :alt="item"
          :key="item"
          @click="$emit('removeItem', item)"
    />
    <button v-show="selectedItems.length"
            class="position-absolute"
            @click="$emit('clearItems')">
      Clear
    </button>
  </div>
</template>

<style scoped>
button {
  top: -10px;
  right: 7px;
  border: none;
  float: right;
  color: #88a0a7;
  font-size: 12px;
  font-weight: 300;
  letter-spacing: .05em;
  background: #123040;
  border-radius: 4px;
  line-height: 1em;
}

.items-panel {
    padding: 5px;
    background: #102531;
    border: 1px solid #17313a;
    margin-bottom: 20px;
}

img {
    width: 30px;
    height: 30px;
    min-width: 30px;
    min-height: 30px;
    opacity: .5;
    transition: all .3s;
    margin: 5px;
}

img:hover {
    opacity: 1;
    cursor: pointer;
    border: 1px solid #d47559;
}

</style>