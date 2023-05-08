/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["templates/*.j2"],
  theme: {
    extend: {
      colors: {
        "primary-bg": "var(--primary-background)",
        "secondary-bg": "var(--secondary-background)",
        "primary-text": "var(--primary-text)",
        "secondary-text": "var(--secondary-text)",
      },
      fontFamily: {
        sans: "SB Body, system-ui, sans-serif",
        heading: "SB Heading, system-ui, sans-serif",
      },
    },
  },
  plugins: [],
};
