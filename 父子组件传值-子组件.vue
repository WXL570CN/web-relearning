<template>
  <div>
    <h1>{{toChild}}</h1>
    <div @click="toFather()">click me</div>
  </div>
</template>

<script>
export default {
  props: ["toChild"],
  methods: {
    toFather() {
      this.$emit("fromChild", "hello, this is from child!");
    }
  }
};
</script>