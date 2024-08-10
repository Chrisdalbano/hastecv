<template>
  <div class="mt-2">
    <label class="font-bold font-open-sans text-2xl">Resume Style</label>
    <select v-model="selectedTemplate" @change="updateTemplate" class="w-full p-2 bg-black text-2xl mt-2 font-open-sans">
      <option value="default">
        <span class="inline-block w-3 h-3 bg-gray-400 rounded-full mr-2"></span>Default
      </option>
      <option value="modern">
        <span class="inline-block w-3 h-3 bg-gray-800 rounded-full mr-2"></span>Modern
      </option>
      <option value="minimal">
        <span class="inline-block w-3 h-3 bg-white rounded-full border border-gray-800 mr-2"></span>Minimal
      </option>
    </select>
  </div>
</template>

<script>
export default {
  name: 'TemplateSelector',
  data() {
    return {
      selectedTemplate: 'default',
    };
  },
  methods: {
    updateTemplate() {
      this.$emit('select', this.selectedTemplate);
    },
  },
};
</script>

<style scoped>

</style>
