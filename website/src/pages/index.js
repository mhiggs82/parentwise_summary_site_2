import React from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import SophiaLogo from '@site/src/components/ParentWise/SophiaLogo';
import CategoryCard from '@site/src/components/ParentWise/CategoryCard';
import BookCard from '@site/src/components/ParentWise/BookCard';
import HomeSearch from '@site/src/components/ParentWise/HomeSearch';

export default function Home() {
  const { siteConfig } = useDocusaurusContext();

  const categories = [
    { badge: 'PRTG', name: 'Parenting', count: 40, description: 'General strategies, philosophies, and foundational advice for raising children.', to: '/docs/parenting' },
    { badge: 'COMM', name: 'Communication', count: 14, description: 'Mastering dialogue, active listening, and conflict resolution with kids.', to: '/docs/communication' },
    { badge: 'SPEC', name: 'Special Needs', count: 15, description: 'Expert guidance for ADHD, Autism, sensory processing, and unique challenges.', to: '/docs/special-needs' },
    { badge: 'DIGI', name: 'Digital', count: 6, description: 'Positive reinforcement, boundaries, and behavioral correction techniques.', to: '/docs/digital' },
    { badge: 'DEV', name: 'Development', count: 23, description: 'Age-appropriate milestones, cognitive growth, and physical changes.', to: '/docs/development' },
    { badge: 'EI', name: 'Emotional Int.', count: 19, description: 'Fostering empathy, self-regulation, and emotional awareness in children.', to: '/docs/emotional-intelligence' },
  ];

  const recentBooks = [
    { badge: 'PRTG', title: 'The Whole-Brain Child', author: 'Daniel Siegel, Tina Payne Bryson', insights: 12, actions: 3, to: '/docs/parenting/FOUND-003 - The Whole-Brain Child by Daniel Siegel and Tina Payne Bryson' },
    { badge: 'COMM', title: 'How to Talk So Kids Will Listen', author: 'Adele Faber, Elaine Mazlish', insights: 15, actions: 6, to: '/docs/communication/COMM-002 - How to Talk So Kids Will Listen and Listen So Kids Will Talk by Adele Faber and Elaine Mazlish' },
    { badge: 'EI', title: 'Emotional Intelligence', author: 'Daniel Goleman', insights: 18, actions: 4, to: '/docs/emotional-intelligence/MENT-001 - Emotional Intelligence Why It Can Matter More Than IQ by Daniel Goleman' },
    { badge: 'SPEC', title: 'Troublemakers', author: 'Carla Shalaby', insights: 9, actions: 5, to: '/docs/special-needs/SPEC-014 - Troublemakers by Carla Shalaby' },
  ];

  return (
    <Layout
      title={siteConfig.title}
      description="Actionable Summary Guides for Modern Parenting">

      <main className="container" style={{ paddingTop: '80px', paddingBottom: '120px' }}>

        {/* Hero Section */}
        <section style={{ textAlign: 'center', marginBottom: '80px' }}>
          <SophiaLogo />
          <Heading as="h1" style={{ fontSize: '48px', marginBottom: '16px' }}>
            ParentWise Actionable Summary Guides
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
              <CategoryCard key={i} {...cat} />
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
