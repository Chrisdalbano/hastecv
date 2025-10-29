<template>
  <div class="bg-primary-black text-whitesmoke font-OpenSans">
    <!-- Hero Section -->
    <section class="hero bg-primary-black text-whitesmoke">
      <div class="center px-4">
        <div class="hero-content">
         
          
          <h1 class="hero-title">
            Create Professional Resumes
            <span class="title-highlight">That Get Results</span>
          </h1>
          
          <p class="hero-description">
            Build ATS-optimized resumes with our intuitive editor. Choose from professional 
            themes, customize layouts, and export to PDF in minutes. No design skills required.
          </p>

          <div class="hero-actions">
            <button @click="navigateToApp" class="btn-primary">
              <span>Build Your Resume</span>
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                <path d="M7.5 15L12.5 10L7.5 5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>
            <button @click="scrollToExamples" class="btn-secondary">
              About HasteCV
            </button>
          </div>

          <div class="hero-stats">
            <div class="stat-item">
              <div class="stat-value">100%</div>
              <div class="stat-label">Free Forever</div>
            </div>
            <div class="stat-divider"></div>
            <div class="stat-item">
              <div class="stat-value">Customizable</div>
              <div class="stat-label">Themes</div>
            </div>
            <div class="stat-divider"></div>
            <div class="stat-item">
              <div class="stat-value">ATS</div>
              <div class="stat-label">Optimized</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section class="features" id="about-hastecv">
      <div class="center">
        <div class="section-header">
          <h2 class="section-title">Powerful Features</h2>
          <p class="section-description">
            Everything you need to create a standout resume
          </p>
        </div>

        <div class="features-grid">
          <div v-for="(feature, index) in features" :key="index" class="feature-card">
            <div class="feature-icon" :style="{ background: feature.gradient }">
              <component :is="feature.icon" />
            </div>
            <div class="feature-content">
              <h3 class="feature-title">{{ feature.title }}</h3>
              <p class="feature-description">{{ feature.description }}</p>
              <ul v-if="feature.benefits" class="feature-benefits">
                <li v-for="(benefit, i) in feature.benefits" :key="i">
                  <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                    <path d="M13.3333 4L6 11.3333L2.66667 8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  {{ benefit }}
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="how-it-works text-whitesmoke bg-gray-800 py-20">
      <div class="center">
        <h2 class="mb-12 text-center text-3xl font-bold text-haste-yellow">
          How HasteCV Works
        </h2>
        <ol class="mx-auto max-w-4xl list-inside space-y-8 text-left">
          <li>
            <h3 class="mb-2 text-2xl font-bold">Choose Your Template</h3>
            <p class="text-lg leading-relaxed">
              Begin by selecting a template that best suits the type of job you
              are applying for. HasteCV offers a couple of templates, giving you
              some flexibility to match your resume with your desired industry.
              Don't know how to start? Generate some 'Test Data' to get some
              inspiration.
            </p>
          </li>
          <li>
            <h3 class="mb-2 text-2xl font-bold">Customize Your CV</h3>
            <p class="text-lg leading-relaxed">
              Use our editor to manually input your personal details, work
              experience, and skills, or take advantage of JSON editing for
              advanced customization. Personalize every detail to stand out from
              the competition.
            </p>
          </li>
          <li>
            <h3 class="mb-2 text-2xl font-bold">
              Generated & Optimized for ATS
            </h3>
            <p class="text-lg leading-relaxed">
              When ready, click the GENERATE button to create your resume. With
              HasteCV, the structure of your resume will be automatically
              optimized for Applicant Tracking Systems (ATS). It structures your
              resume to pass through ATS scans effectively, ensuring it reaches
              hiring managers.
            </p>
          </li>
          <li>
            <h3 class="mb-2 text-2xl font-bold">Download & Apply</h3>
            <p class="text-lg leading-relaxed">
              Once satisfied with your CV, download it as a PDF. Your
              professionally crafted, ATS-ready CV is now ready to send out to
              potential employers and help you land that dream job.
            </p>
          </li>
        </ol>
      </div>
    </section>

    <!-- Additional Tips & Resources Section -->
    <section class="tips-resources text-whitesmoke py-20">
      <div class="center">
        <h2 class="mb-12 text-center text-3xl font-bold text-haste-yellow">
          Tips & Resources for a Winning CV
        </h2>
        <div class="mx-auto max-w-4xl space-y-8 text-left">
          <div>
            <h3 class="mb-2 text-2xl font-bold">Top CV Writing Tips</h3>
            <p class="text-lg leading-relaxed">
              Crafting a winning CV is about showcasing your experience and
              skills in a clear, concise manner. Here are some top tips:
            </p>
            <ul class="mt-2 list-inside list-disc space-y-2">
              <li>Focus on your achievements, not just duties.</li>
              <li>Keep it concise – one to two pages are ideal.</li>
              <li>
                Tailor your CV to the job description for every application.
              </li>
              <li>
                Use action verbs to describe your experience (e.g., led,
                improved, created).
              </li>
            </ul>
          </div>
          <!-- JSON Editor Info -->
          <div class="json-info-card">
            <div class="json-info-header">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
                <rect x="3" y="3" width="18" height="18" rx="2" stroke="currentColor" stroke-width="2"/>
                <path d="M8 8h8M8 12h8M8 16h4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
              </svg>
              <h3>Advanced JSON Editor</h3>
            </div>
            <p class="json-info-text">
              For developers and power users, our JSON editor provides programmatic control
              over your resume data. Perfect for automation, templating, or managing multiple variants.
            </p>
            <div class="json-info-features">
              <span class="feature-badge">Custom Fields</span>
              <span class="feature-badge">Import/Export</span>
              <span class="feature-badge">Git-Friendly</span>
              <span class="feature-badge">API Ready</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import { onMounted, defineComponent, h } from "vue";

