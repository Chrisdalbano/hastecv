<template>
  <div class="min-h-screen bg-gray-100">
    <Header />
    <div class="container mx-auto p-6">
      <div class="grid grid-cols-2 gap-4">
        <div>
          <ResumeForm @submit="generatePdf" @input="updatePreview" />
          <TemplateSelector @select="updateTemplate" />
        </div>
        <div>
          <iframe v-if="downloadLink" :src="downloadLink" class="w-full h-full border"></iframe>
        </div>
      </div>
    </div>
    <div class="text-center p-4">
      <DownloadLink v-if="downloadLink" :downloadLink="downloadLink" />
    </div>
  </div>
</template>

<script>
import Header from './components/Header.vue';
import ResumeForm from './components/ResumeForm.vue';
import DownloadLink from './components/DownloadLink.vue';
import TemplateSelector from './components/TemplateSelector.vue';

export default {
  name: 'App',
  components: {
    Header,
    ResumeForm,
    DownloadLink,
    TemplateSelector,
  },
  data() {
    return {
      downloadLink: null,
      resumeData: {
        name: '',
        title: '',
        contact: {
          email: '',
          phone: '',
          location: ''
        },
        // Add more default fields as necessary
      },
      template: 'default',
    };
  },
  methods: {
    async generatePdf(jsonData) {
      try {
        console.log('Sending data:', jsonData);
        const response = await fetch('http://127.0.0.1:5000/generate', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ data: jsonData, template: this.template }),
        });

        if (!response.ok) throw new Error('Failed to generate PDF');

        const blob = await response.blob();
        this.downloadLink = URL.createObjectURL(blob);
      } catch (error) {
        console.error('Error:', error);
      }
    },
    updatePreview(jsonData) {
      this.resumeData = JSON.parse(jsonData);
    },
    updateTemplate(template) {
      this.template = template;
    },
  },
};
</script>

<style>
@import './assets/tailwind.css';
</style>
