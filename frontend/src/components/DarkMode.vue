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
      localStorage.setItem('theme', this.currentMode);
      this.applyMode();
    },
    applyMode() {
      document.documentElement.className = `${this.currentMode}-theme`;
    },
    initMode() {
      this.currentMode = localStorage.getItem('theme', this.currentMode) ?? 'light';
      this.applyMode();
    },
  },
  mounted() {
    this.initMode();
  },
};
</script>

<style>
#theme-toggle {
  max-width: 35px;
  max-height: 35px;
  position: fixed;
  top: 15px;
  right: 15px;
  z-index: 10;
  filter: var(--icon-primary-color);
  background: rgba(218, 218, 218, 0.616);
  border-radius: 10px;
  padding: 3px;
}
</style>
