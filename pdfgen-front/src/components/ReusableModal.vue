<template>
  <div
    v-if="show"
    class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-95"
  >
    <div class="w-3/4 bg-transparent p-4 md:w-1/2 lg:w-1/3">
      <h2 class="mb-4 text-2xl font-bold">{{ title }}</h2>
      <div>
        <slot></slot>
      </div>
      <div class="mt-4 flex justify-end">
        <button @click="close" class="haste-option">Cancel</button>
        <button @click="save" class="haste-button">Save</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ReusableModal",
  props: {
    show: Boolean,
    title: String
  },
  methods: {
    close() {
      this.$emit("close");
    },
    save() {
      this.$emit("save");
    }
  }
};
</script>

<style scoped>
/* Add any scoped styles for ReusableModal component here */
</style>
