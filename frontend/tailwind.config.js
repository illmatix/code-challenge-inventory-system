/** @type {import('tailwindcss').Config} */
module.exports = {
    darkMode: 'class',
    content: [
        './index.html', // Ensure Tailwind scans your index.html
        './src/components/*.{vue,js,ts,jsx,tsx}',
        './src/views/*.{vue,js,ts,jsx,tsx}',
        './src/layouts/*.{vue,js,ts,jsx,tsx}',
    ],
    theme: {
        extend: {
            colors: {
                // Light mode colors
                light: {
                    background: '#ffffff',
                    text: '#1f2937',
                    primary: '#3b82f6',
                    secondary: '#64748b',
                    accent: '#10b981',
                    muted: '#e5e7eb',
                },
                // Dark mode colors
                dark: {
                    background: '#1f2937',
                    text: '#e5e7eb',
                    primary: '#3b82f6',
                    secondary: '#9ca3af',
                    accent: '#10b981',
                    muted: '#374151',
                },
            }
        },
    },
    variants: {
        extend: {
            textColor: ['dark'], // Enable `dark:text-*` utilities
            backgroundColor: ['dark'], // Enable `dark:bg-*` utilities
        },
    },
    plugins: [
        // Add Tailwind UI plugin here
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
};
