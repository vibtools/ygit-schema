import type { Config } from 'tailwindcss';

export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        background: 'var(--color-background)',
        canvas: 'var(--color-canvas)',
        surface: 'var(--color-surface)',
        'surface-hover': 'var(--color-surface-hover)',
        border: 'var(--color-border)',
        primary: 'var(--color-primary)',
        accent: 'var(--color-accent)',
        success: 'var(--color-success)',
        warning: 'var(--color-warning)',
        danger: 'var(--color-danger)',
        text: 'var(--color-text)',
        content: 'var(--color-text-content)',
        muted: 'var(--color-text-secondary)',
      },
      fontFamily: {
        sans: ['Inter Variable', 'Inter', 'sans-serif'],
        mono: ['JetBrains Mono Variable', 'JetBrains Mono', 'monospace'],
      },
      fontSize: {
        xs: ['var(--text-xs)', { lineHeight: '1.45' }],
        sm: ['var(--text-sm)', { lineHeight: '1.5' }],
        md: ['var(--text-md)', { lineHeight: '1.55' }],
        base: ['var(--text-base)', { lineHeight: '1.65' }],
        h3: ['var(--text-h3)', { lineHeight: '1.4' }],
        lg: ['var(--text-h2)', { lineHeight: '1.35' }],
        '2xl': ['var(--text-h1)', { lineHeight: '1.3' }],
      },
      borderRadius: {
        button: 'var(--radius-sm)',
        code: 'var(--radius-md)',
        card: 'var(--radius-lg)',
      },
      maxWidth: {
        page: 'var(--page-width)',
        content: 'var(--content-width)',
      },
    },
  },
} satisfies Config;