const router = useRouter();

// Feature Icons as inline components
const ThemeIcon = defineComponent({
  render() {
    return h('svg', { width: '32', height: '32', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
      h('circle', { cx: '12', cy: '12', r: '3' }),
      h('path', { d: 'M12 1v6m0 6v6m8.66-5H15m-6 0H3m16.66-5.66l-4.24 4.24m-7.08 0L4.5 6.34m15.16 11.32l-4.24-4.24m-7.08 0L4.5 17.66' })
    ]);
  }
});

const LayoutIcon = defineComponent({
  render() {
    return h('svg', { width: '32', height: '32', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
      h('rect', { x: '3', y: '3', width: '18', height: '18', rx: '2' }),
      h('line', { x1: '3', y1: '9', x2: '21', y2: '9' }),
      h('line', { x1: '9', y1: '21', x2: '9', y2: '9' })
    ]);
  }
});

const EditIcon = defineComponent({
  render() {
    return h('svg', { width: '32', height: '32', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
      h('path', { d: 'M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7' }),
      h('path', { d: 'M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z' })
    ]);
  }
});

const DownloadIcon = defineComponent({
  render() {
    return h('svg', { width: '32', height: '32', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
      h('path', { d: 'M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4' }),
      h('polyline', { points: '7 10 12 15 17 10' }),
      h('line', { x1: '12', y1: '15', x2: '12', y2: '3' })
    ]);
  }
});

const PrivacyIcon = defineComponent({
  render() {
    return h('svg', { width: '32', height: '32', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
      h('path', { d: 'M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z' }),
      h('path', { d: 'M9 12l2 2 4-4' })
    ]);
  }
});

const ATSIcon = defineComponent({
  render() {
    return h('svg', { width: '32', height: '32', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
      h('polyline', { points: '22 12 18 12 15 21 9 3 6 12 2 12' }),
      h('circle', { cx: '12', cy: '12', r: '10' })
    ]);
  }
});

