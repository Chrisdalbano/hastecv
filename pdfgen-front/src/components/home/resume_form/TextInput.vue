<template>
  <div
    class="__input-container relative isolate h-[4.2rem] border-4 border-black bg-white shadow-[5px_5px_0_black,_10px_10px_var(--haste-yellow)]"
  >
    <input
      v-model="model"
      type="text"
      :id="id"
      :name="label"
      autocomplete="off"
      :placeholder="label"
      class="__brutal-input absolute inset-0 z-20 border-0 px-4 text-lg text-black placeholder:text-transparent"
    />
    <label
      :for="id"
      class="pointer-events-none absolute z-10 translate-y-1/2 px-4 pt-[2px] font-mono text-xl font-bold uppercase text-[#888]"
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
  }
});
</script>

<style scoped>
input:focus {
  outline: none;
}

.__brutal-input:focus {
  border-color: hsla(9, 100%, 50%, 0.9);
  transition: all 0.25s;
}

.__brutal-input:focus::placeholder {
  color: transparent;
  transition: all 0.25s;
}

.__input-container > label {
  transition: all 0.5s;
}

.__input-container {
  transition: all 0.5s;
}

.__input-container:has(.__brutal-input:focus) {
  border-color: var(--haste-yellow);
}

.__input-container > .top-border-right {
  transition: all 0.5s;
}

.__brutal-input:focus ~ label {
  background: var(--haste-yellow);
  transform: translateY(-70%) translateX(7px);
  color: white;
  padding-inline: 7px;
  padding-block: 1px;
  letter-spacing: 1px;
  font-size: 0.88rem;
}

.__brutal-input:not(:focus):not(:placeholder-shown) ~ label {
  color: transparent;
}
</style>
