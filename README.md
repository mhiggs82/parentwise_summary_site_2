# ParentWise Actionable Summary Guides

A comprehensive library of actionable book summaries designed to help modern parents navigate the complexities of raising children. Built with Docusaurus and deployed to GitHub Pages.

🌐 **Live Site:** [summaries.getparentwise.com](https://summaries.getparentwise.com)

## Overview

ParentWise provides distilled, actionable insights from over 100 parenting books across six key categories:

- **Foundational** - General strategies, philosophies, and foundational advice for raising children
- **Communication** - Mastering dialogue, active listening, and conflict resolution with kids
- **Special Needs** - Expert guidance for ADHD, Autism, sensory processing, and unique challenges
- **Digital** - Navigating technology, screen time, and digital wellness with children
- **Development** - Age-appropriate milestones, cognitive growth, and character development
- **Emotional Intelligence** - Fostering empathy, self-regulation, and emotional awareness in children

## Features

- 📚 Curated summaries of 100+ parenting books
- 🎯 Action-oriented insights for busy parents
- 🔍 Easy navigation by category
- 📖 Detailed book guides with key takeaways
- 🌙 Dark mode interface for comfortable reading
- 📱 Responsive design for all devices

## Tech Stack

- **Framework:** [Docusaurus 3.9.2](https://docusaurus.io/)
- **Language:** JavaScript/React
- **Styling:** CSS Custom Properties
- **Deployment:** GitHub Pages
- **CI/CD:** GitHub Actions
- **Node.js:** v20+

## Getting Started

### Prerequisites

- Node.js 20.0 or higher
- npm or yarn

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mhiggs82/parentwise_summary_site_2.git
   cd parentwise_summary_site_2
   ```

2. Navigate to the website directory:
   ```bash
   cd website
   ```

3. Install dependencies:
   ```bash
   npm install
   ```

4. Start the development server:
   ```bash
   npm start
   ```

   The site will open at `http://localhost:3000`

### Build

To create a production build:

```bash
npm run build
```

The static files will be generated in the `website/build` directory.

## Project Structure

```
parentwise_summary_site_2/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions deployment workflow
├── website/
│   ├── docs/                   # Book summaries organized by category
│   │   ├── foundational/
│   │   ├── communication/
│   │   ├── special-needs/
│   │   ├── digital-age-technology/
│   │   ├── character-development/
│   │   └── mental-health/
│   ├── src/
│   │   ├── components/
│   │   │   └── ParentWise/    # Custom React components
│   │   ├── css/
│   │   │   └── custom.css     # Custom styling
│   │   └── pages/             # Site pages
│   ├── static/                # Static assets
│   │   ├── img/
│   │   └── CNAME              # Custom domain configuration
│   ├── docusaurus.config.js   # Docusaurus configuration
│   ├── sidebars.js            # Sidebar configuration
│   └── package.json
└── README.md
```

## Deployment

The site is automatically deployed to GitHub Pages when changes are pushed to the `main` branch.

### Deployment Process

1. Push changes to the `main` branch
2. GitHub Actions workflow triggers automatically
3. Site builds and deploys to GitHub Pages
4. Changes are live at [summaries.getparentwise.com](https://summaries.getparentwise.com)

### Manual Deployment

To manually trigger a deployment:

1. Go to the [Actions tab](https://github.com/mhiggs82/parentwise_summary_site_2/actions)
2. Select "Deploy to GitHub Pages"
3. Click "Run workflow"

## Custom Domain

The site uses a custom domain configured via CNAME:
- **Domain:** summaries.getparentwise.com
- **CNAME Record:** Points to GitHub Pages

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

Copyright © 2026 ParentWise Summary Guides. All rights reserved.

## Contact

For questions or support, visit [ParentWise](https://getparentwise.com)
