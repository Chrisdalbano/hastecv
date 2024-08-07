<template>
    <div class="border p-4 mt-4">
      <h2 v-if="data.name" class="text-xl font-bold">{{ data.name }}</h2>
      <p v-if="data.title" class="text-sm">{{ data.title }}</p>
      <p v-if="data.contact && data.contact.email" class="text-sm">{{ data.contact.email }}</p>
      <p v-if="data.contact && data.contact.phone" class="text-sm">{{ data.contact.phone }}</p>
      <p v-if="data.contact && data.contact.location" class="text-sm">{{ data.contact.location }}</p>
      <!-- Add more fields as necessary -->
    </div>
  </template>
  
  <script>
  export default {
    name: 'Preview',
    props: {
      data: {
        type: Object,
        default: () => ({
          name: '',
          title: '',
          contact: {
            email: '',
            phone: '',
            location: ''
          },
          // Add more default fields as necessary
        })
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add any scoped styles for Preview component here */
  </style>
  