import React from 'react';
import Layout from '@theme-original/DocItem/Layout';
import { useDoc } from '@docusaurus/plugin-content-docs/client';

export default function LayoutWrapper(props) {
  const { frontMatter } = useDoc();

  return (
    <div className="pw-doc-container">
      {/* Premium Header */}
      <header style={{ marginBottom: '48px', borderBottom: '1px solid var(--pw-border)', paddingBottom: '32px' }}>
        <div style={{ display: 'flex', gap: '8px', marginBottom: '16px' }}>
          {frontMatter.category_code && <span className="pw-badge" style={{ background: 'var(--pw-purple)', color: 'white' }}>{frontMatter.category_code}</span>}
          <span className="pw-badge" style={{ borderColor: 'var(--pw-success)', color: 'var(--pw-success)', background: 'transparent' }}>5-min read</span>
        </div>

        <h1 style={{ fontSize: '42px', fontWeight: '700', marginBottom: '12px', lineHeight: '1.2' }}>{frontMatter.title}</h1>
        <p className="text-secondary" style={{ fontSize: '18px', marginBottom: '24px' }}>By {frontMatter.author}</p>

        {frontMatter.tags && (
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '12px' }}>
            {frontMatter.tags.map((tag, i) => (
              <span key={i} className="text-tertiary" style={{ fontSize: '14px' }}>#{tag}</span>
            ))}
          </div>
        )}
      </header>

      {/* Main Content */}
      <Layout {...props} />
    </div>
  );
}
