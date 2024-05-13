<script setup>
import {reactive} from 'vue'
import TeamPortrait from "@/components/TeamPortrait.vue";
import ItemPanel from "@/components/ItemPanel.vue";

const teams = reactive([]);
const selectedItems = reactive([]);
const itemsCounter = reactive({});

fetch("/team_comps.json")
    .then(response => response.json())
    .then(data => {
      data = data.map(team => {
        team.diffScore = 0;
        for (const [key, value] of Object.entries(team.ingredients)) {
          team.diffScore += value - (itemsCounter[key] || 0);
        }
        team.diffScore = Math.abs(team.diffScore);
        return team;
      })
      teams.push(...data)
    });


const selectItem = (item) => {
  selectedItems.push(item);
  itemsCounter[item] = itemsCounter[item] ? itemsCounter[item] + 1 : 1;
  sortTeams();
}

const removeItem = (item) => {
  const index = selectedItems.indexOf(item);
  if (index > -1) {
    selectedItems.splice(index, 1);
    itemsCounter[item] -= 1;
    sortTeams();
  }
}

const sortTeams = () => {
  teams.forEach(team => {
    team.diffScore = 0;
    for (const [key, value] of Object.entries(team.ingredients)) {
      team.diffScore += Math.max(0, value - (itemsCounter[key] || 0));
    }
    team.diffScore = Math.abs(team.diffScore);
  });

  teams.sort((a, b) => {
    return a.diffScore - b.diffScore;
  });

}

</script>

<template>
  <div class="row">
    <div class="col">
      <h1 class="text-center">TFT Meta Team Comps Tier List</h1>
    </div>
  </div>
  <div class="container">
    <div class="row tier-group">
      <div class="col-4">
        <ItemPanel :items="selectedItems" @selectItem="selectItem" @removeItem="removeItem"/>
      </div>
      <div class="col-8">
        <TeamPortrait
            v-for="team in teams"
            :key="team.name"
            v-bind="team"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
