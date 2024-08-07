<template>
    <div class="mt-4">
      <label class="block text-sm font-bold mb-2">Select Template</label>
      <select v-model="selectedTemplate" @change="updateTemplate" class="w-full p-2 border">
        <option value="default">Default</option>
        <option value="modern">Modern</option>
        <!-- Add more templates as needed -->
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
  /* Add any scoped styles for TemplateSelector component here */
  </style>
  