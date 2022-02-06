<template>
  <the-document-feed />
</template>

<script>
import TheDocumentFeed from './components/TheDocumentFeed.vue';

export default {
  name: 'App',
  components: {
    TheDocumentFeed,
  },
};
</script>

<style>
@font-face {
  font-family: 'Mukta';
  src: local('Mukta'), url('./assets/fonts/Mukta/Mukta-Regular.ttf');
}
@font-face {
  font-family: 'Mukta';
  font-weight: bold;
  src: local('Mukta'), url('./assets/fonts/Mukta/Mukta-Bold.ttf');
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

body {
  background: #F7F9F7;
}
</style>
