<template>
    <div v-if="show" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
      <div class="bg-gray-100 p-4 rounded-lg shadow-lg w-3/4 md:w-1/2 lg:w-1/3">
        <h2 class="text-2xl font-bold mb-4">{{ title }}</h2>
        <div>
          <slot></slot>
        </div>
        <div class="flex justify-end mt-4">
          <button @click="close" class="bg-gray-300 text-gray-700 px-4 py-2 rounded mr-2">Cancel</button>
          <button @click="save" class="bg-black text-yellow-500 px-4 py-2 rounded">Save</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ReusableModal',
    props: {
      show: Boolean,
      title: String
    },
    methods: {
      close() {
        this.$emit('close');
      },
      save() {
        this.$emit('save');
      }
    }
  }
  </script>
  
  <style scoped>
  /* Add any scoped styles for ReusableModal component here */
  </style>
  