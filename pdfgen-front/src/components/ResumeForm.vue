<template>
  <div class="p-6 bg-white shadow-md rounded-lg">
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-2xl font-bold">Resume Builder</h2>
      <label class="switch">
        <input type="checkbox" v-model="showForm" />
        <span class="slider round">
          <span class="label-text manual" v-show="showForm">Manual</span>
          <span class="label-text json" v-show="!showForm">JSON</span>
        </span>
      </label>
    </div>

    <transition name="fade">
      <form v-show="showForm" @submit.prevent="submitForm" class="space-y-6">
        <h2 class="text-xl font-semibold">Personal Information</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <input
            v-model="resumeData.name"
            class="w-full p-2 border rounded"
            type="text"
            placeholder="Name"
          />
          <input
            v-model="resumeData.title"
            class="w-full p-2 border rounded"
            type="text"
            placeholder="Title"
          />
        </div>

        <h2 class="text-xl font-semibold">Contact Information</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <input
            v-model="resumeData.contact.email"
            class="w-full p-2 border rounded"
            type="email"
            placeholder="Email"
          />
          <input
            v-model="resumeData.contact.phone"
            class="w-full p-2 border rounded"
            type="tel"
            placeholder="Phone"
          />
          <input
            v-model="resumeData.contact.location"
            class="w-full p-2 border rounded"
            type="text"
            placeholder="Location"
          />
          <input
            v-model="resumeData.contact.linkedin"
            class="w-full p-2 border rounded"
            type="text"
            placeholder="LinkedIn"
          />
          <input
            v-model="resumeData.contact.github"
            class="w-full p-2 border rounded"
            type="text"
            placeholder="GitHub"
          />
          <input
            v-model="resumeData.contact.website"
            class="w-full p-2 border rounded"
            type="text"
            placeholder="Website"
          />
        </div>

        <h2 class="text-xl font-semibold">Summary</h2>
        <textarea
          v-model="resumeData.summary"
          class="w-full p-2 border rounded"
          rows="4"
          placeholder="Summary"
        ></textarea>

        <h2 class="text-xl font-semibold">Experience</h2>
        <div
          v-for="(exp, index) in resumeData.experience"
          :key="index"
          class="mb-4 relative"
        >
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <input
              v-model="exp.position"
              class="w-full p-2 border rounded mb-2"
              type="text"
              placeholder="Position"
            />
            <input
              v-model="exp.company"
              class="w-full p-2 border rounded mb-2"
              type="text"
              placeholder="Company"
            />
            <input
              v-model="exp.dates"
              class="w-full p-2 border rounded mb-2"
              type="text"
              placeholder="Dates"
            />
          </div>
          <textarea
            v-model="exp.responsibilities"
            class="w-full p-2 border rounded mb-2"
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
        <button
          @click.prevent="addExperience"
          class="bg-gray-200 text-gray-700 p-2 rounded mt-2"
        >
          Add Experience
        </button>

        <h2 class="text-xl font-semibold">Education</h2>
        <div
          v-for="(edu, index) in resumeData.education"
          :key="index"
          class="mb-4 relative"
        >
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <input
              v-model="edu.degree"
              class="w-full p-2 border rounded mb-2"
              type="text"
              placeholder="Degree"
            />
            <input
              v-model="edu.institution"
              class="w-full p-2 border rounded mb-2"
              type="text"
              placeholder="Institution"
            />
            <input
              v-model="edu.dates"
              class="w-full p-2 border rounded mb-2"
              type="text"
              placeholder="Dates"
            />
          </div>
          <button
            @click.prevent="removeEducation(index)"
            class="absolute top-0 right-0 bg-red-500 text-white p-1 rounded-full"
          >
            x
          </button>
        </div>
        <button
          @click.prevent="addEducation"
          class="bg-gray-200 text-gray-700 p-2 rounded mt-2"
        >
          Add Education
        </button>

        <h2 class="text-xl font-semibold">Skills</h2>
        <div
          v-for="(skill, index) in resumeData.skills"
          :key="index"
          class="mb-4 relative"
        >
          <input
            v-model="resumeData.skills[index]"
            class="w-full p-2 border rounded mb-2"
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
          @click.prevent="addSkill"
          class="bg-gray-200 text-gray-700 p-2 rounded mt-2"
        >
          Add Skill
        </button>

        <button type="submit" class="bg-blue-500 text-white p-2 rounded mt-4">
          Generate Preview
        </button>
      </form>
    </transition>

    <transition name="fade">
      <div v-show="!showForm" class="mt-8">
        <h2 class="text-xl font-semibold mb-4">Or Paste JSON Data</h2>
        <div ref="jsonEditor" class="border rounded h-64"></div>
        <button
          @click="submitJson"
          class="bg-blue-500 text-white p-2 rounded mt-2"
        >
          Generate PDF from JSON
        </button>
      </div>
    </transition>
  </div>
</template>

<script>
import JSONEditor from "jsoneditor";
import "jsoneditor/dist/jsoneditor.css";

export default {
  name: "ResumeForm",
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
      showForm: true,
      editor: null,
    };
  },
  methods: {
    submitForm() {
      this.$emit("submit", JSON.stringify(this.resumeData));
      this.$emit("input", JSON.stringify(this.resumeData));
    },
    submitJson() {
      try {
        const parsedData = this.editor.get();
        this.$emit("submit", JSON.stringify(parsedData));
        this.$emit("input", JSON.stringify(parsedData));
      } catch (error) {
        alert("Invalid JSON format");
      }
    },
    addExperience() {
      this.resumeData.experience.push({
        position: "",
        company: "",
        dates: "",
        responsibilities: "",
      });
    },
    removeExperience(index) {
      this.resumeData.experience.splice(index, 1);
    },
    addEducation() {
      this.resumeData.education.push({
        degree: "",
        institution: "",
        dates: "",
      });
    },
    removeEducation(index) {
      this.resumeData.education.splice(index, 1);
    },
    addSkill() {
      this.resumeData.skills.push("");
    },
    removeSkill(index) {
      this.resumeData.skills.splice(index, 1);
    },
  },
  mounted() {
    const container = this.$refs.jsonEditor;
    this.editor = new JSONEditor(container, {
      modes: ["code", "form", "text", "tree", "view"], // Enable all modes
    });
    this.editor.set(this.resumeData);
  },
};
</script>

<style scoped>
/* Add any scoped styles for ResumeForm component here */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
  opacity: 0;
}

/* Toggle Switch */
.switch {
  position: relative;
  display: inline-block;
  width: 80px;
  height: 34px;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #995757;
  transition: 0.4s;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  color: white;
  font-weight: bold;
  
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  transition: 0.4s;
}

input:checked + .slider {
  background-color: #2196f3;
}

input:checked + .slider:before {
  transform: translateX(46px);
}

.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}

.label-text {
  position: absolute;
  font-size: 12px;
  color: white;
  font-weight: bold;
}

.manual {
  left: 4px;
}

.json {
  right: 4px;
}
</style>
