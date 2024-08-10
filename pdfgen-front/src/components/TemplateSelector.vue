<template>
  <div class="mt-2">
    <label class="font-open-sans text-2xl font-bold">Resume Style</label>
    <select
      v-model="selectedTemplate"
      @change="updateTemplate"
      class="mt-2 w-full bg-black p-2 font-open-sans text-2xl"
    >
      <option value="default">
        <span class="mr-2 inline-block h-3 w-3 rounded-full bg-gray-400"></span
        >Default
      </option>
      <option value="modern">
        <span class="mr-2 inline-block h-3 w-3 rounded-full bg-gray-800"></span
        >Modern
      </option>
      <option value="minimal">
        <span
          class="mr-2 inline-block h-3 w-3 rounded-full border border-gray-800 bg-white"
        ></span
        >Minimal
      </option>
    </select>
  </div>
</template>

<script>
export default {
  name: "TemplateSelector",
  data() {
    return {
      selectedTemplate: "default"
    };
  },
  methods: {
    updateTemplate() {
      this.$emit("select", this.selectedTemplate);
    }
  }
};
</script>

<style scoped></style>
