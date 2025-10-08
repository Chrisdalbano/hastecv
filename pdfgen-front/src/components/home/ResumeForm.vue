<template>
  <div class="form-wrapper">
    <!-- Form Container -->
    <form @submit.prevent="generatePdf" class="form-container">
      <!-- Personal Info Section -->
      <div class="form-section">
        <h3 class="section-title">Personal Information</h3>
        <div class="input-grid">
          <div class="input-group">
            <label for="name-input" class="input-label">Full Name</label>
            <input
              v-model="store.resumeData.name"
              id="name-input"
              type="text"
              class="form-input"
              placeholder="John Doe"
            />
          </div>

          <div class="input-group">
            <label for="title-input" class="input-label">Job Title</label>
            <input
              v-model="store.resumeData.title"
              id="title-input"
              type="text"
              class="form-input"
              placeholder="Software Engineer"
            />
          </div>

          <div class="input-group">
            <label for="email-input" class="input-label">Email</label>
            <input
              v-model="store.resumeData.contact.email"
              id="email-input"
              type="email"
              class="form-input"
              placeholder="john@example.com"
            />
          </div>

          <div class="input-group">
            <label for="phone-input" class="input-label">Phone</label>
            <input
              v-model="store.resumeData.contact.phone"
              id="phone-input"
              type="tel"
              class="form-input"
              placeholder="(555) 123-4567"
            />
          </div>

          <div class="input-group">
            <label for="location-input" class="input-label">Location</label>
            <input
              v-model="store.resumeData.contact.location"
              id="location-input"
              type="text"
              class="form-input"
              placeholder="New York, USA"
            />
          </div>

          <div class="input-group">
            <label for="website-input" class="input-label">Website</label>
            <input
              v-model="store.resumeData.contact.website"
              id="website-input"
              type="url"
              class="form-input"
              placeholder="https://johndoe.com"
            />
          </div>
        </div>
      </div>

      <!-- Summary Section -->
      <div class="form-section">
        <h3 class="section-title">Professional Summary</h3>
        <div class="input-group">
          <label for="summary-input" class="input-label">Summary</label>
          <textarea
            v-model="store.resumeData.summary"
            id="summary-input"
            rows="4"
            class="form-textarea"
            placeholder="Write a brief professional summary..."
          ></textarea>
        </div>
      </div>

      <!-- Experience Section -->
      <div class="form-section">
        <div class="section-header">
          <h3 class="section-title">Work Experience</h3>
          <button @click.prevent="openModal('experience')" class="add-button">
            + Add Experience
          </button>
        </div>

        <div
          v-for="(exp, index) in store.resumeData.experience"
          :key="index"
          class="entry-card"
        >
          <button
            @click.prevent="removeExperience(index)"
            class="remove-button"
            title="Remove"
          >
            ×
          </button>

          <div class="input-grid">
            <div class="input-group">
              <label class="input-label">Position</label>
              <input
                v-model="exp.position"
                type="text"
                class="form-input"
                placeholder="Senior Developer"
              />
            </div>

            <div class="input-group">
              <label class="input-label">Company</label>
              <input
                v-model="exp.company"
                type="text"
                class="form-input"
                placeholder="Tech Corp"
              />
            </div>

            <div class="input-group">
              <label class="input-label">Dates</label>
              <input
                v-model="exp.dates"
                type="text"
                class="form-input"
                placeholder="Jan 2020 - Present"
              />
            </div>

            <div class="input-group">
              <label class="input-label">Location</label>
              <input
                v-model="exp.location"
                type="text"
                class="form-input"
                placeholder="Remote"
              />
            </div>
          </div>

          <div class="input-group mt-4">
            <label class="input-label">Responsibilities</label>
            <textarea
              v-model="exp.responsibilities"
              rows="4"
              class="form-textarea"
              placeholder="• Led a team of developers&#10;• Built scalable applications&#10;• Improved performance by 40%"
            ></textarea>
          </div>

          <div class="input-group mt-4">
            <label class="input-label">Technologies</label>
            <input
              v-model="exp.technologies"
              type="text"
              class="form-input"
              placeholder="React, Node.js, AWS"
            />
          </div>
        </div>

        <div v-if="store.resumeData.experience.length === 0" class="empty-message">
          No work experience added yet. Click "+ Add Experience" to get started.
        </div>
      </div>

      <!-- Education Section -->
      <div class="form-section">
        <div class="section-header">
          <h3 class="section-title">Education</h3>
          <button @click.prevent="openModal('education')" class="add-button">
            + Add Education
          </button>
        </div>

        <div
          v-for="(edu, index) in store.resumeData.education"
          :key="index"
          class="entry-card"
        >
          <button
            @click.prevent="removeEducation(index)"
            class="remove-button"
            title="Remove"
          >
            ×
          </button>

          <div class="input-grid">
            <div class="input-group">
              <label class="input-label">Degree</label>
              <input
                v-model="edu.degree"
                type="text"
                class="form-input"
                placeholder="Bachelor of Science"
              />
            </div>

            <div class="input-group">
              <label class="input-label">Institution</label>
              <input
                v-model="edu.institution"
                type="text"
                class="form-input"
                placeholder="University Name"
              />
            </div>

            <div class="input-group">
              <label class="input-label">Dates</label>
              <input
                v-model="edu.dates"
                type="text"
                class="form-input"
                placeholder="2016 - 2020"
              />
            </div>

            <div class="input-group">
              <label class="input-label">Location</label>
              <input
                v-model="edu.location"
                type="text"
                class="form-input"
                placeholder="New York, USA"
              />
            </div>
          </div>
        </div>

        <div v-if="store.resumeData.education.length === 0" class="empty-message">
          No education added yet. Click "+ Add Education" to get started.
        </div>
      </div>

      <!-- Skills Section -->
      <div class="form-section">
        <div class="section-header">
          <h3 class="section-title">Skills</h3>
          <button @click.prevent="addSkill" class="add-button">
            + Add Skill
          </button>
        </div>

        <div class="skills-grid">
          <div
            v-for="(skill, index) in store.resumeData.skills"
            :key="index"
            class="skill-item"
          >
            <input
              v-model="store.resumeData.skills[index]"
              type="text"
              class="form-input"
              placeholder="JavaScript"
            />
            <button
              @click.prevent="removeSkill(index)"
              class="skill-remove"
              title="Remove"
            >
              ×
            </button>
          </div>
        </div>

        <div v-if="store.resumeData.skills.length === 0" class="empty-message">
          No skills added yet. Click "+ Add Skill" to get started.
        </div>
      </div>
    </form>

    <!-- Modal for Adding Entries -->
    <ReusableModal
      :show="showModal"
      :title="modalTitle"
      @close="closeModal"
      @save="saveEntry"
    >
      <!-- Education Modal Content -->
      <div v-if="modalType == 'education'" class="modal-form">
        <div class="input-group">
          <label class="input-label">Degree</label>
          <input
            v-model="newEntry.degree"
            type="text"
            class="form-input"
            placeholder="Bachelor of Science in Computer Science"
          />
        </div>

        <div class="input-group">
          <label class="input-label">Institution</label>
          <input
            v-model="newEntry.institution"
            type="text"
            class="form-input"
            placeholder="University Name"
          />
        </div>

        <div class="input-group">
          <label class="input-label">Dates</label>
          <input
            v-model="newEntry.dates"
            type="text"
            class="form-input"
            placeholder="2016 - 2020"
          />
        </div>

        <div class="input-group">
          <label class="input-label">Location</label>
          <input
            v-model="newEntry.location"
            type="text"
            class="form-input"
            placeholder="New York, USA"
          />
        </div>
      </div>

      <!-- Experience Modal Content -->
      <div v-else-if="modalType == 'experience'" class="modal-form">
        <div class="input-group">
          <label class="input-label">Position</label>
          <input
            v-model="newEntry.position"
            type="text"
            class="form-input"
            placeholder="Senior Software Engineer"
          />
        </div>

        <div class="input-group">
          <label class="input-label">Company</label>
          <input
            v-model="newEntry.company"
            type="text"
            class="form-input"
            placeholder="Tech Corporation"
          />
        </div>

        <div class="input-group">
          <label class="input-label">Dates</label>
          <input
            v-model="newEntry.dates"
            type="text"
            class="form-input"
            placeholder="Jan 2020 - Present"
          />
        </div>

        <div class="input-group">
          <label class="input-label">Location</label>
          <input
            v-model="newEntry.location"
            type="text"
            class="form-input"
            placeholder="Remote - New York"
          />
        </div>

        <div class="input-group">
          <label class="input-label">Responsibilities</label>
          <textarea
            v-model="newEntry.responsibilities"
            rows="4"
            class="form-textarea"
            placeholder="• Built scalable web applications&#10;• Led a team of developers&#10;• Improved performance metrics"
          ></textarea>
        </div>

        <div class="input-group">
          <label class="input-label">Technologies</label>
          <input
            v-model="newEntry.technologies"
            type="text"
            class="form-input"
            placeholder="React, Node.js, PostgreSQL, AWS"
          />
        </div>
      </div>
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

