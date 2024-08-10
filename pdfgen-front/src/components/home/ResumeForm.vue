<template>
  <div class="py-4">
    <div class="mb-4 flex items-center"></div>
  </div>

  <div class="py-4">
      <form @submit.prevent="submitForm">
        <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
          <input
            v-model="store.resumeData.name"
            class="w-full p-2"
            type="text"
            placeholder="Name"
          />
          <input
            v-model="store.resumeData.title"
            class="w-full p-2"
            type="text"
            placeholder="Title"
          />
        </div>

        <div class="mt-10 grid grid-cols-1 gap-4 md:grid-cols-2">
          <input
            v-model="store.resumeData.contact.email"
            class="w-full p-2"
            type="email"
            placeholder="Email"
          />
          <input
            v-model="store.resumeData.contact.phone"
            class="w-full p-2"
            type="tel"
            placeholder="Phone"
          />
          <input
            v-model="store.resumeData.contact.location"
            class="w-full p-2"
            type="text"
            placeholder="Location"
          />

          <input
            v-model="store.resumeData.contact.website"
            class="w-full p-2"
            type="text"
            placeholder="Website"
          />
        </div>

        <textarea
          v-model="store.resumeData.summary"
          class="mt-10 w-full p-2 text-3xl font-bold"
          rows="4"
          placeholder="Summary"
        ></textarea>

        <div
          v-for="(exp, index) in store.resumeData.experience"
          :key="index"
          class="relative mb-4"
        >
          <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
            <input
              v-model="exp.position"
              class="mb-2 w-full p-2"
              type="text"
              placeholder="Position"
            />
            <input
              v-model="exp.company"
              class="mb-2 w-full p-2"
              type="text"
              placeholder="Company"
            />
            <input
              v-model="exp.dates"
              class="mb-2 w-full p-2"
              type="text"
              placeholder="Dates"
            />
          </div>
          <textarea
            v-model="exp.responsibilities"
            class="mb-2 w-full p-2"
            rows="3"
            placeholder="Responsibilities"
          ></textarea>
          <button
            @click.prevent="removeExperience(index)"
            class="absolute right-0 top-0 rounded-full bg-red-500 p-1 text-white"
          >
            x
          </button>
        </div>
        <div class="flex flex-wrap items-center text-center">
          <button @click.prevent="openModal('experience')" class="haste-option">
            + Experience
          </button>

          <div
            v-for="(edu, index) in store.resumeData.education"
            :key="index"
            class="relative mb-4"
          >
            <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
              <input
                v-model="edu.degree"
                class="mb-2 w-full p-2"
                type="text"
                placeholder="Degree"
              />
              <input
                v-model="edu.institution"
                class="mb-2 w-full p-2"
                type="text"
                placeholder="Institution"
              />
              <input
                v-model="edu.dates"
                class="mb-2 w-full p-2"
                type="text"
                placeholder="Dates"
              />
            </div>
            <button
              @click.prevent="removeEducation(index)"
              class="absolute right-0 top-0 mx-2 rounded-full bg-red-500 p-1 text-white"
            >
              x
            </button>
          </div>
          <button @click.prevent="openModal('education')" class="haste-option">
            + Education
          </button>

          <div
            v-for="(skill, index) in store.resumeData.skills"
            :key="index"
            class="relative mb-4"
          >
            <input
              v-model="store.resumeData.skills[index]"
              class="mb-2 w-full p-2"
              type="text"
              placeholder="Skill"
            />
            <button
              @click.prevent="removeSkill(index)"
              class="absolute right-0 top-0 rounded-full bg-red-500 p-1 text-white"
            >
              x
            </button>
          </div>
          <button @click.prevent="addSkill" class="haste-option">
            + Skill
          </button>
          <button type="submit" class="haste-button">Generate</button>
        </div>

      </form>

   

    <ReusableModal
      :show="showModal"
      :title="modalTitle"
      @close="closeModal"
      @save="saveEntry"
    >
      <template v-if="modalType === 'experience'">
        <input
          v-model="newEntry.position"
          class="mb-2 w-full p-2"
          type="text"
          placeholder="Position"
        />
        <input
          v-model="newEntry.company"
          class="mb-2 w-full p-2"
          type="text"
          placeholder="Company"
        />
        <input
          v-model="newEntry.dates"
          class="mb-2 w-full p-2"
          type="text"
          placeholder="Dates"
        />
        <textarea
          v-model="newEntry.responsibilities"
          class="mb-2 w-full p-2"
          rows="3"
          placeholder="Responsibilities"
        ></textarea>
      </template>
      <template v-if="modalType === 'education'">
        <input
          v-model="newEntry.degree"
          class="mb-2 w-full p-2"
          type="text"
          placeholder="Degree"
        />
        <input
          v-model="newEntry.institution"
          class="mb-2 w-full p-2"
          type="text"
          placeholder="Institution"
        />
        <input
          v-model="newEntry.dates"
          class="mb-2 w-full p-2"
          type="text"
          placeholder="Dates"
        />
      </template>
    </ReusableModal>
  </div>
</template>

<script setup>
import { useResumeDataStore } from "@/stores/resumeData";
import { ref } from "vue";

import ReusableModal from "@/components/ReusableModal.vue";

const store = useResumeDataStore();
const showModal = ref(false);
const modalType = ref("");
const modalTitle = ref("");
const newEntry = ref({});

function submitForm() {
  store.generatePdf(JSON.stringify(store.resumeData));
}

function openModal(type) {
  showModal.value = true;
  modalType.value = type;
  modalTitle.value = `Add ${type.charAt(0).toUpperCase() + type.slice(1)}`;
  newEntry.value = {};
}
function closeModal() {
  showModal.value = false;
  modalType.value = "";
  modalTitle.value = "";
  newEntry.value = {};
}
function saveEntry() {
  if (modalType.value === "experience") {
    store.resumeData.experience.push(newEntry.value);
  } else if (modalType.value === "education") {
    store.resumeData.education.push(newEntry.value);
  }
  closeModal();
}

function addSkill() {
  store.resumeData.skills.push(newEntry.value.skill);
}

function removeExperience(index) {
  store.resumeData.experience.splice(index, 1);
}
function removeEducation(index) {
  store.resumeData.education.splice(index, 1);
}
function removeSkill(index) {
  store.resumeData.skills.splice(index, 1);
}
</script>

<style scoped></style>
