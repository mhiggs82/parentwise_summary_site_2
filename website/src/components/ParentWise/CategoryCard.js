import React from 'react';
import Link from '@docusaurus/Link';
import clsx from 'clsx';

export default function CategoryCard({ badge, name, count, description, to }) {
    return (
        <Link to={to} className="pw-card" style={{ textDecoration: 'none', color: 'inherit' }}>
            <div style={{ marginBottom: '16px' }}>
                <span className="pw-badge" style={{ fontSize: '10px' }}>{badge}</span>
            </div>
            <h3 style={{ margin: '0 0 8px 0', fontSize: '20px' }}>{name}</h3>
            <p className="text-tertiary" style={{ fontSize: '13px', margin: '0 0 12px 0' }}>{count} books</p>
            <p className="text-secondary" style={{ fontSize: '14px', margin: 0, lineHeight: '1.5' }}>
                {description}
            </p>
        </Link>
    );
}
