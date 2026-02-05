import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import {
  useDocById,
  findFirstSidebarItemLink,
} from '@docusaurus/plugin-content-docs/client';
import isInternalUrl from '@docusaurus/isInternalUrl';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

function CardContainer({ href, children, className }) {
  return (
    <Link
      href={href}
      className={clsx('pw-card', styles.cardContainer, className)}
      style={{
        textDecoration: 'none',
        color: 'inherit',
        display: 'flex',
        flexDirection: 'column',
        height: '100%',
        padding: '24px',
        position: 'relative',
        overflow: 'hidden'
      }}>
      {children}
    </Link>
  );
}

function CardCategory({ item }) {
  const href = findFirstSidebarItemLink(item);
  if (!href) return null;

  return (
    <CardContainer href={href} className={item.className}>
      <div style={{ marginBottom: '16px', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <span style={{
          background: 'rgba(124, 91, 255, 0.1)',
          color: 'var(--pw-purple)',
          padding: '4px 12px',
          borderRadius: '20px',
          fontSize: '11px',
          fontWeight: '700',
          letterSpacing: '0.05em'
        }}>COLLECTION</span>
        <span style={{ fontSize: '20px' }}>📦</span>
      </div>
      <Heading as="h3" style={{ fontSize: '20px', marginBottom: '8px', color: 'white', fontWeight: '700' }}>
        {item.label}
      </Heading>
      <p style={{
        fontSize: '14px',
        color: 'var(--pw-text-secondary)',
        lineHeight: '1.5',
        flexGrow: 1,
        marginBottom: '24px'
      }}>
        {item.description ?? `${item.items.length} expert-backed guides.`}
      </p>
      <div style={{
        display: 'flex',
        alignItems: 'center',
        gap: '8px',
        color: 'var(--pw-purple)',
        fontWeight: '600',
        fontSize: '14px',
        marginTop: 'auto'
      }}>
        Browse Collection <span style={{ transition: 'transform 0.2s' }}>→</span>
      </div>
    </CardContainer>
  );
}

function CardLink({ item }) {
  const docId = item.docId ?? undefined;
  const doc = useDocById(docId);

  // Tag Logic: Uses first 3 tags if available, otherwise falls back to category code
  const tags = doc?.frontMatter?.tags;
  let pillText = '';

  if (tags && Array.isArray(tags) && tags.length > 0) {
    pillText = tags.slice(0, 3).join(' • ');
  } else {
    // Fallback: Try to extract category code from filename if not in frontmatter
    let categoryCode = doc?.frontMatter?.category_code || doc?.frontMatter?.category;

    if (!categoryCode) {
      const splitLabel = item.label.split(' - ')[0];
      categoryCode = splitLabel.length < 15 ? splitLabel : 'GUIDE';
    }
    pillText = categoryCode;
  }

  return (
    <CardContainer href={item.href} className={item.className}>
      <div style={{ marginBottom: '16px', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <span style={{
          background: 'rgba(0, 217, 184, 0.1)',
          color: 'var(--pw-success)',
          padding: '4px 12px',
          borderRadius: '20px',
          fontSize: '11px',
          fontWeight: '700',
          letterSpacing: '0.05em',
          textTransform: 'uppercase',
          maxWidth: '85%',
          overflow: 'hidden',
          whiteSpace: 'nowrap',
          textOverflow: 'ellipsis'
        }}>
          {pillText}
        </span>
        <span style={{ fontSize: '18px' }}>📖</span>
      </div>

      <Heading as="h3" style={{
        fontSize: '17px',
        marginBottom: '6px',
        color: 'white',
        lineHeight: '1.4',
        fontWeight: '600',
        display: '-webkit-box',
        WebkitLineClamp: '2',
        WebkitBoxOrient: 'vertical',
        overflow: 'hidden'
      }}>
        {item.label.includes(' - ') ? item.label.split(' - ').slice(1).join(' - ') : item.label}
      </Heading>

      <div style={{ fontSize: '12px', color: 'var(--pw-text-tertiary)', marginBottom: '8px', fontWeight: '500' }}>
        {doc?.frontMatter?.author ? `By ${doc.frontMatter.author}` : 'ParentWise Summary'}
      </div>

      {doc?.frontMatter?.subtitle && (
        <div style={{
          fontSize: '13px',
          color: 'var(--pw-text-main)',
          lineHeight: '1.4',
          marginBottom: '12px',
          fontWeight: '500',
          fontStyle: 'italic',
          display: '-webkit-box',
          WebkitLineClamp: '2',
          WebkitBoxOrient: 'vertical',
          overflow: 'hidden'
        }}>
          {doc.frontMatter.subtitle}
        </div>
      )}

      <p style={{
        fontSize: '13px',
        color: 'var(--pw-text-secondary)',
        lineHeight: '1.6',
        flexGrow: 1,
        marginBottom: '24px',
        display: '-webkit-box',
        WebkitLineClamp: '2',
        WebkitBoxOrient: 'vertical',
        overflow: 'hidden'
      }}>
        {item.description || doc?.description || 'Deep dive into actionable strategies and research-backed frameworks.'}
      </p>

      <div style={{
        marginTop: 'auto',
        paddingTop: '16px',
        borderTop: '1px solid var(--pw-border)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between'
      }}>
        <div style={{ color: 'var(--pw-purple)', fontWeight: '600', fontSize: '13px' }}>
          Read Summary
        </div>
        <div style={{ fontSize: '12px', color: 'var(--pw-text-tertiary)' }}>
          5-min read
        </div>
      </div>
    </CardContainer>
  );
}

export default function DocCard({ item }) {
  switch (item.type) {
    case 'link':
      return <CardLink item={item} />;
    case 'category':
      return <CardCategory item={item} />;
    default:
      return null;
  }
}
