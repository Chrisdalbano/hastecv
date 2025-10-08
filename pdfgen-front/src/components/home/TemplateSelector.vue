<template>
  <div class="template-selector-container">
    <select
      v-model="selectedTemplate"
      @change="updateTemplate"
      class="template-selector-dropdown"
      :title="currentTemplateDescription"
    >
      <option 
        v-for="template in templates" 
        :key="template.value" 
        :value="template.value"
      >
        {{ template.label }}
      </option>
    </select>
    <div v-if="showDescription && currentTemplateDescription" class="template-description">
      {{ currentTemplateDescription }}
    </div>
  </div>
</template>

<script>
export default {
  name: "TemplateSelector",
  props: {
    showDescription: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      selectedTemplate: "executive",
      templates: [
        {
          value: "executive",
          label: "EXECUTIVE",
          description: "Traditional single-column layout with professional navy theme. Perfect for corporate roles."
        },
        {
          value: "technical",
          label: "TECHNICAL",
          description: "Two-column layout with skills sidebar. Ideal for technical and engineering roles."
        },
        {
          value: "modern",
          label: "MODERN",
          description: "Clean, modern design with contemporary colors. Great for creative roles."
        },
        {
          value: "compact",
          label: "COMPACT",
          description: "Maximum content density without looking cramped. Best for experienced professionals."
        },
        {
          value: "creative",
          label: "CREATIVE",
          description: "Bold, eye-catching design with Riot-inspired aesthetics. Perfect for game design and creative tech roles."
        },
        // Legacy support
        {
          value: "default",
          label: "CLASSIC",
          description: "Classic professional layout (legacy)."
        }
      ]
    };
  },
  computed: {
    currentTemplateDescription() {
      const template = this.templates.find(t => t.value === this.selectedTemplate);
      return template ? template.description : '';
    }
  },
  methods: {
    updateTemplate() {
      this.$emit("select", this.selectedTemplate);
    }
  },
  mounted() {
    // Emit initial template
    this.$emit("select", this.selectedTemplate);
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

.template-description {
  margin-top: 0.5rem;
  font-size: 0.75rem;
  color: var(--haste-yellow);
  font-style: italic;
  opacity: 0.8;
  max-width: 200px;
}
</style>