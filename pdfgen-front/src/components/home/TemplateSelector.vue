<template>
  <div class="template-selector-container">
    <select
      v-model="selectedTemplate"
      @change="updateTemplate"
      class="template-selector-dropdown"
    >
      <option value="default">DEFAULT</option>
      <option value="modern">MODERN</option>
      <option value="minimal">MINIMAL</option>
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

<style scoped>


.template-label {
  font-size: 1rem;
  color: var(--haste-yellow);
  font-weight: bold;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.template-selector-dropdown {
  appearance: none;
  background: var(--haste-yellow);
  border: 1px solid var(--haste-yellow);
  padding: 0.3rem 0.8rem;
  font-size: 1rem;
  color: #000;
  font-weight: 600;
  letter-spacing: 1px;
  font-family: monospace;
  text-transform: uppercase;
  outline: none;
  cursor: pointer;
  border-radius: 4px;
  transition: all 0.3s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.template-selector-dropdown:focus,
.template-selector-dropdown:hover {
  color: #fff;
  background: var(--haste-yellow);
}

option {
  background-color: rgba(20, 20, 20, 0.85);
  color: var(--haste-yellow);
  padding: 0.5rem;
  text-align: center;
}
</style>