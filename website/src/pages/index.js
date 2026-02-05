import React from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import SophiaLogo from '@site/src/components/ParentWise/SophiaLogo';
import CategoryCard from '@site/src/components/ParentWise/CategoryCard';
import BookCard from '@site/src/components/ParentWise/BookCard';
import HomeSearch from '@site/src/components/ParentWise/HomeSearch';

// Icon mapping for categories
const getCategoryIcon = (badge) => {
  const icons = {
    'FOUND': '👨‍👩‍👧‍👦',
    'COMM': '💬',
    'SPEC': '🌟',
    'DIGI': '📱',
    'DEV': '🌱',
    'EI': '❤️'
  };
  return icons[badge] || '📚';
};

export default function Home() {
  const { siteConfig } = useDocusaurusContext();

  const categories = [
    { badge: 'FOUND', name: 'Foundational', count: 40, description: 'General strategies, philosophies, and foundational advice for raising children.', to: '/docs/foundational' },
    { badge: 'COMM', name: 'Communication', count: 14, description: 'Mastering dialogue, active listening, and conflict resolution with kids.', to: '/docs/communication' },
    { badge: 'SPEC', name: 'Special Needs', count: 15, description: 'Expert guidance for ADHD, Autism, sensory processing, and unique challenges.', to: '/docs/special-needs' },
    { badge: 'DIGI', name: 'Digital', count: 6, description: 'Navigating technology, screen time, and digital wellness with children.', to: '/docs/digital-age-technology' },
    { badge: 'DEV', name: 'Development', count: 23, description: 'Age-appropriate milestones, cognitive growth, and character development.', to: '/docs/character-development' },
    { badge: 'EI', name: 'Emotional Int.', count: 19, description: 'Fostering empathy, self-regulation, and emotional awareness in children.', to: '/docs/mental-health' },
  ];

  const recentBooks = [
    { badge: 'Foundational', title: 'The Whole-Brain Child', author: 'Daniel Siegel, Tina Payne Bryson', insights: 12, actions: 3, to: '/docs/foundational/FOUND-003%20-%20The%20Whole-Brain%20Child%20by%20Daniel%20Siegel%20and%20Tina%20Payne%20Bryson' },
    { badge: 'Communication', title: 'How to Talk So Kids Will Listen', author: 'Adele Faber, Elaine Mazlish', insights: 15, actions: 6, to: '/docs/communication/COMM-002%20-%20How%20to%20Talk%20So%20Kids%20Will%20Listen%20and%20Listen%20So%20Kids%20Will%20Talk%20by%20Adele%20Faber%20and%20Elaine%20Mazlish' },
    { badge: 'Emotional Intelligence', title: 'Raising An Emotionally Intelligent Child', author: 'Dr. John Gottman, Joan Declaire', insights: 18, actions: 4, to: '/docs/mental-health/MENT-001%20-%20Raising%20An%20Emotionally%20Inteligent%20Child%20by%20Dr.%20John%20Gottman%20and%20Joan%20Declaire' },
    { badge: 'Special Needs', title: 'Troublemakers', author: 'Carla Shalaby', insights: 9, actions: 5, to: '/docs/special-needs/SPEC-014%20-%20Troublemakers%20by%20Carla%20Shalaby' },
  ];

  return (
    <Layout
      title={siteConfig.title}
      description="Actionable Summary Guides for Modern Parenting">

      <main className="container" style={{ paddingTop: '80px', paddingBottom: '120px' }}>

        {/* Hero Section */}
        <section style={{ textAlign: 'center', marginBottom: '80px' }}>
          <SophiaLogo size={120} />
          <Heading as="h1" style={{ fontSize: '48px', marginBottom: '16px' }}>
            ParentWise Actionable Insight Guides
          </Heading>
          <p className="text-secondary" style={{
            fontSize: '18px',
            textTransform: 'uppercase',
            letterSpacing: '0.2em',
            fontWeight: '600',
            marginBottom: '40px'
          }}>
            Focused • Empathetic • Expert-Backed
          </p>
          <HomeSearch />
        </section>

        {/* Categories Section */}
        <section style={{ marginBottom: '80px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '32px' }}>
            <div style={{ width: '4px', height: '24px', background: 'var(--pw-purple)', borderRadius: '2px' }}></div>
            <h2 style={{ margin: 0 }}>Browse Categories</h2>
          </div>
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))',
            gap: '24px'
          }}>
            {categories.map((cat, i) => (
              <CategoryCard key={i} {...cat} icon={getCategoryIcon(cat.badge)} />
            ))}
          </div>
        </section>

        {/* Recent Guides Section */}
        <section>
          <div style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            marginBottom: '32px'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
              <div style={{ width: '4px', height: '24px', background: 'var(--pw-purple)', borderRadius: '2px' }}></div>
              <h2 style={{ margin: 0 }}>Recent Guides</h2>
            </div>
            <div style={{ display: 'flex', gap: '12px' }}>
              <button className="pw-button" style={{ padding: '8px', borderRadius: '50%' }}>←</button>
              <button className="pw-button" style={{ padding: '8px', borderRadius: '50%' }}>→</button>
            </div>
          </div>
          <div style={{
            display: 'flex',
            gap: '24px',
            overflowX: 'auto',
            paddingTop: '20px',
            paddingBottom: '20px',
            scrollSnapType: 'x mandatory'
          }}>

            {recentBooks.map((book, i) => (
              <BookCard key={i} {...book} />
            ))}
          </div>
        </section>

      </main>
    </Layout>
  );
}
