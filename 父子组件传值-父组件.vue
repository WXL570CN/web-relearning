<template>
  <div id="app">
    <Child :toChild="toChild" @fromChild="getChild"></Child>
    <h1>{{childContent}}</h1>
  </div>
</template>

<script>
import Child from "./components/Child.vue";
export default {
  data() {
    return {
      toChild: "hello, this is from father!",
      childContent: "接收子组件的值！"
    };
  },
  components: {
    Child
  },
  methods: {
    getChild(e) {
      this.childContent = e;
    }
  }
};
</script>