const features = [
  {
    title: "Professional Themes",
    description: "Choose from 5 carefully designed professional themes with perfect color contrast.",
    icon: ThemeIcon,
    gradient: 'linear-gradient(135deg, #1E3A8A, #3B82F6)',
    benefits: ['AAA accessibility', 'Industry-specific', 'Customizable colors']
  },
  {
    title: "Flexible Layouts",
    description: "Multiple layout options to match your industry and style preferences.",
    icon: LayoutIcon,
    gradient: 'linear-gradient(135deg, #881337, #BE123C)',
    benefits: ['Single/Multi-column', 'Grid layouts', 'Sidebar options']
  },
  {
    title: "Intuitive Editor",
    description: "Edit your resume with our user-friendly interface or use JSON for advanced control.",
    icon: EditIcon,
    gradient: 'linear-gradient(135deg, #0F766E, #14B8A6)',
    benefits: ['Visual editor', 'JSON support', 'Real-time preview']
  },
  {
    title: "Instant PDF Export",
    description: "Download professional PDF resumes optimized for both ATS systems and human readers.",
    icon: DownloadIcon,
    gradient: 'linear-gradient(135deg, #334155, #64748B)',
    benefits: ['High-quality PDFs', 'ATS-friendly', 'Instant download']
  },
  {
    title: "Complete Privacy",
    description: "Your data stays on your device. We don't collect, store, or share your information.",
    icon: PrivacyIcon,
    gradient: 'linear-gradient(135deg, #065F46, #059669)',
    benefits: ['No data collection', 'No sign-up required', '100% private']
  },
  {
    title: "ATS Optimized",
    description: "Resume structure automatically optimized to pass Applicant Tracking Systems.",
    icon: ATSIcon,
    gradient: 'linear-gradient(135deg, #7C2D12, #C2410C)',
    benefits: ['Keyword friendly', 'Proper formatting', 'Scannable structure']
  }
];

function navigateToApp() {
  router.push("/app");
}

function scrollToExamples() {
  document.getElementById('about-hastecv').scrollIntoView({ behavior: 'smooth' });
}

onMounted(() => {
  // Page animations
});
</script>

<script>
export default {
  useHead: {
    title: "HasteCV - Professional CV Builder",
    meta: [
      {
        name: "description",
        content:
          "Craft professional, ATS-ready resumes in minutes. HasteCV offers quick, easy, and free CV-building tools."
      },
      {
        name: "keywords",
        content:
          "resume builder, ATS resume, job application, CV builder, resume templates"
      },
      { property: "og:title", content: "HasteCV - Professional CV Builder" },
      {
        property: "og:description",
        content:
          "Create ATS-passing resumes with HasteCV, offering fast and free CV-building tools."
      }
    ]
  }
};
</script>

<style scoped>
.center {
  width: min(100% - 2rem, 1200px);
  margin-inline: auto;
  padding-inline: 1rem;
}

/* Hero Section Styling */
.hero {
  background: var(--primary-black);
  position: relative;
  padding: 5rem 0 6rem;
  overflow: hidden;
}

.hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100%;
  max-width: 1400px;
  height: 100%;
  background: radial-gradient(ellipse at top, rgba(var(--haste-primary-rgb), 0.15), transparent 50%);
  pointer-events: none;
}

.hero-content {
  position: relative;
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: var(--gray-800);
  border: 1px solid var(--border-color);
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--gray-300);
  width: fit-content;
  margin: 0 auto;
}

