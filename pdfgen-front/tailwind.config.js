/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      fontFamily: {
        'open-sans': ['OpenSans', 'sans-serif'],
        'cardo' : ['Cardo', 'serif'],
      },
    },
  },
  plugins: [
    function({ addUtilities }) {
      const newUtilities = {
        '.text-haste-yellow': {
          color: 'var(--haste-yellow)',
        },
        '.bg-haste-yellow': {
          backgroundColor: '#ffd510',
        },
        '.border-haste-yellow': {
          borderColor: 'var(--haste-yellow)',
        },
      };

      addUtilities(newUtilities, ['responsive', 'hover']);
    }
  ],
};
