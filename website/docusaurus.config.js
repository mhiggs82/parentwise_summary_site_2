// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import { themes as prismThemes } from 'prism-react-renderer';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'ParentWise Actionable Summary Guides',
  tagline: 'Actionable summaries for modern parents',
  favicon: 'img/sophia-logo-white.svg',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: 'https://summaries.getparentwise.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For custom domains, use '/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'mhiggs82', // Usually your GitHub org/user name.
  projectName: 'parentwise_summary_site', // Usually your repo name.

  onBrokenLinks: 'throw',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
          // Useful options to enforce blogging best practices
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      colorMode: {
        defaultMode: 'dark',
        disableSwitch: true,
        respectPrefersColorScheme: false,
      },
      docs: {
        sidebar: {
          hideable: true,
          autoCollapseCategories: true,
        },
      },
      navbar: {
        title: 'ParentWise',
        logo: {
          alt: 'ParentWise Logo',
          src: 'img/sophia-logo-white.svg',
        },
        items: [
          {
            label: 'Library',
            position: 'left',
            items: [
              { label: 'Summaries', to: '/docs/foundational' },
              { label: 'Glossary', to: '/glossary' },
            ],
          },
          {
            label: 'About',
            position: 'left',
            items: [
              { label: 'Our Mission', to: '/about' },
              { label: 'How it Works', to: '/how-to-use' },
            ],
          },
          { to: '/newsletter', label: 'Wisdom Well', position: 'left' },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Resources',
            items: [
              { label: 'Book Summaries', to: '/docs/foundational' },
              { label: 'Parenting Glossary', to: '/glossary' },
              { label: 'How it Works', to: '/how-to-use' },
            ],
          },
          {
            title: 'Support',
            items: [
              { label: 'Contact Us', to: '/contact' },
              { label: 'Newsletter', to: '/newsletter' },
              { label: 'About ParentWise', to: '/about' },
            ],
          },
          {
            title: 'Legal',
            items: [
              { label: 'Privacy Policy', to: '/privacy' },
              { label: 'Terms of Service', to: '/terms' },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} ParentWise Summary Guides. All rights reserved.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
