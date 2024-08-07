<template>
  <div class="p-6">
    <div class="flex items-center mb-4">
      <button
        @click="toggleView('form')"
        :class="{
          'bg-haste-yellow text-black ': view === 'form',
          'bg-black text-gray-200': view !== 'form',
        }"
        class="px-4 py-2 font-bold "
      >
        Manual
      </button>
      <button
        @click="toggleView('json')"
        :class="{
          'bg-haste-yellow text-black': view === 'json',
          'bg-black text-gray-200': view !== 'json',
        }"
        class="px-4 py-2 font-bold "
      >
        JSON
      </button>
    </div>
    <div v-if="view === 'form'">
      <form @submit.prevent="submitForm">
        <h2 class="text-2xl font-bold mb-4 text-white">Personal Information</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <input
            v-model="resumeData.name"
            class="w-full p-2"
            type="text"
            placeholder="Name"
          />
          <input
            v-model="resumeData.title"
            class="w-full p-2"
            type="text"
            placeholder="Title"
          />
        </div>

        <h2 class="text-2xl font-bold mb-4 mt-6 text-white">
          Contact Information
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <input
            v-model="resumeData.contact.email"
            class="w-full p-2"
            type="email"
            placeholder="Email"
          />
          <input
            v-model="resumeData.contact.phone"
            class="w-full p-2"
            type="tel"
            placeholder="Phone"
          />
          <input
            v-model="resumeData.contact.location"
            class="w-full p-2"
            type="text"
            placeholder="Location"
          />
          <input
            v-model="resumeData.contact.linkedin"
            class="w-full p-2"
            type="text"
            placeholder="LinkedIn"
          />
          <input
            v-model="resumeData.contact.github"
            class="w-full p-2"
            type="text"
            placeholder="GitHub"
          />
          <input
            v-model="resumeData.contact.website"
            class="w-full p-2"
            type="text"
            placeholder="Website"
          />
        </div>

        <h2 class="text-2xl font-bold mb-4 mt-6 text-white">Summary</h2>
        <textarea
          v-model="resumeData.summary"
          class="w-full p-2 bg-black border-solid border-2 border-whitesmoke text-white"
          rows="4"
          placeholder="Summary"
        ></textarea>

        <div
          v-for="(exp, index) in resumeData.experience"
          :key="index"
          class="mb-4 relative"
        >
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <input
              v-model="exp.position"
              class="w-full p-2 mb-2"
              type="text"
              placeholder="Position"
            />
            <input
              v-model="exp.company"
              class="w-full p-2 mb-2"
              type="text"
              placeholder="Company"
            />
            <input
              v-model="exp.dates"
              class="w-full p-2 mb-2"
              type="text"
              placeholder="Dates"
            />
          </div>
          <textarea
            v-model="exp.responsibilities"
            class="w-full p-2 mb-2"
            rows="3"
            placeholder="Responsibilities"
          ></textarea>
          <button
            @click.prevent="removeExperience(index)"
            class="absolute top-0 right-0 bg-red-500 text-white p-1 rounded-full"
          >
            x
          </button>
        </div>
        <div class="flex">
          <button
            @click.prevent="openModal('experience')"
            class="p-2 text-white font-bold rounded mt-2 mr-2"
          >
            Add Experience
          </button>

          <div
            v-for="(edu, index) in resumeData.education"
            :key="index"
            class="mb-4 relative"
          >
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <input
                v-model="edu.degree"
                class="w-full p-2 mb-2"
                type="text"
                placeholder="Degree"
              />
              <input
                v-model="edu.institution"
                class="w-full p-2 mb-2"
                type="text"
                placeholder="Institution"
              />
              <input
                v-model="edu.dates"
                class="w-full p-2 mb-2"
                type="text"
                placeholder="Dates"
              />
            </div>
            <button
              @click.prevent="removeEducation(index)"
              class="absolute top-0 right-0 bg-red-500 text-white p-1 rounded-full mx-2"
            >
              x
            </button>
          </div>
          <button
            @click.prevent="openModal('education')"
            class="text-white font-bold rounded mt-2 mx-4"
          >
            Add Education
          </button>

          <div
            v-for="(skill, index) in resumeData.skills"
            :key="index"
            class="mb-4 relative"
          >
            <input
              v-model="resumeData.skills[index]"
              class="w-full p-2 mb-2"
              type="text"
              placeholder="Skill"
            />
            <button
              @click.prevent="removeSkill(index)"
              class="absolute top-0 right-0 bg-red-500 text-white p-1 rounded-full"
            >
              x
            </button>
          </div>
          <button
            @click.prevent="openModal('skill')"
            class="text-white font-bold rounded mt-2 mx-4"
          >
            Add Skill
          </button>
        </div>

        <div></div>
        <button type="submit" class="haste-button">Generate Preview</button>
      </form>
    </div>

    <div v-if="view === 'json'">
      <div class="mt-8">
        <h2 class="text-2xl font-bold mb-4 text-white">Paste JSON Data</h2>
        <div ref="jsonEditor" class="h-64 my-12"></div>
        <button
          @click="submitJson"
          class="haste-button"
        >
          Generate PDF from JSON
        </button>
      </div>
    </div>

    <ReusableModal
      :show="showModal"
      :title="modalTitle"
      @close="closeModal"
      @save="saveEntry"
    >
      <template v-if="modalType === 'experience'">
        <input
          v-model="newEntry.position"
          class="w-full p-2 mb-2"
          type="text"
          placeholder="Position"
        />
        <input
          v-model="newEntry.company"
          class="w-full p-2 mb-2"
          type="text"
          placeholder="Company"
        />
        <input
          v-model="newEntry.dates"
          class="w-full p-2 mb-2"
          type="text"
          placeholder="Dates"
        />
        <textarea
          v-model="newEntry.responsibilities"
          class="w-full p-2 mb-2"
          rows="3"
          placeholder="Responsibilities"
        ></textarea>
      </template>
      <template v-if="modalType === 'education'">
        <input
          v-model="newEntry.degree"
          class="w-full p-2 mb-2"
          type="text"
          placeholder="Degree"
        />
        <input
          v-model="newEntry.institution"
          class="w-full p-2 mb-2"
          type="text"
          placeholder="Institution"
        />
        <input
          v-model="newEntry.dates"
          class="w-full p-2 mb-2"
          type="text"
          placeholder="Dates"
        />
      </template>
      <template v-if="modalType === 'skill'">
        <input
          v-model="newEntry.skill"
          class="w-full p-2 mb-2"
          type="text"
          placeholder="Skill"
        />
      </template>
    </ReusableModal>
  </div>