function generatePdf() {
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
    store.resumeData.experience.push({ ...newEntry.value });
  } else if (modalType.value === "education") {
    store.resumeData.education.push({ ...newEntry.value });
  }
  closeModal();
}

function addSkill() {
  store.resumeData.skills.push("");
}

function removeSkill(index) {
  store.resumeData.skills.splice(index, 1);
}

function removeExperience(index) {
  store.resumeData.experience.splice(index, 1);
}

function removeEducation(index) {
  store.resumeData.education.splice(index, 1);
}
</script>

<style scoped>
.form-wrapper {
  height: 100%;
  overflow-y: auto;
}

.form-container {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

/* Form Sections */
.form-section {
  background: var(--gray-800);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 1.5rem;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.section-title {
  margin: 0 0 1.5rem 0;
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--haste-primary);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.section-header .section-title {
  margin: 0;
}

/* Input Grid */
.input-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}

.input-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.input-label {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--gray-300);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* Form Inputs */
.form-input,
.form-textarea {
  padding: 0.75rem;
  background: var(--gray-900);
  color: white;
  border: 1px solid var(--border-color);
  border-radius: 6px;
  font-size: 0.9375rem;
  font-family: 'OpenSans', sans-serif;
  transition: all 0.2s;
  outline: none;
}

.form-input:focus,
.form-textarea:focus {
  border-color: var(--haste-primary);
  background: var(--gray-800);
  box-shadow: 0 0 0 3px rgba(var(--haste-primary-rgb), 0.1);
}

.form-input::placeholder,
.form-textarea::placeholder {
  color: var(--gray-500);
}

.form-textarea {
  resize: vertical;
  font-family: 'OpenSans', monospace;
  line-height: 1.6;
}

/* Add Button */
.add-button {
  padding: 0.625rem 1.25rem;
  background: transparent;
  color: var(--haste-primary);
  border: 2px solid var(--haste-primary);
  border-radius: 6px;
  font-weight: 700;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.add-button:hover {
  background: var(--haste-primary);
  color: white;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(var(--haste-primary-rgb), 0.3);
}

/* Entry Cards */
.entry-card {
  position: relative;
  background: var(--gray-900);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 1.5rem;
  margin-bottom: 1rem;
  transition: all 0.2s;
}

.entry-card:hover {
  border-color: var(--haste-primary);
  box-shadow: 0 0 0 1px var(--haste-primary);
}

.remove-button {
  position: absolute;
  top: 1rem;
  right: 1rem;
  width: 32px;
  height: 32px;
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
  border: 1px solid rgba(239, 68, 68, 0.3);
  border-radius: 4px;
  font-size: 1.5rem;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
  line-height: 1;
}

.remove-button:hover {
  background: #ef4444;
  color: white;
  border-color: #ef4444;
}

/* Skills Grid */
.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
}

.skill-item {
  position: relative;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.skill-remove {
  width: 28px;
  height: 28px;
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
  border: 1px solid rgba(239, 68, 68, 0.3);
  border-radius: 4px;
  font-size: 1.25rem;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.2s;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  line-height: 1;
}

.skill-remove:hover {
  background: #ef4444;
  color: white;
  border-color: #ef4444;
}

/* Empty Message */
.empty-message {
  text-align: center;
  padding: 2rem;
  color: var(--gray-400);
  font-size: 0.9375rem;
  font-style: italic;
}

/* Modal Form */
.modal-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

/* Utility Classes */
.mt-4 {
  margin-top: 1rem;
}

/* Scrollbar */
.form-wrapper::-webkit-scrollbar {
  width: 8px;
}

.form-wrapper::-webkit-scrollbar-track {
  background: var(--gray-900);
}

.form-wrapper::-webkit-scrollbar-thumb {
  background: var(--haste-primary);
  border-radius: 4px;
}

.form-wrapper::-webkit-scrollbar-thumb:hover {
  background: var(--haste-primary);
  filter: brightness(1.2);
}

/* Responsive */
@media (max-width: 768px) {
  .form-container {
    padding: 1rem;
    gap: 1.5rem;
  }

  .form-section {
    padding: 1rem;
  }

  .input-grid {
    grid-template-columns: 1fr;
  }

  .skills-grid {
    grid-template-columns: 1fr;
  }

  .section-header {
    flex-direction: column;
    align-items: stretch;
    gap: 1rem;
  }

  .add-button {
    width: 100%;
  }
}
</style>
