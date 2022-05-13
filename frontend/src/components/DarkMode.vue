<template>
  <img id='theme-toggle' v-bind:src="getIcon" v-on:click="toggleMode"/>
</template>

<script>
const sunIcon = require('@/assets/icons/sun.svg');
const moonIcon = require('@/assets/icons/moon.svg');

export default {
  name: 'DarkMode',
  data() {
    return {
      modes: ['light', 'dark'],
      currentMode: 'light',
    };
  },
  computed: {
    getIcon() {
      return this.currentMode === 'light' ? sunIcon : moonIcon;
    },
  },
  methods: {
    toggleMode() {
      this.currentMode = this.currentMode === 'light' ? 'dark' : 'light';
      this.applyMode();
    },
    applyMode() {
      document.documentElement.className = `${this.currentMode}-theme`;
    },
  },
  mounted() {
    this.applyMode();
  },
};
</script>

<style>
#theme-toggle {
  max-width: 35px;
  max-height: 35px;
  position: absolute;
  top: 20px;
  right: 20px;
  filter: var(--icon-primary-color);
}
</style>
