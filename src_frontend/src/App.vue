<template>
  <div id="app">
    <main-app />
  </div>
</template>

<script>
import Main from './components/Main';

export default {
  name: 'App',
  components: {
    'main-app': Main
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
