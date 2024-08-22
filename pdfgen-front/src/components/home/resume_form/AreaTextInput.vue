<template>
  <div
    class="input-container relative isolate h-[4.2rem] border-4 border-black bg-white shadow-[5px_5px_0_black,_10px_10px_var(--haste-yellow)]"
    :style="{
      height: `calc(4.2rem * ${rows})`
    }"
  >
    <textarea
      type="text"
      :id="id"
      :name="label"
      v-model="model"
      :placeholder="label"
      :rows="rows"
      class="brutal-input absolute inset-0 z-20 resize-none border-0 px-4 py-4 text-lg text-black placeholder:text-transparent"
    ></textarea>
    <label
      :for="id"
      class="pointer-events-none absolute z-10 translate-y-4 px-4 font-mono text-xl font-bold uppercase text-[#888]"
    >
      {{ label }}
    </label>
  </div>
</template>

<script setup>
const model = defineModel({ required: true, default: "" });

defineProps({
  label: {
    required: true,
    default: "Name"
  },
  id: {
    required: true,
    default: ""
  },
  rows: {
    default: 5
  }
});
</script>

<style scoped>
textarea:focus {
  outline: none;
}

.brutal-input:focus {
  border-color: hsla(9, 100%, 50%, 0.9);
  transition: all 0.25s;
}

.brutal-input:focus::placeholder {
  color: transparent;
  transition: all 0.25s;
}

.input-container > label {
  transition: all 0.5s;
}

.input-container {
  margin-top: 1rem;
  transition: all 0.5s;
}

.input-container:has(.brutal-input:focus) {
  border-color: var(--haste-yellow);
}

.input-container > .top-border-right {
  transition: all 0.5s;
}

.brutal-input:focus ~ label {
  background: var(--haste-yellow);
  transform: translateY(-70%) translateX(7px);
  color: white;
  padding-inline: 7px;
  padding-block: 3px;
  letter-spacing: 1px;
  font-size: 0.9rem;
}

.brutal-input:not(:focus):not(:placeholder-shown) ~ label {
  color: transparent;
}
</style>