.badge-dot {
  width: 8px;
  height: 8px;
  background: var(--haste-primary);
  border-radius: 50%;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.hero-title {
  font-size: clamp(2.5rem, 5vw, 4rem);
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -0.02em;
  color: white;
  margin: 0;
}

.title-highlight {
  display: block;
  background: var(--haste-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-description {
  font-size: 1.125rem;
  line-height: 1.7;
  color: var(--gray-300);
  max-width: 600px;
  margin: 0 auto;
}

.hero-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.btn-primary {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem 2rem;
  background: var(--haste-primary);
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 12px rgba(var(--haste-primary-rgb), 0.3);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(var(--haste-primary-rgb), 0.4);
}

.btn-primary:active {
  transform: translateY(0);
}

.btn-secondary {
  padding: 1rem 2rem;
  background: transparent;
  color: white;
  border: 2px solid var(--border-color);
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-secondary:hover {
  border-color: var(--haste-primary);
  color: var(--haste-primary);
  background: rgba(var(--haste-primary-rgb), 0.1);
}

.hero-stats {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  padding: 2rem;
  background: var(--gray-900);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  flex-wrap: wrap;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25rem;
}

.stat-value {
  font-size: 1.75rem;
  font-weight: 700;
  color: var(--haste-primary);
  line-height: 1;
}

.stat-label {
  font-size: 0.875rem;
  color: var(--gray-400);
  font-weight: 500;
}

.stat-divider {
  width: 1px;
  height: 40px;
  background: var(--border-color);
}

/* Features Section */
.features {
  padding: 5rem 0;
  background: var(--gray-900);
}

.section-header {
  text-align: center;
  margin-bottom: 3rem;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: white;
  margin: 0 0 1rem;
  letter-spacing: -0.02em;
}

.section-description {
  font-size: 1.125rem;
  color: var(--gray-400);
  max-width: 600px;
  margin: 0 auto;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 1.5rem;
}

.feature-card {
  background: var(--gray-800);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.feature-card:hover {
  transform: translateY(-4px);
  border-color: var(--haste-primary);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
}

.feature-icon {
  width: 56px;
  height: 56px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.feature-content {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  flex: 1;
}

.feature-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: white;
  margin: 0;
  letter-spacing: -0.01em;
}

.feature-description {
  font-size: 0.9375rem;
  color: var(--gray-400);
  line-height: 1.6;
  margin: 0;
}

.feature-benefits {
  list-style: none;
  padding: 0;
  margin: 0.5rem 0 0;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.feature-benefits li {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  color: var(--gray-300);
}

.feature-benefits li svg {
  flex-shrink: 0;
  color: var(--haste-primary);
}

@media (max-width: 768px) {
  .features-grid {
    grid-template-columns: 1fr;
  }
  
  .section-title {
    font-size: 2rem;
  }
  
  .hero-title {
    font-size: 2.5rem;
  }
  
  .hero-stats {
    gap: 1rem;
  }
  
  .stat-divider {
    display: none;
  }
}

/* How-it-works section styling */
.how-it-works {
  padding: 2rem;
  background: var(--primary-black);
  color: whitesmoke;
  border-top: 2px solid var(--haste-yellow);
}

.how-it-works ol {
  counter-reset: step-counter;
}

.how-it-works li {
  position: relative;
  padding-left: 2.5rem;
}

.how-it-works li::before {
  content: counter(step-counter);
  counter-increment: step-counter;
  position: absolute;
  left: 0;
  top: 0;
  width: 2rem;
  height: 2rem;
  background-color: var(--haste-yellow);
  color: var(--primary-black);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
}

/* Tips & Resources Section Styling */
.tips-resources {
  padding: 2rem;
  background: var(--primary-black);
  color: whitesmoke;
  border-top: 2px solid var(--haste-yellow);
}

.tips-resources .list-disc li a {
  color: var(--haste-yellow);
  text-decoration: none;
  transition: color 0.3s;
}

.tips-resources .list-disc li a:hover {
  text-decoration: underline;
}

/* JSON Info Card */
.json-info-card {
  margin-top: 2rem;
  padding: 2rem;
  background: var(--gray-900);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.json-info-header {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.json-info-header svg {
  color: var(--haste-primary);
  flex-shrink: 0;
}

.json-info-header h3 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 700;
  color: white;
}

.json-info-text {
  margin: 0;
  font-size: 1rem;
  color: var(--gray-400);
  line-height: 1.6;
}

.json-info-features {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.feature-badge {
  padding: 0.5rem 1rem;
  background: rgba(var(--haste-primary-rgb), 0.1);
  border: 1px solid rgba(var(--haste-primary-rgb), 0.3);
  border-radius: 6px;
  color: var(--haste-primary);
  font-size: 0.875rem;
  font-weight: 600;
}

@media (max-width: 768px) {
  .json-info-card {
    padding: 1.5rem;
  }
  
  .json-info-header {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