</template>

<script>
import JSONEditor from "jsoneditor";
import "jsoneditor/dist/jsoneditor.css";
import ReusableModal from "./ReusableModal.vue";
import "ace-builds/src-noconflict/ace";
import "ace-builds/src-noconflict/theme-twilight";

export default {
  name: "ResumeForm",
  components: { ReusableModal },
  data() {
    return {
      resumeData: {
        name: "",
        title: "",
        contact: {
          email: "",
          phone: "",
          location: "",
          linkedin: "",
          github: "",
          website: "",
        },
        summary: "",
        experience: [],
        education: [],
        skills: [],
      },
      editor: null,
      view: "form",
      showModal: false,
      modalType: "",
      modalTitle: "",
      newEntry: {},
    };
  },
  methods: {
    submitForm() {
      this.$emit("submit", JSON.stringify(this.resumeData));
    },
    submitJson() {
      try {
        const parsedData = this.editor.get();
        this.$emit("submit", JSON.stringify(parsedData));
        this.resumeData = parsedData;
      } catch (error) {
        alert("Invalid JSON format");
      }
    },
    openModal(type) {
      this.showModal = true;
      this.modalType = type;
      this.modalTitle = `Add ${type.charAt(0).toUpperCase() + type.slice(1)}`;
      this.newEntry = {};
    },
    closeModal() {
      this.showModal = false;
      this.modalType = "";
      this.modalTitle = "";
      this.newEntry = {};
    },
    saveEntry() {
      if (this.modalType === "experience") {
        this.resumeData.experience.push(this.newEntry);
      } else if (this.modalType === "education") {
        this.resumeData.education.push(this.newEntry);
      } else if (this.modalType === "skill") {
        this.resumeData.skills.push(this.newEntry.skill);
      }
      this.closeModal();
    },
    removeExperience(index) {
      this.resumeData.experience.splice(index, 1);
    },
    removeEducation(index) {
      this.resumeData.education.splice(index, 1);
    },
    removeSkill(index) {
      this.resumeData.skills.splice(index, 1);
    },
    toggleView(view) {
      this.view = view;
      if (view === "json") {
        this.$nextTick(() => {
          const container = this.$refs.jsonEditor;
          this.editor = new JSONEditor(container, {
            modes: ["code", "form", "text", "tree", "view"], // Enable all modes
            ace: window.ace,
            theme: "ace/theme/twilight",
          });
          this.editor.set(this.resumeData);
        });
      }
    },
  },
};
</script>

<style scoped>
.text-yellow-500 {
  color: #ffd700;
}

.shadow-md {
  box-shadow: 8px 8px 0px #000;
}

.border {
  border-color: #000;
}

input {
  background-color: #030303;
  border: 1px solid whitesmoke;
  color: whitesmoke;
}
</style>
