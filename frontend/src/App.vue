<template>
  <div>
    <dark-mode/>
    <the-document-feed />
  </div>
</template>

<script>
import TheDocumentFeed from './components/TheDocumentFeed.vue';
import DarkMode from './components/DarkMode.vue';

export default {
  name: 'App',
  components: {
    TheDocumentFeed,
    DarkMode,
  },
};
</script>

<style>
:root {
  --background-color-primary: #f7f9f7;
  --text-primary-color: #000000;
  --icon-primary-color: invert(0%) sepia(93%) saturate(0%) hue-rotate(285deg)
                        brightness(96%) contrast(102%);
  --document-frame-shadow: 0 3px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0
                         rgba(0, 0, 0, 0.19);
}

:root.dark-theme {
  --background-color-primary: #1f1f1f;
  --text-primary-color: #ffffff;
  --icon-primary-color: invert(100%) sepia(39%) saturate(0%) hue-rotate(276deg)
                        brightness(105%) contrast(100%);
  --document-frame-shadow: 0 3px 8px 0 rgba(255, 255, 255, 0.3), 0 6px 20px 0
                         rgba(110, 99, 99, 0.19);
}

body {
  background: var(--background-color-primary);
}
@font-face {
  font-family: "Mukta";
  src: local("Mukta"), url("./assets/fonts/Mukta/Mukta-Regular.ttf");
}
@font-face {
  font-family: "Mukta";
  font-weight: bold;
  src: local("Mukta"), url("./assets/fonts/Mukta/Mukta-Bold.ttf");
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 60px;
}
</style>
