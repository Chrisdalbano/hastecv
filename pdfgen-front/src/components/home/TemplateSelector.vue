<template>
  <div class=" px-4 py-2">
    <select
      v-model="selectedTemplate"
      @change="updateTemplate"
      class="bg-transparent p-2 text-2xl"
    >
      <option value="default">
        <span
          class="mr-2 inline-block h-3 w-3 rounded-full bg-transparent"
        ></span>
        DEFAULT
      </option>
      <option value="modern">
        <span
          class="mr-2 inline-block h-3 w-3 rounded-full bg-transparent"
        ></span>
        MODERN
      </option>
      <option value="minimal">
        <span
          class="mr-2 inline-block h-3 w-3 rounded-full border bg-transparent"
        ></span>
        MINIMAL
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

<style scoped>
select {
  border-style: none;
}

select:focus,
select:hover {
  border-style: none;
}

select option {
  background-color: var(--primary-black);
}

* {
  color: var(--haste-yellow);
  font-size: 20px;
  font-weight: 600;
  letter-spacing: 1px;
  font-family: monospace;
  text-transform: uppercase;
  text-align: center;
  

}
</style>
